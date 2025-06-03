import gradio as gr
import os
from text_extraction import TextExtraction


# Diretório onde os arquivos serão salvos
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


# Função para resposta do chatbot com histórico
def chatbot_response(user_message, history):
    # Exemplo simples: ecoar a mensagem
    bot_message = f"Você disse: {user_message}"
    history = history + [(user_message, bot_message)]
    return history, history


# Função para listar arquivos salvos
def list_files():
    files = os.listdir(UPLOAD_DIR)
    return "Nenhum arquivo salvo." if not files else "\n".join(files)


# Função para salvar o arquivo enviado
def upload_file(file):
    if not file:
        return "File did not sent.", list_files()

    status = "Error"
    try:
        filename = str(file).split("/")[-1]
        if file.endswith('.docx'):
            text = TextExtraction.extract_docx(file)
            status = f"File '{filename}' saved."
        elif file.endswith('.pdf'):
            text = TextExtraction.extract_pdf(file)
            status = f"File '{filename}' saved."
        elif file.endswith('.txt'):
            text = TextExtraction.extract_txt(file)
            status = f"File '{filename}' saved."
        else:
            status = "File extension not supported."
    except Exception as e:
        status += ": " + str(e)
    return status, list_files()


with gr.Blocks() as demo:
    gr.Markdown("# Página Multifuncional com Gradio")

    with gr.Tab("Chatbot"):
        chatbot_ui = gr.Chatbot(label="Conversa")
        msg_input = gr.Textbox(label="Digite sua mensagem e aperte Enter")
        clear_button = gr.Button("Limpar Conversa")
        state = gr.State([])

        msg_input.submit(
            fn=chatbot_response,
            inputs=[msg_input, state],
            outputs=[chatbot_ui, state]
        )
        clear_button.click(
            fn=lambda: ([], []),
            inputs=None,
            outputs=[chatbot_ui, state]
        )

    with gr.Tab("Upload e Lista de Arquivos"):
        file_input = gr.File(label="Selecione um arquivo para upload")
        upload_output = gr.Textbox(label="Status do upload")
        list_output = gr.Textbox(label="Arquivos salvos", lines=10)
        list_button = gr.Button("Atualizar lista")

        # Upload atualiza o status e a lista
        file_input.upload(fn=upload_file, inputs=file_input, outputs=[upload_output, list_output]).then(lambda:None, None, file_input, queue=False)
        # Botão só atualiza a lista
        list_button.click(fn=list_files, inputs=[], outputs=list_output)

demo.launch(server_name="0.0.0.0", server_port=8484)
