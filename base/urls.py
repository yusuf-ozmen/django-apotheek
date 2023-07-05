from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("", include('django.contrib.auth.urls')),
    path("test/", views.test, name="test"),
    path("register/", views.register, name="register"),
    path("profile/", views.edit_profile, name="profile"),
    path("collection/", views.collection, name="collection"),
    path('collection/<int:collection_id>/sign_collected/', views.sign_collected, name='sign_collected'),
]