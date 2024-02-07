from enum import Enum
import utils
import os


root_path = utils.get_root_path()
REF_TEXT = "人间灯火倒映湖中，她的渴望让静水泛起涟漪。若代价只是孤独，那就让这份愿望肆意流淌。流入她所注视的世间，也流入她如湖水般澄澈的目光。"


# 表定义
class PersonaEnum(Enum):
    FU_NING_NA = {
        "name": "芙宁娜",
        "gender": "女",
        "ref_audio": os.path.join(root_path, 'data', 'audio', 'persona', 'fu_ning_na.wav'),
        "ref_text": REF_TEXT,
        "language": "zh",
    }

    NA_XI_TAN = {
        "name": "纳西妲",
        "gender": "女",
        "ref_audio": os.path.join(root_path, 'data', 'audio', 'persona', 'na_xi_tan.wav'),
        "ref_text": REF_TEXT,
        "language": "zh",
    }

    ZHONG_LI = {
        "name": "钟离",
        "gender": "男",
        "ref_audio": os.path.join(root_path, 'data', 'audio', 'persona', 'zhong_li.wav'),
        "ref_text": REF_TEXT,
        "language": "zh",
    }

    NORMAL_MALE = {
        "name": "正常男声",
        "gender": "男",
        "ref_audio": os.path.join(root_path, 'data', 'audio', 'persona', 'normal_male.wav'),
        "ref_text": REF_TEXT,
        "language": "zh",
    }

    NORMAL_FEMALE = {
        "name": "正常女声",
        "gender": "女",
        "ref_audio": os.path.join(root_path, 'data', 'audio', 'persona', 'normal_female.wav'),
        "ref_text": REF_TEXT,
        "language": "zh",
    }


    @staticmethod
    def get_persona_by_name(name):
        for enum in list(PersonaEnum):
            if name == enum.value['name']:
                return enum

    def get_ref_audio(self):
        return self.value["ref_audio"]

    def get_ref_text(self):
        return self.value["ref_text"]

    def get_language(self):
        return self.value["language"]

    def get_name(self):
        return self.value["name"]

    @staticmethod
    def get_name_list():
        name_list = []
        for enum in list(PersonaEnum):
            name_list.append(enum.value["name"])
        return name_list
