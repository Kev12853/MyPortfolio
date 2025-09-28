from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy

from PropertiesApp.models.dwelling_model import Dwelling
from PropertiesApp.forms.dwelling_forms import (
    DwellingCreateForm,
    DwellingDeleteForm,
    DwellingDetailForm,
    DwellingListForm,
    DwellingUpdateForm,
)


class DwellingCreateView(CreateView):
    model = Dwelling
    form_class = DwellingCreateForm
    template_name = "PropertiesApp/user_input/f_create_dwelling.html"
    success_url = reverse_lazy("list-dwelling")


class DwellingListView(ListView):
    model = Dwelling
    form_class = DwellingListForm
    context_object_name = "dwellings"
    template_name = "PropertiesApp/list_dwelling.html"


class DwellingDetailView(DetailView):
    model = Dwelling
    form_class = DwellingDetailForm
    context_object_name = "dwelling"
    template_name = "PropertiesApp/detail_dwelling.html"


class DwellingUpdateView(UpdateView):
    model = Dwelling
    form_class = DwellingUpdateForm
    template_name = "PropertiesApp/user_input/f_update_dwelling.html"
    success_url = reverse_lazy("list-dwelling")


class DwellingDeleteView(DeleteView):
    model = Dwelling
    form_class = DwellingDeleteForm
    template_name = "PropertiesApp/user_input/f_delete_dwelling.html"
    success_url = reverse_lazy("list-dwelling")
