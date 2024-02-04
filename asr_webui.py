import gradio as gr
import utils
from infer.asr_model import ASRModel
import os

root_path = utils.get_root_path()
asr_model = ASRModel()

upload_folder = os.path.join(root_path, "output/upload/")
upload_file_path = ''

title = "ASR Demo"
description = "To transcribe .wav to text with FunASR model."

sample1 = os.path.join(root_path, "data/audio/sample_short.wav")
sample2 = os.path.join(root_path, "data/audio/sample_long.wav")

examples = [
    [sample1, 'sample_short.wav'],
    [sample2, 'sample_long.wav']
]


def toggle(choice):
    if choice == "file":
        return gr.update(visible=True), gr.update(visible=False)
    else:
        return gr.update(visible=False), gr.update(visible=True)


def upload(file_path):
    global upload_file_path
    upload_file_path = file_path


def audio_transcription(file_path):
    if not file_path:
        return "Please upload a .wav audio file"

    text = asr_model.inference(file_path)
    return text


with gr.Blocks() as demo:
    with gr.Row():
        gr.Markdown(f'<H1>{title}</H1>')
    with gr.Row():
        gr.Markdown(description)
    with gr.Row():
        with gr.Column():
            r = gr.Radio(["file", "mic"], value="file", label="How would you like to upload your audio?")
            f = gr.Audio(type="filepath", label="Input Audio")
            m = gr.Mic(label="Input Audio", visible=False)

            gr.Markdown(' ')

            vs_checker = gr.Checkbox(label="Enable Vocal Separation", info="checked if audio is noisy")

            as_checker = gr.Checkbox(label="Enable Audio Slice", info="checked if audio is long")
            submit_btn = gr.Button("Submit")

        with gr.Column():
            output = gr.TextArea(label="Transcription Output")

    r.change(toggle, r, [f, m])
    f.change(upload, f)
    m.change(upload, m)

    if r.value == "file":
        mode_inputs = [f]
    else:
        mode_inputs = [m]

    submit_btn.click(fn=audio_transcription, inputs=mode_inputs, outputs=output)

demo.theme = gr.themes.Soft()
demo.launch(server_name='localhost')
