'''import os
result = os.system('whisper /home/korver/Downloads/c.mp4 --language Japanese' )
print(result)'''
from googletrans import Translator

translator = Translator()
source_file = open('c.txt', 'r')
source_contents = source_file.read()
result = translator.translate(source_contents, src='ja', dest='zh-CN')
print(result.text)
target_file = open('ca.txt', 'w')
target_file.write(result.text)

# print('ch:', translator.translate('我覺得今天天氣不好', dest='zh-tw').text)


