import os, subprocess

def DeleteFolder(Folder):
    try:
        os.chdir(Folder)
        elements = os.listdir() 
        
        for element in elements:
            if os.path.isfile(element):
                os.remove(element)
            else:
                DeleteFolder(element) #si element n'est pas un fichier, c'est un dossier

        os.chdir('..')  # Revenir au répertoire parent
        os.rmdir(Folder)  # Supprimer le répertoire lui-même
    except OSError as error:
        print(f"Erreur lors de la suppression de {Folder}: {error}")

desktop_path = subprocess.run("echo %USERPROFILE%\Desktop", shell=True, capture_output=True, text=True)
os.chdir(desktop_path.stdout[:-1]) #on se place dans le bureau en retirant le \n qui est ajouté par echo

"""elements = os.listdir()
elements.remove("DesktopCleaner.exe")
for element in elements: 
    if os.path.isfile(element):
        os.remove(element)
    else:
        DeleteFolder(element)"""