import gradio as gr
import utils
from infer.asr_model import ASRModel
from tools import slice_tool
import os


root_path = utils.get_root_path()
asr_model = ASRModel()

upload_folder = os.path.join(root_path, "output/upload/")
slice_folder = os.path.join(root_path, "output/slice_trunks/")

upload_file_path = ''

title = "Toolkit Demo"
asr_description = "To transcribe .wav to text with FunASR model, both Mandarin and English supported."
tips_text = "Try microphone input if microphone is available on your device."


def audio_transcription(file_path):
    if not file_path:
        return "Please upload a .wav audio file"
    text = asr_model.inference(file_path)
    return text


def slice_audio(file_path):
    if not file_path:
        return "Please upload a .wav audio file"
    output_folder = utils.create_unique_folder(slice_folder)
    slice_tool.slice_audio(file_path, output_folder, 'trunk_')
    print(output_folder)
    trunks = utils.get_folder_file_list(os.path.normpath(output_folder))

    audio_list = []
    for trunk in trunks:
        audio_list.append(gr.Audio(value=trunk))
    return audio_list


def build_asr_demo():
    with gr.Row():
        gr.Markdown(asr_description)
    with gr.Row():
        with gr.Column():
            gr.Text(tips_text, label='Tips')
            f1 = gr.Audio(type="filepath", label="Input Audio")

            gr.Markdown(' ')
            submit_btn_1 = gr.Button("Submit")

        with gr.Column():
            output = gr.TextArea(label="Transcription Output")

    submit_btn_1.click(fn=audio_transcription, inputs=[f1], outputs=output)


def build_slice_demo():

    with gr.Row():
        gr.Markdown(asr_description)
    with gr.Row():
        with gr.Column():
            gr.Text(tips_text, label='Tips')
            f2 = gr.Audio(type="filepath", label="Input Audio")

            gr.Markdown(' ')
            submit_btn_2 = gr.Button("Submit")

        with gr.Column():
            output_placeholder = gr.TextArea(label="Slice Output")
            output = output_placeholder

    submit_btn_2.click(fn=slice_audio, inputs=[f2], outputs=output_placeholder)


with gr.Blocks() as demo:
    with gr.Row():
        gr.Markdown(f'<H1>{title}</H1>')
    with gr.Tab("ASR Demo"):
        build_asr_demo()
    with gr.Tab("Slice Demo"):
        build_slice_demo()
    with gr.Tab("Vocal Separation Demo"):
        gr.Text('3')


demo.theme = gr.themes.Soft()
demo.launch(server_name='localhost')
