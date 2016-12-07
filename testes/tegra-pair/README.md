Tegra Pair
=========

O Problema
----------
TODO


O Desafio
----------
Crie uma solução para sorteio de desenvolvedores para realizar pair programming.

###### Para ver mais sobre pair programming, acesse: https://www.youtube.com/watch?v=vgkahOzFH2Q&t=23s

Os requisitos são:

* Cadastrar desenvolvedores com nome e nível de experiência (estagiário, junior, pleno, sênior)
* Realizar o sorteio de dois desenvolvedores
* O primeiro desenvolvedor sorteado será o *piloto*
* O segundo desenvolvedor sorteado será o *copiloto*
* O nível do desenvolvedor *copiloto* dependerá do nível do desenvolvedor *piloto* de acordo com as regras de sorteio

### Regras do Sorteio

###### Sorteio do Piloto
* Senior aleatório
* Pleno aleatório
* Junior aleatório
* Estagiário aleatório

###### Pares para Piloto Estagiário
* Senior 4o%
* Pleno 40%
* Junior 20%

###### Pares para Piloto Junior
* Senior 75%
* Pleno 15%
* Junior 5%
* Estagiário 5%

###### Pares para Piloto Pleno
* Senior 20%
* Pleno 10%
* Junior 30%
* Estagiário 40%

###### Pares para Piloto Senior
* Senior 5%
* Pleno 15%
* Junior 60%
* Estagiário 20%

#### Restriçoes
* A solução só pode gerar um dupla por execução  

* A solução não deve permitir que estagiários realizem pair programming com estagiários  

* A solução não deve permitir que os desenvolvedores sorteados na rodada anterior sejam sorteados novamente  


#### Observações:
* Não há restrições para o desenvolvimento de sua solução: use quaisquer linguagens, boas práticas e tecnologias de sua preferência  

* Sinta-se a vontade para acrescentar melhorias com sua criatividade, a fim de proporcionar a melhor experiência a quem for usar o aplicação  

* Faça o melhor possível no tempo designado. Caso não consiga terminar, entregue mesmo assim! :)  

* Não é obrigatório o uso de banco de dados  

* Inclua instruções de como executar seu código  
