from tri_insertion import tri_insertion

def test_liste_vide():
   resultat = tri_insertion([])
   assert resultat == []

def test_un_seul_element():
   resultat = tri_insertion([42])
   assert resultat == [42]

def test_deja_trie():
   resultat = tri_insertion([8, 15, 27, 38, 42, 50])
   assert resultat == [8, 15, 27, 38, 42, 50]

def test_valeur_negative():
   resultat = tri_insertion([-20, 50, -15, 6])
   assert resultat == [-20, -15, 6, 50]

def test_trie_envers():
   resultat = tri_insertion([50, 42, 38, 27, 15, 8])
   assert resultat == [8, 15, 27, 38, 42, 50]

def test_doublons():
   resultat = tri_insertion([15, 17, 16, 9, 16])
   assert resultat == [9, 15, 16, 16, 17]
