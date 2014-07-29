var fertilizer = angular.module("fertilizer", ['ngRoute', 'fertilizerControllers']);


fertilizer.config(['$routeProvider',
  function($routeProvider) {
    $routeProvider.
      when('/', {
        templateUrl: 'partials/location-map.html',
        controller: 'mapController'
      }).
      when('/list', {
        templateUrl: 'partials/location-list.html',
        controller: 'listController'
      }).
      when('/about/yo', {
        templateUrl: 'partials/yo-about.html',
        controller: ''
      }).
      when('/tree/:url', {
        templateUrl: 'partials/location-detail.html',
        controller: 'detailController'
      }).
      when('/tree/hit/:url', {
        templateUrl: 'partials/location-hit.html',
        controller: 'hitController'
      }).
      when('/print/:url', {
        templateUrl: 'partials/location-print.html',
        controller: 'printController'
      }).
      when('/create/:name', {
        templateUrl: 'partials/location-create.html',
        controller: 'createController'
      }).
      otherwise({
        redirectTo: '/'
      });
  }]);
