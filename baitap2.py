from __future__ import unicode_literals
import youtube_dl
ydl_opts = {}
ketqua = []
# with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#     ydl.download(['https://www.youtube.com/watch?v=n6BwAWiHcSg&t=182s'])

# with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#     ydl.download(['https://www.youtube.com/watch?v=Wv2rLZmbPMA', 'https://www.youtube.com/watch?v=GIDoQsQyS0s'])

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    for item in ['https://www.youtube.com/watch?v=n6BwAWiHcSg&t=182s']:
        ketqua.append(ydl.extract_info(item)) 