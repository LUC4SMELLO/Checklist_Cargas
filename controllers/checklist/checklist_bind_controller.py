import customtkinter as ctk


class ChecklistBindController:
    def __init__(self, controller):
        self.controller = controller
        self.view = None

    def set_view(self, view):
        self.view = view

    def configurar_binds(self):
        self.view.entry_numero_carga.bind("<Return>", self.adicionar_carga)

    def adicionar_carga(self, event):
        return self.controller.adicionar_carga()
