# Triple J Player

A discord rich Triple J radio player.

Uses Python 3.11, Selenium, webview, and pypresence

## How it works
![example](https://user-images.githubusercontent.com/22523084/218603388-8c67ef48-34ea-44c1-81b8-66a2b5244f07.png)

- SongFetcher in songfetcher.py uses selenium and chromedriver in headless mode to scrape information from the triple j website
- DiscordPresence in discordpresence.py uses pypresence to update the discord client with information passed to it
- start.py imports, initialises the other classes, runs a threaded loop to fetch song information and update discord status, and uses webview to run the GUI

## How to run it
- Clone the repo
- pip install -r requirements.txt
- python start.py

## Want to contribute?
Check out the issues, I've listed some of the work that needs to be done <3
I also need people to test it out and report bugs, of course.
