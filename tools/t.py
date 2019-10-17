from pytube import YouTube

yt = YouTube('https://www.youtube.com/watch?v=ICdndKkwj7s')
yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download('E:\jobhunt\downloads', 'Havana - Camila Cabello ft. Young Thug', "")