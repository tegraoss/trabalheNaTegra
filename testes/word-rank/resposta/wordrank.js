var fs = require('fs');
var buf = fs.readFileSync(process.argv[2]);
var result = buf.toString();
var rank = [];

//Função que encontra o index do array do elemento 
function findArray(element) {
  var indexFound = rank.findIndex(function(minAr) {
    return minAr[0] === element;
  });

  return indexFound;
}

//Função que ordena o array por ordem alfabetica e por numero de ocorrencias da palavra
function sortArray(a, b) {
  if(a[0] < b[0] && a.length >= b.length) {
    return -1;
  }
  if(a[0] < b[0] && a.length < b.length) {
    return 1;
  }
  if(a[0] > b[0] && a.length > b.length) {
    return -1;
  }
  if(a[0] > b[0] && a.length <= b.length) {
    return 1;
  }
}

//Função que agrupa elementos iguais em um array
function groupEquals() {
  for(var i = 0; i < result.length; i++) {
    var index = findArray(result[i]);
    if(index != -1) {
      rank[index].push(result[i]);
    }
    else {
      rank.push([result[i]]);
    }
  }
}

//Função principal
function main() {
  result = result.replace(/(\.|,|\n|\r)/gm,'').toLowerCase().split(' ');
  groupEquals();
  rank = rank.sort(sortArray);
  for(var i = 0; i < 20; i++) {
    var element = rank[i];
    console.log(element[0],element.length);
  }
}

main();
