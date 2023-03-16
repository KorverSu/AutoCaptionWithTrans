import os
from pytube import YouTube
try:
    yt = YouTube('https://www.youtube.com/watch?v=89dGC8de0CA&list=LL&index=21&ab_channel=AerosmithVEVO')
    print('download...')
    song_name = yt.title+'.mp4'
    yt.streams.filter().get_highest_resolution().download(output_path='./output', filename=song_name)
except Exception as e:
    print('下載mp4期間出了一些問題: ', e)
