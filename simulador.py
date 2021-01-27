from PyQt5 import uic, QtWidgets


def RecuperaDados():
    saldo_devedor = float(tela.lineEdit.text())
    salario = float(tela.lineEdit_2.text())
    anos = int(tela.lineEdit_3.text())

    # calculo de juros
    juros_base = 0.0799
    juros_anos = (anos * juros_base)
    meses = (anos * 12)
    juros_mes = (juros_anos / meses)
    base_salario = (salario / 100) * 30
    base_salario2 = (salario / 100 * 40)

    # calcula a primeira prestação
    valor_primeira_prestacao = (saldo_devedor * juros_mes) + (saldo_devedor / meses)

    # mostra valor da prestação
    tela.label_2.setText('O valor da prestação é de R$: {:.2f} e você poderia pagar\nprestações de até R$: {:.2f}'.format(valor_primeira_prestacao, base_salario))
    print('O valor da prestação é de R$:\033[34m {:.2f}\033[m'.format(valor_primeira_prestacao))

    # mostra o valor de 30% do sálario
    print('Você poderia pagar uma prestação de até R$: \033[34m{}\033[m'.format(base_salario))

    # condição para até 30% do sálario(pode financiar)
    if valor_primeira_prestacao <= base_salario:
        tela.label_3.setStyleSheet('color: green')
        tela.label_3.setText('Parabéns seu financiamento está pré aprovado em {}\nparcelas  decrecentes.\nA primeira tem o valor de R$: {:.2f} !'.format(meses, valor_primeira_prestacao))
        print('\033[32mParabéns seu financiamento está pré aprovado em parcelas decrescentes.\nA primeira tem o valor de R$: {:.2f} e são {} parcelas\033[m\n'.format(valor_primeira_prestacao, meses))
    # condição para até 40% do sálario(para poder financiar)
    elif valor_primeira_prestacao <= base_salario2:
        tela.label_3.setStyleSheet('color: yellow')
        tela.label_3.setText('Falta pouco, tente incrementar sua renda incluindo algum\nparente, sua renda precisa ir de R$:{:.2f} para R$:{:.2f}'.format(salario, salario + (salario/100) * 35))
        print('\033[33mFalta pouco, tente encrementar sua renda incluindo algum parente, sua renda precisa ir de {:.2f} para {:.2f}\033[m\n'.format(salario, salario + (salario/100) * 35))
    # condição de quem não pode financiar
    else:
        tela.label_3.setStyleSheet('color: red')
        tela.label_3.setText('Infelizmente não podemos aprovar seu financiamento,\ntente novamente daqui a 3 meses!')
        print('\033[31mInfelizmente não podemos aprovar seu financiamento, tente novamente daqui a 3 meses!\033[m\n')

    # limpa entrada de dados
    tela.lineEdit.setText('')
    tela.lineEdit_2.setText('')
    tela.lineEdit_3.setText('')


# condição para imprimir tabela
def QuerImprimir():
    tela_2.show()
    '''
    RecuperaDados()
    # entrada de dados
    saldo_devedor = float(tela.lineEdit.text())
    anos = int(tela.lineEdit_3.text())
    # calculo de juros
    juros_base = 0.0799
    juros_anos = (anos * juros_base)
    meses = (anos * 12)
    juros_mes = (juros_anos / meses)
    # tabela de amortização
    amortizacao = saldo_devedor / meses
    print('\033[34mSaldo devedor\033[m, \033[35mJuros\033[m, \033[35mAmortização\033[m, \033[36mParcela Mês\033[m\n')
    for parcela in range(meses):
        saldo_devedor = (saldo_devedor - amortizacao)
        juros_pago = (saldo_devedor * juros_mes)
        prestacao = (amortizacao + juros_pago)
        print(parcela, '\033[34m{:.2f}\033[m / \033[35m{:.2f}\033[m / \033[35m{:.2f}\033[m / \033[36m{:.2f}\033[m'.format(saldo_devedor, juros_pago, amortizacao, prestacao))
        '''
    dados = []
    dados.append(('Saldo devedor', 'Juros Mês', 'Amortização', 'Prestação'))
    # tabela tela 2
    linha = 0
    for registro in dados:
        coluna = 0
        tela_2.tableWidget.insertRow(linha)
        for elemento in registro:
            ceta = QtWidgets.QTableWidgetItem(elemento)
            tela_2.tableWidget.setItem(linha, coluna, ceta)
            coluna += 1
        linha += 1


app = QtWidgets.QApplication([])
# chama interfaces graficas
tela = uic.loadUi('ui/tela_finan.ui')
tela_2 = uic.loadUi(('ui/tela_finan2.ui'))
# vincula botões as funções
tela.pushButton.clicked.connect(RecuperaDados)
tela.pushButton_2.clicked.connect(QuerImprimir)

tela.show()
app.exec()
