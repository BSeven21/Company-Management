from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Company, Location, Employee
from .forms import CompanyForm, EmployeeForm
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.http import HttpResponseRedirect, HttpResponse



def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employees/employee_list.html', {'employee': employees})


def add_employee(request):
    
    if request.method == "POST":
        
        loc = Employee()
        try: 
            
            loc.e_name = request.POST.get('e_name')
            loc.e_phone = request.POST.get('e_phone')
            loc.e_address = request.POST.get('e_address')
            
            e_company = request.POST.get('e_company')
            print("*****printing company:************" , e_company)
            loc.e_com = get_object_or_404(Company, id=e_company)
            
            e_loc = request.POST.get('e_loc')
            print("*****printing Location:************" , e_loc)
            loc.e_loc = get_object_or_404(Location, id=e_loc) 
            
            img = request.FILES.get('e_img')
            loc.e_img = img 


            loc.save()
            messages.success(request, "Employee Saved")
            return redirect('employee_list')
        
        except Exception as e:
            
            messages.error(request, f'{e}')
  

    companies = Company.objects.all()
    locations = Location.objects.all()
           
    return render(request, 'employees/add_employee.html', {'company':companies , 'location': locations})


@login_required
def edit_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == "POST":
        form = EmployeeForm(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employees/edit_employee.html', {'form': form, 'employee': employee})

# View for deleting a company (restricted to logged-in users)
@login_required
def delete_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == "POST":
        employee.delete()
        return redirect('employee_list')
    return render(request, 'employees/delete_employee.html', {'employee': employee})

