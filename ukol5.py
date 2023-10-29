
teploty = [
    [2.1, 5.2, 6.1, -0.1],
    [2.2, 4.8, 5.6, -1.0],
    [3.3, 6.5, 5.9, 1.2],
    [2.9, 5.6, 6.0, 0.0],
    [2.0, 4.6, 5.5, -1.2],
    [1.0, 3.2, 2.1, -2.0],
    [0.4, 2.7, 1.3, -2.8]
]

#Vytvoř seznam průměrných teplot pro každý den.

denni_prumer = [sum(den) / len(den) for den in teploty]
print(denni_prumer)

#Vytvoř seznam ranních teplot.

ranni_teploty = [den[0] for den in teploty]
print(ranni_teploty)


#Vytvoř seznam nočních teplot.

nocni_teploty = [den[3] for den in teploty]
print(nocni_teploty)

#Vytvoř seznam dvouprvkových seznamů obsahujících pouze polední a noční teplotu.

poledni_nocni_teploty = [[den[1], den[3]] for den in teploty]
print(poledni_nocni_teploty)

