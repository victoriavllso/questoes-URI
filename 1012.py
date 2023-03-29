A,B,C = input().split()
A,B,C = float(A), float(B),float(C)

at = (A*C)/2
ac = 3.14159*C*C
atra = (A+B)*C/2
aq = B*B
ar = A*B

print("TRIANGULO: %.3f"%(at))
print("CIRCULO: %.3f"%(ac))
print("TRAPEZIO: %.3f"%(atra))
print("QUADRADO: %.3f"%(aq))
print("RETANGULO: %.3f"%(ar))
