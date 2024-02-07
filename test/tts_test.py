from infer.tts_model import TTSModel
import utils
from infer.persona_enum import PersonaEnum
import os


tts_model = TTSModel()
root_path = utils.get_root_path()

persona_name = PersonaEnum.NORMAL_FEMALE.get_name()
text = '今天天气不错呀，我真的太开心了。'

text_language = 'zh'
output_path = os.path.join(root_path, 'output', 'tts', 'my_file.wav')

tts_model.inference(persona_name, text, text_language, output_path)