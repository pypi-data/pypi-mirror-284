"""
Author: Prashant Verma
email: prashant27050@gmail.com
"""
import tkinter as tk
import customtkinter as ctk
import re

class SyntaxHighlighter:
    def __init__(self, text_widget):
        self.text_widget = text_widget
        self.keywords = ["CREATE", "AVG", "MAX", "MIN", "SUM", "MATCH", "SELECT","COUNT", "FROM", "WHERE", \
                                 "AND", "OR", "NOT", "INSERT", "INTO", "VALUES", "UPDATE", "SET", "DELETE"]
        self.other_keywords = ["WITH", "DISTINCT", "RETURN"]
        self.graph_keywords = []
        self.operators = ["=", "<", ">", "<=", ">=", "!=", "<>", "+", "-", "*", "/", "%"]
        self.configure_tags()

    def configure_tags(self):
        ''' Configure text tags for syntax highlighting '''
        # self.content.configure("title", font=header_font, foreground="blue")
        self.text_widget.tag_config("keyword", foreground="blue")
        self.text_widget.tag_config("other_keywords", foreground="green")
        self.text_widget.tag_config("operator", foreground="red")

    def highlight_syntax(self, event=None):
        ''' Apply syntax highlighting to the text widget '''
        self.text_widget.tag_remove("keyword", "1.0", tk.END)
        self.text_widget.tag_remove("operator", "1.0", tk.END)
        self.text_widget.tag_remove("other_keywords", "1.0", tk.END)

        text = self.text_widget.get("1.0", tk.END).strip()

        for word in self.keywords:
            pattern = r'\b' + re.escape(word) + r'\b'
            for match in re.finditer(pattern, text, re.IGNORECASE):
                start_index = f"1.0 + {match.start()}c"
                end_index = f"1.0 + {match.end()}c"
                self.text_widget.tag_add("keyword", start_index, end_index)

        for word in self.other_keywords:
            pattern = r'\b' + re.escape(word) + r'\b'
            for match in re.finditer(pattern, text, re.IGNORECASE):
                start_index = f"1.0 + {match.start()}c"
                end_index = f"1.0 + {match.end()}c"
                self.text_widget.tag_add("other_keywords", start_index, end_index)

        for op in self.operators:
            pattern = re.escape(op)
            for match in re.finditer(pattern, text):
                start_index = f"1.0 + {match.start()}c"
                end_index = f"1.0 + {match.end()}c"
                self.text_widget.tag_add("operator", start_index, end_index)


