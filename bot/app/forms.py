from django import forms
from app.models import *


class MessageForm(forms.ModelForm):
    class Meta:
        model = UserMessage
        fields = ['message']
        widgets = {
            'message': forms.TextInput(attrs={'class': 'form_input',
                                              'placeholder': 'Message'}),
        }

    def save(self, commit=True):
        message = super(MessageForm, self).save(commit=False)
        if commit:
            message.save()
        else:
            return message
