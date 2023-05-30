from enum import Enum

class languages(Enum):
    colors = {
    'Eng':'color', 'Uzb':'ranglar', 'Rus':'sivet'
    }
    clothes = {
    'Eng':'clothes', 'Uzb':'kiyim', 'Rus':'odejda'
    }
choose_lang = input("Tilni tanlang: ").capitalize
colors = input("Ranglarni kiriting: ")

print(languages[colors].value[choose_lang])