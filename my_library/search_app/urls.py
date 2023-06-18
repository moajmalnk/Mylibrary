from django.urls import path
from search_app import views

app_name = 'search_app'

urlpatterns = [
    path('', views.search_result, name='search'),
    path('patron/', views.patrons, name='patron')
]