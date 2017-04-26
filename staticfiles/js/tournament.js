var app = angular.module('tournment', []);
app.controller('tournamentContrl',function($scope){
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
})