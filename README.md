# Implémentation Simple d’une Blockchain en Python
Une implémentation simple d’une blockchain avec Python. Il est conçu pour aider les débutants à comprendre les concepts fondamentaux de la blockchain, tels que le hachage, la preuve de travail (Proof of Work), et la validation de la chaîne.

# Fonctionnalités
Implémentation d'une blockchain à partir de zéro en Python.
Utilisation de l’algorithme SHA-512 pour un hachage sécurisé.
Prise en charge du minage de nouveaux blocs avec preuve de travail.
Vérification de l’intégrité de la blockchain.
Illustration de la manière dont la modification d’un bloc invalide la chaîne.
Présentation du Concept
Qu’est-ce qu’une Blockchain ?
Une blockchain est un registre distribué et décentralisé qui enregistre des transactions sur plusieurs ordinateurs, de manière à ce que les enregistrements ne puissent pas être modifiés rétroactivement. Chaque bloc dans la chaîne contient :

Données : Les informations ou transactions stockées dans le bloc.
Hash : Un identifiant unique du bloc, généré grâce à la cryptographie.
Hash précédent : Le hachage du bloc précédent, qui lie les blocs entre eux.
Nonce : Un nombre utilisé pour résoudre le puzzle de preuve de travail.
Preuve de Travail
La preuve de travail (Proof of Work ou PoW) est un mécanisme de consensus garantissant la sécurité et l’immutabilité d’une blockchain. Dans cette implémentation, un bloc est considéré comme valide uniquement si son hash commence par un certain nombre de zéros, déterminé par le niveau de difficulté.

Pourquoi une Blockchain est-elle Sécurisée ?
Toute modification d’un bloc change son hash, rompant ainsi la chaîne.
Chaque bloc est cryptographiquement lié à son prédécesseur.
Cela rend extrêmement coûteux, en termes de calcul, la modification des données historiques.
Structure des Fichiers
bash
Copy code
├── blockchain.py      # Script Python contenant l'implémentation de la blockchain
├── README.md          # Documentation pour le dépôt
Comment Utiliser
1. Prérequis
Python 3.x installé sur votre système.
Un éditeur de code ou IDE (ex. : VS Code, PyCharm).
2. Cloner le Dépôt
bash
Copy code
git clone https://github.com/votreutilisateur/blockchain-simple.git
cd blockchain-simple
3. Exécuter le Script
bash
Copy code
python blockchain.py
4. Résultat
Le script minera des blocs pour une série de transactions et affichera la blockchain.
Il illustrera également comment la modification d’un bloc rend la chaîne invalide.
Explications du Code
1. Fonction de Hachage
python
Copy code
def hachage(*args):
    # Génère un hash SHA-512 pour les entrées fournies.
2. Classe Block
python
Copy code
class Block:
     Représente un bloc individuel dans la blockchain.
     Attributs : data, nonce, hash_precedent, numero.
     Méthodes : hash(), __str__().
3. Classe Blockchain
python
Copy code
class Blockchain:
     Gère la chaîne de blocs.
     Attributs : chain, difficulte, nombre_block.
     Méthodes : miner(block), isValid(), __str__().
4. Fonction Principale
python
Copy code
def main():
    # Crée une blockchain, mine de nouveaux blocs et teste l’intégrité de la chaîne.
Exemple de Sortie
yaml
Copy code
Minage du bloc...
Minage du bloc...
Minage du bloc...
Minage du bloc...

Numéro Block: 1
Hash: ...
Précédent: ...
Données: transaction1
Nonce: ...

...

La blockchain est-elle valide ? True

Modification de la blockchain...

La blockchain est-elle valide ? False
