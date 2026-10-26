```
←
```


# Tri à bulle — Pseudo-code

## Cas d'usage réel

_(à toi de le formuler : pourquoi cet algo, dans quel contexte GreenGrow ou autre ?)_

Jeu de données d'exemple :

```
[42, 15, 38, 27, 8, 50]
```

## Pseudo-code

```
ALGORITHME TRI_A_BULLE

VARIABLE Temp, i, j, Tableau Nbre(6): Entier

Début
	Nbre ← [42, 15, 38, 27, 8, 50]
	Pour i allant de 0 à longueur(Nbre) - 2 Faire
    	Pour j allant de 0 à (longueur(Nbre) - 2)- i Faire
        	Si Nbre[j] > Nbre[j+1] Alors
            	Temp ← Nbre[j]
            	Nbre[j] ← Nbre[j+1]
            	Nbre[j+1] ← Temp
            Finsi
    	FinPour
    FinPour
    Ecrire("Tri à bulle effectué": Nbre)
Fin
          
```

## Traces manuelles

| Passe | État du tableau | Ce qui s'est passé |
| ----- | ---------------- | ------------------- |
|       |                  |                     |
