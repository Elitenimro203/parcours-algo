# Tri par insertion — Pseudo-code

## Cas d'usage réel
Trier des relevés d'humidité (%) de capteurs GreenGrow avant affichage sur le
dashboard.

Exemple de jeu de données :
```
[42, 15, 38, 27, 8, 50]
```

## Pseudo-code
_(à compléter pendant la session, au fur et à mesure du raisonnement)_

```
ALGORITHME TRI_INSERTION

VARIABLE Valeur_courante, i, j, Tableau Nbre(6): Entier

Début
    Nbre ← [42, 15, 38, 27, 8, 50]
    Pour i allant de 1 à longueur(Nbre) - 1 Faire
        Valeur_courante ← Nbre [i]
        j ← i - 1
        TantQue j >= 0 et Nbre [j] > Valeur_courante Faire
            Nbre[j+1] ← Nbre[j]
            j ← j-1
        FinTantQue
        Nbre[j+1] ← Valeur_courante
    FinPour
    Ecrire("Tableau trié" :  Nbre)
Fin
```

```
FONCTION TRI_INSERTION(Nbre: Tableau[Réel]) : Tableau [Réel]

Variable valeur_courante: Réel
         i, j : Entier

Début
    Pour i allant de 1 à longueur(Nbre) - 1 Faire
        valeur_courante ← Nbre[i]
        j ← i-1
        TantQue j >= 0 et Nbre[j] > valeur_courante Faire
            Nbre[j+1] ← Nbre[j]
            j ← j-1
        FinTantQue
        Nbre[j+1] ← valeur_courante
    FinPour
    Retourne Nbre
Fin
```

## Traces manuelles
_(noter ici le déroulé pas à pas sur l'exemple GreenGrow)_

| Passe | État du tableau | Élément inséré | Position finale |
|---|---|---|---|
| 1 |  |  |  |
