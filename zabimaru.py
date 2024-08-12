import asyncio
from twitchio.ext import commands
import yt_dlp
import subprocess


# Twitch parameters
TWITCH_TOKEN = input("Enter your token: ")
TWITCH_CHANNEL = input("Enter channel name: ")

# Class Twitch interaction
class TwitchBot(commands.Bot):

    def __init__(self):
        super().__init__(token=TWITCH_TOKEN, prefix='!', initial_channels=[TWITCH_CHANNEL])
        self.chat_text = ''
        

    async def event_ready(self):
        print(f'Logged in as {self.nick}. Channel: {TWITCH_CHANNEL}')

    async def event_message(self, message):
        await self.handle_commands(message=message)

    @commands.command(name='play')
    async def search_music(self, ctx: commands.Context):
        query = ctx.message.content[len('play! '):].strip()
        print(query)
        if query:
            await event_play_music(query)
            await ctx.send(f"Playing: {query}.")
        else:
            await ctx.send(f"Please send another song.")


# Play music from Youtube
async def event_play_music(*urlq):
    query = ''.join(*urlq)
    ydl_opts = {
            'format': 'bestaudio/best',
            'noplaylist': True,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '96',
            }],
            'quiet': True,
            'default_search': 'ytsearch'
        }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(query, download=False)
        print(info)
        if 'entries' in info:
            info = info['entries'][0]
        print(info)
        audio_url = info['url']
        print(audio_url)

    # Запуск ffmpeg для воспроизведения аудио
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
