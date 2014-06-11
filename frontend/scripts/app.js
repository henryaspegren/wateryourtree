var fertilizer = angular.module("fertilizer", ['ngRoute', 'fertilizerControllers']);


fertilizer.config(['$routeProvider',
  function($routeProvider) {
    $routeProvider.
      when('/', {
        templateUrl: 'partials/location-list.html',
        controller: 'locationsController'
      }).
      when('/:url', {
        templateUrl: 'partials/location-detail.html',
        controller: 'locationsController'
      }).
      otherwise({
        redirectTo: '/'
      });
  }]);
