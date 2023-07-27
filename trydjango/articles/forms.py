from dataclasses import field
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

from django.core.validators import validate_email

class RegisterForm(UserCreationForm):
    

    class meta:
        model = User

        fields = ['']
    
    def cleaned(self, *args, **kwargs):
        data = self.cleaned_data

        title = data.get('title')
        qs = User.objects.all().filter(title__iexact=title)
        if qs.exists():
            self.add_error("Title is already taken")
        return data 
        