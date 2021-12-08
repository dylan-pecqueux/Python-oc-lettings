from django.urls import path

from .views import lettings_index, letting

urlpatterns = [
    path("lettings/", lettings_index, name="lettings_index"),
    path("lettings/<int:letting_id>/", letting, name="letting"),
]
