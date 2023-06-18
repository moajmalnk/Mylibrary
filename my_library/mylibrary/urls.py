from . import views
from django.urls import path

app_name = 'mylibrary'

urlpatterns = [
    path('', views.home, name='home'),
    path('book/<int:id>/', views.detail_view, name='detail'),
    path('add/', views.add_book, name='add_book'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('add_patron/', views.patrons, name='add_patron'),
    path('profile/<int:id>/', views.profile, name='profile'),
    path('all_patrons/', views.all_patrons, name='all_patrons'),
    path('update_patron/<int:id>/', views.update_patron, name='update_patron'),
    path('delete_patron/<int:id>/', views.delete_patron, name='delete_patron'),
    path('messages/', views.message, name='message'),
    path('program/', views.programmes, name='program'),
    path('category/', views.all_book_category, name='all_book_category'),
    path('<slug:c_slug>/', views.all_book_category, name='books_by_category'),
    path('<slug:c_slug>/<slug:book_slug>/', views.all_product_details, name='book_category_details'),
]