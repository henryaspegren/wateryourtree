'use strict';
var fertilizerControllers = angular.module("fertilizerControllers", ['ja.qr', 'google-maps']);

fertilizerControllers.controller('locationsController', ['$scope', '$routeParams', '$http',
  function($scope, $routeParams, $http) {
    $scope.url = $routeParams.url;
    $scope.test = "data is finally binding";
    $scope.map = {
    center: {
        latitude: 37.42565,
        longitude: -122.13535
    },
    zoom: 15
    };
    $scope.get_locations = function () {
      $http.get("../core/list")
        .success(function (data, status, headers, config) {
          $scope.locations = data;
        });
    };
    $scope.get_details = function(url) {
      $scope.binding = 'bidning is working'
      $http.get("../core/" + url)
        .success(function (data) {
          $scope.data = data;
        });
      $scope.qr_url = document.domain + "/core/hit/" + url
    };

    $scope.create_location = function(name) {
      $http.post("../core/create/", "Location=" + name)
        .success(function (data, status, headers, config) {
          window.location = "/fertilizer/index.html";
        });
    };
    $scope.select_location = function(location) {
      $scope.location = location;
      $scope.qr_url = document.domain + "/core/hit/" + $scope.location.url;
    };
  }]);
