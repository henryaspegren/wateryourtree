var fertilizer = angular.module("fertilizer", ['ngRoute', 'fertilizerControllers']);


fertilizer.config(['$routeProvider',
  function($routeProvider) {
    $routeProvider.
      when('/fertilizer/index', {
        templateUrl: 'index.html',
        controller: 'locationsController'
      }).
      when('/fertilizer/forest/:name', {
        templateUrl: 'partials/location-detail.html',
        controller: 'locationsController'
      }).
      otherwise({
        redirectTo: '/'
      });
  }]);
