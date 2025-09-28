from django import forms
from django.urls import reverse_lazy
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class TenantForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(TenantForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))
        


    first_name = forms.CharField(label='First Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)
    email = forms.EmailField(label='Email')
    phone = forms.CharField(label='Phone', max_length=15)
    dob = forms.DateField(label='Date of Birth', widget=forms.DateInput(attrs={'type': 'date'}))

    
class AnotherTenantForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(AnotherTenantForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))
        


    first_name = forms.CharField(label='First Name2', max_length=100)
    last_name = forms.CharField(label='Last Name2', max_length=100)
    email = forms.EmailField(label='Email2')
    phone = forms.CharField(label='Phone2', max_length=15)
    dob = forms.DateField(label='Date of Birth2', widget=forms.DateInput(attrs={'type': 'date'}))
