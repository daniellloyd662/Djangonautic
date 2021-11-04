from django.shortcuts import render, redirect
#UserCreationForm and AuthenticationForm are objects included in django with methods and attributes used for UserCreation/Login authentication
# is an object included in django with methods to log a user in
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

#The passed in request can be get/send data (i.e. form submission from pressing a button). HTML sends the data but it must also be specified get/send in views.py

def signup_view(request):
    #Check if the method used in the html submission is 'post'. If true the data is passed into a new instance of UserCreationForm
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()                      #This line saves the form to the database
            login(request,user)                     #Logs in the user after account creation
            return redirect('articles:list')        #Takes user to the list url in the articles articles folder
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST) #request.POST passes in data from the login.html file when the submit button is pressed
        if form.is_valid():
            user = form.get_user()                  #built in method to get user info
            login(request, user)                    #user info is passed in
            if 'next' in request.POST:                      #if a user was redirected to login, this code will redirect them to the original page after auth
                return redirect(request.POST.get('next'))
            else:
                return redirect('articles:list')
    else:
        form = AuthenticationForm()
    return render(request, "accounts/login.html", {'form': form})

#Btn is added in the base layout. If we redirect to the logout url and post data the below function will run and we will be redirected to the list view
def logout_view(request):
    if request.method == "POST":
        logout(request)             #No need to pass in the user since Django already knows who is logged in
        return redirect('articles:list')    #go to view list in app folder articles
