import customtkinter as ctk

from datetime import datetime, timedelta
import holidays

from views.checklist.components.frame_carga import FrameCarga

from validators.checklist.checklist_validator import validar_checklist

from views.dialogs.exibir_mensagem import exibir_mensagem

from constants.cores import COR_FUNDO_FRAME_CARGAS, COR_FUNDO_FRAME_CARGAS_CONCLUIDO

class ChecklistController:
    def __init__(self, model):
        self.view = None
        self.model = model

    def set_view(self, view):
        self.view = view


    def coletar_dados(self, frame):
        data = datetime.now().date()

        dados = {
            "data": data,
            "numero_carga": frame.label_carga.cget("text").strip(),
            "nota_fiscal": frame.check_nota_fiscal_var.get(),
            "boleto": frame.check_boleto_var.get(),
            "acerto": frame.check_acerto_var.get(),
            "mapa": frame.check_mapa_var.get(),
            "troca": frame.check_troca_var.get(),
            "problema": frame.check_problema_var.get()
        }

        return dados

    def adicionar_carga(self):

        quantidade_cargas = len(self.view.frames_carga)

        numero_carga = self.view.entry_numero_carga.get().strip()

        resultado = validar_checklist(numero_carga)
        if not resultado["sucesso"]:
            self.limpar_formulario()
            exibir_mensagem(resultado["titulo"], resultado["mensagem"], resultado["icone"])
            return "break"

        frame = FrameCarga(self.view.container_cargas, self.view.controller)
        frame.label_carga.configure(text=numero_carga)
        frame.grid(row=quantidade_cargas + 1, column=0, padx=(5, 0), pady=(5, 0), sticky="ew")
        self.view.frames_carga.append(frame)

        dados = self.coletar_dados(frame)
        self.model.inserir_carga_pendente(dados)

        self.limpar_formulario()
        self.atualizar_numero_total_cargas()

    def remover_carga(self, frame):
        if frame in self.view.frames_carga:
            self.view.frames_carga.remove(frame)

        dados = self.coletar_dados(frame)
        self.model.excluir_carga_pendente(dados)
        frame.destroy()

        self.atualizar_numero_total_cargas()

    def checkbox_event(self, frame, checkbox_var):
        self.verificar_checkbox(frame, checkbox_var)

    def verificar_checkbox(self, frame, checkbox_var):

        dados = self.coletar_dados(frame)
        self.model.editar_carga_pendente(dados)

        checkboxes = [
            frame.check_nota_fiscal_var.get(),
            frame.check_boleto_var.get(),
            frame.check_acerto_var.get(),
            frame.check_mapa_var.get(),
            frame.check_troca_var.get()
        ]

        if all(checkboxes):
            frame.configure(fg_color=COR_FUNDO_FRAME_CARGAS_CONCLUIDO)

            escolha = exibir_mensagem(
                "Finalizar?",
                "Deseja finalizar a carga?",
                "info",
                opcao_1="Sim",
                opcao_2="Não"
            )

            if escolha == "Sim":
                self.remover_carga(frame)
            else:
                frame.configure(fg_color=COR_FUNDO_FRAME_CARGAS)
                checkbox_var.set(0)

                dados = self.coletar_dados(frame)
                self.model.editar_carga_pendente(dados)
        else:
            frame.configure(fg_color=COR_FUNDO_FRAME_CARGAS)


    def atualizar_numero_total_cargas(self):
        quantidade_cargas = len(self.view.frames_carga)
        self.view.label_total_cargas.configure(text=f"Total: {quantidade_cargas}")
    
    def limpar_formulario(self):
        self.view.entry_numero_carga.delete(0, ctk.END)
        self.view.entry_numero_carga.focus_set()

    def limpar_container_cargas(self):
        self.view.frames_carga.clear()
        for widget in self.view.container_cargas.winfo_children():
            widget.destroy()


    def obter_proximo_dia_util(self):
        feriados_br = holidays.BR()

        data_atual = datetime.now().date()
        proximo_dia = data_atual + timedelta(days=1)
        
        # ENQUANTO FOR FINAL DE SEMANA (SÁB=5 DOM=6) OU FERIADO, PULA +1 DIA
        while proximo_dia.weekday() >= 5 or proximo_dia in feriados_br:
            proximo_dia += timedelta(days=1)
            
        data_formatada = proximo_dia.strftime("%d/%m/%Y")
        self.view.label_data.configure(text=f"Data Faturamento: {data_formatada}")



    # -------------------------------------
    #     CARREGAMENTO CARGAS PENDENTES
    # -------------------------------------

    def inicializar_cargas(self):
        self.limpar_container_cargas()

        registros = self.model.carregar_cargas_pendentes()

        if registros:
            for dados in registros:
                frame = self.view.criar_frame_carga()
                self._preencher_frame(frame, dados)
    
    def _preencher_frame(self, frame, dados):

        frame.label_carga.configure(text=dados["numero_carga"])

        frame.check_nota_fiscal_var.set(dados["nota_fiscal"])
        frame.check_boleto_var.set(dados["boleto"])
        frame.check_acerto_var.set(dados["acerto"])
        frame.check_mapa_var.set(dados["mapa"])
        frame.check_troca_var.set(dados["troca"])
        
        self.atualizar_numero_total_cargas()