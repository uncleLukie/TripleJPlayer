import random
import threading
import time
import webview
import atexit
import songfetcher
import discordpresence

url = "https://www.abc.net.au/listenlive/triplej"
client_id = "1074173586262196254"

stop_thread = False
fetcher = songfetcher.SongFetcher(url)
drpc = discordpresence.DiscordPresence(client_id)


def run_thread():
    global stop_thread, fetcher, drpc
    while not stop_thread:
        time.sleep(random.uniform(2, 4))
        title, artist = fetcher.get_song_info()
        if title and artist:
            print(f"Now playing: {title} by {artist}")
            drpc.update_song_activity(title, artist)
        else:
            #heading = fetcher.get_break_info()
            #drpc.update_break_activity(heading)
            print("Unable to retrieve song info")


def stop_thread_on_exit():
    global stop_thread
    stop_thread = True
    fetcher.driver.close()
    fetcher.driver.quit()
    drpc.client.close()


if __name__ == "__main__":

    t = threading.Thread(target=run_thread)
    t.daemon = True
    t.start()

    webview.create_window('Triple J Player', url, width=360, height=611)
    webview.start()

    atexit.register(stop_thread_on_exit)

    exit(0)
