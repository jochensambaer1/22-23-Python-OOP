# Beeld je in dat je net een nieuwe bankrekening hebt geopend die je 1,2% rente per
# jaar geeft. Deze rente wordt uitbetaald op het einde van het jaar en toegevoegd aan
# je bankrekening. Schrijf een programma dat begint met het lezen van het bedrag dat
# je bij het begin van het jaar op je rekening hebt gezet. Het programma rekent dan uit
# (en toont) de stand van de rekening na 1, 2 en 3 jaar. Toon elk bedrag met wat uitleg
# en afgerond tot op 2 cijfers na de komma.


rente = 1.2
bankrekening = int(input("wat is er in je bankrekening "))
jaar = int (input("hoe veel jaaren "))

jaar1=bankrekening+(rente*bankrekening)
print(f"het eerste jaar is {jaar1}")
jaar2=jaar1+(rente*jaar1)
print(f"het eerste jaar is {jaar2}")
jaar3=jaar2+(rente*jaar2)
print(f"het eerste jaar is {jaar3}")
jaar4=jaar3+(rente*jaar3)
print(f"het eerste jaar is {jaar4}")
jaar5=jaar4+(rente*jaar4)
print(f"het eerste jaar is {jaar5}")
#loop
for i in jaar:
    
  totaal = bankrekening+(rente*bankrekening)
print(f"het {i} jaar is {totaal}")
