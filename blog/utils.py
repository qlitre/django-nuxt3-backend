from django.utils.html import *
from django.conf import settings

img_path_relative = '/media/editor'


@keep_lazy_text
def replace_img_relative_path_to_absolute(text):
    """
    テキストの画像相対パスを絶対パスに変えて返す
    """
    words = word_split_re.split(str(text))
    for i, word in enumerate(words):
        if img_path_relative in word:
            str_img_path_absolute = f'{settings.HOST_URL}{img_path_relative}'
            word = word.replace(img_path_relative, str_img_path_absolute)
        words[i] = word
    return ''.join(words)
