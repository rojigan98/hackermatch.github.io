# v 2.3

import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']
file_url = 'https://docs.google.com/spreadsheets/d/1GH7WE6mUHlc-wH5BGLVIH8zz3CjnSTf3Mx-MHLzr-Jc/edit?usp=sharing'

users_to_find = 10

# indices of columns in sheet
reason_index = 11
email_index = 3
type_index = 9
team_index = 12

# multipliers
reason_multiplier = 1.5  # multiplier for reason score
type_multiplier = 1 # multiplier for type category score


# set credentials for opening sheet
credentials = ServiceAccountCredentials.from_json_keyfile_name('cs.json', scope)
gc = gspread.authorize(credentials)

# get the document
ws = gc.open_by_url(file_url)
# open the worksheet
worksheet = ws.get_worksheet(0)


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

    return (sum/total) #returns score out of 1


def sorting_by_score(dictionary):
    '''Input: A dictionary of having all people and their associated score, and team.
    The higher the score the better they match with the user. Output: A list sorted with score in descending order'''

    #create a list of tuples
    new_list = []
    for key in dictionary.keys():
        new_list.append((dictionary[key], key))


    new_list.sort()
    new_list.reverse()


    return new_list[0:3]


def call_match(email): #program start
    if(email in worksheet.col_values(email_index)):
        ind = worksheet.col_values(email_index).index(email) + 1
        print('test')
        print(str(ind))
        team_scores = match(ind)
        team = sorting_by_score(team_scores)
        team.append((-1,ind)) # start here.

        #final_team_recommendation(dictionary_with_positions, dictionary, user_data)

        # for each tuple in the list of tuples
        for tuple in team:
            # add team number '1' to sheet
            worksheet.update_cell(tuple[1], team_index,2) # dynamically change team number

        # for debugging
        #input(str(team))
    else:
        print('email does not exist')


def get_all_user_data(worksheet, index):
    '''Input: The excel sheet as worksheet and the index of the user as a string. Output: All data about the user, as a list
        Given the user's index this function will find all info about the user in the worksheet and output it'''
    if index <= len(worksheet.col_values(3)):
        return(worksheet.cell(index,3).value)
    else:
        return 0


def get_positions(worksheet):
    '''Input: The excel sheet as worksheet Output: All emails and the position associated with them in a dictionary'''
    new_dict = {}
    for i in range(1, len(worksheet.col_values(3)) + 1):
        new_dict[worksheet.cell(i,3).value] =  worksheet.cell(i,10).value

    return new_dict


def final_team_recommendation(dictionary_with_positions, dictionary, user_data):
    '''NOT TESTED NOT TESTED Input: First input is a dictionary where the name is the key and the associated score
    is the value. The second input is the position that the user selected on his Google Form. More specifically a
    dictionary where the key is the person's email and the associated value is the score. Output: A final team
    recommendation as a list.'''
    sorted_list = sorting_by_score(dictionary)
    user_position = user_data[9]
    final_team = []
    if user_data[2] != sorted_list[0][1]:
        final_team.append(sorted_list[0][1])
        init_val = 1
    else:
        final_team.append(sorted_list[1][1])
        init_val = 2

    if user_position == dictionary_with_positions(final_team[1]):
        same_modifier = True
    else:
        same_modifier = False

    if same_modifier == True:
        people_found = 2
        for i in range(init_val, len(sorted_list)):
            if dictionary_with_positions[sorted_list[i][1]] != user_position and sorted_list[i][1] != user_data[2]:
                final_team.append(sorted_list[i][1])
                people_found += 1
            if people_found == 4:
                return final_team
        return final_team
    else:
        if sorted_list[init_val][1] != user_data[2]:
            final_team.append(sorted_list[init_val][1])
            start_val = init_val + 1
        else:
            final_team.append(sorted_list[init_val + 1][1])
            start_val = init_val + 2
        excess_position = dictionary_with_positions[final_team[1]]
        for i in range(start_val, len(sorted_list)):
            if dictionary_with_positions[sorted_list[i][1]] != excess_position and sorted_list[i][1] != user_data[2]:
                final_team.append(sorted_list[i][1])
                return final_team
        return final_team

def match(email):
    '''(str) -> list of str
    Given the email of the first user, returns list of possible
    users who match with the given user.

    REQ: email exists
    '''
    # loop through everybody
    for p in range (2, len(worksheet.col_values(3)) + 1):
        # if not in team (value is 0)
        if int(worksheet.cell(p, 12).value) == 0 :
            # row index of the checking user
            # user_ind = worksheet.col_values(email_index).index(email) + 1
            user_ind = p

            # dictionary for storing email and score
            user_score = {}

            # list of reasons for checking user
            c_user_row = worksheet.row_values(user_ind)
            c_user_list = c_user_row[reason_index-1].split(',') # list of reasons

            c_user_list_A = [c_user_row[type_index-1]] # list of type

            # loop through each row, excluding the row of user
            for i in range(2, len(worksheet.col_values(3)) + 1):
                # if user is not checking user
                if i != user_ind and int(worksheet.cell(i, 12).value) == 0:
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

                    user_score[i] = reason_score + type_score

            print('passed')
            # user_score is dictionary containing scores.
            # calculate interest score

            # return the dictionary matching p_email to score
            return user_score

#for t in range((len(worksheet.col_values(3)))//4):
 #   pass

# get team

if __name__ == "__main__":
    call_match("jks@yahoo.ca")
