from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Company, Location, Employee
from .forms import CompanyForm, LocationForm, EmployeeForm
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.http import HttpResponseRedirect, HttpResponse


def location_list(request):
    locations = Location.objects.all()
    return render(request, 'locations/location_list.html', {'locations': locations})


def add_location(request):
    
    if request.method == "POST":
        
        loc = Location()
        try: 
            
            loc.l_name = request.POST.get('l_name')
            loc.l_phone = request.POST.get('l_phone')
            loc.l_address = request.POST.get('l_address')
            
            l_company = request.POST.get('l_company')
            # print("*****printing company:************" + l_company)
            loc.l_com = get_object_or_404(Company, id=l_company) 
            
            # try:
            #     loc.l_com = int(l_company)
            # except (ValueError, TypeError):
            #     messages.error(request, "Invalid company ID. Please enter a valid number.")
            #     return render(request, 'companies/forms.html')
    
            loc.save()
            messages.success(request, "Location Saved")
            return redirect('location_list')
        
        except Exception as e:
            
            messages.error(request, f'{e}')
  
        #return HttpResponse("Location added successfully!")

    companies = Company.objects.all()


        
               
    return render(request, 'locations/add_location.html', {'company':companies})


@login_required
def edit_location(request, pk):
    location = get_object_or_404(Location, pk=pk)
    if request.method == "POST":
        form = LocationForm(request.POST, instance=location)
        if form.is_valid():
            form.save()
            return redirect('location_list')
    else:
        form = LocationForm(instance=location)
    return render(request, 'locations/edit_location.html', {'form': form, 'location': location})

# View for deleting a company (restricted to logged-in users)
@login_required
def delete_location(request, pk):
    location = get_object_or_404(Location, pk=pk)
    if request.method == "POST":
        location.delete()
        return redirect('location_list')
    return render(request, 'locations/delete_location.html', {'location': location})

