#!/usr/bin/env python
# coding: utf-8
# written by: Abhishek
# prerequisites: pandas module and class details file


import os
import pandas as pd
from datetime import date

#to get the current working directory
print("Your current working directory is ", os.getcwd())


#Enter the subject name
subject = input('Enter subject name (Ex: AI,CN,SL,OS,GWCC): ')
print("The subject you entered is ", subject)

#Enter the absentees roll numbers
absentees = list(map(str,input('Enter absentees roll numbers with a comma: ').split(',')))
#print(absentees)

#convert 3digit roll numbers into full format ex: 18R11A0501
ab_roll = []
for i in absentees:
    if i == '5F1':
        temp = '14R11A0' + i
    elif i == '5N4':
        temp = '15R11A0' + i
    elif int(i)<540:
        temp = '19R15A0' + i
    else:
        temp = '18R11A0' + i
    ab_roll.append(temp)
#print(ab_roll)

#reading the input class details file name from the user
input_file = input('Enter the input class details filename with extension (only in csv format): ')

#converting csv file into pandas dataframe
df = pd.read_csv(input_file)


#df.head(10)

#function that marks 'A' for the absentees and 'P' for those not in absentees
def find_values(to_search):
    ret_val = ''
    for val in ab_roll:
        if to_search.find(val) >= 0:
            ret_val += 'A' + ','
    return ret_val[:-1] + '' if len(ret_val) > 1 else ret_val + 'P'

#applying the function in each and every row of the dataframe
df['Attendance'] = df['Roll Number'].apply(find_values)


#getting the today's date and appending the date with subject name to create the output file name
d1 = date.today().strftime("%d-%m-%Y")
file_name = str(d1) + '-' + subject+".csv"
#print(file_name)

#convert the dataframe into the csv file
df.to_csv(file_name)

print('The file is ready, please check for the file '+file_name+ 'in your current working directory')



