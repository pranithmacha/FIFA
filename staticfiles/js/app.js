(function(){

	var macsite = angular.module('FifaApp', ['ngMaterial','ngMessages','tournment']);

    macsite.config(function($interpolateProvider) {
        $interpolateProvider.startSymbol('{$');
        $interpolateProvider.endSymbol('$}');
    });
    macsite.controller('macsiteController',function($scope){
        $scope.value="";
    })

})();