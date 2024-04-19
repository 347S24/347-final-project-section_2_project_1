from cProfile import label
from tkinter import Widget
from django.contrib.auth import get_user_model, forms
# from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .models import *

User = get_user_model()


class UserChangeForm(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model = User


class UserCreationForm(forms.UserCreationForm):

    error_message = forms.UserCreationForm.error_messages.update(
        {
            "duplicate_username": _(
                "This username has already been taken."
            )
        }
    )

    class Meta(forms.UserCreationForm.Meta):
        model = User

    def clean_username(self):
        username = self.cleaned_data["username"]

        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username

        raise ValidationError(
            self.error_messages["duplicate_username"]
        )

# class ImageCreationForm(forms.Form):
#     name= forms.CharField(help_text="Name your image")
#     time_date=forms.DateTimeField(help_text="")
#     description=forms.CharField(help_text="Enter image description")
#     tags=forms.ModelMultipleChoiceField(
#         queryset=Tags.objects.all().order_by('name'),
#         label="Tags",
#         widget=forms.SelectMultiple
#     )
