from django import forms


class RegistrationForm(forms.Form):
    user_name = forms.CharField(max_length=40)
    email = forms.EmailField(max_length=40)
    password = forms.PasswordInput()
    confirm_password = forms.PasswordInput()


class TournamentForm(forms.Form):
    tournament_name = forms.CharField(max_length=40, required=True)
    tournament_type = forms.CharField(max_length=40, required=False)
    number_of_games = forms.IntegerField(required=True)

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        self.players = list()
        super(TournamentForm, self).__init__(*args, **kwargs)

    def clean(self):
        # player_id_format = "player_{0}"
        self.players = self.data.get("player_name", [])
        # num_of_players = len(player_names)
        # for name in player_names:
        #     try:
        #         player_name = self.request.POST.get(player_id)
        #         self.players.append(player_name)
        #     except KeyError:
        #         continue
        if not self.players:
            raise forms.ValidationError("could not find any users in the request")

    def get_players(self):
        return self.players



