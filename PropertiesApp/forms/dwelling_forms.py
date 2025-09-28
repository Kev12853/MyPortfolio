from django.forms import ModelForm
from PropertiesApp.models.dwelling_model import Dwelling


class DwellingCreateForm(ModelForm):
    class Meta:
        model = Dwelling
        fields = ["house", "street", "town", "county", "postcode"]


class DwellingListForm(ModelForm):
    class Meta:
        model = Dwelling
        fields = ["house", "street", "town", "county", "postcode"]


class DwellingDetailForm(ModelForm):
    class Meta:
        model = Dwelling
        fields = ["house", "street", "town", "county", "postcode"]


class DwellingUpdateForm(ModelForm):
    class Meta:
        model = Dwelling
        fields = ["house", "street", "town", "county", "postcode"]


class DwellingDeleteForm(ModelForm):
    class Meta:
        model = Dwelling
        fields = []  # No fields needed for deletion
