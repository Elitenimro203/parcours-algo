# `if __name__ == "__main__":`

## Le mécanisme
`__name__` est une variable spéciale que Python assigne automatiquement à
chaque fichier `.py` exécuté. Sa valeur dépend de **comment** le fichier a
été utilisé :

- Fichier lancé **directement** (`python fichier.py`) → `__name__` vaut
  exactement `"__main__"`
- Fichier **importé** depuis un autre script (`from fichier import x`) →
  `__name__` vaut le nom du fichier (`"fichier"`), pas `"__main__"`

Le `if __name__ == "__main__":` teste donc "est-ce que ce fichier est le
point d'entrée direct du programme, ou juste importé par un autre ?".

## Pourquoi ça sert
Quand un fichier est importé, Python exécute **tout le code au niveau
racine** (hors des fonctions), du début à la fin — comme s'il était lancé
normalement. Sans protection, un `import` déclencherait donc aussi les
`print`, les appels de test, les `assert`, etc., écrits en dehors des
fonctions du fichier importé.

Le `if __name__ == "__main__":` évite ça : le code de test/démo à
l'intérieur ne s'exécute que si le fichier est lancé directement, jamais à
l'import.

## `=` vs `==`
- `=` → **assignation** : met une valeur dans une variable
  (ex. `j = i - 1`)
- `==` → **comparaison** : teste si deux valeurs sont égales, renvoie
  `True`/`False` (ex. `__name__ == "__main__"`)

Un `if` a besoin d'une expression qui renvoie `True`/`False`, donc toujours
`==` pour une comparaison, jamais `=`.
