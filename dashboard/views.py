from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from CreateTeam.models import *
from Question.models import *


@login_required
def Homepage(request):
    # Get all the relevant data
    # team_categories = TeamCategory.objects.all()
    players = Player.objects.all()
    questions = Question.objects.filter(user=request.user)
    user_teams = UserTeam.objects.filter(user=request.user)

    # Pass the data to the template
    return render(request, 'Dashboard/Home.html', {
        'questions': questions,
        'players': players,
        'user_teams': user_teams
    })

# Logout View
def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout


# Login View
def login_view(request):
    if request.user.is_authenticated:
        return redirect('Homepage')  # Redirect to Homepage if user is already logged in

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('Homepage')  # Redirect to Homepage upon successful login
        else:
            # Optional: Add error message if login fails
            return render(request, 'Login/Login.html', {'error': 'Invalid username or password'})

    return render(request, 'Login/Login.html')


# Registration View
def Registrationpage(request):
    if request.user.is_authenticated:
        return redirect('Homepage')  # Redirect to Homepage if user is already logged in

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            # Authenticate and log in the user
            user = authenticate(username=user.username, password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('Homepage')  # Redirect to Homepage after successful registration
    else:
        form = RegisterForm()

    return render(request, 'Login/register.html', {'form': form})
