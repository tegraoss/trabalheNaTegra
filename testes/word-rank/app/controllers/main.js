(function(angular, $) {
  "use strict";

  angular.module("wordRankApp")
    .controller("mainController", ["$scope", "$http", "$filter", function($scope, $http, $filter) {
      var resolve = function(fullText) {
        var parts = fullText.match(/([A-z]+)/g);
        var wordsCount = countWords(parts);

        var result = $filter("orderBy")(wordsCount, ['-qty', 'word']);
        $scope.words = result.splice(0, 20);
      }

      var countWords = function(parts) {
        var words = {};

        parts.forEach(function(word) {
          if (words[word]) {
            words[word].qty++;
            return;
          }

          words[word] = {
            word: word,
            qty: 1
          };
        });

        return $.map(words, function(word) {
          return word;
        });
      }

      $http.get("/texto.txt").then(function(response) {
        resolve(response.data);
      });


    }]);



})(angular, jQuery);