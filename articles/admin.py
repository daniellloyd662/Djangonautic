from django.contrib import admin
# Register your models here.

#Article object must be imported in order to be seen on the admin page.
#Once imported,
from .models import Article

admin.site.register(Article)        #This function adds Articles to the admin page so they can be created and viewed from the admin page
