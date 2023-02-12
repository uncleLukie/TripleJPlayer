import webview
import songfetcher

url = "https://www.abc.net.au/listenlive/triplej"

if __name__ == "__main__":
    webview.create_window('DiscordRichJPlayer', url, width=303, height=611)
    webview.start()
    fetcher = songfetcher.SongFetcher(url)
    fetcher.run()