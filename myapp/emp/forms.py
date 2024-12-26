from django import forms

class Feedbackform(forms.Form):
    email=forms.EmailField(label="Enter email")
    name=forms.CharField(label="Enter name")
    feedback=forms.CharField(label="feedback")

