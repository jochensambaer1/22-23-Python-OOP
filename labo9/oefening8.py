# Oefening 8: De dierentuin 2.0
# Bestudeer de oefeningen uit het vorige labo mbt de dieren in de dierentuin
# In plaats van elke dierenklasse rechtstreeks te laten erven van de klasse Dier,
# maak je nieuwe klasses aan: NulpotigDier, TweepotigDier en VierpotigDier
# Deze klasses erven van klasse Dier en bepalen het aantal poten van elke
# instance
# Pas nu klasses Wolf, Schaap, Slang en Papegaai zo aan dat elke klasse erft van
# deze nieuwe klasses ipv rechtstreeks van Dier
# Welke gevolgen zijn er voor je method beschrijvingen?
# Werken we met een klasse attribuut: aantal_poten
# Hebben we een __init__ method nodig in elke subklasse, of volstaat
# Dier.__init__?
# De __str__ method van elke klasse hoort behalve de string die we nu
# teruggeven ook het dierengeluid dat elk dier maakt mee te geven. Dus bij
# schaap: Baa — wit schaap, 4 poten
# Python Programming - Labo 9 5
# Hoe kan je overerving gebruiken om zoveel mogelijk code hergebruik te
# hebben?