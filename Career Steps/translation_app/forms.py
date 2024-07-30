

from django import forms

class TextForm(forms.Form):
    text_message = forms.CharField(label='', widget=forms.Textarea)
