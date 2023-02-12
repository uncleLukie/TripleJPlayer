import webview
import songfetcher

url = "https://www.abc.net.au/listenlive/triplej"

if __name__ == "__main__":
    fetcher = songfetcher.SongFetcher(url)
    fetcher.run()
    webview.create_window('DiscordRichJPlayer', url, width=303, height=611)
    webview.start()
