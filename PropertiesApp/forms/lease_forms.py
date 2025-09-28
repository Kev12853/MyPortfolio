from django import forms
from django.forms import ModelForm

from PropertiesApp.models.dwelling_model import Dwelling
from PropertiesApp.models.lease_model import Lease


class LeaseCreateForm(ModelForm):
    class Meta:
        model = Lease
        fields = ["tenant", "dwelling", "start_date", "end_date", "rent_amount"]

    def get_form(self, form_class=None):
        form = super(LeaseCreateForm, self).get_form(form_class)
        form.fields["start_date"].widget = forms.DateInput(attrs={"type": "date"})
        form.fields["end_date"].widget = forms.DateInput(attrs={"type": "date"})
        form.fields["rent_amount"].widget = forms.DateInput(
            attrs={"type": "number", "step": "10"}
        )
        return form


class LeaseListForm(ModelForm):
    class Meta:
        model = Lease
        fields = ["tenant", "dwelling", "start_date", "end_date", "rent_amount"]


class LeaseDetailView(ModelForm):
    class Meta:
        model = Lease
        fields = ["tenant", "dwelling", "start_date", "end_date", "rent_amount"]


class LeaseUpdateForm(ModelForm):
    class Meta:
        model = Lease
        fields = ["tenant", "dwelling", "start_date", "end_date", "rent_amount"]


class LeaseDeleteForm(ModelForm):
    class Meta:
        model = Lease
        fields = []  # No fields needed for deletion confirmation
