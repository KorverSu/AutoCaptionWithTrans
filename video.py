import os
from googletrans import Translator


def get_srt_file(input_mp4: str, language: str, output_dir: str):
    command = 'whisper {} --language {} --task translate --output_dir {}'.format(input_mp4, language, output_dir)
    os.system(command)


def trans_to_chinese(raw_srt: str):
    translator = Translator()
    ans_srt = raw_srt.split('.')[0] + 'a.srt'
    sf_location = './srt_file/{}'.format(raw_srt)
    tf_location = './srt_file/{}'.format(ans_srt)
    with open(sf_location, 'r') as sf, open(tf_location, 'w') as tf:
        source_contents = sf.read()
        target_contents = translator.translate(source_contents, src='en', dest='zh-TW')
        tf.write(str(target_contents.text))
    return tf_location
