import os
from PIL import Image
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

def main():
    root = tk.Tk()
    
    root.withdraw()
    # folder_name = filedialog.askdirectory(parent=root)
    folder_name = filedialog.askdirectory(initialdir='../../')
    root.deiconify()

    photos = []
    # folder_name = filedialog.Open(root, filetypes = [('*.txt files', '.txt')]).show()

    check = True
    for root_folder, dirs, files in os.walk(folder_name):
        for file in files:
            check = False
            image = Image.open(folder_name + '/' + file)
            if not image.verify:
                continue
            photos.append((file, ('x').join(map(str, image.size)), image.info.get('dpi'), image.mode, image.info.get('compression')))
    if check:
        print('\nThere are no any files in the folder "' + folder_name + '", try other folder...')
        root.destroy()
        return


    root.title("Image data viewer")
    root.geometry("1080x640+240+240") 

    columns = ("file", "size", "dpi", "color_depth", "compression")
    
    tree = ttk.Treeview(columns=columns, show="headings")
    tree.pack(fill=tk.BOTH, expand=1)
    
    tree.heading("file", text="File:")
    tree.heading("size", text="Size(in px):")
    tree.heading("dpi", text="DPI:")
    tree.heading("color_depth", text="Color depth:")
    tree.heading("compression", text="Compression:")
    
    for image in photos:
        tree.insert("", tk.END, values=image)
    
    root.mainloop()


if __name__ == '__main__':
    main()

# pyinstaller --noconfirm --onedir --console  "/home/globus/Programming/FAMCS/Computer Graphics/main.py"