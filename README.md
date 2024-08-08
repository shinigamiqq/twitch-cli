# Twitch CLI

## Installation

Twitch CLI requires Python, ffmpeg and PulseAudio to run.
Preferred OS: Linux

Install the dependencies with pip and start app.

```sh
cd twitch-cli
pip install -r requirements.txt
python hyorinmaru.py
```

## Usage

```sh
Enter your token: TYPE_YOUR_TOKEN_HERE
Enter channel name: TYPE_CHANNEL_NAME_HERE
```
## How to get access token
1. You have to go to [Twitch Developers](https://dev.twitch.tv/console/apps), create your application, and save Client ID and Secret key.
2. Then, go to [Twitch Token Generator](https://twitchtokengenerator.com/) and generate your access token. Choose "Bot Chat Token" and enter your Cliend ID and Secret key from Twitch Developers app.
