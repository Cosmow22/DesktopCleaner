<h2>DesktopCleaner.py :</h2>
  <p>supprimer tous les fichiers présents sur le bureau, à l'exception de ceux autorisés par WhiteList.py</p>

<h2>WhiteList.py :</h2> 
<p>interface graphique qui permet d'ajouter (ou de supprimer) un fichier du bureau à un fichier texte dans le dossier appdata de l'ordinateur</p>

<p>Il est conseillé de placer ses deux fichiers dans le bureau (ils ne se supprimeront pas eux-même).</p>
<!--
<h2>Les limites :<h2> 
<ul>  
  <li>si DesktopCleaner ne parvient pas à supprimer un fichier (un .git notamment), le programme arrête de supprimer les fichiers restants.</li>
  <li>ne pas modifier manuellement le fichier WhiteList.txt contenu dans le dossier appdata de l' ordinateur pour éviter de supprimer un malheureux fichier du bureau</li>
  <li>je me suis rendu compte qu'il existe une fonction (shutil.rmtree) sûrement plus efficaces pour supprimer un dossier non-vide que la mienne.</li>
</ul>
-->
