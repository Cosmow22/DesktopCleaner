# Presentation
## DesktopCleaner.py :
  supprimer tous les fichiers présents sur le bureau, à l'exception de ceux autorisés par WhiteList.py

## WhiteList.py : 
interface graphique qui permet d'ajouter (ou d'enlever) le nom d' un fichier du bureau à un fichier texte dans le dossier appdata de l'ordinateur appelé WhiteList.txt (le programme le crée)

Il est conseillé de placer ses deux programmes dans le bureau, c'est plus pratique (ils ne se supprimeront pas eux-mêmes).

# Le dossier appdata
Pour y accéder et voir le fichier WhiteList.txt, il faut se rendre à cette adresse :
`C:\Users\Utilisateur\AppData\Roaming`
Pour ce faire, vous pouvez :
- rentrer cette commande dans l'invite de commande : `cd %appdata%`
- taper `%appdata%` dans l'application *Executer* de windows ou bien dans la barre d'adresse de l'explorateur de fichiers.
# Attention !
- si DesktopCleaner ne parvient pas à supprimer un fichier (un .git notamment), le programme arrête de supprimer les fichiers restants.
- ne pas modifier manuellement le fichier WhiteList.txt contenu dans le dossier appdata de l' ordinateur pour éviter de supprimer un malheureux fichier du bureau un fois DesktopCleaner lancé

