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
   $mdDialog.show({
      controller: DialogController,
      templateUrl: '/dialog1.html',
      parent: angular.element(document.body),
      targetEvent: ev,
      clickOutsideToClose:true,
      fullscreen: $scope.customFullscreen // Only for -xs, -sm breakpoints.
    })
    .then(function(answer) {
      $scope.status = 'You said the information was "' + answer + '".';
    }, function() {
      $scope.status = 'You cancelled the dialog.';
    });
  };
});

function DialogController($scope, $mdDialog) {
    $scope.hide = function() {
      $mdDialog.hide();
    };

    $scope.cancel = function() {
      $mdDialog.cancel();
    };

    $scope.answer = function(answer) {
      $mdDialog.hide(answer);
    };
  }
