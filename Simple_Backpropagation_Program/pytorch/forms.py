from django import forms


class InputForm(forms.Form):
    number = forms.IntegerField()
