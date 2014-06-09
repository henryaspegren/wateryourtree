var fertilizer = angular.module("fertilizer", ['ja.qr', 'google-maps'])
  .config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded;charset=utf-8';
  }])
  .controller('dataController', function ($scope, $http){
    // URL for the QR code to generate
    $scope.qr_url = "";
    $scope.test = "data is finally binding";
    $scope.selected_location = false;
    $scope.location = "";
    $scope.map = {
      center: {
        latitude: 37.42565,
        longitude: -122.13535
      },
      zoom: 16
    };

    $scope.get_locations = function () {
      $http.get("../core/list")
        .success(function (data, status, headers, config) {
          $scope.locations = data;
        });
    };
    $scope.create_location = function(name) {
      $http.post("../core/create/", "Location=" + name)
        .success(function (data, status, headers, config) {
          window.location = "/fertilizer/location.html";
        });
    };
    $scope.select_location = function(location) {
      $scope.selected_location =  true;
      $scope.location = location;
      $scope.qr_url = document.domain + "/core/hit/" + $scope.location.url;
    };
});
