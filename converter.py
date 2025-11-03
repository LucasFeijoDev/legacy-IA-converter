def convert_code(legacy_code: str, target_language: str) -> str:
    """
    Simula a conversão de código legado para linguagem moderna.
    """

    # Simplificação: apenas detecta padrões e substitui
    converted = legacy_code

    # Exemplo de conversão genérica
    converted = converted.replace("PRINT", "print")
    converted = converted.replace("Dim ", "# variável: ")
    converted = converted.replace("End If", "# fim do if")
    converted = converted.replace("If ", "if ")
    converted = converted.replace("Then", ":")

    explanation = f"# Código convertido automaticamente para {target_language}\n"
    explanation += "# Conversão simulada para demonstração de MVP.\n\n"

    return explanation + converted