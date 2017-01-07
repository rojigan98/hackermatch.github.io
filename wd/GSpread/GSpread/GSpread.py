import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']
file_url = 'https://docs.google.com/spreadsheets/d/1pGw_xOqzh0fQ0iv4z2kQDJJDlz5F7zGmKqsonOSQ-Zo/edit?usp=sharing'

users_to_find = 10

# factor indexes
reason_index = 8
email_index = 10
type_index = 6

# multipliers
reason_multiplier = 1.5     # multiplier for reason score
type_multiplier = 1 # multiplier for type category score


# set credentials for opening sheet
credentials = ServiceAccountCredentials.from_json_keyfile_name('cs.json', scope)
gc = gspread.authorize(credentials)

# get the document
ws = gc.open_by_url(file_url)
# open the worksheet
worksheet = ws.get_worksheet(0)

# get matches
match('sadiw@gmail.com')




    
    
   
def get_all_rows(worksheet):
    '''Input: A worksheet file, Output: A list of lists, each list is a row of data from the sheet
        This function takes in a worksheet and outputs every row as an element of a list. (Each one of these elements is also a list)'''
    res = []
    for i in range(3,len(worksheet.col_values(1)) + 1):
        res.append(worksheet.row_values(i))
    
    return res









    
def match(email):
    '''(str) -> list of str
    Given the email of the first uer, returns list of possible
    users who match with the given user.

    REQ: email exists
    '''

    # row index of the checking user
    user_ind = worksheet.col_values(reason_index).index(email)
    
    # entries not zero based
    num_entries = worksheet.row_count+1

    # dictionary for storing email and score
    user_score = {}

    # list of reasons for checking user
    c_user_row = worksheet.row_values(user_ind)
    c_user_list = c_user_row[reason_index-1].split(',') # list of reasons
    c_user_list_A = [c_user_row[type_index-1]] # list of type

    # loop through each row, excluding the row of user
    for i in range(2, num_entries):
        # if user is not checking user
        if i != user_ind:
            # entire row represents the potential user
            user_row = worksheet.row_values(i)

            # list of reasons for potential user
            p_user_list = user_row[reason_index-1].split(',') # list of reason for potential user
            p_user_list_A = [user_row[type_index-1]] # list of type for potential user
            # add email of potential user and score
            user_score[user_row[email_index-1]] = calc_match(c_user_list,p_user_list) * reason_multiplierd + calc_match(c_user_list_A,p_user_list_A) * type_multiplier

    # user_score is dictionary containing scores. 
    # calculate interest score

    print(str(user_score))

    

    









    
    
    
