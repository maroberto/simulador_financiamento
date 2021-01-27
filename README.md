# Simulador de Financiamento
## Aplicação em Python para simular financiamento de ímovel.
Esta aplicação simples é resultado dos meus estudos em Python. É a primeira versão e está passível de melhorias e mudanças, mas apesar de simples estou muito feliz em poder compartilhar.

![Video Simulador](video_financiamento.gif)
### Como funciona:
Este aplicativo faz uma simualação com base no valor do ímovel acrescido de juros (*7,99 ao ano*) e faz três verificações.
1. Na primeira verifica a possibilidade de pagamento com até **30%** da renda. Se verdadeiro aprova.

![](imagens/ate_30.png)

2. Na segunda se verifica até **40%** da renda. Não aprova mas indica a possibilidade de incrementar a renda.

![](imagens/ate_40.png)

3. Na terceira e última opção a simulação não é aprovada.

![](imagens/acima.png)

*A opção de imprimir ainda não foi implementada e solicito a ajuda da comunidade para resolver o algoritimo desta função.*
### Esta função gera um relatório com base nas informações de input com os seguintes dados.
1. Saldo devedor.
2. juros do mês.
2. Valor da amortização (conforme tabela SAC não se altera do inicio ao fim do financiamento).
3. valor da prestação do mês(valor do juros do mês mais o valor da amortização).


### Para executar este projeto:
É necessário ter instalado o [Python3](https://www.python.org/).
### Bibliotecas e Frameworks:
* [PyQt5](https://pypi.org/project/PyQt5/).
* [Qt Designer](https://build-system.fman.io/qt-designer-download).
## Autores: 
**Marcos Roberto**
## Licença:
[GNU General Public License v3.0]()
