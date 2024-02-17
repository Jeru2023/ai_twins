import gradio as gr
import utils
from infer.tts_model import TTSModel
import os
from infer.persona_enum import PersonaEnum

root_path = utils.get_root_path()
tts_model = TTSModel()

output_folder = os.path.join(root_path, "output/tts/")

title = "TTS Toolkit Demo"
description = "Text to speech with zero shot TTS model."


def tts(persona_name, text, text_language, out_path):
    uuid = utils.generate_unique_id(text)
    output_path = os.path.join(root_path, 'output', 'tts', f'{uuid}.wav')
    print(output_path)
    tts_model.inference(persona_name, text, text_language, output_path)
    #return gr.Audio(output_path)
    return output_path


with gr.Blocks() as demo:
    with gr.Row():
        gr.Markdown(f'<H1>{title}</H1>')
        gr.Markdown(f'{description}')
    with gr.Row():
        with gr.Column():
            p = gr.Dropdown(label="Personas", choices=PersonaEnum.get_name_list())
            lan = gr.Dropdown(label="Language", choices=['zh', 'en'])
            text = gr.TextArea(label="Input Text")
            submit_btn = gr.Button("Submit")
        with gr.Column():
            outputs = gr.Audio(label="Output Audio")

    submit_btn.click(fn=tts, inputs=[p, text, lan], outputs=outputs)

demo.theme = gr.themes.Soft()
demo.launch(server_name='localhost')

