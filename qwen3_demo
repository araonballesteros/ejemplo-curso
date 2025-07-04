import gradio as gr

def reasoning_mode_switch(input_text, mode):
    if not input_text:
        return "Por favor ingresa un texto de entrada."
    if mode == "simple":
        return f"Salida de razonamiento simple para: {input_text}"
    elif mode == "advanced":
        return f"Salida de razonamiento avanzado para: {input_text}"
    else:
        return "Modo no válido seleccionado."

def multilingual_translation(text, language):
    if not text:
        return "Por favor ingresa un texto para traducir."
    translations = {
        "es": f"Traducción al español de '{text}'",
        "fr": f"Traducción al francés de '{text}'",
        "de": f"Traducción al alemán de '{text}'",
    }
    return translations.get(language, "Idioma no soportado.")

with gr.Blocks() as demo:
    gr.Markdown("# Cambiar modo de razonamiento")
    input_text = gr.Textbox(label="Texto de entrada")
    mode = gr.Radio(choices=["simple", "advanced"], label="Modo")
    output = gr.Textbox(label="Resultado")
    btn = gr.Button("Procesar")
    btn.click(reasoning_mode_switch, inputs=[input_text, mode], outputs=output)

    gr.Markdown("# Traducción multilingüe")
    trans_text = gr.Textbox(label="Texto a traducir")
    language = gr.Radio(choices=["es", "fr", "de"], label="Idioma")
    trans_output = gr.Textbox(label="Traducción")
    trans_btn = gr.Button("Traducir")
    trans_btn.click(multilingual_translation, inputs=[trans_text, language], outputs=trans_output)

demo.launch()
