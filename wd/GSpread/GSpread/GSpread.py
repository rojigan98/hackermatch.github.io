# v 0.1

import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']
file_url = 'https://docs.google.com/spreadsheets/d/1GH7WE6mUHlc-wH5BGLVIH8zz3CjnSTf3Mx-MHLzr-Jc/edit?usp=sharing'

users_to_find = 10

# indices of columns in sheet
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



def get_all_rows(worksheet):
    '''Input: A worksheet file, Output: A list of lists, each list is a row of data from the sheet
        This function takes in a worksheet and outputs every row as an element of a list. (Each one of these elements is also a list)'''
    res = []
    for i in range(3,len(worksheet.col_values(1)) + 1):
        res.append(worksheet.row_values(i))
    
    return res


def calc_match(listA, listB):
    '''Input: Two lists, A and B, list A is a list of person A's reasons for doing the hackathon,
    similarly for list B. Output: A score out of 1, of how well the two people match in this category'''
    listC = set(listA + listB)
    total = len(listA) + len(listB)
    if total == 0:
        return 0
    sum = 0
    for val in listC:
        if (val in listA) and (val in listB):
            sum += 2

    return (sum/total)


def sorting_by_score(dictionary):
    '''Input: A dictionary of having all people and their associated score, and team. 
    The higher the score the better they match with the user. Output: A list sorted with score in descending order'''
    
    #create a list of tuples
    new_list = []
    for key in dictionary.keys():
        new_list.append((dictionary[key], key))
    
    
    new_list.sort()
    new_list.reverse()

    return new_list


def get_all_user_data(worksheet, email):
    '''Input: The excel sheet as worksheet and the email of the user as a string. Output: All data about the user, as a list
        Given the user's email this function will find all info about the user in the worksheet and output it'''
    for i in range (1, len(worksheet.col_values(3)) + 1):
        if worksheet.cell(i,3).value == email:
            return worksheet.row_values(i)
    return 0


def get_positions(worksheet):
    '''Input: The excel sheet as worksheet Output: All emails and the position associated with them in a dictionary'''
    new_dict = {}
    for i in range(1, len(worksheet.col_values(3)) + 1):
        new_dict[worksheet.cell(i,3).value] =  worksheet.cell(i,10).value
    
    return new_dict

def final_team_recommendation(dictionary_with_positions, dictionary, user_data):
    ''' NOT TESTED NOT TESTED Input: First input is a dictionary where the name is the key and the associated score is the value. The second input is the position that the user selected on his Google Form. More specifically a dictionary where the key is the person's email and the associated value is the score. Output: A final team recommendation as a list.'''
    sorted_list = sorting_by_score(dictionary)
    user_position = user_data[9]
    final_team = [sorted_list[0][1]]
    if user_position == final_team:
        same_modifier = True
    else:
        same_modifier = False
    
    if same_modifier == True:
        people_found = 2
        for i in range(2, len(sorted_list)):
            if dictionary_with_positions[sorted_list[i][1]] != user_position:
                final_team.append(sorted_list[i][1])
                people_found += 1
            if people_found == 4:
                return final_team
        return final_team
    else:
        final_team.append(sorted_list[2][1])
        excess_position = dictionary_with_positions[sorted_list[2][1]]
        for i in range(3, len(sorted_list)):
            if dictionary_with_positions[sorted_list[i][1]] != excess_position:
                final_team.append(sorted_list[i][1])
                return final_team
        return final_team




def match(email):
    '''(str) -> list of str
    Given the email of the first uer, returns list of possible
    users who match with the given user.

    REQ: email exists
    '''

    # row index of the checking user
    user_ind = worksheet.col_values(email_index).index(email) + 1


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
            reason_score = 0
            type_score = 0

            # input(str(c_user_list) + ' and p is: '+ str(p_user_list))
    
            reason_score = calc_match(c_user_list,p_user_list) * reason_multiplier;
            type_score = calc_match(c_user_list_A,p_user_list_A) * type_multiplier

            user_score[user_row[email_index-1]] = reason_score + type_score

    # user_score is dictionary containing scores. 
    # calculate interest score

    # return the dictionary matching p_email to sccore
    return user_score
    

    


    
    
# get matches
scores = match('sadiwali@hotmail.com')
# filter scores , create group
