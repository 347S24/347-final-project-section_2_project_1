from ast import Del
from pyexpat import model
from turtle import mode
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import *
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.edit import *
from django.urls import reverse, reverse_lazy
from .models import Tags,Image,Album
from django.views import generic
from django.views.generic import (
    DetailView,
    RedirectView,
    UpdateView,
)
from .forms import ImageCreateForm
from django.urls import reverse_lazy
import requests
import os

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


# class ImageCreate(PermissionRequiredMixin, ImageCreateForm):
#     model = Image
#     fields = ["name", "time_date", "description", "tags", "image_id"]
#     permission_required="user.add_image"
def galleryRequest(request):
    images = Image.objects.all()
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + request.user.socialaccount_set.all()[0].socialtoken_set.all()[0].token
    }
    for img in images:
        print(img.image_id)
        r = requests.get('https://photoslibrary.googleapis.com/v1/mediaItems/' + img.image_id, headers=headers)

        answer = r.json()['baseUrl']
        img.image_url = answer
        img.save()
    return HttpResponseRedirect("/gallery")
def imageCreate(request):
      # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = ImageCreateForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            model = form.save()
            list = os.listdir("/home/pinkstacs/347-final-project-section_2_project_1/scannergallery/media/image_uploads")
            for l in list:
                headers = {
                    'Content-Type': 'application/json',
                    'Authorization': 'Bearer ' + request.user.socialaccount_set.all()[0].socialtoken_set.all()[0].token
                }
            
                # request.user is the currently loggedin user
                # print('request.user.socialaccount_set')
                # print(request.user.socialaccount_set.all())
                # print(request.user.socialaccount_set.all()[0].socialtoken_set.all()[0].token)
                # request.user.socialaccount_set.all()[0].socialtoken_set.all()[0].token
                # read image from file
                img = "/home/pinkstacs/347-final-project-section_2_project_1/scannergallery/media/image_uploads/" + l
                with open(img, "rb") as f:
                    image_contents = f.read()

                # upload photo and get upload token
                response = requests.post(
                    "https://photoslibrary.googleapis.com/v1/uploads", 
                    headers=headers,
                    data=image_contents)
                upload_token = response.text
                response2 = requests.post(
                    'https://photoslibrary.googleapis.com/v1/mediaItems:batchCreate', 
                    headers = headers,
                    json={
                        "newMediaItems": [{
                            "description": model.description,
                            "simpleMediaItem": {
                                "uploadToken": upload_token,
                                "fileName": model.name + ".png"
                            }
                        }]
                    }
                )
                img_id = response2.json()['newMediaItemResults'][0]['mediaItem']['id']
                model.image_id = img_id
                #model.image_url = response2.json()['newMediaItemResults'][0]['mediaItem']['baseUrl']
                os.remove(img)
                print(model.image_id)
                model.save()
            return HttpResponseRedirect("/update_gallery")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ImageCreateForm()

    return render(request, "uploadimg.html", {"form": form})

# class ImageUpdate(PermissionRequiredMixin, UpdateView):
#     model = Image
#     fields = "__all__"

class ImageDelete(PermissionRequiredMixin, DeleteView):
    model = Image
    success_url = reverse_lazy("uploadimg")
    def form_valid(self, form):
        try:
            self.object.delete()
            return HttpResponseRedirect(self.success_url)
        except Exception as e:
            return HttpResponseRedirect(
                reverse("author-delete", kwargs={"pk": self.object.pk})
            )

class TagCreate(PermissionRequiredMixin, CreateView):
    model = Tags
    fields = ["name"]

class TagDelete(PermissionRequiredMixin, DeleteView):
    model = Tags
    def form_valid(self, form):
        try:
            self.object.delete()
            return HttpResponseRedirect(self.success_url)
        except Exception as e:
            return HttpResponseRedirect(
                reverse("author-delete", kwargs={"pk": self.object.pk})
            )



user_redirect_view = UserRedirectView.as_view()


