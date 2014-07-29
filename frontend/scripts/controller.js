'use strict';
var fertilizerControllers = angular.module("fertilizerControllers", ['ja.qr', 'google-maps', 'ngAnimate']);

fertilizerControllers.config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded;charset=utf-8';
  }])


fertilizerControllers.controller('mapController', ['$scope', '$http',
  function($scope, $http) {
    $scope.map = {
    center: {
        latitude: 37.42565,
        longitude: -122.13535
    },
    zoom: 14
    };
    $scope.get_locations = function () {
      $http.get("../core/list")
        .success(function (data, status, headers, config) {
          $scope.locations = data;
        });
    };
    $scope.change_window = function(url){
      window.location = '/fertilizer/index.html#/tree/'+String(url);
    };
  }
]);

fertilizerControllers.controller('listController', ['$scope', '$http',
  function($scope, $http) {
    $scope.get_locations = function () {
      $http.get("../core/list")
        .success(function (data, status, headers, config) {
          $scope.locations = data;
        });
      };
    $scope.create_location = function(name) {
      $http.post("../core/create/", "Location=" +String(name))
       .success(function (data, status, headers, config) {
          window.location = '/fertilizer/index.html#/create/'+String(name);
        });
     };
  }]);

fertilizerControllers.controller('detailController', ['$scope', '$routeParams', '$http',
  function($scope, $routeParams, $http) {
    $scope.url = $routeParams.url;
    $scope.map = {
    center: {
        latitude: 37.42565,
        longitude: -122.13535
    },
    zoom: 14
    };
    $scope.get_details = function(url) {
      $scope.binding = 'binding is working';
      $http.get("../core/lookup/" + url)
        .success(function (data) {
          $scope.location = data;
        });
      $scope.qr_url = document.domain + "/fertilizer/index.html#/tree/hit/" + url;
    };
    $scope.update_latitude=function(url, lat) {
      $http.post("../core/updatelatitude/","url_link="+url+";lat_update="+lat);
      $scope.location.lat = lat;
    };
    $scope.update_longitude=function(url,lng) {
      $http.post("../core/updatelongitude/", "url_link="+url+";lng_update="+lng);
      $scope.location.lng = lng;
    };
    $scope.create_comment = function(name, url, comment) {
      var json = {"tree": url, "name": name, "comment": comment};
      $http.post("../core/comment/", json)
        .success(function (data, status, headers, config) {
          $scope.get_comments(url);
        });
    };
    $scope.get_comments = function (tree_url) {
      $scope.show_comments = false;
      $http.get("../core/comments/"+String(tree_url))
        .success( function (data, status, headers, config) {
          $scope.comments = data;
          if (data.length > 0){
            $scope.show_comments = true;
          }
        });
    };
  }]);

fertilizerControllers.controller('hitController', ['$scope', '$routeParams', '$http',
  function($scope, $routeParams, $http) {
    $scope.url = $routeParams.url;
    $scope.hit = function(url,name){
      $http.get("../core/hit/"+url+'/'+name);
      $scope.show= true;
    };
    $scope.get_details = function(url) {
      $scope.binding = 'binding is working';
      $http.get("../core/lookup/" + url)
        .success(function (data) {
          $scope.location = data;
        });
      $scope.qr_url = document.domain + "/fertilizer/index.html#/tree/hit/" + url;
    };
  }]);

fertilizerControllers.controller('printController', ['$scope', '$routeParams', '$http',
  function($scope, $routeParams, $http) {
    $scope.url = $routeParams.url;
    $scope.get_details = function(url) {
      $scope.binding = 'binding is working';
      $http.get("../core/lookup/" + url)
        .success(function (data) {
          $scope.location = data;
        });
      $scope.qr_url = document.domain + "/fertilizer/index.html#/tree/hit/" + url;
    };

  }]);

fertilizerControllers.controller('createController', ['$scope', '$routeParams', '$http',
  function($scope, $routeParams, $http){
    $scope.name = $routeParams.name;
    $scope.update_latitude=function(url, lat) {
      $http.post("../core/updatelatitude/","url_link="+url+";lat_update="+lat);
      $scope.location.lat = lat;
    };

    $scope.update_longitude=function(url,lng) {
      $http.post("../core/updatelongitude/", "url_link="+url+";lng_update="+lng);
      $scope.location.lng = lng;
    };
    $scope.get_details_name = function(name) {
      $scope.name = name;
      $scope.binding = 'binding is working';
      $http.get("../core/name/" + name + '/')
        .success(function (data) {
          $scope.location = data;
        });
      $scope.qr_url = document.domain + "/fertilizer/index.html#/tree/hit/";
    };
  }]);

