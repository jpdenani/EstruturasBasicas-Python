valorHora = float(input("Insira seu valor recebido por hora: "))
horas = int(input("Insira as horas trabalhadas: "))
salario = valorHora*horas
print(f"Seu salário bruto esse mês foi: {salario} reais")

ir = salario * 0.11
inss = salario * 0.08
sindicato = salario * 0.05
salarioLiq = salario - ir - inss - sindicato
print(f"Seu salário líquido foi de: {salarioLiq} reais")