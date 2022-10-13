""" ----
Crie um tipo abstrato de dado (TAD) para manipular números complexos na linguagem Python.
O método deve:

- calcular três números complexos;
- realizar todas as operações básicas;
- e imprimir as propriedades real e img do números.
    ----     """

"""___ Calculando os três números complexos ___"""
# Primeiro valor
x = complex(12,-5)
# Segundo valor
y = complex(1,2)
# Terceiro valor
z = complex(-2,1)

print("O primeiro valor em complexo é {}.".format(x))
print("O segundo valor em comlexo é {}.".format(y))
print("O terceiro valor em complexo é {}.".format(z))

"""___ Partindo para as operações matemáticas ___"""
# Soma
print("Somando os três valores, em complexo, resulta em {}.".format(x+y+z))
# Subtração
print("Subtraindo os três valores, em complexo, resulta em {}.".format(x-y-z))
# Multiplicação
print("Multiplicando os três valores, em complexo, resulta em {}.".format(x*y*z))
# Divisão
print("Somando o primeiro valor com o segundo e dividindo pelo terceiro, em complexo, resulta em {}.".format(((x+y)/z)))

"""___ Impressão das partes reais e imaginarias ___"""
# Primeiro valor
print("O valor real do primeiro número é {} e a parte imaginaria desse mesmo número é {}.".format(x.real,x.imag))
# Segundo valor
print("O valor real do segundo número é {} e a parte imaginaria desse mesmo número é {}.".format(y.real,y.imag))
# Terceiro valor
print("O valor real do terceiro número é {} e a parte imaginaria desse mesmo número é {}.".format(z.real,z.imag))
