""" Purpose of forms.py
forms.py is a crucial component commonly used in web frameworks like Django to handle form processing. Its primary functions include:

Defining Forms: It allows developers to create forms that can collect user input, validate that data, and handle the submission process effectively.
Data Validation: Forms defined in forms.py can include various validation rules to ensure the data received is correct and secure, preventing common errors and malicious input.
Rendering HTML: It facilitates the automatic generation of HTML form elements based on the defined fields, making it easier for developers to create forms without needing to write extensive HTML code.
Integration with Models: In frameworks like Django, forms can be easily tied to models, allowing for streamlined data input and processing, which can reduce boilerplate code.
User Feedback: Provides mechanisms to return error messages or confirmation messages to users, enhancing the user experience during form submissions.

Key Features
Field Types: Supports various field types such as text fields, checkboxes, radio buttons, and select dropdowns.
Custom Validation: Developers can define custom validation methods to enforce specific rules for user input.
CSRF Protection: Automatically includes tools for Cross-Site Request Forgery protection, ensuring secure form submissions.
Easy Handling of Form States: Supports state management, making it easy to handle cases where the form needs to retain data after a validation error.
Overall, forms.py serves as a centralized module for defining and managing forms, which enhances both application functionality and user experience. """

from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, Fieldset, Row, Column

from PropertiesApp.models.tenant_model import Tenant


class Tenant_Form(forms.ModelForm):
    class Meta:
        model = Tenant
        fields = ["first_name", "last_name", "email", "phone"]
        
    first_name = forms.CharField(
        max_length=50,
        required=False,
        widget=forms.TextInput(
            attrs={"class": "input input-bordered w-full", "placeholder": "First Name"}
        ),
    )
    last_name = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(
            attrs={"class": "input input-bordered w-full", "placeholder": "Last Name"}
        ),
    )
    email = forms.EmailField(
        max_length=100,
        required=False,
        widget=forms.EmailInput(
            attrs={"class": "input input-bordered w-full", "placeholder": "Email"}
        ),
    )
    phone = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.TextInput(
            attrs={"class": "input input-bordered w-full", "placeholder": "Phone"}
        ),
    )


class TenantCreateForm(forms.ModelForm):
    class Meta:
        model = Tenant
        fields = ["first_name", "last_name", "email", "phone"]

    def __init__(self, *args, **kwargs):
        super(TenantCreateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.include_media = False
        self.helper.form_method = "post"
        self.helper.form_class = "border p-8"
        self.helper.layout = Layout(
            Div(
                Div("first_name", css_class="md:w-[50%]"),
                Div("last_name", css_class="md:w-[50%]"),
                Div("email", css_class="md:w-[50%]"),
                Div("phone", css_class="md:w-[50%]"),
            ),
            "first_name",
            "last_name",
            "email",
            "phone",
        )


class TenantListForm(forms.ModelForm):
    class Meta:
        model = Tenant
        fields = ["first_name", "last_name", "email", "phone"]


class TenantDetailForm(forms.ModelForm):
    class Meta:
        model = Tenant
        fields = ["first_name", "last_name", "email", "phone"]


class TenantUpdateForm(forms.ModelForm):
    class Meta:
        model = Tenant
        fields = ["first_name", "last_name", "email", "phone"]

    first_name = forms.CharField(
        max_length=50,
        required=False,
        widget=forms.TextInput(
            attrs={
                
                "placeholder": "First Name"
            }
        ),
    )
    last_name = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(
            attrs={                
            "placeholder": "Last Name"
            }
        ),
    )
    email = forms.EmailField(
        max_length=100,
        required=False,
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email"
                }
        ),
    )
    phone = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Phone"
                }
        ),
    )

#"class": "input input-bordered w-full",




class TenantDeleteForm(forms.ModelForm):
    class Meta:
        model = Tenant
        fields = []  # No fields needed for deletion confirmation
