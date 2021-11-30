'''Faça um programa que tenha uma função notas() que pode receber várias 
notas de alunos e vai retornar um dicionário com as seguintes informações:

- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)
'''
def notas(*n, sit = False):
    r = {}
    r["quantidade"] = len(n)
    r["maior"] = max(n)
    r["menor"] = min(n)
    r["media"] = sum(n)/len(n)
    if sit:
        if r["media"] >= 7:
            r["situacao"] = 'Aprovado'
        elif r["media"] < 7 and r["media"] > 5:
            r["situacao"] = 'Recuperação'
        else:
            r["situacao"] = 'Reprovado'
    return r

resp = notas(10, 10, sit = True)
print(resp)
    