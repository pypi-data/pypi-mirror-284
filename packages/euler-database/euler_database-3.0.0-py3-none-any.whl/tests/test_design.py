# import tkinter as tk
# import customtkinter as ctk
# from tkinter import filedialog
# from plotly.subplots import make_subplots
# import plotly.graph_objects as go
# import io
# from PIL import Image, ImageTk

# class KnowledgeGraphApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Knowledge Graph Viewer")
#         ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
#         ctk.set_default_color_theme("blue")

#         self.header = ctk.CTkFrame(root)
#         self.header.pack(side=tk.TOP, fill=tk.X, pady=5)

#         self.header_label = ctk.CTkLabel(self.header, text="Knowledge Graph Viewer", font=ctk.CTkFont(size=20, weight="bold"))
#         self.header_label.pack(side=tk.TOP, pady=5)

#         self.button_frame = ctk.CTkFrame(self.header)
#         self.button_frame.pack(side=tk.TOP, pady=5)

#         self.create_plot_button = ctk.CTkButton(self.button_frame, text="Create Graph", command=self.create_plot)
#         self.create_plot_button.pack(side=tk.LEFT, padx=10)

#         self.load_graph_button = ctk.CTkButton(self.button_frame, text="Load Graph", command=self.load_graph)
#         self.load_graph_button.pack(side=tk.LEFT, padx=10)

#         self.plot_frame = ctk.CTkFrame(root)
#         self.plot_frame.pack(fill=tk.BOTH, expand=True)

#     def create_plot(self):
#         fig = make_subplots(rows=1, cols=1)
#         fig.add_trace(go.Scatter(x=[1, 2, 3], y=[10, 11, 12], mode='lines', name='lines'))

#         fig.update_layout(title="Interactive Graph")
#         self.display_plot(fig)

#     def display_plot(self, fig):
#         # Save the plot to an image file
#         img_bytes = fig.to_image(format="png")
#         img = Image.open(io.BytesIO(img_bytes))

#         # Display the image in the Tkinter canvas
#         self.plot_image = ImageTk.PhotoImage(img)
#         canvas = tk.Canvas(self.plot_frame, width=img.width, height=img.height)
#         canvas.create_image(0, 0, anchor=tk.NW, image=self.plot_image)
#         canvas.pack(expand=True, fill=tk.BOTH)

#     def load_graph(self):
#         file_path = filedialog.askopenfilename(filetypes=[("HTML files", "*.html")])
#         if file_path:
#             with open(file_path, 'r') as f:
#                 plot_html = f.read()
#             self.display_html_plot(plot_html)

#     def display_html_plot(self, plot_html):
#         # Convert HTML to an image and display it
#         fig = go.Figure()
#         fig.write_html("temp_plot.html", full_html=False)

#         # Load HTML file and display in Tkinter (assuming HTML is converted to image)
#         with open("temp_plot.html", "r") as file:
#             html_content = file.read()
#         fig = go.Figure()
#         fig.add_trace(go.Scatter(x=[1, 2, 3], y=[10, 11, 12], mode='lines', name='lines'))
#         self.display_plot(fig)

# if __name__ == "__main__":
#     root = ctk.CTk()
#     app = KnowledgeGraphApp(root)
#     root.mainloop()


# import tkinter as tk
# from tkinterweb import HtmlFrame
# import threading
# import random
# import plotly.graph_objs as go
# import dash
# from dash import dcc, html
# from dash.dependencies import Output, Input

# class DashThread(threading.Thread):
#     def __init__(self, data_list):
#         threading.Thread.__init__(self)
#         self.data_list = data_list

#         self.app = dash.Dash(__name__)

#         # Initialize an empty graph
#         self.app.layout = html.Div(
#             [
#                 dcc.Graph(id="live-graph", animate=True),
#                 dcc.Interval(
#                     id="graph-update",
#                     interval=1 * 1000,
#                 ),
#             ]
#         )

#         @self.app.callback(
#             Output("live-graph", "figure"), [Input("graph-update", "n_intervals")]
#         )
#         def update_graph(n):
#             data = [
#                 go.Scatter(
#                     x=list(range(len(self.data_list[symbol]))),
#                     y=self.data_list[symbol],
#                     mode="lines+markers",
#                     name=symbol,
#                 )
#                 for symbol in self.data_list.keys()
#             ]
#             fig = go.Figure(data=data)

