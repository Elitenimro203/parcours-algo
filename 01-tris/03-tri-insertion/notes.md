# Tri par insertion — Notes

## Complexité

- **Pire cas : O(n²)** — quand le tableau est trié à l'envers, chaque nouvel
  élément doit être décalé jusqu'au tout début.
- **Meilleur cas : O(n)** — quand le tableau est déjà trié, chaque élément
  reste à sa place dès la première comparaison, la boucle `TANT QUE` ne fait
  qu'un seul test et s'arrête.
- **Cas moyen : O(n²)**.
- Le nombre réel de décalages ne dépend pas de la taille du tableau seule,
  mais du nombre d'éléments qui ne sont pas encore à leur bonne position
  (les *inversions*). Sur des données déjà triées ou presque, ce nombre est
  très faible : c'est exactement pour ça que le tri par insertion **limite
  les actions inutiles** — il ne fait que le travail strictement nécessaire,
  contrairement au tri par sélection qui refait toujours le même nombre de
  comparaisons, trié ou pas.
- **Espace : O(1)** — le tri se fait en place, aucune structure auxiliaire.

## Stabilité

**Le tri par insertion est stable.** La condition de la boucle utilise un
`>` strict, pas un `>=` :

```
TANT QUE j >= 0 ET tableau[j] > valeur_courante
```

Si `tableau[j]` est **égal** à `valeur_courante`, la condition devient
fausse et la boucle s'arrête immédiatement — sans décaler cet élément égal.
Résultat : `valeur_courante` vient toujours se placer **juste après**
l'élément égal déjà présent, jamais avant. L'ordre relatif entre deux
valeurs égales est donc préservé — c'est la définition même de la
stabilité.

## Cas d'usage réel identifié

**GreenGrow — relevés de capteurs d'humidité.**
Les données arrivent en flux, un relevé à la fois, et s'ajoutent à une liste
déjà triée pour l'affichage dashboard. C'est exactement le scénario où le
tri par insertion est le plus avantageux des trois vus jusqu'ici :

- Le tri par sélection ferait toujours le même nombre de comparaisons,
  qu'il y ait 0 ou 50 éléments à déplacer — aucun avantage à exploiter sur
  un flux quasi-trié.
- Le tri par insertion, lui, s'adapte : insérer une nouvelle valeur dans
  une liste déjà triée est quasi-instantané (proche de O(n) dans ce
  contexte), au lieu de retrier tout le tableau à chaque nouvel arrivage.

## Comparaison avec les tris déjà vus

|                                                     | Tri à bulle                              | Tri par sélection                  | Tri par insertion |
| --------------------------------------------------- | ----------------------------------------- | ----------------------------------- | ----------------- |
| Complexité pire cas                                | O(n²)                                    | O(n²)                              | O(n²)            |
| Complexité meilleur cas                            | O(n) (avec optimisation arrêt anticipé) | O(n²) (aucune adaptation possible) | O(n)              |
| S'adapte aux données déjà triées ?              | Partiellement                             | Non                                 | Oui, nettement    |
| Bon candidat pour un flux quasi-trié (GreenGrow) ? | Moyen                                     | Non                                 | Oui               |

## Points de confusion rencontrés pendant la session

- **`tableau[j+1] ← tableau[j]` vs `tableau[j+1] ← valeur_courante`**
  La première ligne (dans la boucle) est un **décalage** : on pousse
  l'élément actuellement en trop grand d'une case vers la droite, et ça
  peut se répéter plusieurs fois dans une même insertion. La seconde ligne
  (après la boucle) est l'**installation finale** : elle ne s'exécute
  qu'une seule fois, une fois que la bonne place a été trouvée.
  → Image utile : une file d'attente où les personnes trop grandes reculent
  d'un pas, jusqu'à ce que la nouvelle personne trouve sa place et s'y
  installe.
- **`tableau[j]` n'est pas une valeur figée**
  `tableau[j]` désigne toujours la valeur *actuellement* présente à cet
  index au moment où la ligne s'exécute — pas une valeur "d'origine" de la
  liste non triée. Comme le tableau change au fil des décalages, ce que
  retourne `tableau[j]` change aussi.
- **Le double rôle de la condition `j >= 0 ET tableau[j] > valeur_courante`**

  - `j >= 0` protège contre le débordement (ne jamais essayer de lire
    `tableau[-1]`, qui n'existe pas)
  - `tableau[j] > valeur_courante` est la vraie condition métier
  - Grâce au `ET`, si `j` devient `-1`, la première condition est déjà
    fausse et la seconde n'est jamais évaluée — pas de plantage.
- **Le cas `j = -1` est normal, pas une erreur**
  C'est ce qui arrive quand un élément doit remonter jusqu'à la toute
  première position (ex. le plus petit élément du tableau). La ligne
  finale devient alors `tableau[-1+1] ← valeur_courante`, soit
  `tableau[0]` — cohérent.

## Pour qui reprend ces notes plus tard (portfolio / transmission)

Ce module a demandé plusieurs itérations avant que la logique du
décalage (`tableau[j+1] ← tableau[j]`) soit bien distincte de
l'installation finale (`tableau[j+1] ← valeur_courante`) — c'est normal,
c'est le point qui piège le plus souvent sur cet algorithme. Si ce point
reste flou en le relisant, reprendre l'exemple du tableau
`[42, 15, 38, 27, 8, 50]` pas à pas, ligne par ligne, avant de continuer.
