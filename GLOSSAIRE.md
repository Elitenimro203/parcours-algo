# Glossaire — mécanismes Python rencontrés

Notes ponctuelles sur des mécanismes du langage Python croisés en travaillant
sur les modules du parcours, transverses à tous les algorithmes.

## `if __name__ == "__main__":`

Chaque fichier `.py` reçoit automatiquement une variable spéciale `__name__`,
dont la valeur dépend de comment le fichier est utilisé :
- Fichier lancé directement (`python fichier.py`) → `__name__` vaut `"__main__"`
- Fichier importé depuis un autre script (`from fichier import ...`) →
  `__name__` vaut le nom du fichier, pas `"__main__"`

Ce `if` permet donc d'exécuter un bloc de code (exemples, tests) **seulement**
quand le fichier est lancé directement — pas quand il est importé ailleurs.
Sans cette protection, tout le code hors fonction s'exécuterait aussi à
l'import, polluant la sortie ou ralentissant/cassant l'import.

## `=` vs `==`
_(à compléter)_
