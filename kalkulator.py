n = int(input(("Wprowadź ilość składników posiłku: ")))
kalkulator = [0,0,0]
for i in range(n):
    print(f"Podaj ilości makroskładników {i+1}. składnika w gramach.")
    kalkulator[0] += int(input("Białek: "))
    kalkulator[1] += int(input("Węglowodanów: "))
    kalkulator[2] += int(input("Tłuszczów: "))
    
print(f"Twój posiłek ma {kalkulator[0]} gramów białek, {kalkulator[1]} gramów węglowodanów i {kalkulator[2]} gramów tłuszczów")
    
    
    
