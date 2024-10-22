from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from . import company_views, location_views, employee_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('add/', company_views.add_company, name='add_company'),
    path('', company_views.company_list, name='company_list'),
    path('edit/<int:pk>/', company_views.edit_company, name='edit_company'),
    path('delete/<int:pk>/', company_views.delete_company, name='delete_company'),
    path('add_location/', location_views.add_location, name='add_location'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('location_list/', location_views.location_list, name='location_list'),
    path('delete_location/<int:pk>/', location_views.delete_location, name='delete_location'),
    path('edit_location/<int:pk>/', location_views.edit_location, name='edit_location'),
    path('employee_list/', employee_views.employee_list, name='employee_list'),
    path('add_employee/', employee_views.add_employee, name='add_employee'),
    path('delete_employee/<int:pk>/', employee_views.delete_employee, name='delete_employee'),
    path('edit_employee/<int:pk>/', employee_views.edit_employee, name='edit_employee'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)