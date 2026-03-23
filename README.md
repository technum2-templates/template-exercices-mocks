# Exercices - Mock objects

## Exercice 1 - Rapport de notes

**Niveau :** Facile
**Temps estimé :** 15 minutes
**Concepts :** `MagicMock`, `return_value`, injection par le constructeur

### 1.1 Objectif

Écrire des tests unitaires pour `RapportScolaire` sans se connecter à une vraie base de
données. La classe `BaseDeNotes` est remplacée par un mock.

### 1.2 Instructions

1. Ouvrez `test_rapport_scolaire.py`
2. Créez un `MagicMock()` qui remplace `BaseDeNotes`
3. Configurez le mock pour que `obtenir_notes` retourne une liste de notes
4. Passez le mock au constructeur de `RapportScolaire`
5. Lancez les tests : `python -m unittest test_rapport_scolaire.py`

### 1.3 Critères de réussite

- [ ] Le mock est injecté via le constructeur de `RapportScolaire`
- [ ] `return_value` est utilisé pour configurer les notes retournées
- [ ] La moyenne est testée avec les notes `[12, 14, 16]` (résultat attendu : `14.0`)
- [ ] Un étudiant avec `[12, 14, 16]` a réussi
- [ ] Un étudiant avec `[4, 6, 8]` n'a pas réussi
- [ ] Tous les tests passent

### 1.4 Indices

- `MagicMock()` s'importe depuis `unittest.mock`
- Pour configurer la valeur retournée par une méthode du mock :
  `mon_mock.nom_de_methode.return_value = ...`

---

## Exercice 2 - Convertisseur de devises

**Niveau :** Moyen
**Temps estimé :** 15 minutes
**Concepts :** `MagicMock`, `return_value`, injection par argument de méthode

### 2.1 Objectif

Écrire des tests unitaires pour `Convertisseur` sans appeler une vraie API de taux de
change. Le service de taux est passé en argument de la méthode `convertir`.

### 2.2 Instructions

1. Ouvrez `test_convertisseur.py`
2. Créez un `MagicMock()` qui remplace `ServiceTauxDeChange`
3. Configurez le mock pour que `obtenir_taux` retourne le taux souhaité
4. Passez le mock comme argument `service_taux` de la méthode `convertir`
5. Lancez les tests : `python -m unittest test_convertisseur.py`

### 2.3 Critères de réussite

- [ ] Le mock est passé en argument de la méthode (pas du constructeur)
- [ ] 100 EUR en USD avec un taux de 1.08 donne `108.0`
- [ ] 100 EUR en GBP avec un taux de 0.86 donne `86.0`
- [ ] 250 JPY en EUR avec un taux de 0.0062 donne `1.55`
- [ ] Tous les tests passent

### 2.4 Indices

- La différence avec l'exercice 1 : le mock n'est pas passé au constructeur mais
  directement à la méthode `convertir`
- Chaque test peut configurer un taux différent

---

## Exercice 3 - Générateur de mot de passe

**Niveau :** Difficile
**Temps estimé :** 20 minutes
**Concepts :** `@patch`, mock d'une dépendance importée

### 3.1 Objectif

Écrire des tests unitaires pour `generer_mot_de_passe` en controlant le résultat de
`random.choices` grace à `@patch`. Tester aussi `est_mot_de_passe_fort` directement,
sans mock.

### 3.2 Instructions

1. Ouvrez `test_mot_de_passe.py`
2. Pour `generer_mot_de_passe` : utilisez `@patch("mot_de_passe.random.choices")` pour
   contrôler ce que `random.choices` retourne
3. Pour `est_mot_de_passe_fort` : testez directement, sans mock (cette fonction n'a pas
   de dépendance externe)
4. Lancez les tests : `python -m unittest test_mot_de_passe.py`

### 3.3 Critères de réussite

- [ ] `@patch` est utilisé pour remplacer `random.choices`
- [ ] Le mot de passe généré correspond aux caractères retournés par le mock
- [ ] Un mot de passe avec majuscule, minuscule et chiffre (>= 8 caractères) est fort
- [ ] Un mot de passe trop court n'est pas fort
- [ ] `est_mot_de_passe_fort` est testé sans mock
- [ ] Tous les tests passent

### 3.4 Indices

- `@patch("mot_de_passe.random.choices")` remplace `random.choices` dans le module
  `mot_de_passe`, pas globalement
- Le mock est passé automatiquement en paramètre de la méthode de test
- On ne mock que ce qu'on ne veut pas tester : `est_mot_de_passe_fort` n'a pas besoin
  de mock car elle ne dépend de rien d'externe
