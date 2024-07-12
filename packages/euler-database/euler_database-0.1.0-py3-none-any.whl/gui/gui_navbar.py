"""
Author: Prashant Verma
email: prashant27050@gmail.com
"""
import tkinter as tk
from tkinter import Menu
import customtkinter as ctk
from typing import Optional, Any, Callable

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
        # self.file_menu.add_command(label="Delete Graph")s
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

        # Toolbar buttons with icons
        self.create_icons()

        # self.update_dark_mode()


    def event_bind(self, button_inst, hover_text):
        button_inst.bind("<Enter>", lambda e: self.show_hover_text(hover_text, button_inst))
        button_inst.bind("<Leave>", lambda e: self.hide_hover_text())
    
    def create_icons(self):
        icon_path = "C:\\Users\\DS203\\Desktop\\euler_graph_database\\icons\\"
        self.open_icon = tk.PhotoImage(file= f"{icon_path}open.png").subsample(2, 2)
        self.save_icon = tk.PhotoImage(file=f"{icon_path}save.png").subsample(2, 2)
        self.save_query_icon = tk.PhotoImage(file=f"{icon_path}save_query.png").subsample(2, 2)
        self.visual_icon = tk.PhotoImage(file=f"{icon_path}visual.png").subsample(2, 2)
        self.exit_icon = tk.PhotoImage(file=f"{icon_path}exit.png").subsample(2, 2)

        icon_size = self.open_icon.width() 

        gray_color = "#f8f7f7" #"#808080"

        self.open_button = ctk.CTkButton(self.toolbar_frame, image=self.open_icon, text="", command=self.load_graph_func, width=icon_size, height=icon_size, fg_color=gray_color)
        self.open_button.pack(side=tk.LEFT, padx=2, pady=2)
        self.event_bind(self.open_button, "Load Graph")
    
        self.save_button = ctk.CTkButton(self.toolbar_frame, image=self.save_icon, text="", width=icon_size, height=icon_size, fg_color=gray_color)
        self.save_button.pack(side=tk.LEFT, padx=2, pady=2)
        self.event_bind(self.save_button, "Save")

        self.save_query_button = ctk.CTkButton(self.toolbar_frame, image=self.save_query_icon, text="", width=icon_size, height=icon_size, fg_color=gray_color)
        self.save_query_button.pack(side=tk.LEFT, padx=2, pady=2)
        self.event_bind(self.save_query_button, "Save Query")
       
        self.visualize_button = ctk.CTkButton(self.toolbar_frame, image=self.visual_icon, text="", command=self.visualize_graph_func, width=icon_size, height=icon_size, fg_color=gray_color)
        self.visualize_button.pack(side=tk.LEFT, padx=2, pady=2)
        self.event_bind(self.visualize_button, "Visualization")
      
        self.exit_button = ctk.CTkButton(self.toolbar_frame, image=self.exit_icon, text="",command=self.exit_app, width=icon_size, height=icon_size, fg_color=gray_color)
        self.exit_button.pack(side=tk.LEFT, padx=2, pady=2)
        self.event_bind(self.exit_button, "Exit")
      

    def show_hover_text(self, text, button):
        self.hover_label.config(text=text)
        self.hover_label.update_idletasks()  
        button_x = button.winfo_x() + (button.winfo_width() // 2) - (self.hover_label.winfo_width() // 2)
        self.hover_label.place(x=button_x)
        self.hover_label.lift()

    def hide_hover_text(self):
        self.hover_label.pack_forget()

    def new_file(self):
        print("New File action")

    def open_file(self):
        print("Open File action")

    def save_file(self):
        print("Save File action")

    def exit_app(self):
        self.parent.quit()
