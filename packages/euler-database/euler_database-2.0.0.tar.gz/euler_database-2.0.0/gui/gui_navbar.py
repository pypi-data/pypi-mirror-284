"""
Author: Prashant Verma
email: prashant27050@gmail.com
"""
import tkinter as tk
from tkinter import Menu
import customtkinter as ctk
from tkinter import font as tkfont
import os
from PIL import ImageFont

class Navbar:
    def __init__(self, parent, load_query, save_query, load_graph_func, 
                 visualize_graph_func, add_node_func, add_edge_func, 
                 save_graph_func, about_func, help_func, create_new):
        
        self.parent = parent
        self.load_graph_func = load_graph_func
        self.visualize_graph_func = visualize_graph_func
        self.save_query = save_query
        self.load_query = load_query
        self.menu_bar = Menu(parent)
        parent.config(menu=self.menu_bar)

        self.file_menu = Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", command=create_new)
        self.file_menu.add_command(label="Open")
        self.file_menu.add_command(label="Open Euler File", command=load_query)
        self.file_menu.add_command(label="Save Euler Query", command=save_query)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=parent.quit)

        self.edit_menu = Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Cut")
        self.edit_menu.add_command(label="Copy")
        self.edit_menu.add_command(label="Paste")

        self.help_menu = Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Help", menu=self.help_menu)
        self.help_menu.add_command(label="About Euler Graph", command=about_func)

        self.toolbar_frame = ctk.CTkFrame(self.parent)
        self.toolbar_frame.pack(side=tk.TOP, fill=tk.X, pady=5) 

        self.hover_label = tk.Label(self.toolbar_frame, text="", bg="#808080", fg="white", font=("Helvetica", 10))
        self.hover_label.place_forget()
        self.create_buttons()

    def event_bind(self, button_inst, hover_text):
        button_inst.bind("<Enter>", lambda e: self.show_hover_text(hover_text, button_inst))
        button_inst.bind("<Leave>", lambda e: self.hide_hover_text())

    def create_buttons(self):
        gray_color = "#f8f7f7"

        # Load Font Awesome
        fa_path = os.path.join(os.path.dirname(__file__), 'fonts', 'fa-solid-900.ttf')
        fa_font = ImageFont.truetype(fa_path, 16)

        # Register Font Awesome
        font_family = fa_font.getname()[0]
        self.fa_font = ctk.CTkFont(family=font_family, size=16)

        button_options = {
            "font": self.fa_font,
            "fg_color": gray_color,
            "width": 40,  # Adjust the width
            "height": 40,  # Adjust the height
            "text_color": "black"  # Change the icon color to black
        }

        self.open_button = ctk.CTkButton(self.toolbar_frame, text="\uf07c", command=self.load_graph_func, **button_options)
        self.open_button.pack(side=tk.LEFT, padx=2, pady=2)
        self.event_bind(self.open_button, "Load Graph")
    
        self.save_button = ctk.CTkButton(self.toolbar_frame, text="\uf0c7", **button_options)
        self.save_button.pack(side=tk.LEFT, padx=2, pady=2)
        self.event_bind(self.save_button, "Save")

        self.save_query_button = ctk.CTkButton(self.toolbar_frame, text="\uf0c5", command=self.save_query, **button_options)
        self.save_query_button.pack(side=tk.LEFT, padx=2, pady=2)
        self.event_bind(self.save_query_button, "Save Query")
       
        self.visualize_button = ctk.CTkButton(self.toolbar_frame, text="\uf06e", command=self.visualize_graph_func, **button_options)
        self.visualize_button.pack(side=tk.LEFT, padx=2, pady=2)
        self.event_bind(self.visualize_button, "Visualize")
      
        self.exit_button = ctk.CTkButton(self.toolbar_frame, text="\uf011", command=self.exit_app, **button_options)
        self.exit_button.pack(side=tk.LEFT, padx=2, pady=2)
        self.event_bind(self.exit_button, "Exit")

    def show_hover_text(self, text, button):
        self.hover_label.config(text=text)
        self.hover_label.update_idletasks()  
        button_x = button.winfo_x() + (button.winfo_width() // 2) - (self.hover_label.winfo_width() // 2)
        self.hover_label.place(x=button_x)
        self.hover_label.lift()

    def hide_hover_text(self):
        self.hover_label.place_forget()

    def new_file(self):
        print("New File action")

    def open_file(self):
        print("Open File action")

    def save_file(self):
        print("Save File action")

    def exit_app(self):
        self.parent.quit()
