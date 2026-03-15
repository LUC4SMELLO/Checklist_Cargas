import customtkinter as ctk

from PIL import Image

from constants.paths import ICONS_DIR

from constants.textos import FONTE_LABEL, FONTE_TEXTO
from constants.cores import (
    COR_TEXTO,
    COR_BOTAO,
    COR_HOVER_BOTAO,
    COR_FUNDO_FRAME_CARGAS
)


class FrameCarga(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, height=90, border_width=0, corner_radius=0, fg_color=COR_FUNDO_FRAME_CARGAS)

        self.controller = controller

        self.grid_columnconfigure(0, minsize=50)
        self.grid_columnconfigure(1, minsize=20)
        self.grid_columnconfigure(2, minsize=20)
        self.grid_columnconfigure(3, minsize=50)
        self.grid_columnconfigure(4, minsize=20)
        self.grid_columnconfigure(5, minsize=20)
        self.grid_columnconfigure(6, minsize=20)

        self.label_carga = ctk.CTkLabel(self, text="7201001", font=("Segoe UI", 16), text_color=COR_TEXTO)
        self.label_carga.grid(row=0, column=0, padx=(5, 0), pady=(0, 0))

        self.check_nota_fiscal_var = ctk.IntVar(value=0)
        self.check_nota_fiscal = ctk.CTkCheckBox(
            self,
            text="",
            command=lambda: controller.checkbox_event(self, self.check_nota_fiscal_var),
            variable=self.check_nota_fiscal_var,
            onvalue=1,
            offvalue=0,
            fg_color="green",
            hover_color=COR_HOVER_BOTAO,
            border_color="gray",
            )
        self.check_nota_fiscal.grid(row=0, column=1, padx=(60, 0), pady=(0, 0))

        self.check_boleto_var = ctk.IntVar(value=0)
        self.check_boleto = ctk.CTkCheckBox(
            self,
            text="",
            command=lambda: controller.checkbox_event(self, self.check_boleto_var),
            variable=self.check_boleto_var,
            onvalue=1,
            offvalue=0,
            fg_color="green",
            hover_color=COR_HOVER_BOTAO,
            border_color="gray",
            )
        self.check_boleto.grid(row=0, column=2, padx=(10, 0), pady=(0, 0))


        self.check_acerto_var = ctk.IntVar(value=0)
        self.check_acerto = ctk.CTkCheckBox(
            self,
            text="",
            command=lambda: controller.checkbox_event(self, self.check_acerto_var),
            variable=self.check_acerto_var,
            onvalue=1,
            offvalue=0,
            fg_color="green",
            hover_color=COR_HOVER_BOTAO,
            border_color="gray",
            )
        self.check_acerto.grid(row=0, column=3, padx=(0, 0), pady=(0, 0))

        self.check_mapa_var = ctk.IntVar(value=0)
        self.check_mapa = ctk.CTkCheckBox(
            self,
            text="",
            command=lambda: controller.checkbox_event(self, self.check_mapa_var),
            variable=self.check_mapa_var,
            onvalue=1,
            offvalue=0,
            fg_color="green",
            hover_color=COR_HOVER_BOTAO,
            border_color="gray",
            )
        self.check_mapa.grid(row=0, column=4, padx=(0, 0), pady=(0, 0))

        self.check_troca_var = ctk.IntVar(value=0)
        self.check_troca = ctk.CTkCheckBox(
            self,
            text="",
            command=lambda: controller.checkbox_event(self, self.check_troca_var),
            variable=self.check_troca_var,
            onvalue=1,
            offvalue=0,
            fg_color="green",
            hover_color=COR_HOVER_BOTAO,
            border_color="gray",
            )
        self.check_troca.grid(row=0, column=5, padx=(0, 0), pady=(0, 0))

        self.check_problema_var = ctk.IntVar(value=0)
        self.check_problema = ctk.CTkCheckBox(
            self,
            text="",
            command=lambda: controller.checkbox_event(self, self.check_problema_var),
            variable=self.check_problema_var,
            onvalue=1,
            offvalue=0,
            fg_color="green",
            hover_color=COR_HOVER_BOTAO,
            border_color="gray",
            )
        self.check_problema.grid(row=0, column=6, padx=(0, 0), pady=(0, 0))

        self.icone_lixeira = ctk.CTkImage(
            light_image=Image.open(ICONS_DIR / "lixeira_dark.png"),
            dark_image=Image.open(ICONS_DIR / "lixeira_dark.png"),
            size=(22, 22)
        )
        self.botao_remover_carga = ctk.CTkButton(
            self,
            image=self.icone_lixeira,
            text="",
            command=lambda: controller.remover_carga(self, True),
            width=20,
            height=20,
            fg_color="transparent",
            hover_color=COR_HOVER_BOTAO,
            cursor="hand2",
        )
        self.botao_remover_carga.grid(row=0, column=7, padx=(0, 0), pady=(0, 0))
