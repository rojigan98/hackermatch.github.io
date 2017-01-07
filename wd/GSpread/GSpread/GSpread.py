import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']
file_url = 'https://docs.google.com/spreadsheets/d/1pGw_xOqzh0fQ0iv4z2kQDJJDlz5F7zGmKqsonOSQ-Zo/edit?usp=sharing'

users_to_find = 10



def main():
    '''() -> NoneType
    Set up the authorization of the excel sheet (Step 1)
    '''
    # set credentials for opening sheet
    credentials = ServiceAccountCredentials.from_json_keyfile_name('cs.json', scope)
    gc = gspread.authorize(credentials)

    # get the document
    ws = gc.open_by_url(file_url)
    # open the worksheet
    worksheet = ws.get_worksheet(0)

    a_list = worksheet.row_values(2)
    # return the worksheet ready for reading

    
    print(worksheet.row_count)


main()

        
    

    
    
    
def match(email):
    '''(str) -> list of str
    Given the email of the first uer, returns list of possible
    users who match with the given user.

    REQ: email exists
    '''

    
    
    
    