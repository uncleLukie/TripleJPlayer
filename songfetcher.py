from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
import time

class SongFetcher:
    def __init__(self, url):
        self.url = url
        self.play_button_clicked = False
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.set_window_size(480, 640)
        self.driver.get(url)

    def get_song_info(self):
        try:
            # Find the parent element with class "Song_nowSongWrapper__BH7vs"
            song_wrapper = self.driver.find_element(By.CLASS_NAME, "Song_nowSongWrapper__BH7vs")

            song_title_element = song_wrapper.find_element(By.CLASS_NAME, "Heading_heading__XLh_j")
            song_title = song_title_element.text

            song_artist_element = song_wrapper.find_element(By.CLASS_NAME, "Song_songArtist__sD5_H")
            song_artist = song_artist_element.text

            # song_album_element = song_wrapper.find_element(By.CLASS_NAME, "Song_songRelease__jYe_C")
            # song_album = song_album_element.text

            # TODO: add image album url--not functional, maybe selenium headless does not retrieve images?
            # song_img_element = song_wrapper.find_element(By.CLASS_NAME, "Image_image__ZCYel Song_songImg__CZsrK")
            # song_img_url = song_img_element.get_attribute("src")

            return song_title, song_artist

        except:
            return None, None

    def get_program_name(self):
        try:
            program_name = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".ProgramInfo_programName__2ceHG"))
            )
            return program_name.text
        except TimeoutException:
            print("Program name not found")
    def press_play_button(self):
        try:
            play_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".jw-icon-playback"))
            )
            if play_button.get_attribute("class").find("jw-icon-play") != -1 and not self.play_button_clicked:
                play_button.click()
                self.play_button_clicked = True
        except TimeoutException:
            print("Play button not found")

    def __del__(self):
        if hasattr(self, "driver"):
            self.driver.close()
