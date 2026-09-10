# Parcours Algo — Portfolio d'ingénieur

Dépôt de travail regroupant l'ensemble des algorithmes, structures de données
et patterns d'entretien étudiés durant le parcours (ESATIC → M2 MBDS → CMU
Africa), avec pour chaque sujet : pseudo-code, implémentation Python testée,
notes, et — désormais — les éléments qui font qu'un projet ouvre vraiment des
portes (tests, CI, article technique, déploiement).

Chaque brique s'appuie autant que possible sur un cas d'usage réel (GreenGrow,
PrintFlow OS, ou un projet standalone à plus fort signal marché selon le
sujet) plutôt que sur un exercice isolé.

## Organisation

```
parcours-algo/
├── 00-patterns-entretien/        # Transverse — en parallèle du reste
│   ├── two-pointers/
│   ├── sliding-window/
│   ├── backtracking/
│   ├── binary-search-on-answer/
│   └── greedy/
├── 00-fondamentaux-python/       # Transverse — mécanismes du langage rencontrés
├── 01-tris/
│   ├── 01-tri-bulle/             ✅
│   ├── 02-tri-selection/         ✅
│   ├── 03-tri-insertion/         ✅
│   ├── 04-tri-rapide/            ⏳
│   ├── 05-tri-fusion/            ⏳
│   └── 06-tri-tas/               ⏳
│   └── 🎯 PROJET — Moteur de tri GreenGrow (benchmark comparatif)
├── 02-structures-donnees/        # Piles, files, listes, BST, AVL, hachage ⏳
│   └── 🎯 PROJET — Gestionnaire de file PrintFlow
├── 03-graphes/                   # BFS, DFS, Dijkstra, A*, Kruskal/Prim ⏳
│   └── 🎯 PROJET — Réseau de zones GreenGrow (+ déploiement minimal)
├── 04-programmation-dynamique/   ⏳
│   └── 🎯 PROJET — Allocation ressources GreenGrow (+ déploiement minimal)
├── 05-optimisation-multiobjectif/ # ✅ Pareto, NSGA-II — à ranger ici
├── 06-revisions-espacees/        # Suivi des révisions courtes espacées
├── 07-portfolio-final/           # Synthèse des capstones (à créer en fin de parcours)
├── 08-checklists/                # Checklist de sortie obligatoire par module
└── projets-appliques/
    ├── greengrow/
    └── printflow/
```

## Convention par sujet

Chaque dossier de sujet contient :
- `pseudocode.md`
- `<nom_algo>.py` — testé, avec vrais tests unitaires (pas un `assert` isolé)
- `notes.md` — complexité, pièges, cas d'usage réel, signal de reconnaissance
  (pour les patterns d'entretien)

Voir `08-checklists/README.md` pour les critères de sortie complets (tests,
CI, article, éventuel déploiement).

## Règle de fonctionnement

C'est Kouadio qui écrit le pseudo-code et le code à chaque palier. Claude pose
les questions, vérifie, corrige, pousse plus loin — ne résout pas les
exercices à sa place. Le choix du projet à chaque palier (GreenGrow/PrintFlow
vs projet standalone à plus forte valeur de portfolio) est évalué au cas par
cas selon le sujet et le niveau démontré en session.

## Statut d'avancement

| Sujet | Statut |
|---|---|
| Patterns d'entretien | ⏳ À démarrer (en parallèle) |
| Tri à bulle | ✅ Acquis |
| Tri par sélection | ✅ Acquis |
| Tri par insertion | ✅ Acquis |
| Tri rapide / fusion / tas | ⏳ À venir |
| Structures de données | ⏳ À venir |
| Graphes | ⏳ À venir |
| Programmation dynamique | ⏳ À venir |
| Optimisation multi-objectif | ✅ Acquis (à ranger dans ce dépôt) |

Voir `ROADMAP.md` pour le détail des prochains paliers.
