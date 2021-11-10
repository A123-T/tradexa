from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import post


# THESE ARE THE PREDEFINED FORMS PROVIDED BY DJANGO
class SignUpForm(UserCreationForm):
    class Meta: 
        model = User
        fields = ['username','first_name','last_name','email']

class modify_post1(ModelForm):
    class Meta:
        model = post
        fields = ['text']