import datetime
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Profile, Medicine, Collection
from .forms import NameForm, MedicineForm, CollectionForm, ProfileForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.

def test(request):
    return HttpResponse("test");

def index(request):
    return render(request, "base/index.html")

def register(requests):
    if requests.method == "POST":
        form = UserCreationForm(requests.POST)
        if form.is_valid():
            user = form.save()
            login(requests, user)
            return redirect("index")
    else:
        form = UserCreationForm()
    
    context = {"form": form}
    return render(requests, "registration/register.html", context)

@login_required
def edit_profile(request):
    profile = Profile.objects.get(user=request.user)
    
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully")
            return redirect("profile")
    else:
        form = ProfileForm(instance=profile)
    
    context = {"form": form}
    return render(request, "base/profile.html", context)

@login_required
def collection(request):
    user = request.user
    collections = Collection.objects.filter(user=user)
    return render(request, 'base/collection.html', {'collections': collections})

@login_required
def sign_collected(request, collection_id):
    collection = Collection.objects.get(pk=collection_id)

    if collection.collectedapproved:
        collection.collected = True
        collection.save()
        messages.success(request, 'Medicine marked as collected.')
    else:
        messages.error(request, 'Medicine must first be approved by an admin.')

    return redirect('collection')