<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/SuperSayf/WITS-Struggles-Discord-Bot">
    <img src="https://cdn.discordapp.com/avatars/856515082955128852/76aca5b5ba04a571c87c9f37ad54256f.png?size=4096" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">WITS Struggles Discord Bot</h3>

  <p align="center">
    A custom struggling bot!
    <br />
    <br />
    <a href="https://github.com/SuperSayf/WITS-Struggles-Discord-Bot/issues">Report Bug</a>
    ·
    <a href="https://github.com/SuperSayf/WITS-Struggles-Discord-Bot/issues">Request Feature</a>
  </p>
</p>

# WITS Struggles Discord Bot

This is a custom bot I coded up for our unofficial university server, which comes
packed with quite a few features


## Features

- Levelling system (Leaderboard/Ranks)
- Intergration with my C# app (Linked via MongoDB)
- Add new rows to a google spreadsheet
- Chat with the bot (Basic AI)
- Music (From YouTube) (Has an equalizer)
- Rock, Paper and Scissors game using discord buttons
## Commands

| Command             | Info                                                                |
| ----------------- | ------------------------------------------------------------------ |
| \|ping | Returns Pong! |
| \|rip | Returns a gravestone image embedded with your pfp |
| \|rip @user | Returns a gravestone image embedded with the mentioned pfp |
| \|rank | Returns your current rank in the server |
|\|leaderboard|Returns a list of the top ranking people in the server|
|\|rps|Play Rock, Paper and Scissors with the bot using buttons|
|\@WITS 2.0 example|The bot will respond to anything you say/ask|
|\|drive 1 2 3|Adds specified information to a linked google spreadsheet|
|\|play|Play a song or playlist|
|\|pause|Pause player|
|\|skip|Skip current song|
|\|connect|Connect to vc|
|\|disconnect|Leave current vc|
|\|seek|Seek player|
|\|nowplaying|Now playing|
|\|queue|See queue|
|\|equalizer|Set equalizer|
|\|volume|Set volume|
|\|resume|Resume player|
|\|loop|Loop song/playlist|


## Screenshots

![Rank](https://i.imgur.com/GMFag8B.png)

![Leaderboard](https://i.imgur.com/DlwDED8.png)

![Music](https://i.imgur.com/YFQaNe0.png)

![AI](https://i.imgur.com/lYwMoyR.png)

  
## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`FIREBASE_API_KEY`

`FIREBASE_AUTH_DOMAIN`

`FIREBASE_DATABASE_URL`

`FIREBASE_PROJECT_ID`

`FIREBASE_STORAGE_BUCKET`

`FIREBASE_MESSAGIN_SEND_ID`

`FIREBASE_APP_ID`

`FIREBASE_MEASUREMENT_ID`

`DISCORD_BOT_TOKEN`

`SPREADSHEET_ID`

`MONGO_TOKEN`

  
## Run Locally

Clone the project

```bash
  git clone https://github.com/SuperSayf/WITS-Struggles-Discord-Bot
```

Go to the project directory

```bash
  cd WITS-Struggles-Discord-Bot
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Add .env file

```bash
  see above section
```

Start the bot

```bash
  python main.py
```

  
## Acknowledgements

 - [Dismusic](https://pypi.org/project/dismusic/)
 - [PRSAW](https://github.com/CodeWithSwastik/prsaw)
  
## Authors

- [@SuperSayf](https://github.com/SuperSayf)

  
## License

[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)

  