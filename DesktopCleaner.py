import os
from subprocess import run


def DeleteFolder(Folder) -> None:
    try:
        os.chdir(Folder)
        elements = os.listdir()

        for element in elements:
            if os.path.isfile(element):
                os.remove(element)
            else:
                DeleteFolder(element)

        os.chdir("..")  # Revenir au répertoire parent
        os.rmdir(Folder)  # Supprimer le répertoire lui-même

    except OSError as error:
        print(f"Erreur lors de la suppression de {Folder}: {error}")


desktop_path = run(
    "echo %USERPROFILE%\Desktop", shell=True, capture_output=True, text=True
)
os.chdir(
    desktop_path.stdout[:-1]
)  # on se place dans le bureau en retirant le \n qui est ajouté par echo
elements = [element for element in os.listdir()]

if __name__ == "__main__":
    from WhiteList import white_list

    elements = [
        element
        for element in elements
        if element not in white_list
        and os.path.splitext(element)[0] not in ("DesktopCleaner", "WhiteList")
    ]
    for element in elements:
        if os.path.isfile(element):
            os.remove(element)
        else:
            DeleteFolder(element)  # si element n'est pas un fichier, c'est un dossier
