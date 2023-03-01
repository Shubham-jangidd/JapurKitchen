from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import  validate_email
from django.utils.translation import gettext, gettext_lazy as _
from django.forms import ModelForm
from .models import contactus



class LoginForm(AuthenticationForm):
    # username = UsernameField(widget=forms.TextInput(
    #     attrs={'autofocus': True, 'class': 'form-control', }))
    username = forms.CharField(label='Email', required=True,
                            widget=forms.EmailInput(
                                attrs={'class': 'form-control'}), validators=[validate_email])
    password = forms.CharField(label=_("Password"), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'current-password', 'class': 'form-control'}))

class CustomerRegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm Password',
                                widget=forms.PasswordInput(
                                    attrs={'class': 'form-control'}))

    email = forms.EmailField(
        label=_("Email"), max_length=254, widget=forms.EmailInput(
            attrs={'autocomplete': 'email', 'class': 'form-control'}))


    first_name = forms.CharField(label="First Name", required=True, 
                            widget=forms.TextInput(attrs={'class': 'form-control'})
                            )

    last_name = forms.CharField(label="Last Name", required=True, 
                            widget=forms.TextInput(attrs={'class': 'form-control'})
                            )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']
        # labels = {'email': 'Email'}
        # widgets = {'username': forms.TextInput(
        #     attrs={'class': 'form-control'})}




# class aboutForm(AboutForm):
#     # username = UsernameField(widget=forms.TextInput(
#     #     attrs={'autofocus': True, 'class': 'form-control', }))
#     username = forms.CharField(label='Email', required=True,
#                             widget=forms.EmailInput(
#                                 attrs={'class': 'form-control'}), validators=[validate_email])
#     password = forms.CharField(label=_("Password"), strip=False, widget=forms.PasswordInput(
#         attrs={'autocomplete': 'current-password', 'class': 'form-control'}))

# class ContactForm(forms.Form):
#     first_name = forms.CharField(max_length = 50)
#     email = forms.EmailField(max_length = 150)
#     message = forms.CharField(widget = forms.Textarea, max_length = 2000)


class ContactForm(forms.ModelForm):

    first_name = forms.CharField(label="first_name", required=True, 
                            widget=forms.TextInput(attrs={'class': 'form-control col-md-6', 'placeholder':"Full Name"})
                            )
    email = forms.EmailField(max_length = 150)
    message = forms.CharField(widget = forms.Textarea, max_length = 2000)

    class Meta:
        model = contactus
        fields = [ 'first_name', 'email', 'message' ]