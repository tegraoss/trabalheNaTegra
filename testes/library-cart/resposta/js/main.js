var books = [
  {id: 1, title: "The Pragmatic Programmer: From Journeyman to Master", author: "Andrew Hunt & Dave Thomas", price: 40.00, stock: 12},
  {id: 2, title: "The Mythical Man-Month: Essays on Software Engineering", author: "Frederick P. Brooks", price: 80.00, stock: 1},
  {id: 3, title: "Expressões Regulares - Uma Abordagem Divertida", author: "Aurelio Marinho Jargas", price: 20.00, stock: 13},
  {id: 4, title: "Domain Driven Design: Tackling Complexity in the Heart of Software", author: "Erick Evans", price: 120.00, stock: 42},
  {id: 5, title: "Patterns of Enterprise Application Architecture", author: "Martin Fowler", price: 32.00, stock: 42},
  {id: 6, title: "Epigrams in Programming", author: "Alan Perils", price: 31.00, stock: 0},
  {id: 7, title: "Implementing Domain-Driven Design", author: "Vaughn Vernon", price: 31.00, stock: 42},
  {id: 8, title: "Dive Into HTML5", author: "Mark Pilgrim", price: 22.00, stock: 42},
  {id: 9, title: "Scalable Internet Architectures", author: "Theo Schlossnagle", price: 18.00, stock: 4},
  {id: 10, title: "Refactoring: Improving the Design of Existing Code", author: "Martin Fowler", price: 33.00, stock: 2},
  {id: 11, title: "Treinamento Em C", author: "Victorine Viviane Mizrahi", price: 42.00, stock: 6},
  {id: 12, title: "Algoritmos: Teoria e Prática", author: "Thomas H. Cormen", price: 4.60, stock: 1}
];
var cart = [];
var coupon = "";
var total = 0;
var app = angular.module("library-cart", ["ngRoute"]);

function calcTotal() {
  total = 0;
  for(var i = 0; i < cart.length; i++) {
    total += (cart[i].item.price * cart[i].quant);
    total = Math.round(total * 100) / 100;
  }
  $scope.total = total;
}

app.controller("products-controller", function($scope) {
  $scope.books = books;
  $scope.addToCart = addToCart;


  function addToCart(book) {
    for(var i = 0; i < books.length; i++) {
      if (books[i].id == book.id) {
        if(books[i].stock > 0) {
          books[i].stock -= 1;
          var index = cart.map(function(el) {
            return el.item.id;
          }).indexOf(book.id);

          if(index != -1) {
            cart[index].quant += 1;
            calcTotal();
          }
          else {
            cart.push({item: book, quant: 1, desc: false});
            calcTotal();
          }
        }
      }
    }
  };

});

app.controller("cart-controller", function($scope) {
  $scope.cart = cart;
  $scope.coupon = coupon;
  $scope.calcSubtotal = calcSubtotal;
  $scope.removeFromCart = removeFromCart;
  $scope.calcDesconto = calcDesconto;
  $scope.total = total;

  // $scope.$watch('total', function() {
  //   $scope.total = total;
  // });

  function calcDesconto() {
    if($scope.coupon == "TrabalheNaTegra") {
      for(var i = 0; i < cart.length; i++) {
        if(cart[i].item.author == "Martin Fowler") {
          if(cart[i].desc == false) {
            cart[i].item.price = cart[i].item.price * 0.9;
            cart[i].desc = true;
          }
        }
      }
      calcTotal();
    }
  }

  function calcSubtotal(book) {
    return Math.round((book.item.price * book.quant) * 100) / 100;
  }

  function removeFromCart(book) {
    for(var i = 0; i < books.length; i++) {
      if (books[i].id == book.item.id) {
        if(book.quant >= 1) {
          books[i].stock += 1;
          var index = cart.map(function(el) {
            return el.item.id;
          }).indexOf(book.item.id);

          if(cart[index].quant > 1) {
            cart[index].quant -= 1;
            calcTotal();
          }
          else {
            cart.splice(index,1);
            calcTotal();
          }
        }
      }
    }
  };

});

app.config(function($routeProvider, $locationProvider) {

  $locationProvider.html5Mode({
    enabled: true,
    requireBase: false
  });

  $routeProvider
  .when("/", {
    templateUrl: "../pages/products.html",
    controller: "products-controller"
  })
  .when("/cart", {
    templateUrl: "../pages/cart.html",
    controller: "cart-controller"
  })
  .otherwise({
    redirectTo: "/"
  });

});
