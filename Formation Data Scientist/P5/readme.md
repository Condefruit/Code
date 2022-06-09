## Projet 05 du parcours Data Scientist (OpenClassrooms)
La présentation c'est par [ici](https://github.com/Condefruit/Code/blob/main/Formation%20Data%20Scientist/P5/POLIST_04_support_presentation.pdf)

-------------------

### Segmentation des clients d'un site e-commerce

On se place dans la peau d'un consultant pour Olist, une entreprise brésilienne qui propose une solution de vente sur les marketplaces en ligne.

La Mission : <br>
Aider les équipes d’Olist à comprendre les différents types d'utilisateurs par l'utilisation de méthodes non supervisées pour regrouper des clients de profils similaires. Ces catégories ont pour objectif d'être utilisées par l’équipe Marketing pour mieux communiquer.
 
Pour ce faire, on va <br>
:one: Analyser et traiter le jeu de données <br>
:two: Proposer une segmentation proche du métier (des catégories claires et en nombre raisonnable) <br> 
:three: Estimer une fréquence de mise à jour pour garantir la pertinance de la segmentation <br>.


--------------------------

#### K-means :

Après une première étape de nettoyage et de feature engineering [feature engineering](https://github.com/Condefruit/Code/blob/main/Formation%20Data%20Scientist/P5/POLIST_01_notebookanalyse_vfinal.ipynb) <br>
J'ai utilisé en autres, un algorithme K-means plus ou moins complexe (nombre de feature) pour déterminer des groupes actionnables (voir les 4 parties du notebook "notebookessais"). <br>
[L'opération de maintenance](https://github.com/Condefruit/Code/blob/main/Formation%20Data%20Scientist/P5/POLIST_03_notebookmaintenance_Vfinale.ipynb) est estimée en fonction des scores ARI de nos classifications en fonction de leur différente échelle de temps d'actualisation.


