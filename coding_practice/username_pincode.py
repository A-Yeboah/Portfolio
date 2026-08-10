#!/usr/bin/env python3
#Check a user name and pin code to grant access

database=[
    ['Ebenezer', '1234'],
    ['Ampiaw', '1235'],
    ['Yeboah', '1236'],
    ['Kwesi', '1237'],
    ['Korkor', '1238']
    ]
username = input('Enter username: ')
pin_code= input('Enter correct Pin code: ')

if [username, pin_code] in database: print('Access granted')
else: print('Denied access. Username or Pin code is wrong or does not exist!')
