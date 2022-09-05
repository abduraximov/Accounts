from django.db import models
from django.forms import ModelForm
from .models import accounts

class CreateForm(ModelForm):
    class Meta:
        model = accounts
        fields = '__all__'