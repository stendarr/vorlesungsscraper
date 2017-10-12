#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Make sure you have `requests` and `bs4` installed -> pip install requests/bs4

Check README.md and LICENSE before using this program.

Checklist | Lectures
----------|----------
AlgDat    |    n/a
----------|----------
DisMat    |    n/a  
----------|----------
EProg     |     y   
----------|----------
LinAlg    |     y   

'''

import urllib.request, urllib.parse, os, sys, http.client
from urllib.request import Request, urlopen
from html.parser import *
from sys import platform
try:
    import requests
except:
    print('Installing `requests` is NOT optional, m8')
    sys.exit(0)
try:
    from bs4 import BeautifulSoup, SoupStrainer
except:
    print('Installing `BeautifulSoup` is NOT optional, m8')
    sys.exit(0)

user_agent = 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
link_counter = 0
download_counter = 0
link_list = []
filename_list = []

#Generate folders if nonexistent
directories = ["Vorlesungen/EProg", "Vorlesungen/LineareAlgebra"]

for i in directories:
    if not os.path.isdir(i):
        os.makedirs(i)
        print("This folder was generated:   ",i) 
    else:
        print("This folder already exists:  ",i)
print("\n\n")


#START Einführung in die Programmierung
#Check main site for all available lectures
print("Eprog")
eprog_link = 'http://www.video.ethz.ch/lectures/d-infk/2017/autumn/252-0027-00L.html'
eprog_link_dict = {}
eprog_date_dict = {}
eprog_counter = 0

request = Request(eprog_link, headers={'User-Agent' : user_agent})
soup = BeautifulSoup(urllib.request.urlopen(request), 'html.parser')

for div in soup.find_all('div', class_='newsListBox'):
    link = 'http://www.video.ethz.ch'+str(div).partition('\n<a href="')[-1].rpartition('"><h2>Einf')[0]
    date = str(div).partition('<p>')[-1].strip().rpartition(', Gross Thomas')[0]
    eprog_link_dict[eprog_counter] = link
    eprog_date_dict[eprog_counter] = date
    print('['+str(eprog_counter)+']',date,'\n',link,'\n')
    eprog_counter += 1  
    
try:
    choice = [int(x) for x in input("Enter numbers of lectures, separated by space (e.g. 0 3 5 7)\nJust press enter if you don't want to download anything\n").split()]
except:
    print("You done fucked up")
    sys.exit()
    
print('')

#Get video url from each site choosen
for c in choice:
    request = Request(eprog_link_dict[c], headers={'User-Agent' : user_agent})
    soup = BeautifulSoup(urllib.request.urlopen(request), 'html.parser')

    link = soup.find('li', class_='video')
    link = link.find('a').get('href')

    split = urllib.parse.urlsplit(link)
    filename = 'Vorlesungen/EProg/'+str(eprog_date_dict[c])+".mp4"
    #Let's hope everything is .mp4

    print('\n',link)
    
    if os.path.isfile(filename):
        print("---skipped - already exists")
    else:
        print('The next few moments you will maybe think nothing is happening - you\'re wrong.')
        print("---downloading file (press Ctrl+C to abort)")
        file = urllib.request.urlopen(link)
        with open(filename, 'wb') as f:
            while True:
                tmp = file.read(1024)
                if not tmp:
                    break
                f.write(tmp)
        print("---downloaded file")
        download_counter += 1
        link_list.append(link)
        filename_list.append(filename)


print("\n\n")

#START Lineare Algebra
#Check main site for all available lectures
print("Lineare Algebra")
la_link = 'http://www.video.ethz.ch/lectures/d-math/2017/autumn/401-0131-00L.html'
la_link_dict = {}
la_date_dict = {}
la_counter = 0

request = Request(la_link, headers={'User-Agent': user_agent})
soup = BeautifulSoup(urllib.request.urlopen(request), 'html.parser')

for div in soup.find_all('div', class_='newsListBox'):
    link = 'http://www.video.ethz.ch'+str(div).partition('\n<a href="')[-1].rpartition('"><h2>Lineare')[0]
    date = str(div).partition('<p>')[-1].strip().rpartition(', Imamoglu')[0]
    la_link_dict[la_counter] = link
    la_date_dict[la_counter] = date
    print('['+str(la_counter)+']',date,'\n',link,'\n')
    la_counter += 1


try:
    choice = [int(x) for x in input("Enter numbers of lectures, separated by space (e.g. 0 3 5 7)\nJust press enter if you don't want to download anything\n").split()]
except:
    print("You done fucked up")
    sys.exit()
    
print('')

#open every chosen lecture
for c in choice:
    request = Request(la_link_dict[c], headers={'User-Agent' : user_agent})
    soup = BeautifulSoup(urllib.request.urlopen(request), 'html.parser')

    link = soup.find('li', class_='video')
    link = link.find('a').get('href')

    split = urllib.parse.urlsplit(link)
    filename = 'Vorlesungen/LineareAlgebra/'+str(la_date_dict[c])+".mp4"
    #Let's hope everything is .mp4

    print('\n',link)

    if os.path.isfile(filename):
        print("---skipped - already exists")
    else:
        print('The next few moments you will maybe think nothing is happening - you\'re wrong.')
        print("---downloading file (press Ctrl+C to abort)")
        file = urllib.request.urlopen(link)
        with open(filename, 'wb') as f:
            while True:
                tmp= file.read(1024)
                if not tmp:
                    break
                f.write(tmp)
        print("---downloaded file")
        download_counter += 1
        link_list.append(link)
        filename_list.append(filename)
        

print(la_counter+eprog_counter,"Files Found and",download_counter,"Files downloaded")
if platform == "win32":
    input('\nEOF') #Just so Windows users don't get butthurt about not seeing the output
