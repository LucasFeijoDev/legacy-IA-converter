from flask import Flask, render_template, request

app = Flask(__name__)

def convert_code_legacy_to_modern(legacy_code, target_language="python"):
    """
    Conversor simulado de código legado para linguagens modernas.
    Suporta conversão básica para Python ou JavaScript.
    """
    lines = legacy_code.splitlines()
    converted = []

    # Detecta tipo do código legado (heurística simples)
    if any("DISPLAY" in line for line in lines):
        source_type = "COBOL"
    elif any("PRINT" in line for line in lines):
        source_type = "VB6"
    else:
        source_type = "Desconhecido"

    converted.append(f"# Conversão simulada de {source_type} para {target_language.capitalize()}" if target_language == "python" else f"// Conversão simulada de {source_type} para {target_language.capitalize()}")

    for line in lines:
        line = line.strip()

        # Conversão para Python
        if target_language == "python":
            if line.startswith("DISPLAY"):
                content = line.replace("DISPLAY", "").strip().replace('"', "'")
                converted.append(f"print({content})")
            elif "STOP RUN" in line:
                converted.append("exit()")
            elif "PRINT" in line:
                content = line.replace("PRINT", "").strip().replace('"', "'")
                converted.append(f"print({content})")
            elif "If" in line and "Then" in line:
                converted.append(line.replace("If", "if").replace("Then", ":"))
            elif "End If" in line:
                converted.append("# fim do if")
            else:
                converted.append(f"# {line}  # Linha não reconhecida")

        # Conversão para JavaScript
        elif target_language == "javascript":
            if line.startswith("DISPLAY") or line.startswith("PRINT"):
                content = line.replace("DISPLAY", "").replace("PRINT", "").strip()
                converted.append(f"console.log({content});")
            elif "STOP RUN" in line:
                converted.append("// programa finalizado")
            elif "If" in line and "Then" in line:
                converted.append(line.replace("If", "if (").replace("Then", ") {"))
            elif "End If" in line:
                converted.append("}")
            else:
                converted.append(f"// {line}  // Linha não reconhecida")

    converted.append("\n# fim da conversão" if target_language == "python" else "\n// fim da conversão")
    return "\n".join(converted)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/convert', methods=['POST'])
def convert():
    legacy_code = request.form['legacy_code']
    target_language = request.form.get('language', 'python')
    converted = convert_code_legacy_to_modern(legacy_code, target_language)
    return render_template('index.html', converted_code=converted, legacy_code=legacy_code)


if __name__ == '__main__':
    app.run(debug=True)