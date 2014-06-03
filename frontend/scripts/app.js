var fertilizer = angular.module("fertilizer", ['ngRoute','ja.qr', 'locationsController']);

fertilizer.config(['$routeProvider',
  function($routeProvider) {
    $routeProvider.
      when('/fertilizer/location', {
        templateUrl: 'location1.html',
        controller: 'locationsController'
      }).
      when('fertilizer/create', {
        templateUrl: 'create.html'
        controller: 'locationsController'
      }).
      otherwise({
        redirectTo: '/'
      });
    });
}]);
