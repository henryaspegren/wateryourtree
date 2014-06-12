'use strict';
var fertilizerControllers = angular.module("fertilizerControllers", ['ja.qr', 'google-maps']);

fertilizerControllers.config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded;charset=utf-8';
  }])

fertilizerControllers.controller('locationsController', ['$scope', '$routeParams', '$http',
  function($scope, $routeParams, $http) {
    $scope.url = $routeParams.url;
    $scope.name = $routeParams.name;
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
      $scope.binding = 'binding is working'
      $http.get("../core/" + url)
        .success(function (data) {
          $scope.location = data;
        });
      $scope.qr_url = document.domain + "/core/hit/" + url
    };
    $scope.get_details_name = function(name) {
      $scope.binding = 'binding is working'
      $http.get("../core/name/" + name)
        .success(function (data) {
          $scope.location = data;
        });
      $scope.qr_url = document.domain + "/core/hit/"
    };
    $scope.update_latitude=function(url, lat) {
      $http.post("../core/updatelatitude/","url_link="+url+";lat_update="+lat)
    };

    $scope.update_longitude=function(url,lng) {
      $http.post("../core/updatelongitude/", "url_link="+url+";lng_update="+lng)
    };

    $scope.create_location = function(name) {
      $http.post("../core/create/", "Location=" +name)
       .success(function (data, status, headers, config) {
          window.location = '/fertilizer/index.html#/create/'+name;
        });
     };
    $scope.select_location = function(location) {
      $scope.location = location;
      $scope.qr_url = document.domain + "/core/hit/" + $scope.location.url;
    };
  }]);
