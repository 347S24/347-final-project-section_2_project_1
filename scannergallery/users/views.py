from pyexpat import model
from turtle import mode
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from .models import Tags,Image,Album
from django.views import generic
from django.views.generic import (
    DetailView,
    RedirectView,
    UpdateView,
)

import requests

User = get_user_model()


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    # These Next Two Lines Tell the View to Index
    #   Lookups by Username
    slug_field = "username"
    slug_url_kwarg = "username"

    


user_detail_view = UserDetailView.as_view()


class UserUpdateView(LoginRequiredMixin, UpdateView):
    fields = [
        "name",
    ]

    # We already imported user in the View code above,
    #   remember?
    model = User

    # Send the User Back to Their Own Page after a
    #   successful Update
    def get_success_url(self):
        return reverse(
            "users:detail",
            kwargs={'username': self.request.user.username},
        )

    def get_object(self):
        # Only Get the User Record for the
        #   User Making the Request
        return User.objects.get(
            username=self.request.user.username
        )


user_update_view = UserUpdateView.as_view()


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse(
            "users:detail",
            kwargs={"username": self.request.user.username},
        )

class TagsDetailView(generic.DetailView):
    model=Tags


class TagsListView(generic.ListView):
    model=Tags


class ImageDetailView(generic.DetailView):
    model=Image


class ImageListView(generic.ListView):
    model=Image


class AlbumListView(generic.ListView):
    model=Album


class AlbumDetailView(generic.DetailView):
    model=Album


class ImageCreate(PermissionRequiredMixin, CreateView):
    model = Image
    fields = ["name", "time_date", "description", "tags", "image_id"]
    permission_required = 'catalog.add_image'

class ImageUpdate(PermissionRequiredMixin, UpdateView):
    model = Image
    fields = "__all__"
    permission_required = "catalog.change_image"

class ImageDelete(PermissionRequiredMixin, DeleteView):
    model = Image

    def form_valid(self, form):
        try:
            self.object.delete()
            return HttpResponseRedirect(self.success_url)
        except Exception as e:
            return HttpResponseRedirect(
                reverse("author-delete", kwargs={"pk": self.object.pk})
            )

user_redirect_view = UserRedirectView.as_view()


