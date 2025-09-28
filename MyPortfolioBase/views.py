from django.shortcuts import render
from django.views import View

from PropertiesApp import forms1 as forms

class HomePage(View):
    def get(self, request):
        context = {'myform': forms.TenantForm(),
                    'myform1': forms.AnotherTenantForm()}
        return render(request, 'home.html', context)

