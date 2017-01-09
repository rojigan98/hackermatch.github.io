# v 2.4

import gspread
import math
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']
file_url = 'https://docs.google.com/spreadsheets/d/1GH7WE6mUHlc-wH5BGLVIH8zz3CjnSTf3Mx-MHLzr-Jc/edit?usp=sharing'

# indices of columns in sheet
reason_index = 10
email_index = 2
type_index = 8
team_index = 11
position_index = 9


# multipliers
reason_multiplier = 1.5     # multiplier for reason score
type_multiplier = 1 # multiplier for type category score

# set credentials for opening sheet
credentials = ServiceAccountCredentials.from_json_keyfile_name('cs.json', scope)
gc = gspread.authorize(credentials)





def find_team(worksheet, ind,curr_team,num_parts, worksheet_raw):

    potential_team_list = []

    # (list of str, str)
    my_matches = (worksheet[ind][reason_index].split(','), worksheet[ind][type_index])
    # -> (int, int)
    my_matches = (calc_match(my_matches[0]), c_interests(my_matches[1]))

    # for every other user
    for i in range(num_parts):
        # if user is not me
        if i != ind and int(worksheet[i][team_index]) == 0 :
            # compute tuple of potential interests
            # (list of str, str)
            po_matches = (worksheet[i][reason_index].split(','), worksheet[i][type_index])
            # -> (int, int)
            po_matches = (calc_match(po_matches[0]), c_interests(po_matches[1]))
            # compare and store score
            potential_team_list.append((get_score(my_matches,po_matches), i+2))

    # filter top 3
    potential_team_list.sort()
    potential_team_list = potential_team_list[0:3]
    potential_team_list.append((-1,ind+2))

    # update your team to google sheets
    #print(str(potential_team_list))
    for i in range(4):
        print(str(i) + ' is i and ' + str(potential_team_list[i][1]) + ' and team index is ' + str(team_index + 1))
        worksheet_raw.update_cell(potential_team_list[i][1], team_index+1, str(curr_team)) # dynamically chnage team number
        # write to list
        worksheet[potential_team_list[i][1]-2][team_index] = curr_team
            
def calc_match(listA):
    '''Input: Two lists, A and B, list A is a list of person A's reasons for doing the hackathon,
    similarly for list B. Output: A score out of 1, of how well the two people match in this category'''
    sum = 0

    for item in listA:
        if item.strip() == 'Learning':
            sum += 1
        elif item.strip() == 'Networking':
            sum+= 2
        elif item.strip() == 'Meeting employers':
            sum+= 3
        elif item.strip() == 'Improving teamwork':
            sum+= 4
        elif item.strip() == 'Collecting stickers':
            sum+= 5
        elif item.strip() == 'Winning':
            sum+= 6
        else:   
            sum = 0

    return sum
            
def get_score(t_Aa,t_Bb):

    # find distance
    row_by_score = 0

    # look through the 3 reason(s), find shortest distance between vectors
    row_by_score += math.sqrt((t_Aa[0]-t_Bb[0])**2+(t_Aa[1]-t_Bb[1])**2)

    return row_by_score

def c_interests(t_A_in):
    t_A = 0    

    if t_A_in.strip() == 'Mobile apps':
        t_A = 1
    if t_A_in.strip() == 'Hardware':
        t_A = 2
    if t_A_in.strip() == 'Website':
        t_A = 3
    if t_A_in.strip() == 'Gaming':
        t_A = 4
    return t_A
  
    
def deb_print(str, worksheet_raw):
    worksheet_raw.update_acell('M1', str)


# run this mainly, finds team for everybody automatically
def start():


    # get the document
    ws = gc.open_by_url(file_url)
    # worksheet is data type
    worksheet_raw = ws.get_worksheet(0)

    # open the worksheet in a 2D list
    worksheet = []
    for i in range(2, worksheet_raw.row_count + 1):
        worksheet.append(worksheet_raw.row_values(i))
    # write total entries in M2

    current_team = 1

    #print('starts')
    # convert empty to zero:
    for i in range(len(worksheet)):
#        worksheet_raw.update_cell(i,team_index+1,0)
        worksheet[i][team_index] = 0
        

    if(len(worksheet) % 4 != 0):
        deb_print('Need ' + str(4-len(worksheet) % 4) + ' participants before matching', worksheet_raw)
    else:
        deb_print('',worksheet_raw)
    
    num_parts = 0
    # only consider groups of 4
    num_parts = len(worksheet) - len(worksheet) % 4
    worksheet_raw.update_acell('M2', str(num_parts))

    for i in range(num_parts):
        # if not in team
        if int(worksheet[i][team_index]) == 0:
            # find team
            find_team(worksheet, i, current_team, num_parts, worksheet_raw)
            current_team +=1


        

def infinite():
    '''A function that runs the function start() every 15 seconds'''
    
    import time
    
    
    init_time = time.time()
    
    #runs an infinite loop to continuously refresh server for demo purposes
    while True:
        if (time.time() - init_time >= 1):
            init_time = time.time()
            start()
            print('started')



# start loop
infinite()
