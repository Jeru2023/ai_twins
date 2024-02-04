import gradio as gr
import utils
from infer.asr_model import ASRModel
import os

root_path = utils.get_root_path()
asr_model = ASRModel()


def audio_transcription(file_obj):
    wav_file_path = file_obj.name
    if not wav_file_path:
        return "Please upload a .wav audio file"
    text = asr_model.inference(wav_file_path)
    return text


title = "ASR Demo"
description = "transcribe .wav to text"


sample1 = os.path.join(root_path, "data/audio/sample_short.wav")
sample2 = os.path.join(root_path, "data/audio/sample_long.wav")

examples = [
    [sample1, 'sample_short.wav'],
    [sample2, 'sample_long.wav']
]


# inputs = gr.File(label='Upload a .wav audio file', file_types=[".wav"])
#
# demo = gr.Interface(
#     fn=audio_transcription,
#     inputs=inputs,
#     outputs="text",
#     examples=examples,
#     title=title,
#     description=description,
#     theme=gr.themes.Soft(),
# )

def toggle(choice):
    if choice == "file":
        return gr.update(visible=True), gr.update(visible=False)
    else:
        return gr.update(visible=False), gr.update(visible=True)


with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column():
            r = gr.Radio(["file", "mic"], value="file", label="How would you like to upload your audio?")
            m = gr.Mic(label="Input")
            f = gr.Audio(type="filepath", label="Input", visible=False)
        with gr.Column():
            output = gr.Audio(label="Output")

    r.change(toggle, r, [m, f])
    m.change(lambda x: x, m, output)
    f.change(lambda x: x, f, output)

demo.launch()

demo.launch(server_name='localhost')
