from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Company, Location
from .forms import CompanyForm
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.http import HttpResponseRedirect, HttpResponse


# View for adding a new company (restricted to logged-in users)
@login_required
def add_company(request):
    if request.method == "POST":
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            messages.warning(request, "Company Saved")
            return redirect('company_list')
    else:
        form = CompanyForm()
    return render(request, 'companies/add_company.html', {'form': form})

# View for listing companies (anyone can view)
def company_list(request):
    companies = Company.objects.all()
    return render(request, 'companies/company_list.html', {'companies': companies})

# View for editing a company (restricted to logged-in users)
@login_required
def edit_company(request, pk):
    company = get_object_or_404(Company, pk=pk)
    if request.method == "POST":
        form = CompanyForm(request.POST, instance=company)
        if form.is_valid():
            form.save()
            return redirect('company_list')
    else:
        form = CompanyForm(instance=company)
    return render(request, 'companies/edit_company.html', {'form': form, 'company': company})

# View for deleting a company (restricted to logged-in users)
@login_required
def delete_company(request, pk):
    company = get_object_or_404(Company, pk=pk)
    if request.method == "POST":
        company.delete()
        return redirect('company_list')
    return render(request, 'companies/delete_company.html', {'company': company})
