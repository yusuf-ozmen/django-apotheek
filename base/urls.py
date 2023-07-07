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
    path('medicines/', views.medicines, name='medicines'),
    path('medicines/create/', views.create_medicine, name='create_medicine'),
    path('medicines/edit/<int:id>/', views.edit_medicine, name='edit_medicine'),
    path('medicines/delete/<int:id>/', views.delete_medicine, name='delete_medicine'),
    path('pickups/', views.pickups, name='pickups'),
    path('pickups/create/', views.create_pickup, name='create_pickup'),
    path('pickups/approve/<int:id>/', views.approve_pickup, name='approve_pickup'),
    path('pickups/delete/<int:id>/', views.delete_pickup, name='delete_pickup'),
]