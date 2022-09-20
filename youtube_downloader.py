from yt_dlp import YoutubeDL
import keyboard


Ip = input('youtubeのアドレスを入力してください:')
yt_opts = YoutubeDL({'format': 'mp4'})
yt_opts.download(Ip)
