from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
from PropertiesApp.models.tenant_model import Tenant
from django.views.generic import TemplateView
from pathlib import Path

from PropertiesApp.models.dwelling_model import Dwelling, Student
from PropertiesApp.forms.dwelling_forms import (
    DwellingCreateForm,
    DwellingDeleteForm,
    DwellingDetailForm,
    DwellingListForm,
    DwellingUpdateForm,
)
from PropertiesApp.forms.tenant_forms import (
    Tenant_Form,
    TenantCreateForm,
    TenantListForm,
    TenantDetailForm,
    TenantDeleteForm,
)


from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django import forms
from django.forms import modelform_factory
# Create your views here.


class HomePageView(TemplateView):
    template_name = "students/studenthome.html"


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = []


def get_student_list(request):
    context = {}
    students = Student.objects.all()
    for student in students:
        if student.profile_image:
            original_url = student.profile_image.url
            student.profile_image_url = original_url.lstrip(
                "/"
            )  # Removes leading slashes
            if student.profile_image_thumbnail:
                # original_url = student.profile_image_thumbnail.url
                student.profile_image_thumbnail_url = original_url.lstrip(
                    "/"
                )  # Removes leading slashes
            else:
                student.profile_image_thumbnail_url = original_url.lstrip(
                    "/"
                )  # Removes leading slashes
        else:
            student.profile_image_url = (
                "mymedia/images/IMG_2104.jpg"  # Provide a path to a default image
            )
        print("Profile Image URL:", student.profile_image_url)
    context["students"] = students

    return render(request, "students/partials/student_list.html", context)


def add_student(request):
    context = {"form": StudentForm()}
    return render(request, "students/partials/add_student.html", context)


def add_student_submit(request):
    context = {}
    form = StudentForm(request.POST, request.FILES)
    context["form"] = form
    if form.is_valid():
        context["student"] = form.save()
        student = context["student"]
        if student.profile_image:  # if there is an image
            original_url = student.profile_image.url            
            student.profile_image_url = original_url.lstrip("/")  # Removes leading slashes
            if student.profile_image_thumbnail:  # if there is an thumbnail image
                thumbnail_url = student.profile_image_thumbnail.url
                student.profile_image_thumbnail_url = thumbnail_url.lstrip(
                    "/"
                )  # Removes leading slashes
            else:
                student.profile_image_thumbnail_url = original_url.lstrip(
                    "/"
                )  # Removes leading slashes
        else:  # no image proided so use place holder image
            student.profile_image_url = (
                "mymedia/images/IMG_2104.jpg"  # Provide a path to a default image
            )
    else:
        return render(request, "students/partials/add_student.html", context)
        # if here then form is valid and has been saved or is a get request so has been
        # so prepare the image url's
       
    return render(request, "students/partials/student_row.html", context)


def add_student_cancel(request):
    return HttpResponse()


def edit_student(request, student_pk):
    student = Student.objects.get(pk=student_pk)
    context = {}
    context["student"] = student
    context["form"] = StudentForm(
        initial={
            "first_name": student.first_name,
            "last_name": student.last_name,
            "gender": student.gender,
            "age": student.age,
            "major": student.major,
            "profile_image": student.profile_image
        }
    )
    return render(request, "students/partials/edit_student.html", context)


@require_http_methods(["GET", "POST"])
def edit_student_submit(request, student_pk):
    context = {}
    student = Student.objects.get(pk=student_pk)
    context["student"] = student
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()    
        else: #form not valid so go straight back
            return render(request, "students/partials/edit_student.html", context)

    # if here then form is valid and has been saved or is a get request so has been
    # so prepare the image url's
    if student.profile_image: #if there is an image
        original_url = student.profile_image.url
        student.profile_image_url = original_url.lstrip(
            "/"
        )  # Removes leading slashes
        if student.profile_image_thumbnail:
            # original_url = student.profile_image_thumbnail.url
            student.profile_image_thumbnail_url = original_url.lstrip(
                "/"
            )  # Removes leading slashes
        else:
            student.profile_image_thumbnail_url = original_url.lstrip(
                "/"
            )  # Removes leading slashes
    else: # no image proided so use place holder image
        student.profile_image_url = (
            "mymedia/images/IMG_2104.jpg"  # Provide a path to a default image
        )

    # update the html
    print("Profile Image URL:", student.profile_image_url)
    return render(request, "students/partials/student_row.html", context)


def delete_student(request, student_pk):
    student = Student.objects.get(pk=student_pk)
    student.delete()
    return HttpResponse()


# =============================================================================
class DwellingHomeView(CreateView):
    form_class = Tenant_Form
    template_name = "tenants/add-tenant-modal.html"
    success_url = reverse_lazy("dwellings")

    def form_valid(self, form):
        # Set the user before saving the form if you have logged in users
        # tenant = form.save(commit=False)
        # tenant.user = self.request.user

        tenant = form.save()
        # Prepare response for htmx
        context = {"tenant": tenant}
        response = render(self.request, "tenants/tenant_row.html", context)
        response["HX-Trigger"] = "tenant-added"
        return response

    def get(self, request, *args, **kwargs):
        form = Tenant_Form()
        context = {"form": form, "tenants": Tenant.objects.all()}
        return render(request, "dwellings/dwellings.html", context)


class DwellingCreateView(CreateView):
    model = Dwelling
    form_class = DwellingCreateForm
    template_name = "PropertiesApp/f_create_dwelling.html"
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
    template_name = "PropertiesApp/f_update_dwelling.html"
    success_url = reverse_lazy("list-dwelling")


class DwellingDeleteView(DeleteView):
    model = Dwelling
    form_class = DwellingDeleteForm
    template_name = "PropertiesApp/f_delete_dwelling.html"
    success_url = reverse_lazy("list-dwelling")
