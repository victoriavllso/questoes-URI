n1, n2, n3, n4 = input().split()
n1 = float(n1) 
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)

media = (2*n1 + 3*n2 + 4*n3 + 1*n4)/10
print("Media: %.1f"%(media))

if 7.0 <= media:
    print("Aluno aprovado.")
elif media <5.0:
    print("Aluno reprovado.")
elif 5.0<=media<=6.9:
    print("Aluno em exame.")
    notaexame = float(input())
    print("Nota do exame: %.1f"%(notaexame))
    mf = (media+notaexame)/2
    if mf>=5:
        print("Aluno aprovado.")
        print("Media final: %.1f"%(mf))
    else:
        print("Aluno reprovado.")
