from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import random


class SongFetcher:
    def __init__(self, url):
        # Create options for running in headless mode
        options = Options()
        options.add_argument("--headless")

        # Create a new instance of the Chrome driver
        self.driver = webdriver.Chrome(options=options)

        # Navigate to a web page
        self.driver.get(url)

    def get_song_info(self):
        try:
            # Find the parent element with class "Song_nowSongWrapper__BH7vs"
            song_wrapper = self.driver.find_element(By.CLASS_NAME, "Song_nowSongWrapper__BH7vs")

            song_title_element = song_wrapper.find_element(By.CLASS_NAME, "Heading_heading__XLh_j")
            song_title = song_title_element.text

            song_artist_element = song_wrapper.find_element(By.CLASS_NAME, "Song_songArtist__sD5_H")
            song_artist = song_artist_element.text

            song_album_element = song_wrapper.find_element(By.CLASS_NAME, "Song_songRelease__jYe_C")
            song_album = song_album_element.text

            return song_title, song_artist, song_album

        except:
            return None, None, None

    def run(self):
        while True:
            time.sleep(random.uniform(5, 8))
            title, artist, album = self.get_song_info()
            if title and artist and album:
                print(f"Now playing: {title} by {artist} in release {album}")
            else:
                print("Unable to retrieve song info")

    def __del__(self):
        self.driver.quit()