from django import forms


class RegistrationForm(forms.Form):
    user_name = forms.CharField(max_length=40, required=True)
    email = forms.EmailField(max_length=40, required=True)
    password = forms.PasswordInput()
    confirm_password = forms.PasswordInput()


class GameSummaryForm(forms.Form):
    player_one = forms.CharField(max_length=40, required=True)
    player_two = forms.CharField(max_length=40, required=True)
    player_one_goals = forms.IntegerField(required=True, min_value=0)
    player_two_goals = forms.IntegerField(required=True, min_value=0)


class TournamentForm(forms.Form):
    tournament_name = forms.CharField(max_length=40, required=True)
    # tournament_type = forms.CharField(max_length=40, required=False)
    number_of_games = forms.IntegerField(required=True, max_value=38, min_value=1)
    # num_of_players = forms.IntegerField(required=True, max_value=10, min_value=2)

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        self.players = list()
        super(TournamentForm, self).__init__(*args, **kwargs)

    def clean(self):
        player_numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
        player = "player_{0}"
        for num in player_numbers:
            player_num = player.format(num)
            if self.request.POST.get(player_num):
                self.players.append(self.request.POST.get(player_num))
        if not self.players:
            raise forms.ValidationError("could not find any users in the request")

    def get_players(self):
        return self.players



