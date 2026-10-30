#!/usr/bin/python
# -*- coding:utf-8 -*-
import django
from django import forms
class UserForm(forms.Form):
    name = forms.CharField(label="Name")
    age = forms.IntegerField(label="Age")
    email = forms.EmailField(
        label="Email",
        widget=forms.TextInput(attrs={"placeholder": "Place Input Email"}),
    )