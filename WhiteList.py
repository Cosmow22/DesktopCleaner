import os
import tkinter
from tkinter import ttk
from math import ceil 
from subprocess import run
from DesktopCleaner import elements, DESKTOP_PATH

APP_DATA_PATH = (run("echo %APPDATA%", shell = True, text = True, capture_output = True).stdout)[:-1]


def is_script_name(element: str) -> None:
    if os.path.splitext(element)[0] in ('DesktopCleaner', 'WhiteList'): 
        return True
    else: 
        return False

def open_element(element: str) -> None:
    if "." in element:
        run(f"{element}", shell=True, text=True)
    else:
        run(f"explorer {element}", shell=True, text=True)

class App(tkinter.Tk):
    def __init__(self, elements, connected, white_list):
        super().__init__()
        self.elements = elements
        WhiteList(self)
        (ttk.Label(self, text="Cocher : ajout du fichier à la liste d'exclusion de suppression\nDouble clic droit : ouvrir le fichier/dossier et voir ce qu'il y a dedans.")
        ).pack(ipadx=10, padx=10)
        if connected:
            self.white_list = white_list
            self.display_elements()        
            
    def display_elements(self):
        elements_copy = self.elements.copy()
        list_length_elements = list(map(len, elements_copy))
        median = ceil(len(list_length_elements) / 2)
        max_char_for_element = list_length_elements[median]
        n_column = len(elements_copy) // 5
        
        check_frame = ttk.Frame(self)
        check_frame.pack(expand = True, fill = 'both', padx = 10, pady = 5)
        check_frame.columnconfigure((0,1,2), weight = 1, uniform="a")
        check_frame.rowconfigure(tuple(range(3)), weight = 1)
        row, column = 0, 0
        for element in self.elements: 
            if is_script_name(element):
                self.elements.remove(element)
                self.elements.append(element)
        for element in self.elements:
            #print(f'element : {element}; row : {row}; column : {column}; n_element : {self.elements.index(element) + 1}')  
            if (self.elements.index(element)+1) % n_column == 0:
                CheckButton(check_frame, element, row, column, self.white_list, max_char_for_element)
                column = 0
                row += 1
            else:
                CheckButton(check_frame, element, row, column, self.white_list, max_char_for_element)                
                column += 1


class WhiteList(ttk.Frame):  
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.file_frame = ttk.Frame(master = parent)
        self.file_frame.columnconfigure(0, weight = 3)
        self.file_frame.columnconfigure(1, weight = 1)
        self.file_frame.rowconfigure(0, weight = 1)
        os.chdir(APP_DATA_PATH)
        if "WhiteList.txt" in os.listdir():
            self.widgets_for_an_existing_whitelist()
            os.chdir(DESKTOP_PATH)
        else: 
            self.widgets_for_no_whitelist()
            
    def widgets_for_an_existing_whitelist(self):
        ttk.Label(self.file_frame, text = "Vous êtes connecté à la white list.").grid(row = 0, column = 0, sticky='ns', padx = (10, 0))
        open_file_btn = ttk.Button(self.file_frame, text = "Ouvrir WhiteList.txt", command = lambda: run(f"notepad {APP_DATA_PATH}\WhiteList.txt", shell = True))
        open_file_btn.grid(row = 0, column = 1, sticky='ns', padx = 10)
        self.file_frame.pack(fill = 'both', pady = 10)

    def widgets_for_no_whitelist(self):
            ttk.Label(self.file_frame, text = "Vous n'êtes pas connecté à la white list.").grid(row = 0, column = 0, sticky='ns', padx = (10, 0))
            create_file_btn = ttk.Button(self.file_frame, text = "Créer WhiteList.txt", command = self.create_file)
            create_file_btn.grid(row = 0, column = 1, sticky='ns', padx = 10)
            self.file_frame.pack(fill = 'both', pady = 10)
    
    def create_file(self):
        run(f"%SystemRoot%\system32\WindowsPowerShell\v1.0\powershell.exe echo> {APP_DATA_PATH}\WhiteList.txt", shell = True)
        for widget in self.file_frame.winfo_children(): widget.destroy()
        self.widgets_for_an_existing_whitelist()
        app.white_list = WhiteList.existing_file_names()
        App.display_elements(app) 
    
    def existing_file_names() ->list:
        with open(f"{APP_DATA_PATH}\WhiteList.txt", 'r', encoding = 'UTF-8') as file:    
            return [line.strip() for line in file]
    
    def write(element):
        with open(f"{APP_DATA_PATH}\WhiteList.txt", 'a', encoding = 'UTF-8') as file:    
            file.write(f'{element}\n')
    
    def unwrite(element):
        with open(f"{APP_DATA_PATH}\WhiteList.txt", 'r', encoding = 'UTF-8') as file:
            lines = file.readlines()
        with open(f"{APP_DATA_PATH}\WhiteList.txt", 'w', encoding = 'UTF-8') as file:    
            for line in lines:
                if line.strip() != element:
                    file.write(f'{line}')
    
      
class CheckButton(ttk.Checkbutton):
    def __init__(self, parent, element, row, column, white_list, max_char):
        super().__init__(parent)    
        self.white_list = white_list
        self.row = row
        self.column = column
        self.element = element
        self.state = tkinter.BooleanVar(value = self.state())
        #print(f'{element} → {element[:max_char]} (len : {len(element)})')
        self.check = ttk.Checkbutton(
                                master = parent,
                                text = self.element[:max_char],
                                variable = self.state,
                                onvalue = True,
                                offvalue = False,
                                state = ('disabled' 
                                    if is_script_name(element)
                                    else 'normal'
                                    ),  
                                command = lambda: WhiteList.write(self.element) if self.state.get() == True else WhiteList.unwrite(self.element)
                            )
        self.check.grid(row = self.row, column = self.column, sticky = 'w')
        self.check.bind("<Double-Button-3>", lambda event: open_element(self.element))
        self.check.bind("<Enter>", lambda event: print(event))
    
    def state(self):
        if self.element in self.white_list: 
            return True
        return False


if os.path.isfile(f'{APP_DATA_PATH}\WhiteList.txt'):
    connected = True
    white_list = WhiteList.existing_file_names()
else: 
    connected = False
    white_list = 'not linked'
        
if __name__ == '__main__':
    app = App(elements, connected, white_list)
    app.mainloop()