"""
tri par sélection — appliqué aux relevés d'humidité des capteurs GreenGrow.

Complexité :
- Temps  :
- Espace :

Stabilité :
"""


def tri_selection(releves: list[int]) -> list[int]:
    """
    Trie une liste de relevés par tri par sélection, en place.
    """
    raise NotImplementedError("À écrire toi-même, à partir de pseudocode.md")


if __name__ == "__main__":
    capteurs_greengrow = [42, 15, 38, 27, 8, 50]
    print("Avant tri :", capteurs_greengrow)
    resultat = tri_selection(capteurs_greengrow)
    print("Après tri :", resultat)
    assert resultat == sorted(capteurs_greengrow)
    print("✅ Test basique OK")
