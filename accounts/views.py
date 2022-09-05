from django.contrib.auth.models import  User
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import accounts
from .forms import CreateForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def accountsView(request):
    
    users = accounts.objects.raw('SELECT * FROM accounts_accounts')
    print(users.query)

    context = {
        'users': users
    }
    return render(request, 'home.html', context)
@login_required(login_url='login')
def accountsCreate(request):
    form = CreateForm()
    if request.user.is_superuser:
        if request.method == 'POST':
            form = CreateForm(request.POST)
            if form.is_valid:
                form.save()
                return redirect('home')
        context = {
            'form': form
        }
    else:
        return HttpResponse('You are not allowed !!!')    
    return render(request, 'create.html', context)

def register(request):
    if request.method == "POST":
        if request.POST['password'] == request.POST['coniform_password']:
            User.objects.create_user(
                username = request.POST['username'],
                password = request.POST['password']
            )
        else:
            messages.info(request, 'Parol to`g`ri kelmadi.')
            return redirect('register')
        # data = User();
        # data.save()
        return redirect('home')
    
    return render(request, 'users/register.html')

def login_user(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or Password wrong!!!')
    return render(request, 'users/login.html')

def logout_user(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login')
def accountsUpdate(request, pk):
    accounts1 = accounts.objects.get(id=pk)
    form = CreateForm(instance=accounts1)

    if request.method == 'POST':
        form = CreateForm(request.POST, instance=accounts1)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    context = {'form': form}
    return render(request, 'create.html', context)    
@login_required(login_url='login')
def accountsDelete(request, pk):
    accounts1 = accounts.objects.get(id=pk)
    accounts1.delete()
    return redirect('home')

def search(request):
    if request.method == "POST":
        search = request.POST['search']
        results = accounts.objects.filter(first_name__contains = search)
        
        context = {
        'search': search,
        'results': results
        }
        return render(request, 'search.html', context)
    else:
        return render(request, 'search.html')