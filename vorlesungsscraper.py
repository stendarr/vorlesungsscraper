#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Make sure you have `requests` and `bs4` installed -> pip install requests/bs4

Check README.md and LICENSE before using this program.

Checklist | Lectures |
----------|----------|
DigiTech  |     y    |
----------|----------|
PP        |     y    |
----------|----------|
AnalysisI |     y    |
----------|----------|
AW        |    n/a   |  

'''

import urllib.request, urllib.parse, os, sys, http.client
from urllib.request import Request, urlopen
from html.parser import *
from sys import platform
try:
    import requests
except:
    print('Installing `requests` is NOT optional, m8')
    sys.exit(1)
try:
    from bs4 import BeautifulSoup, SoupStrainer
except:
    print('Installing `BeautifulSoup` is NOT optional, m8')
    sys.exit(1)
try:
    urllib.request.urlopen('https://www.google.com')
except urllib.error.URLError:
    input("There is no connection - please connect to the internet and try again.")
    sys.exit(1)

user_agent = 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
link_counter = 0
download_counter = 0
link_list = []
filename_list = []


#Generate folders if nonexistent
directories = ["Vorlesungsaufzeichnungen/DigiTech", "Vorlesungsaufzeichnungen/PP", "Vorlesungsaufzeichnungen/Analysis I"]

for i in directories:
    if not os.path.isdir(i):
        os.makedirs(i)
        print("This folder was generated:   ",i)
    else:
        print("This folder already exists:  ",i)
print("\n\n")


#START DigiTech
#Check main site for all available lectures
print("DigiTech")
digitech_link = 'https://www.video.ethz.ch/lectures/d-infk/2018/spring/252-0028-00L.html'
digitech_link_dict = {}
digitech_date_dict = {}
digitech_counter = 0

request = Request(digitech_link, headers={'User-Agent' : user_agent})
soup = BeautifulSoup(urllib.request.urlopen(request), 'html.parser')

for div in soup.find_all('div', class_='newsListBox'):
    link = 'http://www.video.ethz.ch'+str(div).partition('\n<a href="')[-1].rpartition('"><h2>Design')[0]
    date = str(div).partition('<p>')[-1].strip().rpartition(', Onur Mutlu')[0]
    digitech_link_dict[digitech_counter] = link
    digitech_date_dict[digitech_counter] = date
    print('['+str(digitech_counter)+']',date,'\n',link,'\n')
    digitech_counter += 1

try:
    choice = [int(x) for x in input("Enter numbers of lectures, separated by space (e.g. 0 3 5 7)\nJust press enter if you don't want to download anything\n").split()]
except:
    print("You done fucked up")
    sys.exit()

print('')

#Get video url from each site choosen
for c in choice:
    request = Request(digitech_link_dict[c], headers={'User-Agent' : user_agent})
    soup = BeautifulSoup(urllib.request.urlopen(request), 'html.parser')

    link = soup.find('li', class_='video')
    link = link.find('a').get('href')

    split = urllib.parse.urlsplit(link)
    filename = 'Vorlesungsaufzeichnungen/DigiTech/'+str(digitech_date_dict[c])+".mp4"
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
#end DigiTech


#START Parallel Programming
#Check main site for all available lectures
print("Parallel Programming")
pp_link = 'https://www.video.ethz.ch/lectures/d-infk/2018/spring/252-0029-00L.html'
pp_link_dict = {}
pp_date_dict = {}
pp_counter = 0
pp_links = []

request = Request(pp_link, headers={'User-Agent': user_agent})
soup = BeautifulSoup(urllib.request.urlopen(request), 'html.parser')

for div in soup.find_all('div', class_='newsListBox'):
    link = 'http://www.video.ethz.ch'+str(div).partition('\n<a href="')[-1].rpartition('"><h2>Paralle')[0]
    date = str(div).partition('<p>')[-1].strip().rpartition(', Torste')[0]
    pp_link_dict[pp_counter] = link
    pp_date_dict[pp_counter] = date
    print('['+str(pp_counter)+']',date,'\n',link,'\n')
    pp_counter += 1

try:
    choice = [int(x) for x in input("Enter numbers of lectures, separated by space (e.g. 0 3 5 7)\nJust press enter if you don't want to download anything\n").split()]
except:
    print("You done fucked up")
    sys.exit()

print('')

#open every chosen lecture
for c in choice:
    request = Request(pp_link_dict[c], headers={'User-Agent' : user_agent})
    soup = BeautifulSoup(urllib.request.urlopen(request), 'html.parser')

    link = soup.find('li', class_='video')
    link = link.find('a').get('href')

    split = urllib.parse.urlsplit(link)
    filename = 'Vorlesungsaufzeichnungen/PP/'+str(pp_date_dict[c])+".mp4"
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

print("\n\n")        
#end PP


#START Analysis I
#Check main site for all available lectures
print("Analysis I")
analysis_link = 'https://www.video.ethz.ch/lectures/d-math/2018/spring/401-0212-16L.html'
analysis_link_dict = {}
analysis_date_dict = {}
analysis_counter = 0

request = Request(analysis_link, headers={'User-Agent' : user_agent})
soup = BeautifulSoup(urllib.request.urlopen(request), 'html.parser')

for div in soup.find_all('div', class_='newsListBox'):
    link = 'http://www.video.ethz.ch'+str(div).partition('\n<a href="')[-1].rpartition('"><h2>Analysis')[0]
    date = str(div).partition('<p>')[-1].strip().rpartition(', Emmanuel')[0]
    analysis_link_dict[analysis_counter] = link
    analysis_date_dict[analysis_counter] = date
    print('['+str(analysis_counter)+']',date,'\n',link,'\n')
    analysis_counter += 1

try:
    choice = [int(x) for x in input("Enter numbers of lectures, separated by space (e.g. 0 3 5 7)\nJust press enter if you don't want to download anything\n").split()]
except:
    print("You done fucked up")
    sys.exit()

print('')

#Get video url from each site choosen
for c in choice:
    request = Request(analysis_link_dict[c], headers={'User-Agent' : user_agent})
    soup = BeautifulSoup(urllib.request.urlopen(request), 'html.parser')

    link = soup.find('li', class_='video')
    link = link.find('a').get('href')

    split = urllib.parse.urlsplit(link)
    filename = 'Vorlesungsaufzeichnungen/Analysis I/'+str(analysis_date_dict[c])+".mp4"
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
#end DigiTech


print()
print(analysis_counter+pp_counter+digitech_counter,"Files Found and",download_counter,"Files downloaded")
if len(filename_list) != 0:
    print("Lectures downloaded into: ")
    for fn in filename_list:
        print(fn)
if platform == "win32":
    input('\nEOF') #Just so Windows users don't get butthurt about not seeing the output
