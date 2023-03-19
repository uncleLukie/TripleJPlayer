import random
import time
import atexit
import songfetcher
import discordpresence
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import subprocess


url = "https://www.abc.net.au/listenlive/triplej"
client_id = "1074173586262196254"

fetcher = songfetcher.SongFetcher(url)
drpc = discordpresence.DiscordPresence(client_id)


def stop_thread_on_exit():
    fetcher.driver.close()
    fetcher.driver.quit()
    drpc.client.close()


class browser_window_is_open(object):
    def __call__(self, driver):
        try:
            driver.current_url
            return True
        except:
            return False


if __name__ == "__main__":

    atexit.register(stop_thread_on_exit)

    # Click the play button before entering the loop
    fetcher.press_play_button()

    try:
        while True:
            wait = WebDriverWait(fetcher.driver, 2)
            try:
                if not wait.until(browser_window_is_open()):
                    print("Browser window closed. Exiting...")
                    break
            except TimeoutException:
                print("Browser window closed. Exiting...")
                break

            time.sleep(random.uniform(2, 4))
            title, artist = fetcher.get_song_info()
            if title and artist:
                print(f"Now playing: {title} by {artist}")
                drpc.update_song_activity(title, artist)
            else:
                print("Unable to retrieve song info")
                drpc.update_break_activity(fetcher.get_program_name())
    except KeyboardInterrupt:
        print("Exiting...")
