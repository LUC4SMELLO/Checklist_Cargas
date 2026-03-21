import tkinter as tk
import customtkinter as ctk
from constants.paths import ICONS_DIR


janela = ctk.CTk()
janela.title("Checklist Cargas")
janela.geometry("855x540")
janela.resizable(False, False)
janela.iconbitmap(ICONS_DIR / "checklist_cargas_icon.ico")

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")
