# __author__ = 'SAMSUNG'

# forms.py

from django import forms
from .models import SignUp


class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['full_name','email','password']

    def clean_email(self):
        print("\n+++++++++++++++++++++++++++")
        print("forms.py --> clean_email")
        print(SignUp.objects.values('email'))
        email = self.cleaned_data.get("email")
        if not "edu" in email:
            raise forms.ValidationError("Please use a valid .edu email Address")
        print(email)
        print("+++++++++++++++++++++++++++")
        return email
    def clean_full_name(self):
        print("forms.py --> clean_full_name")
        full_name = self.cleaned_data.get("full_name")
        print(full_name)
        print("+++++++++++++++++++++++++++\n")
        return full_name