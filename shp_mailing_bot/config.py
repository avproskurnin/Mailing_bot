import os

# Environment config
CNC_SPREADSHEET_ID = os.getenv('CNC_SPREADSHEET_ID')
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

# Google Sheets API config
GOOGLE_SHEET_API_AUTH_SCOPE_URL = 'https://www.googleapis.com/auth/spreadsheets.readonly'
CNC_SPREADSHEET_CELLS_RANGE = 'Data!A1:А13'

# Bot config
INITIAL_GREETING_MESSAGE = '''
👋🏻 Привет, преподаватель Школы программистов!
*Этот бот был разработан, чтобы оперативно доставлять всю важную информацию лично тебе!*
Совсем скоро сюда начнут приходить первые сообщения – не пропусти их 😉
'''

SUPER_ADMINS = {"Катерина мать ботов": 693767247,
                "Лена": 362305244,
                "Антон": 147216337}