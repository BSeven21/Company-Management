from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Company, Location, Employee
from .forms import CompanyForm
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.http import HttpResponseRedirect, HttpResponse

def register_view(request):
    if request.method == 'POST':
        user_name = request.POST['username']
        pass_word = request.POST['password']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        admin = request.POST['admin']
        print("admin value*********",admin)


        if admin=='on':
            superuser = True
        else:
            superuser = False

        user = User.objects.create_user(username=user_name, password=pass_word, first_name=firstname, last_name=lastname, is_superuser=superuser, is_staff=superuser)



        user.save()
        messages.success(request, 'Registration successful.')
        return redirect('login')  
    return render(request, 'companies/register.html')


# View for user login
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('company_list')  
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'companies/login.html')


# View for user loginout
def logout_view(request):
    logout(request)  
    return redirect('login') 


