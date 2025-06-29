from django import forms

class userFrom(forms.Form):
    num1 = forms.ChoiceField()
    num2 = forms.ChoiceField()