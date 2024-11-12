from django.contrib import admin
from django.urls import path, include
from cinema.views import CustomAuthToken

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/cinema/", include("cinema.urls", namespace="cinema")),
    path("api/user/", include("user.urls", namespace="user")),
    path("api/token-auth/", CustomAuthToken.as_view(), name="token-auth"),
    path("__debug__/", include("debug_toolbar.urls")),
]
