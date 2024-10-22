from django import forms
from .models import Company, Location, Employee

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'zip_code', 'email_address', 'phone', 'web']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter company name'}),
            'zip_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter zip code'}),
            'email_address': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email address'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter phone number'}),
            'web': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Enter website URL'}),
        }

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['l_name', 'l_phone', 'l_address', 'l_com']
        widgets = {
            'l_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter location name'}),
            'l_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter phone number'}),
            'l_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter address'}),
            'l_com': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter company name'}),
        }

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['e_name', 'e_phone', 'e_address', 'e_com', 'e_img']
        widgets = {
            'e_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter employee name'}),
            'e_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter phone number'}),
            'e_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter address'}),
            'e_com': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter company name'}),
            'e_img': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Upload employee image'}),
        }

