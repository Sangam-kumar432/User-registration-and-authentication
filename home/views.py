import random
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from django.contrib import messages

from home.models import Quiz


# password for test1 : Len123@#$pass
# user = admin , password = 12345678
# Create your views here.
def home(request):
    if request.user.is_anonymous:
        return render(request, 'home.html')
    return render(request, 'index.html')


def registeruser(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(
                    username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                return redirect('login')

        else:
            messages.info(request, 'password not matching..')
            return redirect('register')
    else:
        return render(request, 'register.html')


def loginuser(request):
    if request.method == 'POST':
        # check whether user has correct credentiaLs
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return render(request, 'index.html')
        else:
            # No backend authenticated the credentials
            return render(request, 'login.html')
    return render(request, 'login.html')


def play(request):
    que = Quiz.objects.first()

    if request.method == 'POST':
        # getting the answer submitted by user
        answer = request.POST.get('answer')

        # getting the sum of two integers in class Quiz
        val = str(que.sum())
        if  val == answer  :
            messages.info(request, 'Correct')
            return redirect('/play')
        else:
            messages.info(request, 'Wrong')
            return redirect('/play')

    return render(request, 'play.html' ,{"que":que})



def logoutuser(request):
    logout(request)
    return redirect("/")
