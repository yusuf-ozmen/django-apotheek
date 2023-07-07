from django import forms
from .models import Medicine, Collection, Profile

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    your_last_name = forms.CharField(label='Your last name', max_length=100)

class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ("name", "manufacturer", "cures", "side_effects")

class CollectionForm(forms.ModelForm):
    class Meta:
        model = Collection
        fields = ("medicine", "date", "user", "collected")

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("location", "date_of_birth", "bio")