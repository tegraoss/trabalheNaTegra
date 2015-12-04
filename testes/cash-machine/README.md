Cash Machine
============

O Problema
----------
Desenvolva uma aplicação que simule a entrega de notas quando um cliente efetuar um saque em um caixa eletrônico. 

Sua aplicação deve:
* Entregar sempre o menor número de notas possíveis
* Sacar valores apenas com as notas disponíveis
* Ter saldo do cliente infinito
* Ter quantidade de notas infinita
* Possuir apenas notas de ```R$ 100,00```, ```R$ 50,00```, ```R$ 20,00``` e ```R$ 10,00```
* Retornar mensagens de erro em caso de entradas inválidas

Observação:
* Não há restrições para o desenvolvimento de sua solução: use quaisquer linguagens, boas práticas e tecnologias de sua preferência.

Exemplos:
---------
* 
 **Entrada:** 30.00  
 **Resultado:** [20.00, 10.00]

* 
  **Entrada:** 80.00  
  **Resultado:** [50.00, 20.00, 10.00]

* 
  **Entrada:** 125.00  
  **Resultado:** *Erro de notas indisponíveis*

* 
 **Entrada:** -130.00   
 **Resultado:** *Erro de valor inválido*

* 
  **Entrada:** NULL  
  **Resultado:** *Erro de valor nulo*
