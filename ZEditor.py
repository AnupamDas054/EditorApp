import tkinter as tk
from tkinter import ttk
from tkinter import  filedialog , font , messagebox , colorchooser
import  os

main_apps = tk.Tk()
main_apps.geometry('1200x800')
main_apps.title('ZEditor')
################# main_menu function ####################

main_menu=tk.Menu()
#File Functionality
file=tk.Menu(main_menu,tearoff=False)
file.add_command(label='New',compound=tk.RIGHT,accelerator='cntrl+N')
file.add_command(label='Open',compound=tk.RIGHT,accelerator='cntrl+O')
file.add_command(label='Save',compound=tk.RIGHT,accelerator='cntrl+S')
file.add_command(label='Save as',compound=tk.RIGHT,accelerator='cntrl+Alt+S')
file.add_command(label='Exit',compound=tk.RIGHT,accelerator='cntrl+Q')






view=tk.Menu(main_menu,tearoff=False)
colorpalate=tk.Menu(main_menu,tearoff=False)
edit=tk.Menu(main_menu,tearoff=False)

main_menu.add_cascade(label='File',menu=file)
main_menu.add_cascade(label='Edit',menu=edit)
main_menu.add_cascade(label='View',menu=view)
main_menu.add_cascade(label='Color Theme',menu=colorpalate)


main_apps.config(menu=main_menu)
main_apps.mainloop()
