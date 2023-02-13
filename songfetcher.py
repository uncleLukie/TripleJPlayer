from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class SongFetcher:
    def __init__(self, url):
        # Create options for running in headless mode
        options = Options()
        options.add_argument("--headless")

        # Create a new instance of the Chrome driver
        self.driver = webdriver.Chrome(options=options)

        self.url = url
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

            # song_album_element = song_wrapper.find_element(By.CLASS_NAME, "Song_songRelease__jYe_C")
            # song_album = song_album_element.text

            # TODO: add image album url--not functional, maybe selenium headless does not retrieve images?
            # song_img_element = song_wrapper.find_element(By.CLASS_NAME, "Image_image__ZCYel Song_songImg__CZsrK")
            # song_img_url = song_img_element.get_attribute("src")

            return song_title, song_artist

        except:
            return None, None

    def get_break_info(self):
        heading = self.driver.find_element(By.CLASS_NAME, "Heading_heading__XLh_j")
        return heading

    def __del__(self):
        self.driver.close()
        self.driver.quit()
