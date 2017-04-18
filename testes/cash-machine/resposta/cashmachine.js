// medson10<medson.oliveira@fatec.sp.gov.br>
var ent = process.argv[2];
var saque = [];

//Função que verifica se o valor ja está abaixo do valor das notas disponiveis
function verify() {
  if (ent >= 100 || ent >= 50 || ent >= 20 || ent >= 10) {
    return false;
  }
  return true;
}

//Função que adiciona as notas ao array saque
function entrega() {
  switch (true) {
    case ent >= 100:
      saque.push("100.00");
      ent -= 100;
      break;
    case ent >= 50:
      saque.push("50.00");
      ent -= 50;
      break;
    case ent >= 20:
      saque.push("20.00");
      ent -= 20;
      break;
    case ent >= 10:
      saque.push("10.00");
      ent -= 10;
      break;
  }
}

//Função principal
function main() {
  if (ent < 0 || isNaN(ent)) {
    console.log("Erro de valor inválido");
  }
  else if(ent == null) {
    console.log("Erro de valor nulo");
  }
  else {
    while(ent > 0) {
      if (verify(ent) && ent > 0) {
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
