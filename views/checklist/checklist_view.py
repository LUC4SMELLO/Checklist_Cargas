import customtkinter as ctk

from PIL import Image

from views.checklist.components.frame_carga import FrameCarga

from constants.paths import ICONS_DIR

from constants.textos import (
    FONTE_TITULO,
    FONTE_SUBTITULO,
    FONTE_LABEL,
    FONTE_TEXTO,
    FONTE_PEQUENA,
    FONTE_BOTAO_PRINCIPAL,
    FONTE_BOTAO_SECUNDARIO
)

from constants.cores import (
    COR_BOTAO,
    COR_BOTAO_SELECIONADO,
    COR_HOVER_BOTAO,
    COR_TEXTO,
    COR_TEXTO_BOTAO,
    COR_LINHAS,
    COR_FUNDO_CONTAINER_CARGAS
)


class ChecklistView(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)


        self.controller = controller
        self.frames_carga = []


        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)


        self.main_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.main_frame.grid_rowconfigure(0, weight=0)
        self.main_frame.grid_rowconfigure(1, weight=0)
        self.main_frame.grid_rowconfigure(2, weight=0)
        self.main_frame.grid_rowconfigure(3, weight=0)
        self.main_frame.grid_rowconfigure(5, weight=0)
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid(row=0, column=0, sticky="nsew")

        self.header_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.header_frame.grid_rowconfigure(0, weight=1)
        self.header_frame.grid_rowconfigure(1, weight=1)
        self.header_frame.grid_rowconfigure(2, weight=1)
        self.header_frame.grid_columnconfigure(0, weight=1)
        self.header_frame.grid_columnconfigure(1, weight=0)
        self.header_frame.grid(row=0, column=0, sticky="ew")

        ctk.CTkLabel(self.header_frame, text="Checklist Cargas", font=FONTE_TITULO, text_color=COR_TEXTO).grid(row=0, column=0, padx=(40, 0), pady=(10, 10), sticky="ws")

        ctk.CTkFrame(self.header_frame, height=2, fg_color=COR_LINHAS).grid(row=1, column=0, padx=(20, 20), pady=(5, 0), sticky="ew", columnspan=4)

        self.toolbar_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.toolbar_frame.grid_rowconfigure(0, weight=0)
        self.toolbar_frame.grid_rowconfigure(1, weight=0)
        self.toolbar_frame.grid_rowconfigure(2, weight=0)
        self.toolbar_frame.grid_columnconfigure(0, minsize=140) # LABEL
        self.toolbar_frame.grid_columnconfigure(1, minsize=110) # ENTRY
        self.toolbar_frame.grid_columnconfigure(2, minsize=40)  # BOTÃO
        self.toolbar_frame.grid_columnconfigure(3, minsize=0)   # VAZIO
        self.toolbar_frame.grid_columnconfigure(4, weight=1)    # COLUNA FLEXÍVEL
        self.toolbar_frame.grid_columnconfigure(5, minsize=200) # DATA
        self.toolbar_frame.grid(row=1, column=0, sticky="ew")

        ctk.CTkLabel(self.toolbar_frame, text="Número Carga:", font=FONTE_LABEL, text_color=COR_TEXTO).grid(row=0, column=0, padx=(40, 0), pady=(15, 0), sticky="e")
        self.entry_numero_carga = ctk.CTkEntry(self.toolbar_frame, font=FONTE_TEXTO, text_color=COR_TEXTO, width=100, height=30, corner_radius=2)
        self.entry_numero_carga.grid(row=0, column=1, padx=(8, 0), pady=(15, 0), sticky="w")

        self.icone_mais = ctk.CTkImage(
            light_image=Image.open(ICONS_DIR / "mais_dark.png"),
            dark_image=Image.open(ICONS_DIR / "mais_dark.png"),
            size=(18, 18)
        )
        self.botao_adicionar_carga = ctk.CTkButton(
            self.toolbar_frame,
            image=self.icone_mais,
            text="",
            command=self.controller.adicionar_carga,
            width=20,
            height=30,
            fg_color=COR_BOTAO,
            hover_color=COR_HOVER_BOTAO,
            cursor="hand2"
        )
        self.botao_adicionar_carga.grid(row=0, column=2, padx=(5, 0), pady=(15, 0), sticky="w")

        self.label_data = ctk.CTkLabel(self.toolbar_frame, text="Data Faturar: 16/03/2026", font=FONTE_LABEL, text_color=COR_TEXTO)
        self.label_data.grid(row=0, column=5, padx=(0, 40), pady=(15, 0))

        ctk.CTkFrame(self.toolbar_frame, height=2, fg_color=COR_LINHAS).grid(row=1, column=0, padx=(20, 20), pady=(15, 0), sticky="ew", columnspan=6)

        self.icone_reiniciar = ctk.CTkImage(
            light_image=Image.open(ICONS_DIR / "reiniciar_dark.png"),
            dark_image=Image.open(ICONS_DIR / "reiniciar_dark.png"),
            size=(22, 22)
        )
        self.botao_reiniciar = ctk.CTkButton(
            self.toolbar_frame,
            image=self.icone_reiniciar,
            text="",
            command=self.controller.reiniciar_cargas,
            width=20,
            height=30,
            fg_color=COR_BOTAO,
            hover_color=COR_HOVER_BOTAO,
            cursor="hand2"
        )
        self.botao_reiniciar.grid(row=1, column=5, padx=(0, 40), pady=(15, 0), sticky="e")

        self.tabs_frame = ctk.CTkFrame(self.toolbar_frame, fg_color="transparent", height=30)
        self.tabs_frame.grid(row=1, column=0, padx=(40, 0), pady=(15, 0), columnspan=4)

        ctk.CTkFrame(self.tabs_frame, height=2, fg_color=COR_LINHAS).grid(row=0, column=0, padx=(20, 20), pady=(0, 0), sticky="ew", columnspan=6)

        self.botao_cargas_pendentes = ctk.CTkButton(
            self.tabs_frame,
            text="Pendentes",
            command= lambda: controller.selecionar_tab(self.botao_cargas_pendentes),
            font=FONTE_BOTAO_SECUNDARIO,
            text_color=COR_TEXTO,
            fg_color=COR_BOTAO,
            hover_color=COR_HOVER_BOTAO,
            width=133
            )
        self.botao_cargas_pendentes.configure(fg_color=COR_BOTAO_SELECIONADO)
        self.botao_cargas_pendentes.grid(row=0, column=0)

        self.botao_cargas_concluidas = ctk.CTkButton(
            self.tabs_frame,
            text="Concluídas",
            command= lambda: controller.selecionar_tab(self.botao_cargas_concluidas),
            font=FONTE_BOTAO_SECUNDARIO,
            text_color=COR_TEXTO,
            fg_color=COR_BOTAO,
            hover_color=COR_HOVER_BOTAO,
            width=133
            )
        self.botao_cargas_concluidas.grid(row=0, column=1, padx=(5, 0))



        self.cargas_header = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.cargas_header.grid(row=2, column=0, sticky="ew")

        self.cargas_header.grid_columnconfigure(0, minsize=50)
        self.cargas_header.grid_columnconfigure(1, minsize=20)
        self.cargas_header.grid_columnconfigure(2, minsize=20)
        self.cargas_header.grid_columnconfigure(3, minsize=50)
        self.cargas_header.grid_columnconfigure(4, minsize=20)
        self.cargas_header.grid_columnconfigure(5, minsize=20)
        self.cargas_header.grid_columnconfigure(6, minsize=20)
        self.cargas_header.grid_columnconfigure(7, minsize=20)

        ctk.CTkLabel(self.cargas_header, text="Carga", font=FONTE_LABEL, text_color=COR_TEXTO).grid(row=0, column=0, padx=(40, 0), pady=(25, 0))
        ctk.CTkLabel(self.cargas_header, text="Nota Fiscal", font=FONTE_LABEL, text_color=COR_TEXTO).grid(row=0, column=1, padx=(40, 0), pady=(25, 0))
        ctk.CTkLabel(self.cargas_header, text="Boleto", font=FONTE_LABEL, text_color=COR_TEXTO).grid(row=0, column=2, padx=(40, 0), pady=(25, 0))
        ctk.CTkLabel(self.cargas_header, text="Acerto", font=FONTE_LABEL, text_color=COR_TEXTO).grid(row=0, column=3, padx=(45, 0), pady=(25, 0))
        ctk.CTkLabel(self.cargas_header, text="Mapa", font=FONTE_LABEL, text_color=COR_TEXTO).grid(row=0, column=4, padx=(50, 0), pady=(25, 0))
        ctk.CTkLabel(self.cargas_header, text="Troca", font=FONTE_LABEL, text_color=COR_TEXTO).grid(row=0, column=5, padx=(60, 0), pady=(25, 0))
        ctk.CTkLabel(self.cargas_header, text="Problema", font=FONTE_LABEL, text_color=COR_TEXTO).grid(row=0, column=6, padx=(40, 0), pady=(25, 0))
        ctk.CTkLabel(self.cargas_header, text="", font=FONTE_LABEL, text_color=COR_TEXTO).grid(row=0, column=7, padx=(40, 0), pady=(25, 0))

        self.container_cargas = ctk.CTkScrollableFrame(
            self.main_frame,
            fg_color=COR_FUNDO_CONTAINER_CARGAS,
            height=290
        )
        self.container_cargas.grid_columnconfigure(0, weight=1)
        self.container_cargas.grid_columnconfigure(1, weight=0)
        self.container_cargas.grid_columnconfigure(2, weight=0)
        self.container_cargas.grid_columnconfigure(3, weight=0)
        self.container_cargas.grid_columnconfigure(4, weight=0)
        self.container_cargas.grid_columnconfigure(5, weight=0)
        self.container_cargas.grid(row=3, column=0, padx=(20, 20), sticky="nsew")


        self.footer_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.footer_frame.grid_columnconfigure(0, minsize=100)
        self.footer_frame.grid_columnconfigure(1, minsize=100)
        self.footer_frame.grid_columnconfigure(2, minsize=100)
        self.footer_frame.grid_columnconfigure(3, minsize=100)
        self.footer_frame.grid(
            row=4,
            column=0,
            sticky="ew",
            padx=(0, 0),
            pady=(0, 0)
        )

        self.label_total_cargas = ctk.CTkLabel(self.footer_frame, text="Total: 0", font=("Segoe UI", 14, "bold"), text_color=COR_TEXTO)
        self.label_total_cargas.grid(row=0, column=0, padx=(40, 0), pady=(5, 0))

    def criar_frame_carga(self):
        quantidade_cargas = len(self.frames_carga)

        frame = FrameCarga(self.container_cargas, self.controller)
        frame.grid(row=quantidade_cargas + 1, column=0, padx=(5, 0), pady=(5, 0), sticky="ew")
        self.frames_carga.append(frame)

        return frame

