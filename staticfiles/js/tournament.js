var app = angular.module('tournment', []);
app.controller('tournamentContrl',function($scope, $mdDialog){
	$scope.hideTournament = false;
	$scope.createTournament = false;
	$scope.Matchlist=null;
    var num_players = 10;
	//ng repeat value to be obtained
	$scope.range = new Array(num_players);


	$scope.createMatch=function(){
        $scope.createTournament = true;
	}
	$scope.playMatch=function(){
		$scope.hideTournament = true;
		debugger;
		$scope.Matchlist=[{
			name: 'Pranith',
			played: 12,
			won: 9,
			draw: 1,
			lost:2,
			points: 28,
			goals: 28,
			home_goals: 18,
			away_goals: 10,
		}, {
			name: 'Navya',
			played: 12,
			won: 9,
			draw: 1,
			lost:2,
			points: 28,
			goals: 28,
			home_goals: 18,
			away_goals: 10,
		},{
			name: 'sanjana',
			played: 12,
			won: 9,
			draw: 1,
			lost:2,
			points: 28,
			goals: 28,
			home_goals: 18,
			away_goals: 10,
		}]
	}
debugger;
	//dialog box
	$scope.showPrompt = function(ev) {
    // Appending dialog to document.body to cover sidenav in docs app
    var confirm = $mdDialog.prompt()
      .title('What would you name your dog?')
      .textContent('Bowser is a common name.')
      .placeholder('Dog name')
      .ariaLabel('Dog name')
      .initialValue('Buddy')
      .targetEvent(ev)
      .ok('Okay!')
      .cancel('I\'m a cat person');

    $mdDialog.show(confirm).then(function(result) {
      $scope.status = 'You decided to name your dog ' + result + '.';
    }, function() {
      $scope.status = 'You didn\'t name your dog.';
    });
  };
})