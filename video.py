import os
from googletrans import Translator

"""
result = os.system('whisper ~/Downloads/ee.mp4 --language Japanese --task translate --output_dir "./srt_file"')
translator = Translator()

with open('./srt_file/ee.srt', 'r') as sf, open('./srt_file/eea.srt', 'w') as tf:
    source_contents = sf.read()
    target_contents = translator.translate(source_contents, src='en', dest='zh-TW')
    tf.write(str(target_contents.text))

print("translate over")
"""


def get_srt_file(input_mp4: str, language: str, output_dir: str):
    command = 'whisper {} --language {} --task translate --output_dir {}'.format(input_mp4, language, output_dir)
    os.system(command)


def trans_to_chinese(raw_srt: str, ans_art: str):
    translator = Translator()
    sf_location = './srt_file/{}'.format(raw_srt)
    tf_location = './srt_file/{}'.format(ans_art)
    with open(sf_location, 'r') as sf, open(tf_location, 'w') as tf:
        source_contents = sf.read()
        target_contents = translator.translate(source_contents, src='en', dest='zh-TW')
        tf.write(str(target_contents.text))
    print("translate over")

