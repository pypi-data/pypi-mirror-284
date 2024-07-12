"""
Author: Prashant Verma
email: prashant27050@gmail.com
"""
import tkinter as tk
from tkinter import font as tkfont
import customtkinter as ctk

class ModalDialog:
    def __init__(self, root, title, content, is_about=False):
        self.top = ctk.CTkToplevel(root)
        self.top.title(title)
        self.top.geometry("750x550")
        header_font = ctk.CTkFont(family="Helvetica", size=14, weight="bold")
        bold_font = ctk.CTkFont(family="Helvetica", size=10, weight="bold")
        normal_font = ctk.CTkFont(family="Helvetica", size=10)

        header_label = ctk.CTkLabel(self.top, text=title, font=header_font, bg_color="gray", fg_color="blue", pady=10)
        header_label.pack(side=tk.TOP, fill=tk.X)

        self.content = ctk.CTkTextbox(self.top, wrap=tk.WORD, padx=10, pady=10, font=normal_font)
        self.content.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
        self.content.insert(tk.END, content)

        if is_about:
            self.content.tag_add("title", "1.0", "1.end")
            self.content.configure("title", font=header_font, foreground="blue")
            self.content.tag_add("bold", "3.0", "3.4")  # "© 2024 Euler Graph Database."
            self.content.configure("bold", font=bold_font, foreground="green")
        else:
            lines = content.split('\n')
            line_start = 0
            for line in lines:
                if line.startswith("1. "):
                    end_idx = line.find(":")
                    self.content.tag_add(f"section_title_{line_start}", f"{line_start+1}.0", f"{line_start+1}.{end_idx}")
                    self.content.configure(f"section_title_{line_start}", font=bold_font, foreground="purple")
                line_start += 1

        self.content.configure(state=tk.DISABLED)

        self.ok_button = ctk.CTkButton(self.top, text="OK", command=self.top.destroy, font=bold_font, bg_color="lightblue", fg_color="blue")
        self.ok_button.pack(pady=10)

