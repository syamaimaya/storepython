from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . models import Department

class Register(UserCreationForm):
    username=forms.CharField(max_length=50)

    class Meta:
        model = User
        fields=['username','password1','password2']

    def save(self, commit=True):
        user=super(Register,self).save(commit=False)
        if commit:
            user.save()
        return user