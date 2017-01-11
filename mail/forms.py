from django import forms
from mail.models import *


class SendForm(forms.ModelForm):
    class Meta:
        model = Mail
        fields = ['message', 'head', 'recipient',]
        widgets = {
            'recipient': forms.TextInput(
                attrs={'placeholder': 'ustymchyk.nazar@gmail.com'}),
            'head': forms.TextInput(
                attrs={'placeholder': 'About my birthday'}),
            'message': forms.Textarea(
                attrs={'cols': '30', 'rows': '10'}),
        }
