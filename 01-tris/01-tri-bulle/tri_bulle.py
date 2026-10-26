"""
tri à bulle — appliqué aux relevés d'humidité des capteurs GreenGrow.

Complexité :
- Temps  :
- Espace :

Stabilité :
"""


def tri_bulle(releves: list[int]) -> list[int]:
    """
    Trie une liste de relevés par tri à bulle, en place.
    """
    for i in range(len(releves) - 1):
        for j in range(len(releves) - 1 - i):
            if releves[j] > releves[j + 1]:
                temp = releves[j]
                releves[j] = releves[j + 1]
                releves[j+1] = temp
    return releves


if __name__ == "__main__":
    capteurs_greengrow = [42, 15, 38, 27, 8, 50]
    print("Avant tri :", capteurs_greengrow)
    resultat = tri_bulle(capteurs_greengrow)
    print("Après tri :", resultat)
    assert resultat == sorted(capteurs_greengrow)
    print("✅ Test basique OK")