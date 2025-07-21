from django.urls import path
from . import views

urlpatterns = [
  path("userprofiles/", views.UserProfileListCreate.as_view(), name="userprofile-view-create")
]