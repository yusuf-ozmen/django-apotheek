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

    collection.collected = True
    collection.save()
    messages.success(request, 'Medicine marked as collected.')

    return redirect('collection')

@staff_member_required
def medicines(request):
    medicines = Medicine.objects.all()
    return render(request, 'base/medicines.html', {'medicines': medicines})

@staff_member_required
def create_medicine(request):
    if request.method == 'POST':
        form = MedicineForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Medicine created.")
            return redirect('medicines')
    else:
        form = MedicineForm()
    return render(request, 'base/create_medicine.html', {'form': form})

@staff_member_required
def edit_medicine(request, id):
    medicine = Medicine.objects.get(pk=id)
    if request.method == 'POST':
        form = MedicineForm(request.POST, instance=medicine)
        if form.is_valid():
            form.save()
            messages.success(request, "Medicine edited.")
            return redirect('medicines')
    else:
        form = MedicineForm(instance=medicine)
    return render(request, 'base/edit_medicine.html', {'form': form})

@staff_member_required
def delete_medicine(request, id):
    medicine = Medicine.objects.get(pk=id)
    if request.method == 'POST':
        medicine.delete()
        messages.success(request, "Medicine deleted.")
        return redirect('medicines')
    return render(request, 'base/delete_medicine.html', {'medicine': medicine})

@staff_member_required
def pickups(request):
    pickups = Collection.objects.all()
    return render(request, 'base/pickups.html', {'pickups': pickups})

@staff_member_required
def create_pickup(request):
    if request.method == 'POST':
        form = CollectionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Pick up created.")
            return redirect('pickups')
    else:
        form = CollectionForm()
    return render(request, 'base/create_pickup.html', {'form': form})

@staff_member_required
def approve_pickup(request, id):
    pickup = Collection.objects.get(pk=id)
    pickup.collectedapproved = True
    pickup.collectedapproved_by = request.user
    pickup.save()
    messages.success(request, "Pick up approved.")
    return redirect('pickups')

@staff_member_required
def delete_pickup(request, id):
    pickup = Collection.objects.get(pk=id)
    if request.method == 'POST':
        pickup.delete()
        messages.success(request, "Pick up deleted.")
        return redirect('pickups')
    return render(request, 'base/delete_pickup.html', {'pickup': pickup})
