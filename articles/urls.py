from django.urls import path
from . import views

#This urls.py file must be registered in the root urls.py file in order to be accessible
app_name = 'articles'
urlpatterns = [
    path('', views.article_list, name='list'),
    #Below URL MUST COME BEFORE <SLUG> PATH. OTHERWISE WHEN articles/create/ is entered in the search bar the slug path will assume it is a slug and throw an error
    path('create/', views.article_create, name = 'create'),
    #Below url
    path('<slug:slug>/',views.article_detail, name='detail'),             #First slug is the type of parameter (slug) and the second slug is the name of the parameter


]
