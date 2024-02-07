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
text2 = """
1.毕生之研的品牌定位。毕生之研是上海科黛生物科技有限公司旗下的护肤品牌，成立于2016年，以实验室20余年生物科研经验为基础，坚持使用高效的浓度、安全的成分和科学的配方，致力于提供进阶护肤方案。
2.毕生之研的产品特色。毕生之研的产品特色包括注重公开透明的展现，提高护肤行业的透明度，以及使用高效的浓度、安全的成分和科学的配方。
3.毕生之研的抗衰产品成分。毕生之研的抗衰产品添加了南非凤凰草、DPHP水润肌肤淡唇纹、B5泛醇、柑橘果提取物、油橄榄叶提取物、VC-IP等成分，具有抗衰作用。
"""
# 你们害死我儿子了！快点出来你这个群主！再这样我去报警了啊！
# 我跟你们说你们这一帮人啊，一天到晚啊，
# 搞这些什么游戏啊，动漫啊，会害死你们的，你们没有前途我跟你说。
# 你们这九百多个人，好好学习不好吗？
# 一天到晚在上网。有什么意思啊？麻烦你重视一下你们的生活的目标啊？
# 有一点学习目标行不行？一天到晚上网是不是人啊？

text_language = 'zh'
output_path = os.path.join(root_path, 'output', 'tts', 'my_file.wav')

tts_model.inference(persona_name, text, text_language, output_path)