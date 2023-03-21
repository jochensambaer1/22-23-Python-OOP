#Je maakt een programma dat een letter van het alfabet vraagt aan de gebruiker. Als
#de gebruiker een klinker (a, e, i, o of u) invoert dan volgt een bericht dat de letter die
#is ingevoerd een klinker is. Bij invoer van y volgt de boodschap dat deze letter soms
#als klinker, en soms als medeklinker kan gelden. In elk ander geval volgt de
#boodschap dat een medeklinker werd ingevoerd. Bij een string die langer is dan 1
#karakter zorg je voor een bericht dat je de uitkomst niet kan bereken als meer dan
#één karakter werd ingevoerd. Tip: je kan dit laatste checken met de len() functie.
letter =input("geef een leter in " )
if "a" |"e" |"i" |"o" |"u" :
    print("het is een klinker ")
elif "y":
    print("het is soms een klinker")
else :
    print("het is een medeklinker")

