from CTkMessagebox import CTkMessagebox
from typing import Literal

from constants.textos import FONTE_TEXTO
from constants.cores import COR_TEXTO, COR_BOTAO, COR_TEXTO_BOTAO, HOVER_BOTAO


def exibir_mensagem(
        titulo: str,
        mensagem: str,
        icone: Literal["info", "warning", "cancel", "check"] = "info",
        opcao_1:str ="Ok",
        opcao_2:str =None,
        opcao_3:str =None
        ) -> str:
    """
    Exibe um popup com uma mensagem.

    Parameters
    ----------
        titulo : str
            O texto que será o título do popup.
        mensagem : str
            O texto que será a mensagem do popup.
        icone : str
            O ícone do popup, podem ser (check, cancel, info, question, warning).
            O padrão é "info".
        opcao_1: str
            O texto do primeiro botão.
        opcao_2: str
            O texto do segundo botão.
        opcao_3: str
            O texo do terceiro botão.
        
    """
    mensagem = CTkMessagebox(
        title=titulo,
        message=mensagem,
        icon=icone,
        width=350,
        height=50,
        font=FONTE_TEXTO,
        text_color=COR_TEXTO,
        button_color=COR_BOTAO,
        cancel_button_color=COR_BOTAO,
        button_text_color=COR_TEXTO_BOTAO,
        button_hover_color=HOVER_BOTAO,
        option_1=opcao_1,
        option_2=opcao_2,
        option_3=opcao_3,
        )

    return mensagem.get()