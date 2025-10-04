# FOR - loop que percorre sequências, repetindo ações para cara elemento.
# WHILE - loop que pode executa ações definidas ou enquanto a condição for verdadeira


notas = []

for x in range(5):
    codigo_aluno = input("Matricula: ")
    nota = float(input("Nota: "))
    resultado = [codigo_aluno, nota]
    notas.append(resultado)

print("quantidade de notas", len(notas))

for n in notas:
    codigo_aluno = n [0]
    nota = n[1]
    print("Matricula", codigo_aluno, "tirou a nota", nota)

        