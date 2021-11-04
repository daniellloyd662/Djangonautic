from django.shortcuts import render, redirect
from .models import Article
from django.contrib.auth.decorators import login_required
from . import forms

#The below function renders an html template article_list.
#The folder name must be specified since it is not included in the settings file like the root template folder

def article_list(request):
    articles = Article.objects.all().order_by('date')           #Returns all objects of type Article ordered by date and stores them as an 'articles' variable
    #Below function sends a dictionary to the html template with a property called 'articles' that is equal to our articles variable defined above. See article_list.html for application
    return render(request, 'articles/article_list.html', {'articles':articles})

#Below function will be used to return a unique html page for each article that can be accessed via a link
def article_detail(request, slug):
    # return HttpResponse(slug)
    article = Article.objects.get(slug = slug)
    #Returns the article_detail.html template with the corresponding article object passed in under the name 'article'
    return render(request, 'articles/article_detail.html',{'article': article})

@login_required(login_url="/accounts/login/")   #Decorator adds a requirement that the user be logged in. Passing in the login_url redirects the user to this page if not logged in
def article_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES)      #Request.POST is the data passed in when the article create button is pressed. Request.FILES is used for files
        if form.is_valid():
            #save article to db
            instance = form.save(commit = False)                     #commit = False, allows us to save the article instance without adding to database
            instance.author = request.user                          #request.user pulls the current user in the django app
            instance.save()
            return redirect('articles:list')
    else:
        form = forms.CreateArticle()                                            #let form be an instance of the CreateArticle object specified in forms.py
    return render(request, 'articles/article_create.html', {'form':form})   #pass in a dictionary with a 'form' key to be used in the html doc
