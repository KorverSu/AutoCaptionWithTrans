from moviepy.editor import *
from PIL import Image, ImageFont, ImageDraw


def time2sec(t):
    arr = t.split('-> ')
    s1 = arr[0].split(',')
    s2 = arr[1].split(',')
    start = int(s1[0].split('：')[0]) * 3600 + int(s1[0].split('：')[1]) * 60 + int(s1[0].split('：')[2]) + float(
        s1[1]) * 0.001
    end = int(s2[0].split('：')[0]) * 3600 + int(s2[0].split('：')[1]) * 60 + int(s2[0].split('：')[2]) + float(
        s2[1]) * 0.001
    return [start, end]


with open('./srt_file/ca.srt', 'r') as f:
    srt = f.read()
srt_list = srt.split('\n')
sec_index = 1
text_index = 2
sec_list = [[0, 0]]
text_list = ['']
print(srt_list[4])
for i in range(len(srt_list)):
    if i == sec_index:
        sec_index = sec_index + 4
        if sec_list[-1][1] != time2sec(srt_list[i])[0]:
            sec_list.append([sec_list[-1][1], time2sec(srt_list[i])[0]])
            text_list.append('')
        sec_list.append(time2sec(srt_list[i]))
    if i == text_index:
        text_index = text_index + 4
        text_list.append(srt_list[i])

img_empty = Image.new('RGBA', (480, 240))
font = ImageFont.truetype('./font/NotoSansTC-Regular.otf', 20)
video = VideoFileClip("/home/korver/Downloads/c.mp4").resize((480, 240))
video_duration = float(video.duration)
output_list = []

if sec_list[-1][1] != video_duration:
    sec_list.append([sec_list[-1][1], video_duration])
    text_list.append('')


def text_clip(text, name):
    img = img_empty.copy()
    draw = ImageDraw.Draw(img)
    text_width = 21 * len(text)
    draw.text(((480 - text_width) / 2, 200), text, fill=(255, 255, 255), font=font, stroke_width=2, stroke_fill='black')
    img.save(name)


def text_in_video(t, text_img):
    clip = video.subclip(t[0], t[1])
    text = ImageClip(text_img, transparent=True).set_duration(t[1] - t[0])
    combine_clip = CompositeVideoClip([clip, text])
    output_list.append(combine_clip)


for i in range(len(text_list)):
    text_clip(text_list[i], 'srt.png')
    text_in_video(sec_list[i], 'srt.png')

output = concatenate_videoclips(output_list)
output.write_videofile("./output/output.mp4", temp_audiofile="temp-audio.m4a", remove_temp=True, codec="libx264",
                       audio_codec="aac")
print('ok')
