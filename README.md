# Un parseur de logs pour des stats

L'objectif de l’exercice est de parser des logs de issus du serveur plan de Mappy pour en sortir des informations.
Le log est constitué d'un timestamp puis d'une url qu'a reçu un serveur de plan.
Les logs sont déjà rangés par ordre chronologique de timestamp (c'est garanti).

Une tuile de plan correspond à une url de la forme :
``/map/1.0/slab/photo/256/16/32798/22739``

Dans notre cas, "photo" correspond à ce qu'on appelle le viewmode, cela va déterminer le mode d'affichage du plan. Parmi les valeurs possibles du viewmode, on retrouve : photo, standard, standard_hd (hd = haute définition), traffic, traffic_hd, etc.

L’objectif de l'exercice de sortir le nombre de viewmodes identiques qui se suivent dans les lignes avec le nombre d’occurrences. Les urls qui ne correspondent pas à une tuile doivent être ignorées.

Ex : si en entrée on a 

````
2017-10-05 00:01:09,745 /map/1.0/slab/standard/256/19/263920/186677
2017-10-05 00:01:09,752 /map/1.0/slab/standard/256/12/2056/1387
2017-10-05 00:01:09,772 /map/1.0/slab/standard/256/14/8338/5848
2017-10-05 00:01:09,775 /map/1.0/slab/standard/256/19/263921/186678
2017-10-05 00:01:09,785 /map/1.0/slab/traffic/256/14/8338/5850
2017-10-05 00:01:09,807 /map/1.0/slab/traffic_hd/256/12/2061/1387
2017-10-05 00:01:09,839 /map/1.0/multi-descr/standard_hd/256/13/7773,6273;7773,6274;7774,6273;7774,6274;7775,6273;7775,6274;7776,6273;7776,6274;7777,6273;7777,6274;7778,6273;7778,6274
2017-10-05 00:01:09,862 /map/1.0/slab/traffic_hd/256/12/2060/1396
2017-10-05 00:01:09,878 /map/1.0/multi-descr/standard/256/14/8529,5662;8529,5663;8529,5664;8530,5662;8530,5663;8530,5664;8531,5662;8531,5663;8531,5664;8532,5662;8532,5663;8532,5664;8533,5662;8533,5663;8533,5664
2017-10-05 00:01:09,976 /map/1.0/slab/standard_hd/256/14/8620/6047
2017-10-05 00:01:10,029 /map/1.0/slab/traffic/256/14/8336/5847
2017-10-05 00:01:10,047 /map/1.0/slab/traffic/256/17/134034/90800
2017-10-05 00:01:10,055 /map/1.0/slab/standard/256/19/260681/184714
2017-10-05 00:01:10,073 /map/1.0/slab/standard/256/17/67270/47296
2017-10-05 00:01:10,076 /map/1.0/slab/public_transport_hd/256/15/33165/22527
2017-10-05 00:01:10,109 /map/1.0/slab/standard/256/18/126515/84965
2017-10-05 00:01:10,113 /map/1.0/slab/standard/256/18/134034/89724
2017-10-05 00:01:10,114 /map/1.0/slab/standard/256/19/270890/191082
2017-10-05 00:01:10,208 /map/1.0/toto
2017-10-05 00:01:10,222 /map/1.0/slab/standard/256/14/8248/6005
2017-10-05 00:01:10,224 /map/1.0/slab/standard_hd/256/18/132782/90227
````


En sortie on aura (séparé par des tabulations) :
````
standard    4
traffic 1
traffic_hd  2
standard_hd 1
traffic 2
standard    2
public_transport_hd 1
standard    3
standard    2
standard_hd 1
````

Dernier raffinement : on souhaite savoir quels étaient les niveaux de zoom (le nombre après 256) représentés pour chaque viewmode.
Une troisième colonne devra donc indiquer la liste des niveaux de zooms. Il doivent apparaître une fois seulement, séparés par des virgules et on se moque de l'ordre (tant que le niveau de zoom est unique dans la liste). Donc notre sortie finale peut ressembler à ça :

````
standard    4   19,12,14
traffic 1   14
traffic_hd  2 12 
standard_hd 1   12
traffic 2   14,17
standard    2   19,17
public_transport_hd 1   15
standard    4   18,19,14
standard_hd 1   18
````
Un fichier tornik-map-20171006.10000.tsv est fourni à des fins de tests

L’exécutable doit pouvoir prendre en entrée un fichier dans la ligne de commande, ou bien lire sur l'entrée standard (si on lui a pipé une entrée) et envoyer le résultat dans la sortie standard.

Le résultat de l'exercice sera un dépot git (idéalement sur github). Nous devons être autonomes pour valider le traitement de l'excercice.

# Une dernière chose 
souvent certains pensent que ce type d'exercice a pour but de montrer qu'on connait des fonctionnalités exotiques du langage... L'objectif est opposé : produire du code qui sera maintenable (donc lisible) par le plus grand monde dans l'équipe.

Bon code !



