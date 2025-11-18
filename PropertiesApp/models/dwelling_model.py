from django.db import models
from django.core.files.base import ContentFile
from PIL import Image as PILImage
from io import BytesIO
from django.core.files import File
from pathlib import Path
from django.core.exceptions import ObjectDoesNotExist  # Import the exception
import os


class Dwelling(models.Model):
    house = models.CharField(max_length=100)
    street = models.CharField(max_length=100, blank=True, null=True)
    town = models.CharField(max_length=100, blank=True, null=True)
    county = models.CharField(max_length=100, blank=True, null=True)
    postcode = models.CharField(max_length=20)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.house} {self.street}"


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    age = models.DecimalField(max_digits=7, decimal_places=0)
    major = models.CharField(max_length=50)
    profile_image = models.ImageField(upload_to="images/", null=True, blank=True)
    profile_image_thumbnail = models.ImageField(
        upload_to="images/thumbnails/", null=True, blank=True
    )

    def create_thumbnail(self):
        # Open the original image
        img = PILImage.open(self.profile_image)

        # Create a thumbnail
        img.thumbnail((50, 50))  # Specify the thumbnail size

        # Save the thumbnail to a BytesIO object
        thumb_io = BytesIO()
        img.save(thumb_io, format="JPEG")  # Save as JPEG or PNG
        return ContentFile(thumb_io.getvalue())  # Return as ContentFile

    def save(self, *args, **kwargs):
        # Save to generate primary key if it's a new instance
        is_new_instance = not self.pk
        if is_new_instance:
            super().save(*args, **kwargs)  # Initial save
            original_profile_image_path = (
                self.profile_image.path if self.profile_image else None
            )
            # Construct the new filename for the profile image
            original_image_name = Path(self.profile_image.name)
            new_image_name = f"profile_{self.first_name}_{self.last_name}_{self.pk}{original_image_name.suffix}"

            # Create thumbnail and generate thumbnail name
            thumb_file = self.create_thumbnail()
            new_image_name_path = Path(new_image_name)
            new_thumbnail_name = (
                f"{new_image_name_path.stem}_thumbnail{new_image_name_path.suffix}"
            )

            # Save the profile image with the new name
            self.profile_image.save(new_image_name, self.profile_image.file, True)
            # Save the thumbnail with the new name
            self.profile_image_thumbnail.save(new_thumbnail_name, thumb_file, True)
            # If there's an original image, delete it
            if original_profile_image_path and os.path.isfile(
                original_profile_image_path
            ):
                os.remove(original_profile_image_path)

            # Call the original save method to save any other model fields
            super().save(*args, **kwargs)
        else: # must already have a pk
            pass
        pass
