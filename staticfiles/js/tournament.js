var app = angular.module('tournment', []);
app.controller('tournamentContrl',function($scope){
	$scope.hideTournament = false;
	$scope.tournament = false;
	$scope.group = false;
	$scope.league = false;
	$scope.tournament= function(){
		$scope.hideTournament = true;
		$scope.tournament = true;
		$scope.group = false;
		$scope.league = false;
	}
	$scope.league= function(){
		$scope.hideTournament = true;
		$scope.league = true;
		$scope.tournament = false;
		$scope.group = false;
	}
	$scope.group= function(){
		$scope.hideTournament = true;
		$scope.group = true;
		$scope.league = false;
		$scope.tournament = false;
	}
})