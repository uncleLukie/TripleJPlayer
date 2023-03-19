from pypresence import Presence


class DiscordPresence:

    def __init__(self, client_id):
        self.client_id = client_id
        self.client = Presence(client_id, pipe=0)
        self.client.connect()

    def update_song_activity(self, song_title, song_artist):
        details = f"{song_title}"
        state = f"by {song_artist}"
        self.client.update(details=details,
                           state=state,
                           large_image="app_icon",
                           buttons=[{"label": "Download on GitHub", "url": "https://github.com/unclelukie/TripleJPlayer"}]
                           )

    def update_break_activity(self, heading):
        details = f"{heading}"
        state = f"on the Js"
        self.client.update(details=details,
                           state=state,
                           large_image="app_icon",
                           buttons=[{"label": "Download on GitHub", "url": "https://github.com/unclelukie/TripleJPlayer"}]
                           )

    def __del__(self):
        self.client.close()
