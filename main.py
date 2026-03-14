from views.janela import janela

from views.checklist.checklist_view import ChecklistView
from controllers.checklist.checklist_controller import ChecklistController
from models.checklist.checklist_model import ChecklistModel

if __name__ == "__main__":

    model = ChecklistModel()

    controller = ChecklistController(model)

    view = ChecklistView(janela, controller)

    controller.set_view(view)
    controller.inicializar_cargas()

    janela.grid_rowconfigure(0, weight=1)
    janela.grid_columnconfigure(0, weight=1)
    
    view.grid(row=0, column=0, sticky="nsew")
    
    janela.mainloop()
