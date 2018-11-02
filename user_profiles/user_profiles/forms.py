# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
# from django import forms
# from django.core.exceptions import ValidationError

# class SignUpForm(UserCreationForm):
#     birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')

#     class Meta:
#         model = User
#         fields = ('username', 'birth_date', 'password1', 'password2', )

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError


class CustomUserCreationForm(forms.Form):
    username = forms.CharField(label='Enter Username', min_length=4, max_length=150)
    # email = forms.EmailField(label='Enter email')
    # TRUE_FALSE_CHOICES = ( ('is_admin', 'Admin'),('non_admin', 'Officer'))
    # utype = forms.ChoiceField(choices = TRUE_FALSE_CHOICES, label="User Profile", 
    #                           initial='', widget=forms.Select(), required=True)
    is_superuser = forms.BooleanField(label="Is Admin", initial=False)
    # is_staff 
    password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise  ValidationError("Username already exists")
        return username

    def clean_is_superuser(self):
        # import code; code.interact(local=dict(globals(), **locals()))
        is_superuser = self.cleaned_data['is_superuser']
        return is_superuser

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")

        return password2

    def save(self, commit=True):
        # import code; code.interact(local=dict(globals(), **locals()))

        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['password1'],
            self.cleaned_data['is_superuser']            
        )
        # import code; code.interact(local=dict(globals(), **locals()))
        return user
