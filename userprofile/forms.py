from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username':forms.TextInput(attrs={'placeholder':'Username','id':'username' }),
            'email': forms.EmailInput(attrs={'placeholder':'Email', 'id':'email'}),
            # 'password1': forms.PasswordInput(attrs={'placeholder':'Password','id':'password1'}),
            # 'password2': forms.PasswordInput(attrs={'id':'password2'})
        }
    
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super().__init__(*args, **kwargs)    
        self.fields['password1'].widget = forms.PasswordInput(attrs={'placeholder': (" Enter Password"), })
        self.fields['password2'].widget = forms.PasswordInput(attrs={'placeholder': ("Enter Password Again")})