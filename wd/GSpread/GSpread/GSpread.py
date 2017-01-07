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

        
    


def get_all_rows(worksheet):
    '''Input: A worksheet file, Output: A list of lists, each list is a row of data from the sheet
        This function takes in a worksheet and outputs every row as an element of a list. (Each one of these elements is also a list)'''
    res = []
    for i in range(3,len(worksheet.col_values(1)) + 1):
        res.append(worksheet.row_values(i))
    
    return res



def calc_match_reason(listA, listB):
    '''Input: Two lists, A and B, list A is a list of person A's reasons for doing the hackathon, similarly for list B. Output: A score out of 1, of how well the two people match in this category'''
    listC = set(listA + listB)
    total = len(listA) + len(listB)
    if total == 0:
        return 0
    sum = 0.0
    for val in listC:
        if (val in listA) and (val in listB):
            sum += 2
    
    return (sum/total)






def match(email):
    '''(str) -> list of str
    Given the email of the first uer, returns list of possible
    users who match with the given user.

    REQ: email exists
    '''

    
    
    
    
