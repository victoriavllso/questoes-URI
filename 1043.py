A,B,C = input().split()
A, B, C = float(A), float(B), float(C)
if (A<B+C) and (B<A+C) and (C<A+B):
    perimetro = (A+B+C)
    print("Perimetro = %.1f"%(perimetro))
else:
    area = ((A+B)*C/2)
    print("Area = %.1f"%(area))
