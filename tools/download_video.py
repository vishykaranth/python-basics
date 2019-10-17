import pytube
video_url = 'https://www.youtube.com/watch?v=IvBd0kbGItE' # copy and paste url
youtube = pytube.YouTube(video_url)
# video = youtube.streams.first()
myVideoStream = youtube.streams
# webmStreams = myVideoStream.filter(file_extension = "mp4")
list = myVideoStream.filter(resolution='720p').filter(mime_type='video/mp4').all()
# print(webmStreams)
# webmStreams.last().download('E:\jobhunt\downloads', 'dance01', "")
list[-1].download('E:\jobhunt\downloads', 'dance01', "")
# video.download('E:\jobhunt\downloads', 'test.mp4', "") # path, where to video download.