#             # Update x-axis range to show last 120 data points
#             max_len = max([len(self.data_list[symbol]) for symbol in self.data_list.keys()])
#             fig.update_xaxes(range=[max(0, max_len - 120), max_len])

#             return fig

#     def run(self):
#         self.app.run_server(debug=False, use_reloader=False)

# class App:
#     def __init__(self, root):
#         self.root = root
#         self.data_list = {"ETHUSDT": [], "BTCUSD": [], "BNBUSDT": []}

#         # Start the Dash application in a separate thread
#         self.dash_thread = DashThread(self.data_list)
#         self.dash_thread.start()

#         # Create a HtmlFrame to embed Dash app
#         self.webview = HtmlFrame(root)
#         self.webview.pack(fill=tk.BOTH, expand=tk.YES)
#         self.webview.load_website("http://localhost:8050")

#         # Start the price generation in tkinter after Dash app is launched
#         self.root.after(1000, self.generate_prices)

#     def generate_prices(self):
#         for symbol in self.data_list.keys():
#             new_price = random.randint(1, 100)  # Generate random price
#             self.data_list[symbol].append(new_price)  # Store the price in list

#         # Schedule the function to run again after 1 second
#         self.root.after(1000, self.generate_prices)

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = App(root)
#     root.mainloop()


import tkinter as tk
import customtkinter as ctk
from tkinter import filedialog
import matplotlib.pyplot as plt
import networkx as nx
from PIL import Image, ImageTk

class KnowledgeGraphApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Knowledge Graph Viewer")
        ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
        ctk.set_default_color_theme("blue")

        self.toolbar_frame = ctk.CTkFrame(root)
        self.toolbar_frame.pack(side=tk.TOP, fill=tk.X, pady=5)  # Added padding here

        # # Space for the hover label below the toolbar
        # self.hover_label_frame = ctk.CTkFrame(root, height=20)  # Adjust height as needed
        # self.hover_label_frame.pack(side=tk.TOP, fill=tk.X)

        # # Text label for displaying hover text
        # self.hover_label = tk.Label(self.hover_label_frame, text="", bg="#808080", fg="white", font=("Helvetica", 10), padx=5, pady=2)
        # self.hover_label.pack(side=tk.TOP, pady=2)

        # Header frame
        self.header = ctk.CTkFrame(root)
        self.header.pack(side=tk.TOP, fill=tk.X, pady=5)

        self.header_label = ctk.CTkLabel(self.header, text="Knowledge Graph Viewer", font=ctk.CTkFont(size=20, weight="bold"))
        self.header_label.pack(side=tk.TOP, pady=5)

        self.button_frame = ctk.CTkFrame(self.header)
        self.button_frame.pack(side=tk.TOP, pady=5)

        self.create_plot_button = ctk.CTkButton(self.button_frame, text="Create Graph", command=self.create_plot)
        self.create_plot_button.pack(side=tk.LEFT, padx=10)

        self.load_graph_button = ctk.CTkButton(self.button_frame, text="Load Graph", command=self.load_graph)
        self.load_graph_button.pack(side=tk.LEFT, padx=10)

        self.main_frame = ctk.CTkFrame(root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        self.plot_frame = ctk.CTkFrame(self.main_frame)
        self.plot_frame.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)

        # Canvas for displaying the graph
        self.canvas = tk.Canvas(self.plot_frame)
        self.canvas.pack(expand=True, fill=tk.BOTH)

        # Frame for holding the slider
        self.slider_frame = ctk.CTkFrame(self.main_frame)
        self.slider_frame.pack(fill=tk.Y, side=tk.RIGHT)

        # Slider to control graph size
        self.size_slider = ctk.CTkSlider(self.slider_frame, from_=5, to=20, command=self.update_graph_size)
        self.size_slider.set(12)  # Default value
        self.size_slider.pack(padx=10, pady=10, side=tk.TOP)

        self.current_size = 12

        # Text label for displaying hover text
        self.hover_label = tk.Label(self.toolbar_frame, text="", bg="#808080", fg="white", font=("Helvetica", 10))
        self.hover_label.place_forget()

        # Toolbar buttons with icons
        self.create_icons()

    def create_icons(self):
        # Load icons (you need to provide your own icons for this)

        self.open_icon = tk.PhotoImage(file="C:\\Users\\DS203\\Desktop\\euler_graph_database\\icons\\open.png").subsample(2, 2)
        self.save_icon = tk.PhotoImage(file="C:\\Users\\DS203\\Desktop\\euler_graph_database\\icons\\save.png").subsample(2, 2)
        self.exit_icon = tk.PhotoImage(file="C:\\Users\\DS203\\Desktop\\euler_graph_database\\icons\\exit.png").subsample(2, 2)

        icon_size = self.open_icon.width()  # Assuming all icons have the same size

        gray_color = "#808080"

        self.open_button = ctk.CTkButton(self.toolbar_frame, image=self.open_icon, text="", width=icon_size, height=icon_size, fg_color=gray_color)
        self.open_button.pack(side=tk.LEFT, padx=2, pady=2)
        self.open_button.bind("<Enter>", lambda e: self.show_hover_text("Open", self.open_button))
        self.open_button.bind("<Leave>", lambda e: self.hide_hover_text())

        self.save_button = ctk.CTkButton(self.toolbar_frame, image=self.save_icon, text="", width=icon_size, height=icon_size, fg_color=gray_color)
        self.save_button.pack(side=tk.LEFT, padx=2, pady=2)
        self.save_button.bind("<Enter>", lambda e: self.show_hover_text("Save", self.save_button))
        self.save_button.bind("<Leave>", lambda e: self.hide_hover_text())

        self.exit_button = ctk.CTkButton(self.toolbar_frame, image=self.exit_icon, text="", width=icon_size, height=icon_size, fg_color=gray_color)
        self.exit_button.pack(side=tk.LEFT, padx=2, pady=2)
        self.exit_button.bind("<Enter>", lambda e: self.show_hover_text("Exit", self.exit_button))
        self.exit_button.bind("<Leave>", lambda e: self.hide_hover_text())

    def show_hover_text(self, text, button):
        self.hover_label.config(text=text)
        self.hover_label.update_idletasks()  # Make sure label dimensions are updated
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
        self.root.quit()

    def create_plot(self):
        self.visualize_graph(self.current_size)

    def visualize_graph(self, size):
        print("Visualization started")
        G = nx.Graph()

        # Example nodes and edges
        self.graph = {
            'nodes': {1: {'label': 'Node 1', 'properties': 'A'}, 2: {'label': 'Node 2', 'properties': 'B'}},
            'edges': {1: {'source': 1, 'target': 2}}
        }

        for node_id, node in self.graph['nodes'].items():
            G.add_node(node_id)
        for edge_id, edge in self.graph['edges'].items():
            G.add_edge(edge['source'], edge['target'])

        pos = nx.fruchterman_reingold_layout(G)

        plt.figure(figsize=(size, size * 0.75))  # Adjust the figure size

        nx.draw_networkx_nodes(G, pos, node_size=500, node_color='blue')
        nx.draw_networkx_edges(G, pos, width=2, edge_color='#888')

        node_labels = {node: f"{self.graph['nodes'][node]['label']}\n{self.graph['nodes'][node]['properties']}" for node in G.nodes()}
        nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=12, font_color='black')
        plt.axis('off')
        plt.savefig('graph.png')
        plt.close()

        self.display_plot('graph.png')
        print("Visualization completed")

    def display_plot(self, file_path):
        img = Image.open(file_path)
        self.plot_image = ImageTk.PhotoImage(img)
        
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.plot_image)
        self.canvas.image = self.plot_image  # Keep a reference to avoid garbage collection

        # Adjust canvas size to fit the image
        self.canvas.config(width=self.plot_image.width(), height=self.plot_image.height())

    def load_graph(self):
        file_path = filedialog.askopenfilename(filetypes=[("HTML files", "*.html")])
        if file_path:
            with open(file_path, 'r') as f:
                plot_html = f.read()
            self.display_html_plot(plot_html)

    def update_graph_size(self, value):
        self.current_size = int(value)
        self.create_plot()

if __name__ == "__main__":
    root = ctk.CTk()
    app = KnowledgeGraphApp(root)
    root.mainloop()
