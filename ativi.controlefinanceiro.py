gastosAlimentacao = float(input("Digite o valor dos gastos com alimentação: "))
gastosTransporte = float(input("Digite o valor dos gastos com transporte: "))
gastosLazer = float(input("Digite o valor dos gastos com lazer: "))

salario = float(input("Digite o valor da mesada: "))

totalGastos = gastosTransporte + gastosAlimentacao + gastosLazer

if totalGastos > salario:
    print("Foi gasto mais que o salário")
else:
    print("Os gastos estão dentro do salário")