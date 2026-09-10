# Roadmap — thèmes à aborder

## Patterns d'entretien (00-patterns-entretien/) — transverse, en parallèle
- [ ] Two pointers
- [ ] Sliding window
- [ ] Backtracking
- [ ] Binary search on answer
- [ ] Greedy (+ preuve d'optimalité)

## Tris (01-tris/)
- [x] Tri à bulle
- [x] Tri par sélection
- [x] Tri par insertion
- [ ] Tri rapide (quicksort)
- [ ] Tri fusion (merge sort)
- [ ] Tri par tas (heap sort)
- [ ] 🎯 Capstone : benchmark comparatif des 6 tris sur flux GreenGrow

## Structures de données (02-structures-donnees/)
- [ ] Piles / files
- [ ] Listes chaînées (simple, double)
- [ ] Arbres binaires / arbres de recherche (BST)
- [ ] Arbres équilibrés (AVL — au moins la théorie)
- [ ] Tables de hachage
- [ ] Tas binaire (heap) — prérequis pour tri par tas
- [ ] 🎯 Capstone : gestionnaire de file PrintFlow (FIFO + undo + BST)

## Graphes (03-graphes/)
- [ ] Représentations (liste d'adjacence, matrice)
- [ ] Parcours BFS / DFS
- [ ] Plus court chemin (Dijkstra)
- [ ] A*
- [ ] Arbre couvrant minimal (Kruskal / Prim)
- [ ] 🎯 Capstone : réseau de zones GreenGrow + déploiement minimal (interface cliquable)

## Programmation dynamique (04-programmation-dynamique/)
- [ ] Mémoïsation vs tabulation
- [ ] Problèmes classiques (sac à dos, sous-séquence commune, etc.)
- [ ] 🎯 Capstone : allocation de ressources GreenGrow + déploiement minimal

## Déjà couvert ailleurs, à ranger dans ce dépôt
- [x] Optimisation multi-objectif (Pareto, somme pondérée, Tchebycheff, NSGA-II)
- [x] Théorie des langages et compilation (guides existants, à lier ou migrer)

## Portfolio final (07-portfolio-final/)
- [ ] Assembler les capstones en un module réutilisable, documenté, testé
- [ ] Vérifier que chaque module coché a passé la checklist de sortie
      (voir `08-checklists/README.md`)

## Notes
Ce fichier évolue à chaque session. Chaque case cochée doit correspondre à un
module ayant validé sa checklist de sortie complète — pas juste un code qui
tourne.
