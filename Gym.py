import gspread
from oauth2client.service_account import ServiceAccountCredentials
gc = gspread.service_account(filename='mycredentials.json')
gsheet = gc.open_by_url("https://docs.google.com/spreadsheets/d/10y7dOAuof2OPSvnezkRrGLOyZ7yUGHuwyUtLFIb8W5E/edit#gid=0")
mydata = gsheet.sheet1.get_all_records()
print(mydata)

wsheet = gsheet.worksheet("Sheet1")

wsheet.update('E2', 'GYM')
wsheet.update('E3', 'GYM')
wsheet.update('E4', 'GYM')
wsheet.update('E5', 'GYM')
wsheet.update('E6', 'GYM')
wsheet.update('E7', 'GYM')



