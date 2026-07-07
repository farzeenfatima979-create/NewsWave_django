from django.urls import path
from . import views

urlpatterns = [
    path('',                  views.home,           name='home'),
    path('category/<str:cat>/', views.category,     name='category'),
    path('search/',           views.search,          name='search'),
    path('article/',          views.article_detail,  name='article_detail'),
    path('about/',            views.about,           name='about'),
    path('contact/',          views.contact,         name='contact'),
]
