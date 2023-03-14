'''import os
result = os.system('whisper /home/korver/Downloads/c.mp4 --language Japanese' )
print(result)'''
from googletrans import Translator

translator = Translator(service_urls=['translate.google.cn'])
translator.raise_Exception = True
text = '今日の天気は晴れです'
result = translator.translate(text, src='ja', dest='zh-CN')

print(result.text)



# print('ch:', translator.translate('我覺得今天天氣不好', dest='zh-tw').text)


