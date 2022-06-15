import pytube
from pytube import Playlist, YouTube

# str(input("Downloading folder: "))
DOWNLOAD_FOLDER = '/Users/averianovaleksei/Desktop/egoroff_channel_2'
# str(input("Youtube video url: "))
playlist_url = 'https://www.youtube.com/watch?v=jtIq61A1LLw&list=PLQAt0m1f9OHvyjJNjZK_unnLwMOXPTja8'
p = Playlist(playlist_url)
i = 0
for url in p.video_urls:
  i += 1
  try:
    yt = YouTube(url)
    print(yt)
  except pytube.exceptions.VideoUnavailable:
    print(f'[INFO] !!! Video {url} is unavaialable, skipping.')
    pass
  else:
    title = yt.title
    kek = yt.streams.get_highest_resolution()
    print(f'[INFO] {i}.Downloading video: {title} ({kek.resolution})')
    kek.download(DOWNLOAD_FOLDER)

print('[INFO] DONE.')
