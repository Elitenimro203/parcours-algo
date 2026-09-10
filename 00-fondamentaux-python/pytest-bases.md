# `pytest` — bases

## Convention de nommage (obligatoire pour que pytest détecte les tests)
- Fichier : `test_*.py` (ou `*_test.py`)
- Fonction : doit commencer par `test_`

Sans ce préfixe, `pytest` ignore silencieusement la fonction — pas
d'erreur, elle est juste invisible pour lui.

## Structure d'une fonction de test
Toujours le même schéma en 2 étapes, **sans paramètre ni `return`** :
1. Appeler la fonction qu'on veut tester, avec des données créées
   directement dans le corps du test
2. Vérifier avec `assert` que le résultat obtenu correspond à l'attendu

```python
def test_nom_du_cas():
    resultat = ma_fonction(donnees_du_cas)
    assert resultat == valeur_attendue
```

## `assert` dans pytest vs `assert` de script
Même mot-clé qu'ailleurs, mais `pytest` capture l'échec proprement : si
l'assertion est fausse, il indique précisément quelle ligne a échoué et
pourquoi — contrairement à un `assert` isolé dans un script, qui plante
tout le programme sans ce détail.

## Isolation des cas
Chaque scénario (cas limite, cas normal...) devient sa **propre fonction**.
Si un test échoue, les autres s'exécutent quand même — on voit d'un coup
lesquels passent et lesquels non.

## Lancer les tests
Depuis le dossier contenant le fichier de test :
```
pytest
```
Il détecte lui-même tous les fichiers `test_*.py` et exécute toutes les
fonctions `test_*` qu'il y trouve.

## Point de méthode (retenu en pratique)
Avant d'écrire l'appel dans un test, se demander concrètement : *cette
variable/fonction existe-t-elle déjà, ici, dans ce fichier précis ?* — ne
pas réutiliser un nom vu dans un autre fichier sans vérifier. Écrire la
valeur brute (`[]`, `[42]`, `[8, 15, 27]`) avant de se poser la question de
l'abstraction.
