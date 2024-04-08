import os 
import subprocess

def DeleteFolder(Folder):
    try:
        os.chdir(Folder)
        print(os.getcwd(), "l7")
        elements = os.listdir() 
        
        for element in elements:
            if os.path.isfile(element):
                os.remove(element)
            else:
                DeleteFolder(element) 

        print(os.getcwd(), "l16")
        os.chdir(os.path.dirname(os.getcwd()))  # Revenir au répertoire parent
        print(os.getcwd(), "l18")
        os.rmdir(Folder)  # Supprimer le répertoire lui-même
    
    except OSError as error:
        print(f"Erreur lors de la suppression de {Folder}: {error}")

desktop_path = subprocess.run("echo %USERPROFILE%\Desktop", shell=True, capture_output=True, text=True)
os.chdir(desktop_path.stdout[:-1]) # on se place dans le bureau en retirant le \n qui est ajouté par echo
elements = os.listdir()
if __name__ == '__main__':
    elements.remove("DesktopCleaner.exe") # sinon le programme cherchera à se supprimer lui-même
    for element in elements: 
        print(element)
        if os.path.isfile(element):
            os.remove(element)
        else:
            DeleteFolder(element) #si element n'est pas un fichier, c'est un dossier