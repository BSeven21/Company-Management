from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Employee Administration"
admin.site.site_title = "Employee Admin Site"
admin.site.index_title = "Employee Admin"

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('Testapp.urls')),
    
]
