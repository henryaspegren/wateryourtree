var fertilizer = angular.module("Fertilizer", ['ja.qr'])
  .config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded;charset=utf-8';
  }])
  .controller('Location', function ($scope, $http){
    // URL for the QR code to generate
    $scope.qr_url = "";

    $scope.selected_location = false;
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
          window.location = "/fertilizer/location.html";
        });
    };
    $scope.select_location = function(location) {
      $scope.selected_location =  true;
      $scope.location = location;
      $scope.qr_url = document.domain + "/core/hit/" + $scope.location.url;
    };
});
