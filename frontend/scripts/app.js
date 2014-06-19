var fertilizer = angular.module("fertilizer", ['ngRoute', 'fertilizerControllers']);


fertilizer.config(['$routeProvider',
  function($routeProvider) {
    $routeProvider.
      when('/', {
        templateUrl: 'partials/location-map.html',
        controller: 'locationsController'
      }).
      when('/list', {
        templateUrl: 'partials/location-list.html',
        controller: 'locationsController'
      }).
      when('/tree/:url', {
        templateUrl: 'partials/location-detail.html',
        controller: 'locationsController'
      }).
      when('/tree/hit/:url', {
        templateUrl: 'partials/location-hit.html',
        controller: 'locationsController'
      }).
      when('/print/:url', {
        templateUrl: 'partials/location-print.html',
        controller: 'locationsController'
      }).
      when('/create/:name', {
        templateUrl: 'partials/location-create.html',
        controller: 'locationsController'
      }).
      otherwise({
        redirectTo: '/'
      });
  }]);
