// medson10<medson.oliveira@fatec.sp.gov.br>
var ent = process.argv[2];
var saque = [];

//Função que verifica se o valor ja está abaixo do valor das notas disponiveis
function verify() {
  if (ent >= 10) {
    return false;
  }
  return true;
}

//Função que adiciona as notas ao array saque
function entrega() {
  if(ent >= 100) {
    saque.push("100.00");
    ent -= 100;
  }
  else if(ent >= 50) {
    saque.push("50.00");
    ent -= 50;
  }
  else if(ent >= 20) {
    saque.push("20.00");
    ent -= 20;
  }
  else if(ent >= 10) {
    saque.push("10.00");
    ent -= 10;
  }
}

//Função principal
function main() {
  if(ent == null) {
    console.log("Erro de valor nulo");
  }
  else if (ent < 0 || isNaN(ent)) {
    console.log("Erro de valor inválido");
  }
  else {
    while(ent > 0) {
      if (verify() && ent > 0) {
        break;
      }
      else {
        if(ent > 0) {
          entrega(ent);
        }
        else {
          break;
        }
      }
    }
    if(ent > 0) {
      console.log("Erro de notas indisponíveis");
    }
    else {
      console.log(saque);
    }
  }
}

main();
