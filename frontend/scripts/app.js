var fertilizer = angular.module("Fertilizer", ['ja.qr'])
  .config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
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
    $scope.create_location = function() {
      $http.post("../core/create/", "Location=" + $scope.location)
        .success(function (data, status, headers, config) {
          console.log("success");
        });
    };
    $scope.select_location = function(location) {
      $scope.selected_location =  true;
      $scope.location = location;
      $scope.qr_url = "http://127.0.0.1:8000/core/hit/" + $scope.location.url;
    };
});
