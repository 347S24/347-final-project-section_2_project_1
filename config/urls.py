from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views

# looked at doc for pyhthon module search path https://docs.python.org/3/library/sys_path_init.html
from scannergallery.users.views import ImageListView
# import sys

# print('\n\n\n\n\n\n\n')
# print(sys.path)
# print('\n\n\n\n\n\n\n')


urlpatterns = [
    path(
        "",
        TemplateView.as_view(template_name="pages/home.html"),
        name="home",
    ),
    path(
        "about/",
        TemplateView.as_view(template_name="pages/about.html"),
        name="about",
    )
    ,path(
        "settings/",
        TemplateView.as_view(template_name="pages/settings.html"),
        name="settings",
    # ),path(
    #     "gallery/",
    #     TemplateView.as_view(template_name="pages/gallery.html"),
    #     name="gallery",
    ),path(
        "gallery",
         ImageListView.as_view(),
        name="gallery"
    ),path(
        "uploadimg/",
        TemplateView.as_view(template_name="pages/uploadimg.html"),
        name="uploadimg",
    ),path(
        "auth/settings/",
        TemplateView.as_view(template_name="pages/auth.html"),
        name="auth",
    ),path(
        "auth/gallery/",
        TemplateView.as_view(template_name="pages/auth.html"),
        name="auth2",
    ),path(
        "auth/uploadimg/",
        TemplateView.as_view(template_name="pages/auth.html"),
        name="auth3",
    ),
    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls),
    # User management
    path(
        "users/",
        include("scannergallery.users.urls", namespace="users"),
    ),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('accounts/', include('allauth.socialaccount.urls')),
    path("accounts/", include("allauth.urls")),

    

    # Your stuff: custom urls includes go here
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [
            path("__debug__/", include(debug_toolbar.urls))
        ] + urlpatterns
