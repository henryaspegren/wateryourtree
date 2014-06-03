'use strict';
var fertilizer = angular.module("fertilizer", ['ja.qr']);

fertilizer.controller('locationsController', function ($scope, $http){
    // URL for the QR code to generate
    $scope.test = "data is finally binding";
    $scope.qr_url = "";
    $scope.location = "";

    $scope.get_locations = function () {
      $http.get("../core/list")
        .success(function (data, status, headers, config) {
          $scope.locations = data;
        });
    };
    $scope.create_location = function(name) {
      $http.post("../core/create/", "Location=" + name)
        .success(function (data, status, headers, config) {
          window.location = "/fertilizer/create.html";
        });
    };
    $scope.select_location = function(location) {
      $scope.selected_location =  true;
      $scope.location = location;
      $scope.qr_url = document.domain + "/core/hit/" + $scope.location.url;
    };
});
