import tkinter as tk
import customtkinter as ctk
from constants.paths import ICONS_DIR


janela = ctk.CTk()
janela.title("Checklist Cargas")
janela.geometry("855x540")
janela.resizable(False, False)

icon = tk.PhotoImage(file=str(ICONS_DIR / "checklist_cargas_icon.png"))
janela.iconphoto(True, icon)

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")
