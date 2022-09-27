from yt_dlp import YoutubeDL
import keyboard


Ip = input('ダウンロード先のアドレスを入力してEnterを押してください:')
yt_opts = YoutubeDL({'format': 'mp4'})
yt_opts.download(Ip)
