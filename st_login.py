# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 17:55:34 2019

@author: user
"""

#AUTOMATE CBIT STUDENT INFO LOGIN 
from selenium import webdriver
from time import sleep

roll=input('Enter Roll Number')
#passw=input('Enter password')
roll1=int(roll)
driver=webdriver.Chrome()

driver.get('https://erp.cbit.org.in/')
sleep(1)
username_box = driver.find_element_by_name('txtUserName') 
username_box.send_keys(roll) 
print ("Roll Number entered") 
sleep(1)

login_button=driver.find_element_by_id('btnNext')
login_button.click()
sleep(2)

password_box = driver.find_element_by_name('txtPassword') 
password_box.send_keys(roll1) 
print ("Password entered") 
sleep(1)

login2_button=driver.find_element_by_id('btnSubmit')
login2_button.click()
sleep(1)
