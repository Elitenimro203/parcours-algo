"""
Tri par insertion — appliqué aux relevés d'humidité des capteurs GreenGrow.

Complexité (à confirmer en fin de session) :
- Temps  : O(?) pire cas, O(?) meilleur cas
- Espace : O(?)
"""


def tri_insertion(releves: list[int]) -> list[int]:
    """
    Trie une liste de relevés d'humidité par insertion, en place.

    TODO: implémenter pendant la session, en s'appuyant sur pseudocode.md
    """
    for i in range(1, len(releves)): 
        releve_courant = releves[i]
        j = i - 1
        while j >= 0 and releves[j] > releve_courant:
            releves[j + 1] = releves[j]
            j -= 1
        releves[j + 1] = releve_courant

    return releves


if __name__ == "__main__":
    capteurs_greengrow = [42, 15, 38, 27, 8, 50]
    print("Avant tri :", capteurs_greengrow)
    resultat = tri_insertion(capteurs_greengrow)
    print("Après tri :", resultat)

    assert resultat == sorted(capteurs_greengrow), "Le tri ne produit pas le bon résultat"
    print("✅ Test basique OK")
