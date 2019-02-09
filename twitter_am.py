# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 18:47:33 2019

@author: user
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 17:22:03 2019

@author: user
"""
#TWITTER AUTOMATION
from selenium import webdriver
from time import sleep

#enter ID and password
userid=input("Enter email ID ")
userpass=input("Enter Password ")

#webdriver
mydriver=webdriver.Chrome()
mydriver.get('https://twitter.com/login') 
sleep(1)

#Username provided
my_id=mydriver.find_element_by_class_name("js-username-field") 
my_id.send_keys(userid)
sleep(1)

#Password provided
my_pass=mydriver.find_element_by_class_name('js-password-field') 
my_pass.send_keys(userpass)

#Login Button Pressed
login_button=mydriver.find_element_by_css_selector('button.submit.EdgeButton.EdgeButton--primary.EdgeButtom--medium')
login_button.submit()

print('Twitter opened and login done')
#Close Window
print('Press 1 to quit')
c=int(input())
if c==1:
    mydriver.quit()
    print('window closed')
