import random
import threading
import time
import webview
import songfetcher
import atexit
import discordpresence

url = "https://www.abc.net.au/listenlive/triplej"
client_id = "1074173586262196254"

stop_thread = False
fetcher = songfetcher.SongFetcher(url)


def run_thread():
    global stop_thread, fetcher
    while not stop_thread:
        time.sleep(random.uniform(2, 4))
        title, artist, album = fetcher.get_song_info()
        if title and artist and album:
            print(f"Now playing: {title} by {artist} in release {album}")
            # drpc.update(title, artist, album)
        else:
            print("Unable to retrieve song info")


def stop_thread_on_exit():
    global stop_thread
    stop_thread = True
    fetcher.driver.close()
    fetcher.driver.quit()


if __name__ == "__main__":
    # drpc = discordpresence.DiscordPresence(client_id, token)

    t = threading.Thread(target=run_thread)
    t.daemon = True
    t.start()

    webview.create_window('DiscordRichJPlayer', url, width=360, height=611)
    webview.start()

    atexit.register(stop_thread_on_exit)

    exit(0)
