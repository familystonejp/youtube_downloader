from yt_dlp import YoutubeDL
import keyboard


Ip = input('ダウンロード先のアドレスを入力してEnterを押してください:')
Pass = input('passwordを入力してEnterを押してください。必要なければそのままEnterを押してください:')
yt_opts = YoutubeDL({
    'format': 'mp4',
    'videopassword': Pass
    })
yt_opts.download(Ip)