from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, Fieldset, Row, Column

from PropertiesApp.models.tenant_model import Tenant

class QuickAddTenant_Form(forms.ModelForm):
    class Meta:
        model = Tenant
        fields = ["first_name", "last_name", "email", "phone"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "id-exampleForm"
        #self.helper.form_class = "border "
        self.helper.form_method = "post"
        self.helper.form_action = "alist-tenant"
        self.helper.layout = Layout(
            Row(
                Column("first_name", css_class="form-group col-md-2 mb-0 mr-6"),
                Column("last_name", css_class="form-group col-md-3 mb-0 mr-6"),
                Column("email", css_class="form-group col-md-3 mb-0 mr-6"),
                Column("phone", css_class="form-group col-md-3 mb-0"),
                # css_class='form-row'
            ),
            Submit("submit", "Add Tenant", css_class="btn btn-primary"),
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


class TenantDeleteForm(forms.ModelForm):
    class Meta:
        model = Tenant
        fields = []  # No fields needed for deletion confirmation
