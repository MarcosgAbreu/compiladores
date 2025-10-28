v1 = float(input("Digite o primeiro valor: "))
v2 = float(input("Digite o segundo valor: "))

v1_int = (v1 % 1 == 0)
v2_int = (v2 % 1 == 0)

if v1_int and v2_int:
    print("Compativel")  # dois inteiros
elif not v1_int and not v2_int:
    print("Compativel")  # dois floats
else:
    print("Nao compativel")  # tipos diferentes
