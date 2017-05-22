(function(){

	var macsite = angular.module('FifaApp', ['ngMaterial','ngMessages','ngRoute','tournment']);

    macsite.config(function($interpolateProvider,$routeProvider, $locationProvider) {
        $interpolateProvider.startSymbol('{$');
        $interpolateProvider.endSymbol('$}');
        $locationProvider.hashPrefix('');
            $routeProvider
                .when('/login', {
                    path: "/login",
                    templateUrl:"templates/login.html"
                })
                .when('/register',{
                    templateUrl:"templates/register.html"
                })
                .when('/selectMatch',{
                    templateUrl:"templates/tournament.html",
                    controller:"tournamentContrl"
                })
    });
    macsite.controller('macsiteController',function($scope){
        $scope.value="";
    })
})();