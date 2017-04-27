var niveis = ['Estagiario', 'Junior', 'Pleno', 'Senior'];
var probabilities = [[10, 20, 60, 100], [20, 60, 100], [5, 10, 25, 100], [10, 30, 60, 100], [5, 20, 40, 100]];
var driver_cat = ['Pleno', 'Senior', 'Junior', 'Estagiario'];
var driver_est = ['Junior', 'Pleno', 'Senior'];
var driver_jun = ['Estagiario', 'Junior', 'Pleno', 'Senior'];
var driver_pln = ['Pleno', 'Senior', 'Junior', 'Estagiario'];
var driver_sen = ['Senior', 'Pleno', 'Estagiario', 'Junior'];

var devs = [{nome: 'Alan', nivel: 'Estagiario'}, {nome: 'Bruce', nivel: 'Pleno'}, {nome: 'Carlos', nivel: 'Pleno'}, {nome: 'Cris', nivel: 'Pleno'}, {nome: 'Daniela', nivel: 'Junior'},
{nome: 'Elen', nivel: 'Senior'}, {nome: 'Francisco', nivel: 'Junior'}, {nome: 'Gustavo', nivel: 'Junior'}, {nome: 'Heloisa', nivel: 'Pleno'}];

var dupla = {driver: {}, navigato: {}};
var dupla_ant = {driver: {}, navigato: {}};
var nome = '';
var nivel = '';
var category = '';
var driver = {name: '', nivel: ''};
var navigato = {name: '', nivel: ''};

var app = angular.module('tegra-pair', ['ngRoute']);

app.controller('cadastro-controller', function($scope) {
  $scope.nome = nome;
  $scope.niveis = niveis;
  $scope.nivel = nivel;
  $scope.cadastrar = cadastrar;

  function cadastrar() {
    devs.push({nome:$scope.nome, nivel: $scope.nivel});
  }

});

app.controller('sorteio-controller', function($scope, $timeout) {
  $scope.sortear = sortear;
  $scope.dupla = dupla;

  function findCategory(dev) {
    switch(dev.nivel) {
      case 'Estagiario':
        return driver_est;
        break;
      case 'Junior':
        return driver_jun;
        break;
      case 'Pleno':
        return driver_pln;
        break;
      case 'Senior':
        return driver_sen;
        break;
      default:
        return driver_cat;
    }
  }

  function findProbability(dev) {
    switch(dev.nivel) {
      case 'Estagiario':
        return probabilities[1];
        break;
      case 'Junior':
        return probabilities[2];
        break;
      case 'Pleno':
        return probabilities[3];
        break;
      case 'Senior':
        return probabilities[4];
        break;
      default:
        return probabilities[0];
    }
  }

  function findDev(dev) {
    var prob = findProbability(dev);
    var number = Math.floor(Math.random() * 101);
    var categorys = [];
    for(var i = 0; i < prob.length; i++) {
      if(number <= prob[i]) {
        categorys = findCategory(dev);
        category = categorys[i];
        break;
      }
    }
    var devsFiltered = devs.filter(function(a) {
      return a.nivel == category;
    });
    var num = Math.floor(Math.random() * devsFiltered.length);

    return devsFiltered[num];

  }

  function sortear() {

    dupla = {driver: {}, navigato: {}};
    driver = {nome: '', nivel: ''};
    navigato = {nome: '', nivel: ''};
    driver = findDev(driver);
    navigato = findDev(driver);
    dupla.driver = driver;
    dupla.navigato = navigato;
    console.log(dupla);

    if(dupla.driver == dupla_ant.driver && dupla.navigato == dupla_ant.navigato) {
      alert('Erro: dupla sorteada igual a dupla anterior');
    }
    else {
      dupla_ant = {driver: {}, navigato: {}};
      dupla_ant.driver = dupla.driver;
      dupla_ant.navigato = dupla.navigato;
    }

    $timeout(function() {
      $scope.dupla = dupla;
    }, 100);

  }

});

app.config(function($routeProvider, $locationProvider) {

  $locationProvider.html5Mode({
    enabled: true,
    requireBase: false
  });

  $routeProvider
  .when('/', {
    templateUrl: '../pages/cadastro.html',
    controller: "cadastro-controller"
  })
  .when('/sorteio', {
    templateUrl: '../pages/sorteio.html',
    controller: 'sorteio-controller'
  })
  .otherwise({
    redirectTo: '/'
  });

});
