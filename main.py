from pypresence import Presence
from yandex_music import Client
from yandex_music.exceptions import UnauthorizedError
import time
import json

with open('config.json') as f:
    data = json.load(f)
token = data['token']
update_delay = data['update_delay']
start_delay = data['start_delay']

def getTrack():
    client = Client(token).init()
    queues = client.queues_list()
    last_queue = client.queue(queues[0].id)
    last_track_id = last_queue.get_current_track()
    last_track = last_track_id.fetch_track()
    tid = last_track_id.track_id
    url = f"https://music.yandex.ru/track/{tid}"
    artists = ', '.join(last_track.artists_name())
    title = last_track.title
    image_link=last_track.get_cover_url(size="200x200")
    duration_min = str((last_track.duration_ms // (1000 * 60)) % 60)
    duration_sec = str((last_track.duration_ms // 1000) % 60)
    return artists, title, url, image_link, duration_min, duration_sec

time.sleep(start_delay)
client_id = '1079901231817965598'
RPC = Presence(client_id)
RPC.connect()

while True:
    try:
        track = getTrack()
        RPC.update(
            buttons=[{"label": "Слушать", "url": track[2]}],
            state="by " + track[0],
            details="" + track[1],
            large_image=track[3],
            large_text=track[1],
            small_image="ym_avatar",
            small_text=track[4] + ":" + track[5]
        )
    except (UnauthorizedError, UnicodeEncodeError):
        print("Неверный токен!")
        print("Введите верный токен в файле config.json!")
        break
    except:
        RPC.update(
            state="Yandex Music RPC by lodo4nik",
            large_image="ym_avatar",
            large_text="Yandex Music",
            buttons=[{"label": "Repository", "url": "https://github.com/lodo4nik"}],
        )
    time.sleep(update_delay)
input("Press enter to close program")