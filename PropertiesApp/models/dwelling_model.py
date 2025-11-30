from django.db import models
from django.core.files.base import ContentFile
from PIL import Image as PILImage
from io import BytesIO
from django.conf import settings
from django.core.files import File
from pathlib import Path
from django.core.exceptions import (
    ObjectDoesNotExist,
)  # Import the exception
import os
from django.core.files.storage import (
    default_storage,
)  # Import the storage system


class Dwelling(models.Model):
    house = models.CharField(max_length=100)
    street = models.CharField(
        max_length=100, blank=True, null=True
    )
    town = models.CharField(
        max_length=100, blank=True, null=True
    )
    county = models.CharField(
        max_length=100, blank=True, null=True
    )
    postcode = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.house} {self.street}"


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    age = models.DecimalField(
        max_digits=7, decimal_places=0
    )
    major = models.CharField(max_length=50)

    profile_image = models.ImageField(
        upload_to="images/", null=True, blank=True
    )
    profile_image_thumbnail = models.ImageField(
        upload_to="images/thumbnails/",
        null=True,
        blank=True,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Cache the initial value of the file field when the object is initialized
        self.__original_profile_image = self.profile_image

    new_record = True
    thumb_req = False
    original_image_name = ""
    new_image_name = ""
    original_profile_image_path = ""
    NewRecordFlagFromFormSubmit = True
    IsNewRecord = True
    IsThumbnailRequired = True
    IsEditing = False
    HasFormImage = None
    HasOriginalImage = None
    OriginalStudent = None
    OriginalImageFilePath = ""

    def save(self, *args, **kwargs):

        isNewRecord = self._state.adding
        userHasSubmittedProfileImage = bool(self.profile_image)
        profileImageName = self.profile_image.name
        profileImagePath = Path(self.profile_image.name)
        # hasThumbnailImage = bool(self.profile_image_thumbnail)
        # thumbnailImageName = self.profile_image_thumbnail.name
        # thumbnailImagePath = Path(self.profile_image_thumbnail.name)

        # get a pk
        #is this an add new record
        if isNewRecord:
            super().save(*args, **kwargs)
            # has a image been submitted by the user
            if userHasSubmittedProfileImage:
                #if yes then do all the add record stuff
                # name the image
                new_image_name = f"profile_{self.first_name}_{self.last_name}_{self.pk}{profileImagePath.suffix}"

                #save image
                self.profile_image.save(
                    new_image_name,
                    self.profile_image.file,
                    False,
                )
                # create thumbnail
                thumb_file = (
                    self.CreateThumbnailImage()
                )
                newNamePath = Path(self.profile_image.name) 
                thumbnail_name = f"{newNamePath.stem}_thumbnail{newNamePath.suffix}"       
                # Save the thumbnail with the new name
                self.profile_image_thumbnail.save(
                    thumbnail_name,
                    thumb_file,
                    False,
                )
                # update the database
                super().save(*args, **kwargs)

                pass
                # Use the default storage to delete the *old* path string
                if default_storage.exists(f"images/{profileImagePath}"):
                    try:
                        default_storage.delete(
                            f"images/{profileImagePath}"
                        )
                    except:
                        pass
 
            pass
        elif not isNewRecord:
            # get the current record
            currentRecord = (self.__class__.objects.get(
                            pk=self.pk ))
            if userHasSubmittedProfileImage:

                # # get the current profile image path from the record
                # currentImagePath = Path(currentRecord.profile_image.name)
                # try:
                #     currentRecord.profile_image.file.close()
                # except:
                #     pass
                currentThumbnailPath = Path(
                    currentRecord.profile_image_thumbnail.name
                )
                # #currentImagePath = currentRecord.profile_image

                # # name the image
                new_image_name = f"profile_{self.first_name}_{self.last_name}_{self.pk}{profileImagePath.suffix}"
                # # Use the default storage to delete the *old* path string
                # if default_storage.exists(
                #     currentImagePath
                # ):
                #     try:
                #         default_storage.delete(
                #             currentImagePath
                #         )
                #     except Exception as e:
                #         # Handle only true *errors* like permissions or connection failures
                #         print(f"Failed to delete file that exists: {e}")
                                #save image
                self.profile_image.save(
                    new_image_name,
                    self.profile_image.file,
                    False,
                )
                # create thumbnail
                thumb_file = (
                    self.CreateThumbnailImage()
                )
                newNamePath = Path(self.profile_image.name)
                # Use the default storage to delete the *old* path string
                if default_storage.exists(
                    currentThumbnailPath
                ):
                    try:
                        default_storage.delete(
                            currentThumbnailPath
                        )
                    except:
                        pass
                thumbnail_name = f"{newNamePath.stem}_thumbnail{newNamePath.suffix}"       
                # Save the thumbnail with the new name
                self.profile_image_thumbnail.save(
                    thumbnail_name,
                    thumb_file,
                    False,
                )

            # user has not submitted a profile image
            else:
                pass

            # update the database
            super().save(*args, **kwargs)
            pass

        #or an edit
        # else:
        #     pass
        # crash out for now

        return

        # get flag from form submission kwarg. if its None the this is a recursive call so dont change the value
        # self.NewRecordFlagFromFormSubmit = kwargs.pop(
        #     "isNewRecord", self.NewRecordFlagFromFormSubmit
        # )
        # self.new_record = flagFromFormSubmit if flagFromFormSubmit is not None else self.IsEditing
        # if not self.new_record: self.IsEditing = True

        # is it a new record  self.__original_file_upload = self.file_upload

        if self.NewRecordFlagFromFormSubmit:
            try:
                # so do the new record stuff
                if (
                    self.IsNewRecord
                    or self.IsThumbnailRequired
                ):
                    # Save to generate primary key if it's a new record
                    super().save(*args, **kwargs)

                    # Determine if there is a form image and if it has not yet been saved
                    self.HasFormImage = bool(
                        self.HasExistingProfileImage()
                    )
                    if (
                        self.HasFormImage
                        and self.IsNewRecord
                    ):
                        self.CreateProfileImage()
                        # set the flag to stop this 'if' running next time round
                        self.IsNewRecord = False
                        # Save the profile image with the new name
                        # this will make a recursive call to def save, ie this method
                        self.profile_image.save(
                            self.new_image_name,
                            self.profile_image.file,
                            True,
                        )
                    # if not a new record, is it a thumbnail
                    elif self.IsThumbnailRequired:
                        # Create thumbnail and generate thumbnail name
                        thumb_file = (
                            self.CreateThumbnailImage()
                        )
                        new_image_name_path = Path(
                            self.new_image_name
                        )
                        new_thumbnail_name = f"{self.new_image_name_path.stem}_thumbnail{self.new_image_name_path.suffix}"

                        # set the flag to stop this 'if' running next time
                        self.IsThumbnailRequired = False
                        # self.IsEdit = True
                        # Save the thumbnail with the new name
                        # recursive call
                        self.profile_image_thumbnail.save(
                            new_thumbnail_name,
                            thumb_file,
                            True,
                        )
                # supersave
                super().save(*args, **kwargs)  #  save
            except:
                pass

        # is it an edit
        elif not self.NewRecordFlagFromFormSubmit:
            try:
                # Get the original object if the first time here
                if not self.OriginalStudent:
                    self.OriginalStudent = (
                        self.__class__.objects.get(
                            pk=self.pk
                        )
                    )
                # Student.new_record = False
                # original_profile_image_path = (
                #     original_obj.profile_image.path
                #     if original_obj.profile_image
                #     else None
                # )
                self.HasFormImage = (
                    self.HasExistingProfileImage()
                )
                self.HasOriginalImage = bool(
                    self.OriginalStudent.profile_image
                )

                # Determine if there is a form image
                if self.HasFormImage:
                    # there is a form image
                    # is it a new record, ie first time round the method ###bad name##
                    if self.IsNewRecord:
                        # Construct the new filename for the profile image
                        form_image_path = Path(
                            self.profile_image.name
                        )
                        self.new_image_name = f"profile_{self.first_name}_{self.last_name}_{self.pk}{form_image_path.suffix}"
                        # set the flag
                        self.IsNewRecord = False
                        # Save the profile image with the new name
                        self.profile_image.save(
                            self.new_image_name,
                            self.profile_image.file,
                            True,
                        )
                    # no been round already and new profile image is saved to disk and db
                    # so have we done the thumbnail?
                    elif self.IsThumbnailRequired == True:
                        # not been here before so create thumbnail
                        thumb_file = (
                            self.CreateThumbnailImage()
                        )
                        new_image_name_path = Path(
                            self.new_image_name
                        )

                        # crerate thumbnail name
                        form_image_path = Path(
                            self.profile_image.name
                        )
                        new_image_name = f"profile_{self.first_name}_{self.last_name}_{self.pk}{form_image_path.suffix}"

                        new_thumbnail_name = f"{new_image_name.stem}_thumbnail{new_image_name.suffix}"

                        # super().save(*args, **kwargs)  #  save

                        # set the flag to say we've done this thumbnail
                        self.IsThumbnailRequired = False

                        # Save the thumbnail with the new name
                        self.profile_image_thumbnail.save(
                            new_thumbnail_name,
                            thumb_file,
                            True,
                        )
                    # done! end of if and elif
                    # nextime round we will land here
                    # If there's an original image, delete it
                    if (
                        original_profile_image_path
                        and os.path.isfile(
                            original_profile_image_path
                        )
                    ):
                        os.remove(
                            original_profile_image_path
                        )

                if (
                    not self.HasExistingProfileImage()
                    and not originalStudent.profile_image
                ):
                    # Call the original save method to save any other model fields
                    super().save(*args, **kwargs)
                    return
                #
                else:
                    pass

                # Check if we need to remove the old profile image
                # if there is an image and current image path          and
                #       = true        and    37.41       = true       and       37.41       = true                     34.49
                if (
                    self.profile_image
                    and original_profile_image_path
                    and original_profile_image_path
                    != self.profile_image.path
                ):
                    pass
                    if os.path.isfile(
                        original_profile_image_path
                    ):
                        os.remove(
                            original_profile_image_path
                        )  # Remove the old image

                    # Construct the new filename for the updated profile image
                    original_image_name = Path(
                        self.profile_image.name
                    )
                    new_image_name = f"profile_{self.first_name}_{self.last_name}_{self.pk}{original_image_name.suffix}"

                    # Create thumbnail and generate thumbnail name
                    thumb_file = (
                        self.CreateThumbnailImage()
                    )  ###error here
                    new_image_name_path = Path(
                        new_image_name
                    )
                    new_thumbnail_name = f"{new_image_name_path.stem}_thumbnail{original_image_name.suffix}"

                    # Save the profile image with the new name
                    self.profile_image.save(
                        new_image_name,
                        self.profile_image.file,
                        True,
                    )
                    # Save the thumbnail with the new name
                    self.profile_image_thumbnail.save(
                        new_thumbnail_name, thumb_file, True
                    )
            except self.__class__.DoesNotExist:
                # Handle the case where the object does not exist
                # This is usually not expected but can be a safeguard
                pass
            # Call the original save method to save any other model fields
            super().save(*args, **kwargs)

        # neither !??
        else:
            pass

    def HasExistingProfileImage(self):
        return bool(
            self.profile_image
            and hasattr(self.profile_image, "file")
            and self.profile_image.file
        )

    def CreateThumbnailImage(self):
        """Create a thumbnail"""

        # Open the original image
        img = PILImage.open(self.profile_image)

        # Specify the thumbnail size
        img.thumbnail((
            50,
            50,
        ))
        # Save the thumbnail to a BytesIO object
        thumb_io = BytesIO()

        # Save as JPEG or PNG
        img.save(thumb_io, format="JPEG")

        # Return as ContentFile
        return ContentFile(thumb_io.getvalue())

    def CreateProfileImage(self):
        # Construct the new filename for the profile image
        self.original_profile_image_name = Path(
            self.profile_image.name
        )
        self.original_profile_image_path = os.path.join(
            settings.MEDIA_ROOT,
            "images",
            self.original_profile_image_name,
        )
        self.new_image_name = f"profile_{self.first_name}_{self.last_name}_{self.pk}{self.original_profile_image_name.suffix}"
        return


    def save2(self, *args, **kwargs):
        isNew = self._state.adding
        super().save(*args, **kwargs)
        #is this an add
        if self._state.adding:
            # has a image been submitted by the user
            if self.profile_image:
                #if yes then do all the add record stuff
                a = self.profile_image.name
                pass
            pass
            

        #or an edit
        else:
            pass
            


    def save1(self, *args, **kwargs):
        # does it have a pk
        self.not_got_a_pk = self.pk is None
        if (
            self.not_got_a_pk
        ):  # D1 - no pk so its a new record
            print(Student.new_record)
            # Save to generate primary key if it's a new record
            super().save(*args, **kwargs)  # Initial save
            if (
                self.HasExistingProfileImage()
            ):  # D2 - Determine if there is a form image
                # Construct the new filename for the profile image
                self.original_profile_image_name = Path(
                    self.profile_image.name
                )
                self.original_profile_image_path = (
                    os.path.join(
                        settings.MEDIA_ROOT,
                        "images",
                        self.original_profile_image_name,
                    )
                )
                self.new_image_name = f"profile_{self.first_name}_{self.last_name}_{self.pk}{self.original_profile_image_name.suffix}"
                self.not_got_a_pk = False
                # Save the profile image with the new name
                self.profile_image.save(
                    self.new_image_name,
                    self.profile_image.file,
                    True,
                )
            if self.thumb_req:  # D3 - if not a new record, is it a thumbnail
                # Create thumbnail and generate thumbnail name
                thumb_file = self.CreateThumbnailImage()
                new_image_name_path = Path(
                    self.new_image_name
                )
                new_thumbnail_name = f"{new_image_name_path.stem}_thumbnail{new_image_name_path.suffix}"
                self.thumb_req = False
                # Save the thumbnail with the new name
                self.profile_image_thumbnail.save(
                    new_thumbnail_name, thumb_file, True
                )
            # supersave
            super().save(*args, **kwargs)  #  save
            # # If there's an original image, delete it
            ## this isnt working because of a file permissions error

            # self.original_profile_image_path = os.path.join(settings.MEDIA_ROOT, self.original_image_name)
            # if self.original_profile_image_path and os.path.isfile(
            #     self.original_profile_image_path
            # ):
            #     os.remove(self.original_profile_image_path)

        else:
            # must already have a pk so its an edit
            # image options when starting this code are ...
            # 1 there is no form image (there never was or the user has cleared the image )
            # 2 the forms image is the same as the db record
            # 3 the form image is different to the db record (user has chosen a new image)
            try:
                # return
                # Get the original object
                print(Student.new_record)

                original_obj = self.__class__.objects.get(
                    pk=self.pk
                )
                Student.new_record = False
                original_profile_image_path = (
                    original_obj.profile_image.path
                    if original_obj.profile_image
                    else None
                )

                # Determine if there is a form image
                if self.HasExistingProfileImage():
                    # there is a form image

                    # save the new image with its thumbnail
                    # Construct the new filename for the profile image
                    original_image_name = Path(
                        self.profile_image.name
                    )
                    new_image_name = f"profile_{self.first_name}_{self.last_name}_{self.pk}{original_image_name.suffix}"

                    # Create thumbnail and generate thumbnail name
                    thumb_file = self.CreateThumbnailImage()
                    new_image_name_path = Path(
                        new_image_name
                    )
                    new_thumbnail_name = f"{new_image_name_path.stem}_thumbnail{new_image_name_path.suffix}"

                    # Save the profile image with the new name
                    self.profile_image.save(
                        new_image_name,
                        self.profile_image.file,
                        True,
                    )
                    # Save the thumbnail with the new name
                    self.profile_image_thumbnail.save(
                        new_thumbnail_name, thumb_file, True
                    )
                    # If there's an original image, delete it
                    if (
                        original_profile_image_path
                        and os.path.isfile(
                            original_profile_image_path
                        )
                    ):
                        os.remove(
                            original_profile_image_path
                        )

                if (
                    not self.HasExistingProfileImage()
                    and not original_obj.profile_image
                ):
                    # Call the original save method to save any other model fields
                    super().save(*args, **kwargs)
                    return
                #
                else:
                    pass

                # Check if we need to remove the old profile image
                # if there is an image and current image path          and
                #       = true        and    37.41       = true       and       37.41       = true                     34.49
                if (
                    self.profile_image
                    and original_profile_image_path
                    and original_profile_image_path
                    != self.profile_image.path
                ):
                    pass
                    if os.path.isfile(
                        original_profile_image_path
                    ):
                        os.remove(
                            original_profile_image_path
                        )  # Remove the old image

                    # Construct the new filename for the updated profile image
                    original_image_name = Path(
                        self.profile_image.name
                    )
                    new_image_name = f"profile_{self.first_name}_{self.last_name}_{self.pk}{original_image_name.suffix}"

                    # Create thumbnail and generate thumbnail name
                    thumb_file = self.CreateThumbnailImage()
                    new_image_name_path = Path(
                        new_image_name
                    )
                    new_thumbnail_name = f"{new_image_name_path.stem}_thumbnail{new_image_name_path.suffix}"

                    # Save the profile image with the new name
                    self.profile_image.save(
                        new_image_name,
                        self.profile_image.file,
                        True,
                    )
                    # Save the thumbnail with the new name
                    self.profile_image_thumbnail.save(
                        new_thumbnail_name, thumb_file, True
                    )
                pass

            except self.__class__.DoesNotExist:
                # Handle the case where the object does not exist
                # This is usually not expected but can be a safeguard
                pass

            # Call the original save method to save any other model fields
            super().save(*args, **kwargs)
