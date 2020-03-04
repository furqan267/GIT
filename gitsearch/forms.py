from django import forms

class SubmitGit(forms.Form):
    url = forms.CharField()