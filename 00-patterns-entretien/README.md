# Patterns d'entretien technique — module transverse

Contrairement aux autres modules (organisés par structure/algorithme), celui-ci
est organisé par **pattern de raisonnement**, parce que c'est ainsi que les
entretiens techniques big tech (Google, Meta, Amazon, etc.) testent — pas par
"connais-tu Dijkstra" mais "sais-tu reconnaître qu'un problème se résout par
fenêtre glissante".

**À travailler en parallèle des autres modules, pas après.** Rythme suggéré :
un pattern toutes les 1-2 semaines, en alternance avec le programme principal.

## Patterns couverts
- `two-pointers/` — paires, sous-tableaux, palindromes
- `sliding-window/` — sous-tableaux/sous-chaînes de taille fixe ou variable
- `backtracking/` — permutations, combinaisons, contraintes (sudoku, N-reines)
- `binary-search-on-answer/` — quand la réponse elle-même se cherche par dichotomie
- `greedy/` — preuve d'optimalité locale = optimalité globale

## Convention
Chaque dossier contient, comme les autres modules :
- `pseudocode.md`
- un fichier Python par exercice représentatif du pattern
- `notes.md` — signal de reconnaissance ("comment je sais que c'est CE pattern")

## Objectif de sortie
Pour chaque pattern : être capable de le reconnaître en moins de 2 minutes de
lecture d'un énoncé nouveau, sans l'avoir vu avant.
