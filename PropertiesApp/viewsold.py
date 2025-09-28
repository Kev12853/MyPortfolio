from django.shortcuts import render
from . import forms

def home(request):
    context = {'form': forms.TenantForm()}
    return render(request, 'PropertiesApp/home.html', context)


