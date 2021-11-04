from django.contrib import admin
from django.urls import path, include
from . import views                                                     #Views is imported so that the functions in views can be passed into path functions
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from articles import views as article_views #We import articles as article_views to avoid confusion from the above import of views (from . import views)

#We pass into path one url and a function from views.py that runs when the url is entered in the search bar
#By convention we typically name this function the same as the url but this is not mandatory
urlpatterns = [
    #Below function tells the root urls.py file to include urls from the articles app and to let them be accessible by adding them after articles/ in the search bar
    path('articles/',include('articles.urls')), #when articles/ is after the base url then use the articles.urls file for slugs (suffix urls)
    path('accounts/',include('accounts.urls')),
    path('admin/', admin.site.urls),
    path('about/', views.about),
    path('', article_views.article_list, name = "home") #This url directs us to the article_list.html page
]

urlpatterns += staticfiles_urlpatterns()        #Tells django to serve static files
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)  #adds the urls for media files so they can be accessed
