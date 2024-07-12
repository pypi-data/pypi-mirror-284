"""
Author: Prashant Verma
email: prashant27050@gmail.com
"""
import tkinter as tk
from tkinter import Menu, filedialog, messagebox, simpledialog
from tkinter import ttk
from PIL import Image, ImageTk
from graph_api import KnowledgeGraphAPI
import threading
from query_executor import QueryExecutor
from gui_navbar import Navbar
import json
from knowlegde_graphy import KnowledgeGraph
from query_parser import QueryParser
from edge_node import Node, Edge
from syntax_highlighter import SyntaxHighlighter
from modal_dialog import ModalDialog

graph = KnowledgeGraph()

class KnowledgeGraphApp:
    def __init__(self, root):
        self.api = KnowledgeGraphAPI()
        self.parser = QueryParser(graph)
        self.query_executor = QueryExecutor(self.api.graph)
        self.root = root
        self.root.title("Euler Graph Database - Knowledge Graph Viewer")

        self.header = tk.Label(root, text="Euler Graph Database", bg="lightblue", font=("Helvetica", 16), pady=10)
        self.header.pack(side=tk.TOP, fill=tk.X)

        self.footer = tk.Label(root, text="© 2024 Euler Graph Database. All rights reserved.", bg="lightblue", font=("Helvetica", 10), pady=5)
        self.footer.pack(side=tk.BOTTOM, fill=tk.X)

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
            self.display_help
        )

        self.notebook = ttk.Notebook(root)
        self.notebook.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.query_frame = tk.Frame(self.notebook)
        self.notebook.add(self.query_frame, text="Query")

        self.query_entry = tk.Text(self.query_frame, wrap=tk.WORD, width=80, height=10)
        self.query_entry.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        self.button_frame = tk.Frame(self.query_frame)
        self.button_frame.pack(pady=10)

        self.query_save_button = tk.Button(self.button_frame, text="Save Query", command=self.save_query)
        self.query_save_button.pack(side=tk.LEFT, padx=5)

        self.load_button = tk.Button(self.button_frame, text="Load Query", command=self.load_query)
        self.load_button.pack(side=tk.LEFT, padx=5)

        self.execute_query_button = tk.Button(self.button_frame, text="Execute Query", command=self.execute_query)
        self.execute_query_button.pack(side=tk.LEFT, padx=5)

        self.syntax_highlighter = SyntaxHighlighter(self.query_entry)  
        self.query_entry.bind("<KeyRelease>", self.syntax_highlighter.highlight_syntax) 

        self.bottom_frame = tk.Frame(self.query_frame)
        self.bottom_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        self.visualization_frame = tk.Frame(self.bottom_frame)
        self.visualization_frame.grid(row=0, column=0, sticky='nsew')

        self.text_output_frame = tk.Frame(self.bottom_frame)
        self.text_output_frame.grid(row=0, column=1, sticky='nsew')

        self.json_output_frame = tk.Frame(self.bottom_frame)
        self.json_output_frame.grid(row=0, column=2, sticky='nsew')

        self.bottom_frame.grid_columnconfigure(0, weight=1, uniform="bottom")
        self.bottom_frame.grid_columnconfigure(1, weight=1, uniform="bottom")
        self.bottom_frame.grid_columnconfigure(2, weight=1, uniform="bottom")
        self.bottom_frame.grid_rowconfigure(0, weight=1)

        self.canvas = tk.Canvas(self.visualization_frame, width=400, height=300)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.query_output_text = tk.Text(self.text_output_frame, wrap=tk.WORD, height=15)
        self.query_output_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.query_output_scroll = tk.Scrollbar(self.text_output_frame, command=self.query_output_text.yview)
        self.query_output_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.query_output_text.config(yscrollcommand=self.query_output_scroll.set)

        self.json_output_text = tk.Text(self.json_output_frame, wrap=tk.WORD, height=15)
        self.json_output_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.json_output_scroll = tk.Scrollbar(self.json_output_frame, command=self.json_output_text.yview)
        self.json_output_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.json_output_text.config(yscrollcommand=self.json_output_scroll.set)

    def execute_query(self):
        query = self.query_entry.get("1.0", tk.END).strip()
        if not self.api.graph:
            messagebox.showwarning("Graph not loaded", "Please load or create a graph before executing a query.")
            return
        result =  self.query_executor.execute_query(query) if query[0].lower() == "find" else self.parser.parse(query)
        
        if result:
            self.query_output_text.delete("1.0", tk.END)
            self.query_output_text.insert(tk.END, result)
            self.json_output_text.delete("1.0", tk.END)
            self.json_output_text.insert(tk.END, self.api.graph)
        else:
            messagebox.showwarning("Query Result", "No result found for the query.")

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
            self.navbar.visualize_button.config(state=tk.NORMAL)
            messagebox.showinfo("Info", "Graph loaded successfully.")

    def visualize_graph(self):
        threading.Thread(target=self.visualize_graph_thread).start()

    def visualize_graph_thread(self):
        self.navbar.visualize_button.config(state=tk.DISABLED)
        self.navbar.visualize_button.update()
        file_path = 'graph.png'
        self.api.visualize_graph(file_path)
        self.display_image(file_path)
        self.navbar.visualize_button.config(state=tk.NORMAL)

    def display_image(self, file_path):
        image = Image.open(file_path)
        image = image.resize((600, 500), resample=Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        self.canvas.image = photo
        self.canvas.create_image(0, 0, anchor=tk.NW, image=photo)
        self.canvas.bind("<Button-1>", self.on_image_click)

    def add_node(self):
        node_id = simpledialog.askstring("Input", "Enter node ID:")
        node_label = simpledialog.askstring("Input", "Enter node label:")
        if node_id and node_label:
            self.api.create_node(node_id, node_label)
            messagebox.showinfo("Info", "Node added successfully.")

    def add_edge(self):
        edge_id = simpledialog.askstring("Input", "Enter edge ID:")
        source = simpledialog.askstring("Input", "Enter source node ID:")
        target = simpledialog.askstring("Input", "Enter target node ID:")
        edge_label = simpledialog.askstring("Input", "Enter edge label:")
        if edge_id and source and target and edge_label:
            self.api.create_edge(edge_id, source, target, edge_label)
            messagebox.showinfo("Info", "Edge added successfully.")

    
    def save_graph(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
        if file_path:
            self.api.save_graph(file_path)
            messagebox.showinfo("Info", "Graph saved successfully.")

    def display_about(self):
        about_content = (
            "Euler Graph Database - Knowledge Graph Viewer\n\n"
            "Version 1.0\n\n"
            "Author: Prashant Verma \n\n"
            "Email: prashant27050@gmail.com\n\n"
            "© 2024 Euler Graph Database. All rights reserved.\n\n"
            "This application allows you to create, visualize, and manage knowledge graphs."
        )
        ModalDialog(self.root, "About", about_content)

    def display_help(self):
        help_content = (
            "User Manual\n\n"
            "1. Load Graph: Load an existing graph from a file.\n"
            "2. Visualize Graph: Display the loaded graph.\n"
            "3. Add Node: Add a new node to the graph.\n"
            "4. Add Edge: Add a new edge to the graph.\n"
            "5. Save Graph: Save the current graph to a file.\n"
            "6. Execute Query: Run a query on the graph.\n"
            "7. About: Display information about the application.\n"
            "8. Help: Display this user manual."
        )
        ModalDialog(self.root, "Help", help_content)

if __name__ == "__main__":
    root = tk.Tk()
    app = KnowledgeGraphApp(root)
    root.mainloop()


