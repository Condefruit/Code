## Projet 06 du parcours Data Scientist (OpenClassrooms)
La présentation c'est par [ici](https://github.com/Condefruit/Code/blob/main/Formation%20Data%20Scientist/P6/P6_03_presentation.pdf)

-------------------

### Classification automatiqueme de biens de consommation

Data Scientist au sein de la société "Place de marché”, qui souhaite lancer une marketplace e-commerce. <br>
L'attribution de la catégorie d'un article est effectuée manuellement par les vendeurs. Pour travailler avec de plus gros volume et faciliter l’expérience utilisateurs/vendeurs, on cherche à réaliser cette tache de manière automatique. <br>
L'objectif est donc Etudier la faisabilité d'un moteur de classification <br>

 
Pour ce faire, on va <br>
:one: Analyser le jeu de données en réaliser un prétraitement <br>
:two: Extraire les features texte de la description des produits <br> 
:three: Extraire les features visuelles des images des produits <br>.


--------------------------

#### Non supervisée :

J'ai d'abord choisi de réaliser une première version [non supervisée](https://github.com/Condefruit/Code/blob/main/Formation%20Data%20Scientist/P6/P6_01_Non_supervis%C3%A9_finale.ipynb) (sans l'utilisation des étiquettes). <br>
Pour le texte : Retrait ponctuation / Tokenization / Lemmatization / Retrait des stop words + méthode de réduction de dimension (PCA/t-SNE) + K-Means <br>
Pour les images : Pré-traitement (Echelle de gris / redimensionnement / histogramme / filtre) + Sift  + méthode de réduction de dimension (PCA/t-SNE) + K-Means <br>

--------------------------

#### Semi-supervisée :

Dans un deuxième temps, j'ai utilisé une méthode ["semi-supervisée"](https://github.com/Condefruit/Code/blob/main/Formation%20Data%20Scientist/P6/P6_02_Semi_Supervis%C3%A9_finale_p1.ipynb). <br>
Les traitements sont les même avec le rajout d'un transfert learning (CNN) pour la partie images.


