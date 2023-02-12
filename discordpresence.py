import discord


class DiscordStatus:
    def __init__(self, client_id, token):
        self.client_id = client_id
        self.token = token
        self.client = discord.Client()

    async def update(self, song_title, song_artist, song_album):
        await self.client.start(self.token)
        game = discord.Game(name=f"{song_title} by {song_artist}")
        await self.client.change_presence(activity=game)

    def __del__(self):
        self.client.close()