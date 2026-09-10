# Checklist de sortie — un module n'est "fini" que si tout est coché

À copier/valider pour chaque module (tri, structure de données, pattern, etc.)
avant de le marquer comme acquis dans `ROADMAP.md`.

## Checklist standard

- [ ] **Pseudo-code** rédigé et compris (pas recopié — reformulable de tête)
- [ ] **Code Python** fonctionnel, écrit par toi, revu en session
- [ ] **Tests unitaires réels** (pas juste un `assert` en bas de fichier) —
      cas normal, cas limite (liste vide, un seul élément, déjà trié...), cas
      invalide si pertinent
- [ ] **CI GitHub Actions** qui exécute les tests automatiquement au push
- [ ] **Complexité prouvée** (pas juste affirmée) — temps ET espace, pire/
      meilleur/moyen cas selon pertinence
- [ ] **README du module** avec le cas d'usage réel (GreenGrow/PrintFlow ou
      autre) et pourquoi cet algo est adapté à ce cas
- [ ] **Article technique court** (~500 mots, Medium/dev.to) expliquant le
      choix et le raisonnement — systématique, pas optionnel
- [ ] *(si capstone graphes ou DP)* **Déploiement minimal** avec interface
      cliquable, pas juste un script

## Modules avec exigence supplémentaire "ship it"
- Capstone Graphes (réseau de zones GreenGrow)
- Capstone Programmation Dynamique (allocation ressources GreenGrow)
