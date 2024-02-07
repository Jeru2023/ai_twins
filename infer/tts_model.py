import os
import sys
import utils
from infer.persona_enum import PersonaEnum
import torch
import utils
import soundfile as sf

root_path = utils.get_root_path()
GPTSoVITS_DIR = os.path.join(root_path, 'GPTSoVITS')
sys.path.append(GPTSoVITS_DIR)
sys.path.append("%s/GPT_SoVITS" % GPTSoVITS_DIR)

from GPTSoVITS import api


class TTSModel:
    def __init__(self):
        pass

    @staticmethod
    def inference(persona_name, text, text_language, out_path):
        persona = PersonaEnum.get_persona_by_name(persona_name)
        prompt_text = persona.get_ref_text().strip("\n")
        ref_audio_path = persona.get_ref_audio()
        prompt_language = persona.get_language()

        with torch.no_grad():
            gen = api.get_tts_wav(ref_audio_path, prompt_text, prompt_language, text, text_language)
            sampling_rate, audio_data = next(gen)

        sf.write(out_path, audio_data, sampling_rate, format="wav")


tts_model = TTSModel()
root_path = utils.get_root_path()

persona_name = PersonaEnum.NORMAL_FEMALE.get_name()
text = '今天天气不错呀，我真的太开心了。'

text_language = 'zh'
output_path = os.path.join(root_path, 'output', 'tts', 'my_file.wav')

tts_model.inference(persona_name, text, text_language, output_path)