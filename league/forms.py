from django import forms


class RegistrationForm(forms.Form):
    user_name = forms.CharField(max_length=40)
    email = forms.EmailField(max_length=40)
    password = forms.PasswordInput()
    confirm_password = forms.PasswordInput()


