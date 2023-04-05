# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Device

class DeviceForm(forms.ModelForm):
    COLOR_CHOICES = [
        ('red', 'Red'),
        ('green', 'Green'),
        ('blue', 'Blue'),
    ]
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Device Name',
                'class': 'form-control'
            }
        )
    )
    color = forms.ChoiceField(
        choices=COLOR_CHOICES,
        widget=forms.Select(
            attrs={
                'class': 'form-control'
            }
        )
    )

    description = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Device Description',
                'class': 'form-control'
            }
        )
    )

    class Meta:
        model = Device
        fields = ('name', 'color', 'description')

class AddDeviceForm(forms.Form):
    device_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Device Name",
                "class": "form-control"
            }
        ))
    device_color = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Device IP",
                "class": "form-control"
            }
        ))
    device_description = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Device port",
                "class": "form-control"
            }
        ))

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control"
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password check",
                "class": "form-control"
            }
        ))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
