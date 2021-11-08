# TG Music Player
## Requirements

- `FFmpeg`
- `Python 3.7+`

## Deployment

### Config

Copy `example.env` to `.env` and fill it with your credentials.

### The good way

1. Install Python requirements:
   ```bash
   pip install -U -r requirements.txt
   ```
2. Run:
   ```bash
   python main.py
   ```
### Docker

1. Build:
   ```bash
   docker build -t musicplayer .
   ```
2. Run:
   ```bash
   docker run --env-file .env musicplayer
   ```

### Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/sadew451/TgMusicPlayer)

## Get Your String Session By [Pyrogram](https://t.me/SDStringSessonGenbot)
## Commands

## License

### GNU Affero General Public License v3.0

[Read more](https://t.me/SDBOTs_Inifinity)
