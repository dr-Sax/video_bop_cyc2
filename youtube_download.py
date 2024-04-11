import yt_dlp
from yt_dlp.utils import download_range_func

from astradb_2 import *

def yt_vid_downloader(st, et, name, link, scene):
    start_time = st[0] * 60 + st[1]
    end_time = et[0] * 60 + et[1] 

    yt_opts = {
        'verbose': True,
        'download_ranges': download_range_func(None, [(start_time, end_time)]),
        'force_keyframes_at_cuts': True,
        'format': 'best[ext=mp4]',
        'outtmpl': f'C:/Users/nicor/OneDrive/Documents/Code/video-bop/video_dwnlds/{HAIKU}/{NAME}.mp4'
    }

    with yt_dlp.YoutubeDL(yt_opts) as ydl:
        ydl.download(link)

def download_blows():
        haikus = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8']
        session = open_session()
        keyspace = "blows"
        vals_list = []
        for a in haikus:
            vals = read_from_table(session, keyspace, a)
            vals_list.append(vals)

        close_session(session)

        print(vals_list)

download_blows()

# ST = [8, 45]
# ET = [9, 2]
# NAME = 'not a flower'
# LINK = 'https://www.youtube.com/watch?v=UyktuCjOisc'
# HAIKU = '16'

# yt_vid_downloader(ST, ET, NAME, LINK, HAIKU)


