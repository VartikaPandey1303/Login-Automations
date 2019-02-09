# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 17:22:03 2019

@author: user
"""
#FACEBOOK AUTOMATION
from selenium import webdriver
from time import sleep

#enter ID and password
userid=input("Enter email ID ")
userpass=input("Enter Password ")

#webdriver
mydriver=webdriver.Chrome()
mydriver.get('https://www.facebook.com/') 
sleep(1)

#Username provided
my_id=mydriver.find_element_by_id('email')
my_id.send_keys(userid)
sleep(1)

#Password provided
my_pass=mydriver.find_element_by_id('pass')
my_pass.send_keys(userpass)

#Login Button Pressed
login_button=mydriver.find_element_by_id('loginbutton')
login_button.click()

print('FB opened and login done')
#Close Window
print('Press 1 to quit')
c=int(input())
if c==1:
    mydriver.quit()
    print('window closed')
