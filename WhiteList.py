import tkinter as tk
import subprocess
import os
from tkinter import ttk
from DesktopCleaner import elements
from math import ceil

APP_DATA_PATH = (subprocess.run("echo %APPDATA%", shell = True, text = True, capture_output = True).stdout)[:-1]

class App(tk.Tk):
    def __init__(self, elements):
        super().__init__()
        self.elements = elements
        WhiteList(self)        
            
    def display_elements(self):
        check_frame = ttk.Frame(self)
        check_frame.columnconfigure((0,1,2), weight = 1)
        check_frame.rowconfigure(tuple(range(ceil(len(elements) / 3))), weight = 1)
        row, column = 0, 0
        for element in self.elements:
            if (elements.index(element)+1) % 3 == 0:
                CheckButton(check_frame, element, row, column)
                column = 0
                row += 1
            else:
                CheckButton(check_frame, element, row, column)                
                column += 1
        check_frame.pack()

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
        else: 
            self.widgets_for_no_whitelist()
            
    def widgets_for_an_existing_whitelist(self):
        ttk.Label(self.file_frame, text = "Vous êtes connecté à la white list.").grid(row = 0, column = 0, sticky='ns', padx = (10, 0))
        open_file_btn = ttk.Button(self.file_frame, text = "Ouvrir WhiteList.txt", command = lambda: subprocess.run(f"notepad {APP_DATA_PATH}\WhiteList.txt", shell = True))
        open_file_btn.grid(row = 0, column = 1, sticky='ns', padx = 10)
        self.file_frame.pack(fill = 'both', pady = 10)
        App.display_elements(self.parent)    
    
    def widgets_for_no_whitelist(self):
            ttk.Label(self.file_frame, text = "Vous n'êtes pas connecté à la white list.").grid(row = 0, column = 0, sticky='ns', padx = (10, 0))
            create_file_btn = ttk.Button(self.file_frame, text = "Créer WhiteList.txt", command = self.create_file)
            create_file_btn.grid(row = 0, column = 1, sticky='ns', padx = 10)
            self.file_frame.pack(fill = 'both', pady = 10)
    
    def create_file(self):
        subprocess.run(f"%SystemRoot%\system32\WindowsPowerShell\v1.0\powershell.exe echo> {APP_DATA_PATH}\WhiteList.txt", shell = True)
        self.file_frame.pack_forget()
        self.widgets_for_an_existing_whitelist()
    
    def existing_file_names() ->list:
        with open(f"{APP_DATA_PATH}\WhiteList.txt", 'r', encoding = 'UTF-8') as file:    
            return [line.strip() for line in file]
    
    def write(element):
        print("writing...", element)
        with open(f"{APP_DATA_PATH}\WhiteList.txt", 'a', encoding = 'UTF-8') as file:    
            file.write(f'{element}\n')
    
    def unwrite(element):
        print("unwriting...", element)
        with open(f"{APP_DATA_PATH}\WhiteList.txt", 'r', encoding = 'UTF-8') as file:
            lines = file.readlines()
        with open(f"{APP_DATA_PATH}\WhiteList.txt", 'w', encoding = 'UTF-8') as file:    
            for line in lines:
                if line.strip() != element:
                    file.write(f'{line}')
    
      
class CheckButton(ttk.Checkbutton):
    global white_list
    white_list = WhiteList.existing_file_names()
    def __init__(self, parent, element, row, column):
        super().__init__(parent)    
        self.row = row
        self.column = column
        self.element = element
        self.state = tk.BooleanVar(value = self.state())
        self.check = ttk.Checkbutton(
                                master = parent,
                                text = self.element,
                                variable = self.state,
                                onvalue = True,
                                offvalue = False,
                                command = lambda: WhiteList.write(self.element) if self.state.get() == True else WhiteList.unwrite(self.element)
                            )
        self.check.grid(row = self.row, column = self.column, sticky = 'w')
    
    def state(self):
        if self.element in white_list: 
            return True
        return False
        
if __name__ == '__main__':
    app = App(elements)
    app.mainloop()