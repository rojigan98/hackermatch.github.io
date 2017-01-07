import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']


credentials = ServiceAccountCredentials.from_json_keyfile_name('cs.json', scope)
gc = gspread.authorize(credentials)

ws = gc.open_by_url('https://docs.google.com/spreadsheets/d/1do7z8J9mDvTui6i3oQJzRt91oKzXMYNNiigdYWgThrU/edit?usp=sharing')

worksheet = ws.get_worksheet(0)

val = worksheet.cell(1, 2).value
print(val)

print('reaches end')