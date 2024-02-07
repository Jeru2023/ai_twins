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
g_audio_list = []

title = "ASR Toolkit Demo"
asr_description = "To transcribe .wav to text with FunASR model, both Mandarin and English supported."
slice_description = "Maximum first 5 slice trunks listed in this demo page."
tips_text = "Try microphone input if microphone is available on your device."


def audio_transcription(file_path):
    if not file_path:
        return "Please upload a .wav audio file"
    text = asr_model.inference(file_path)
    return text


def get_default_slice_outputs():
    audio_list = []
    for i in range(5):
        audio_list.append(gr.Audio(label="audio trunk " + str(i + 1)))
    return audio_list


def slice_audio(file_path, threshold, min_length, min_interval):
    if not file_path:
        return "Please upload a .wav audio file"
    output_folder = utils.create_unique_folder(slice_folder)
    slice_tool.slice_audio(file_path, output_folder, 'trunk', int(threshold), int(min_length), int(min_interval))

    trunks = utils.get_folder_file_list(os.path.normpath(output_folder))

    for trunk in trunks:
        g_audio_list.append(gr.Audio(value=trunk))

    return g_audio_list


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
        gr.Markdown(slice_description)
    with gr.Row():
        with gr.Column():
            f2 = gr.Audio(type="filepath", label="Input Audio")

            gr.Markdown(' ')
            threshold = gr.Textbox(label="The dB threshold for silence detection", value="-35")
            min_length = gr.Textbox(label="The minimum milliseconds required for each sliced audio clip", value="5000")
            min_interval = gr.Textbox(label="The minimum milliseconds for a silence part to be sliced", value="300")
            submit_btn_2 = gr.Button("Submit")

        with gr.Column():
            outputs = get_default_slice_outputs()

    submit_btn_2.click(fn=slice_audio, inputs=[f2, threshold, min_length, min_interval], outputs=outputs)


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
