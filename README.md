# parcours-algo

![tests](https://github.com/Elitenimro203/parcours-algo/actions/workflows/tests.yml/badge.svg)

Mon parcours d'ingénierie algorithmique, de la complexité à la programmation
dynamique. Chaque notion est travaillée en trois temps : **pseudo-code**,
**implémentation Python testée**, **notes** (complexité prouvée, pièges, cas
d'usage). Chaque palier se ferme par un **projet réel déployé**, pas par un
exercice jetable.

> Kouadio · Master MBDS, ESATIC (Abidjan) · Python, FastAPI, SQL, React/TypeScript

## Feuille de route (26 oct. 2026 → 3 janv. 2027)

| Semaine | Thème | Pattern d'entretien | Livrable |
|---|---|---|---|
| S1 | Complexité, hachage, tri rapide | Two pointers | Dépôt public + CI pytest |
| S2 | Tri fusion, tri par tas, dichotomie | Binary search on answer | Module tris fermé + article 1 |
| S3 | Listes chaînées | Sliding window | Entretien blanc 1 |
| S4 | Piles, files, deques | Pile monotone | File d'impression PrintFlow (C) |
| S5 | Arbres binaires, ABR | Parcours DFS/BFS | Bibliothèque d'arbres testée |
| S6 | Tas, trie, union-find | Backtracking | Module structures fermé + article 2 |
| S7 | Graphes : BFS, DFS, tri topologique | Grilles comme graphes | Moteur de graphe testé |
| S8 | Dijkstra, Prim, Kruskal | Greedy | **Capstone Vigie des Eaux** déployé + article 3 |
| S9 | Programmation dynamique 1D | Mémoïsation, tabulation | Bibliothèque DP testée |
| S10 | DP 2D, sac à dos | Révision des patterns | **Capstone GreenGrow** déployé + article 4 |

Environ 130 exercices LeetCode répartis sur les 10 semaines, chacun noté
(pattern, complexité, erreur commise) dans le `notes.md` de son dossier.

## Avancement

- [x] Tri à bulle
- [x] Tri par sélection
- [x] Tri par insertion
- [ ] Tri rapide · tri fusion · tri par tas
- [ ] Structures de données
- [ ] Graphes
- [ ] Programmation dynamique
- [ ] Portfolio final

## Capstones

| Projet | Algorithmes | Problème réel |
|---|---|---|
| **Vigie des Eaux** (S8) | BFS, Dijkstra | Trouver les zones en aval d'un point de pollution et le trajet d'intervention le plus court sur un réseau hydrographique |
| **GreenGrow** (S10) | Sac à dos 0/1 | Choisir les cultures à placer dans des bacs selon la surface, l'eau disponible et le rendement attendu |

Projets appliqués intermédiaires : file d'impression de **PrintFlow OS** (S4,
file circulaire en C), recherche par préfixe et classement des retards pour
**GestPresence** (S6, trie et tas derrière une route FastAPI).

## Organisation du dépôt

```
00-fondamentaux-python/       mécanismes du langage (__main__, pytest…)
00-patterns-entretien/        two-pointers, sliding-window, backtracking, greedy…
01-tris/                      bulle, sélection, insertion, rapide, fusion, tas
02-structures-donnees/
03-graphes/
04-programmation-dynamique/
05-optimisation-multiobjectif/
06-revisions-espacees/        exercices ratés repris à J+1, J+7, J+21
07-portfolio-final/
08-checklists/
projets-appliques/            greengrow, printflow…
```

Chaque dossier d'algorithme suit la même forme :

```
01-tris/03-tri-insertion/
├── pseudocode.md
├── tri_insertion.py
├── test_tri_insertion.py
└── notes.md          complexité (temps et espace) et sa preuve
```

## Lancer les tests

```bash
python -m pip install -r requirements-dev.txt
pytest
```

La CI GitHub Actions relance `pytest` à chaque push et chaque pull request.

## Checklist de sortie d'un module

Un module n'est fermé que si les cinq cases sont cochées : code, tests
unitaires, complexité prouvée, README, article technique.

## Articles

À venir : un article par module fermé (Medium ou dev.to).
