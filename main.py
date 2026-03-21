from views.janela import janela

from views.checklist.checklist_view import ChecklistView
from controllers.checklist.checklist_controller import ChecklistController
from models.checklist.checklist_model import ChecklistModel

from services.monitor import DBMonitor

from constants.banco_dados import BANCO_DADOS_CARGAS


def fechar():
    monitor.stop()
    janela.destroy()


if __name__ == "__main__":

    janela.grid_rowconfigure(0, weight=1)
    janela.grid_columnconfigure(0, weight=1)

    model = ChecklistModel()
    controller = ChecklistController(model)
    view = ChecklistView(janela, controller)

    controller.set_view(view)
    controller.obter_proximo_dia_util()
    controller.inicializar_cargas(cargas="pendente")

    view.grid(row=0, column=0, sticky="nsew")

    controller.binds.configurar_binds()

    # MONITORAMENTO DO BANCO DE DADOS
    monitor = DBMonitor(
        BANCO_DADOS_CARGAS,
        controller.on_db_change,
        janela
    )

    controller.set_monitor(monitor)
    monitor.start()

    janela.protocol("WM_DELETE_WINDOW", fechar)
    janela.mainloop()
