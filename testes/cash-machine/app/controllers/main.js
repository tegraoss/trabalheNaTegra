(function(angular, $) {
  "use strict";

  angular.module("cashMachineApp")
    .controller("mainController", ["$scope", function($scope) {
      var notes = [100, 50, 20, 10];
      var minimunNote = notes[notes.length - 1];

      $scope.submit = function(e) {
        e.preventDefault();
        $scope.errorMessage = "";
        $scope.result = [];

        var value = $scope.value;

        if (!value) {
          return;
        }

        if (!$.isNumeric(value)) {
          $scope.errorMessage = "Not a number";
          return;
        }

        if (value < minimunNote) {
          $scope.errorMessage = "Must be greater than " + minimunNote;
          return;
        }

        if (value % minimunNote != 0) {
          $scope.errorMessage = "Unavailable Note";
          return;
        }

        notes.forEach(function(note) {
          var rest = Math.floor(value / note);

          if (rest == 0) {
            return;
          }

          for (var x = 0; x < rest; x++) {
            $scope.result.push({
              value: note
            });
          }

          value -= note * rest;
        });
      };

    }]);



})(angular, jQuery);