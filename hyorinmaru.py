import asyncio
from twitchio.ext import commands
import yt_dlp
import subprocess


# Twitch parameters
TWITCH_TOKEN = input('Enter your token: ')
TWITCH_CHANNEL = input("Enter channel name: ")

# Class Twitch interaction
class TwitchBot(commands.Bot):

    def __init__(self):
        super().__init__(token=TWITCH_TOKEN, prefix='', initial_channels=[TWITCH_CHANNEL])
        self.chat_text = ''
        

    async def event_ready(self):
        print(f'Logged in as {self.nick}. Channel: {TWITCH_CHANNEL}')
        await event_play()

    async def event_message(self, message):
        print(f"{message.author.name}: {message.content}")
        self.chat_text += message.author.name + ': ' + message.content + '\n'
        await self.handle_commands(message)


# Play audio function
async def event_play():
        url = f"https://www.twitch.tv/{TWITCH_CHANNEL}"
        ydl_opts = {
            'format': 'bestaudio/best',
            'noplaylist': True,
            'quiet': True,
            'extract_flat': True,
            'dump_single_json': True,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url=url, download=False)
            if 'entries' in info:
                info = info['entries'][0]
        
            audio_url = info['url']

            ffmpeg_process = subprocess.Popen([
                'ffmpeg', '-i', audio_url, '-loglevel', 'error', '-f', 'pulse', 'default'
            ])

# Launch
async def main():
    bot = TwitchBot()
    await bot.start()

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except Exception as e:
        print(f"Error: {e}")
