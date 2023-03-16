import os
from googletrans import Translator
result = os.system('whisper ~/Downloads/c.mp4 --language Japanese --task translate --output_dir "./srt_file"')
translator = Translator()
try:
    with open('./srt_file/c.srt', 'r') as sf, open('./srt_file/ca.srt', 'w') as tf:
        source_contents = sf.read()
        target_contents = translator.translate(source_contents, src='en', dest='zh-TW')
        tf.write(str(target_contents.text))
except Exception as e:
    print("翻譯過程中出現了問題:", e)


