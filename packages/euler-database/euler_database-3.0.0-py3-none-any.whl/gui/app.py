"""
Author: Prashant Verma
email: prashant27050@gmail.com
"""

import sys
import os
# # Print sys.path before modification
# print("Before modification:", sys.path)

# Modify sys.path to include the parent directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# # Print sys.path after modification
# print("After modification:", sys.path)

import tkinter as tk
from tkinter import Menu, filedialog, messagebox, simpledialog, ttk
from PIL import Image, ImageTk
import threading
import customtkinter as ctk
from euler.graph_api import KnowledgeGraphAPI
from euler.query_executor import QueryExecutor
from gui.gui_navbar import Navbar
from euler.knowlegde_graphy import KnowledgeGraph
from euler.query_parser import QueryParser
from gui.syntax_highlighter import SyntaxHighlighter
from gui.modal_dialog import ModalDialog
from docs.information import info
from gui.base64_images import logo_base64
from base64 import b64decode

graph = KnowledgeGraph()

class KnowledgeGraphApp:
    def __init__(self, root):
        self.api = KnowledgeGraphAPI()
        self.parser = QueryParser(self.api.graph)
        self.query_executor = QueryExecutor(self.api.graph)
        self.root = root
        self.root.title("Euler Graph Database - Knowledge Graph Database")

        ctk.set_appearance_mode("System")  
        ctk.set_default_color_theme("blue")

        self.navbar = Navbar(
            root,
            self.load_query,
            self.save_query,
            self.load_graph,
            self.visualize_graph,
            self.add_node,
            self.add_edge,
            self.save_graph,
            self.display_about,
            self.display_help,
            self.create_new_graph,
        )

    
        # self.euler_logo = tk.PhotoImage(file=b64decode(logo_base64.IMAGE_DATA)).subsample(5, 5)
        self.header_frame = ctk.CTkFrame(root)
        self.header_frame.pack(side=ctk.TOP, fill=ctk.X)

        # self.logo_label = ctk.CTkLabel(self.header_frame, text='EulerGraph')
        # self.logo_label.pack(side=tk.LEFT, padx=10)

        self.header_label = ctk.CTkLabel(self.header_frame, text="Euler Graph Database", font=ctk.CTkFont(size=20, weight="bold"))
        self.header_label.pack(side=ctk.LEFT, padx=10)
       
        self.dark_mode_switch = ctk.CTkSwitch(self.header_frame, text='Mode', command=self.toggle_dark_mode)
        self.dark_mode_switch.pack(side=ctk.RIGHT, padx=10)


        self.footer = ctk.CTkLabel(root, text="© 2024 Euler Graph Database. All rights reserved.", font=ctk.CTkFont(size=10))
        self.footer.pack(side=ctk.BOTTOM, fill=ctk.X, pady=5)        

        self.notebook = ttk.Notebook(root)
        self.notebook.pack(side=ctk.TOP, fill=ctk.BOTH, expand=True)

        self.query_frame = ctk.CTkFrame(self.notebook)
        self.notebook.add(self.query_frame, text="Query")

        query_font = ctk.CTkFont(family="Courier New", size=15)
        self.query_entry = ctk.CTkTextbox(self.query_frame, wrap=tk.WORD, width=80, height=5, font=query_font)
        self.query_entry.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
        # self.query_entry.insert(tk.END, "$euler: ", 'static')

        self.button_frame = ctk.CTkFrame(self.query_frame)
        self.button_frame.pack(pady=10)

        self.query_save_button = ctk.CTkButton(self.button_frame, text="Save Query", command=self.save_query)
        self.query_save_button.pack(side=ctk.LEFT, padx=5)

        self.load_button = ctk.CTkButton(self.button_frame, text="Load Query", command=self.load_query)
        self.load_button.pack(side=ctk.LEFT, padx=5)

        self.execute_query_button = ctk.CTkButton(self.button_frame, text="Execute Query", command=self.execute_query)
        self.execute_query_button.pack(side=ctk.LEFT, padx=5)

        self.syntax_highlighter = SyntaxHighlighter(self.query_entry)
        self.query_entry.bind("<KeyRelease>", self.syntax_highlighter.highlight_syntax)
        
        self.bottom_frame = ctk.CTkFrame(root)
        self.bottom_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        self.tab_view = ctk.CTkTabview(self.bottom_frame)
        self.tab_view.pack(fill=tk.BOTH, expand=True)

        self.visualization_frame = self.tab_view.add("Visualization")
        self.text_output_frame = self.tab_view.add("Output")
        self.json_output_frame = self.tab_view.add("Structure")

        self.canvas_container = ctk.CTkFrame(self.visualization_frame)
        self.canvas_container.pack(fill=tk.BOTH, expand=True)

        self.canvas = ctk.CTkCanvas(self.canvas_container, width=400, height=300, bg='white')
        self.canvas.grid(row=0, column=0, sticky="nsew")

        self.scrollbar_y = ttk.Scrollbar(self.canvas_container, orient=tk.VERTICAL, command=self.canvas.yview)
        self.scrollbar_y.grid(row=0, column=1, sticky='ns')

        self.scrollbar_x = ttk.Scrollbar(self.canvas_container, orient=tk.HORIZONTAL, command=self.canvas.xview)
        self.scrollbar_x.grid(row=1, column=0, sticky='ew')

        self.canvas.configure(yscrollcommand=self.scrollbar_y.set, xscrollcommand=self.scrollbar_x.set)
        self.canvas_container.grid_rowconfigure(0, weight=1)
        self.canvas_container.grid_columnconfigure(0, weight=1)

        self.query_output_text = ctk.CTkTextbox(self.text_output_frame, wrap=tk.WORD, height=15, border_spacing=10, activate_scrollbars=True)
        self.query_output_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.json_output_text = ctk.CTkTextbox(self.json_output_frame, wrap=tk.WORD, activate_scrollbars=True, border_spacing=10, height=15)
        self.json_output_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Move the segmented button (tabs) to the left side
        self.tab_view._segmented_button.grid(row=1, column=0, sticky="SW")

    def toggle_dark_mode(self):
        current_mode = ctk.get_appearance_mode()
        if current_mode == "Dark":
            new_mode = "Light"
        else:
            new_mode = "Dark"

        ctk.set_appearance_mode(new_mode)
        self.update_text_area_color()
        self.update_navbar_dark_mode()

    def update_text_area_color(self):
        if ctk.get_appearance_mode() == "Dark":
            pass
        else:
            pass

    def update_navbar_dark_mode(self):
        pass

    def execute_query(self):
        query = self.query_entry.get("1.0", tk.END).strip()
        if not self.api.graph:
            messagebox.showwarning("Graph not loaded", "Please load or create a graph before executing a query.")
            return
        result = self.query_executor.execute_query(query) if query[0].lower() == "find" else self.parser.parse(query)
        self.update_graph_structure()
        self.update_visualization()
        if result:
            self.query_output_text.delete("1.0", tk.END)
            self.query_output_text.insert(tk.END, result)
        else:
            messagebox.showwarning("Query Result", "No result found for the query.")

    def update_visualization(self):
        self.visualize_graph()

    def update_graph_structure(self):
        self.json_output_text.delete("1.0", tk.END)
        self.json_output_text.insert(tk.END, self.api.get_graph_json())

    def save_query(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".euler", filetypes=[("Euler files", "*.euler")])
        if file_path:
            try:
                with open(file_path, 'w') as file:
                    file.write(self.query_entry.get("1.0", tk.END).strip())
                messagebox.showinfo("Save Query", f"Queries saved successfully to {file_path}")
            except Exception as e:
                messagebox.showerror("Save Query", f"Failed to save queries: {str(e)}")

    def load_query(self):
        file_path = filedialog.askopenfilename(filetypes=[("Euler files", "*.euler")])
        if file_path:
            try:
                with open(file_path, 'r') as file:
                    content = file.read()
                self.query_entry.delete("1.0", tk.END)
                self.query_entry.insert(tk.END, content)
                messagebox.showinfo("Load Query", f"Queries loaded successfully from {file_path}")
            except Exception as e:
                messagebox.showerror("Load Query", f"Failed to load queries: {str(e)}")

    def load_graph(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.api.load_graph(file_path)
            self.navbar.visualize_button.configure(state=ctk.NORMAL)
            messagebox.showinfo("Info", "Graph loaded successfully.")
            self.update_graph_structure()
    
    def create_new_graph(self):
        global graph
        graph = KnowledgeGraph()
        messagebox.showinfo("Info", "New graph created successfully.")
        
        self.query_output_text.delete("1.0", tk.END)
        self.json_output_text.delete("1.0", tk.END)
      
        self.canvas.delete("all")
        self.update_graph_structure()
        self.update_visualization()


    def visualize_graph(self):
        threading.Thread(target=self.visualize_graph_thread).start()

    def visualize_graph_thread(self):
        self.navbar.visualize_button.configure(state=ctk.DISABLED)
        self.navbar.visualize_button.update()
        file_path = 'graph.png'
        self.api.visualize_graph(file_path)
        self.display_image(file_path)
        self.navbar.visualize_button.configure(state=ctk.NORMAL)

    def display_image(self, file_path):
        image = Image.open(file_path)
        self.canvas.image = ImageTk.PhotoImage(image)

        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        img_width, img_height = image.size
        x_center = (canvas_width - img_width) // 2
        y_center = (canvas_height - img_height) // 2

        self.canvas.create_image(max(0, x_center), max(0, y_center), anchor=tk.NW, image=self.canvas.image)
        self.canvas.configure(scrollregion=self.canvas.bbox(tk.ALL))

    def add_node(self):
        node_id = simpledialog.askstring("Input", "Enter node ID:")
        node_label = simpledialog.askstring("Input", "Enter node label:")
        if node_id and node_label:
            self.api.create_node(node_id, node_label)
            messagebox.showinfo("Info", "Node added successfully.")
            self.update_graph_structure()

    def add_edge(self):
        edge_id = simpledialog.askstring("Input", "Enter edge ID:")
        source = simpledialog.askstring("Input", "Enter source node ID:")
        target = simpledialog.askstring("Input", "Enter target node ID:")
        edge_label = simpledialog.askstring("Input", "Enter edge label:")
        if edge_id and source and target and edge_label:
            self.api.create_edge(edge_id, source, target, edge_label)
            messagebox.showinfo("Info", "Edge added successfully.")
            self.update_graph_structure()

    def save_graph(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
        if file_path:
            self.api.save_graph(file_path)
            messagebox.showinfo("Info", "Graph saved successfully.")

    def display_about(self):
        ModalDialog(self.root, "About", info.about_content)

    def display_help(self):
        ModalDialog(self.root, "Help", info.help_content)


def main():
    root = ctk.CTk()
    app = KnowledgeGraphApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
