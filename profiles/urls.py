from django.urls import path

from .views import profiles_index, profile

urlpatterns = [
    path("profiles/", profiles_index, name="index"),
    path("profiles/<str:username>/", profile, name="profile"),
]
