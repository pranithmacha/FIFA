from django import forms


class RegistrationForm(forms.Form):
    user_name = forms.CharField(max_length=40)
    email = forms.EmailField(max_length=40)
    password = forms.PasswordInput()
    confirm_password = forms.PasswordInput()


class Tournament(forms.Form):
    tournament_name = forms.CharField(max_length=40)
    tournament_type = forms.CharField(max_length=40)
    number_of_games = forms.IntegerField(required=True, None=False)


class MyForm(forms.Form):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(MyForm, self).__init__(*args, **kwargs)

    def clean(self):
        pass