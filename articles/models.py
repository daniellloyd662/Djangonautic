from django.db import models
from django.contrib.auth.models import User
##============Models============
#Models in python are a class which represent a table in a database
#Each type of data we have is represented by it's own model
#Each model maps to a single table in a database

##==========Migrations==========
#Models must be migrated to the database so that the tables can be created (In this case, a table tiitled Articles). Until then it only exists in code
#A migration file tracks changes made to a model. Create using python manage.py makemigrations
#The migration file will be used to track changes over time (Check _pycache__ for files with xxxx_initial.py format)
#Run python manage.py after using makemigrations to mirror the model (In the migrations file) into a database

#The class below inherits from model.Model
#Field types specify what type of data each variable is. They also set a default widget ie textbox vs dropdown
#Field types allow us to pass in kwargs to specify restrictions or modifications on input data
class Article(models.Model):
    title = models.CharField(max_length = 100)
    slug = models.SlugField()                           #This is used to specify the url associated with the html page for this object
    body = models.TextField()
    date = models.DateTimeField(auto_now_add = True)
    thumb = models.ImageField(default='default.png', blank=True)    #Shows default.png as default
    author = models.ForeignKey(User, default=None, on_delete = models.CASCADE)                  #User is imported from django models library


    #add in author later
    def __str__(self):                          #Adding this function sets what will be returned when viewing Article objects in a python shell/Admin view
        return self.title

    def snippet(self):                          #This function is in place of article.body in the html code to return a trimmed version of the body
        return self.body[:50]+'...'
