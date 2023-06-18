from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from .models import Book_details, Patron, Category
from .forms import BookForm, PatronForm


def profile(request, id):
    patron = Patron.objects.get(id=id)
    context = {
        'patron': patron
    }
    template = 'profile.html'
    return render(request, template, context)


def home(request, slug=None,):
    if request.user.is_authenticated:
        page = None
        book_list = None
        if slug is not None:
            page = get_object_or_404(Book_details, slug=slug)
            book_list = Book_details.objects.all().filter(category=page)
        else:
            book_list = Book_details.objects.all().filter()
        paginator = Paginator(book_list, 6)
        try:
            page = int(request.GET.get('page', '1'))
        except():
            page = 1
        try:
            book = paginator.page(page)
        except (EmptyPage, InvalidPage):
            book = paginator.page(paginator.num_pages)
        return render(request, 'home.html', {'book': book, 'category': page})
    return redirect('/')


def detail_view(request, id):
    book = Book_details.objects.get(id=id)
    context = {
        'book': book
    }
    return render(request, 'detail.html', context)


def add_book(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        slug = request.POST.get('slug')
        desc = request.POST.get('desc')
        auther = request.POST.get('auther')
        category = request.POST.get('category')
        price = request.POST.get('price')
        stock = request.POST.get('stock')
        img = request.FILES['img']
        lang = request.POST.get('lang')
        book = Book_details(
            name=name,
            slug=slug,
            desc=desc,
            auther=auther,
            category=category,
            price=price,
            stock=stock,
            img=img,
            lang=lang
        )
        book.save()
    return render(request, 'add books.html')


def update(request, id):
    book = Book_details.objects.get(id=id)
    form = BookForm(request.POST or None, request.FILES, instance=book)
    if form.is_valid():
        form.save()
        return redirect('/mylibrary/')
    return render(request, 'update.html', {'book': book, 'form': form})


def delete(request, id):
    book = Book_details.objects.get(id=id)
    if request.method == 'POST':
        book = Book_details.objects.get(id=id)
        book.delete()
        return redirect('/mylibrary/')
    context = {
        'book': book
    }
    return render(request, 'delete.html', context)


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if password == password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'USERNAME TAKEN')
                return redirect('/signup/')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'EMAIL TAKEN')
                return redirect('/signup/')
            else:
                user = User.objects.create_user(username=username, password=password, email=email)
                user.save()
                return redirect('/login/')
        else:
            messages.info(request, 'PASSWORD NOT MATCHED')
            return redirect('/signup/')
    return render(request, 'signup.html')


def user_login(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'INVALID CREDENTIALS')
            return redirect('/login/')
        return redirect('/')
    return render(request, 'login.html')


def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('/login/')


def patrons(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        gmail = request.POST.get('gmail')
        card_no = request.POST.get('card_no')
        phone = request.POST.get('phone')
        # img = request.FILES['img']
        patron = Patron(name=name, gmail=gmail, card_no=card_no, phone=phone)
        patron.save()
    return render(request, 'add_patron.html')


def all_patrons(request):
    patron = Patron.objects.all()
    template = 'all_patrons.html'
    context = {
        'patron': patron
    }
    return render(request, template, context)


def update_patron(request, id):
    patron = Patron.objects.get(id=id)
    form = PatronForm(request.POST or None, request.FILES, instance=patron)
    if form.is_valid():
        form.save()
        return redirect('/mylibrary/')
    context = {
        'patron': patron,
        'form': form
    }
    template = 'update_patron.html'
    return render(request, template, context)


def delete_patron(request, id):
    patron = Patron.objects.get(id=id)
    if request.method == 'POST':
        patron = Patron.objects.get(id=id)
        patron.delete()
        return redirect('/mylibrary/')
    context = {
        'patron': patron
    }
    template = 'delete_patron.html'
    return render(request, template, context)


def message(request):
    return render(request, 'message.html')


def programmes(request):
    return render(request, 'programmes.html')


def all_book_category(request, c_slug=None):
    c_page = None
    books_list = None
    if c_slug is not None:
        c_page = get_object_or_404(Category, slug=c_slug)
        books_list = Book_details.objects.all().filter(category=c_page)
    else:
        books_list = Book_details.objects.all()
    return render(request, 'category.html', {'category': c_page, 'book': books_list})


def all_product_details(request, c_slug, book_slug):
    try:
        book = Book_details.objects.get(category__slug=c_slug, slug=book_slug)
    except Exception as e:
        raise e
    return render(request, 'product.html', {'book': book})