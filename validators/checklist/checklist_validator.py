def validar_checklist(numero_carga: dict):

    if not numero_carga or str(numero_carga).strip() == "":
        return {
            "sucesso": False,
            "titulo": "Erro",
            "mensagem": f"O campo 'Número da Carga' é obrigatório!",
            "icone": "cancel"
        }
        
    if any(char.isalpha() for char in str(numero_carga)):
        return {
            "sucesso": False,
            "titulo": "Erro",
            "mensagem": "Letras não são permitidas!",
            "icone": "cancel"
        }

    if not str(numero_carga).isdigit():
        return {
        "sucesso": False,
        "titulo": "Erro",
        "mensagem": "Apenas números são permitidos!",
        "icone": "cancel"
        }

    if len(numero_carga) < 7 or len(numero_carga) > 7:
        return {
            "sucesso": False,
            "titulo": "Erro",
            "mensagem": "Tamanho inválido!",
            "icone": "cancel"
        }
        

    return {
        "sucesso": True,
        "titulo": "Sucesso",
        "mensagem": "Checklist correto!",
        "icone": "check"
    }