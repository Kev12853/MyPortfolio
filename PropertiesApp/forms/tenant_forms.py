from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit

from PropertiesApp.models.tenant_model import Tenant


class TenantCreateForm(forms.ModelForm):
    class Meta:
        model = Tenant
        fields = ["first_name", "last_name", "email", "phone"]

    """ def __init__(self, *args, **kwargs):
        super(TenantCreateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.form_class = "border p-8"
        self.helper.layout = Layout(
            Div(
                Div("name", css_class="md:w-[50%]"),
                Div("reason", css_class="md:w-[50%]"),
                css_class="md:flex md:justify-between",
            ),
            "first_name",
            "last_name",
            "email",
            "phone",
            Submit(
                "submit",
                "Submit",
                css_class="text-white bg-blue-700"
                " hover:bg-blue-800 focus:ring-4 focus:ring-blue-300"
                " font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-2 dark:bg-blue-600"
                " dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800",
            ),
        )
 """

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


class TenantDeleteForm(forms.ModelForm):
    class Meta:
        model = Tenant
        fields = []  # No fields needed for deletion confirmation
