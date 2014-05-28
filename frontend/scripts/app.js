angular.module("Fertilizer", [])
  .config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    $httpProvider.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded;charset=utf-8';
  }])
  .controller('Location', function ($scope, $http){
    $scope.getLocation = function() {
      $http.get("../core/TG9jYXRpb24=/json")
        .success(function (data, status, headers, config) {
          $scope.location = data;
        });
    };
    $scope.getLocations = function () {
      $http.get("../core/list")
        .success(function (data, status, headers, config) {
          $scope.locations = data;
        });
    };
    $scope.createLocation = function() {
      $http.post("../core/create/", "Location=" + $scope.location)
        .success(function (data, status, headers, config) {
          console.log("success");
        });
    };
});
