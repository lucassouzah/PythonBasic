salario = float (input("Informe o valor do seu salario: "))

if  salario <= 3000:
    print("Programador Junior!")
elif salario > 3000 and salario <= 6000:
    print("Programador Pleno!")
elif salario > 6000 and salario <=12000:
    print("Programador Senior")  
else:
    print("Gerente de TI")     