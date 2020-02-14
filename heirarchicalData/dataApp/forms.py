from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import File

class AddFileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ('name', 'folder', 'parent')

    def __init__(self, user, *args, **kwargs):
        super(AddFileForm, self).__init__(*args, **kwargs)
        self.fields['parent'].queryset = File.objects.filter(folder=True, user=user)

class LoginForm(forms.Form):
    username = forms.CharField(max_length=40)
    password = forms.CharField(widget=forms.PasswordInput)


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Please enter a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')