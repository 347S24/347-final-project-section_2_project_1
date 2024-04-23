from cProfile import label
from tkinter import Widget
from attr import fields
from django.contrib.auth import get_user_model, forms
from django import forms as dj_forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .models import *
from django.forms import widgets


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

class ImageCreateForm(dj_forms.ModelForm):
    # name = dj_forms.CharField()
    # time_date = dj_forms.DateTimeField()
    # description = dj_forms.CharField()
    # tags = dj_forms.ModelMultipleChoiceField(queryset=Tags.objects.all(), widget=dj_forms.CheckboxSelectMultiple)

    class Meta:
        model = Image
        exclude=["image_id"]
        widgets={'time_date':widgets.DateInput(attrs={'type': 'date'})} 



