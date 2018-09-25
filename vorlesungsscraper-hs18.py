#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Make sure you have `requests` and `bs4` installed -> pip install requests/bs4

Check README.md and LICENSE before using this program.

Checklist | Lectures |
----------|----------|
LinAlg    |     y    |
----------|----------|
EProg     |     y    |
----------|----------|
DiskMath  |    n/a   |
----------|----------|
A&D       |    n/a   |

'''

import urllib.request, urllib.parse, os, sys, http.client, threading, time
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

alles = False
if len(sys.argv) == 2 and sys.argv[1] == "--all":
    alles = True

user_agent = 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
link_counter = 0
download_counter = 0
link_list = []
filename_list = []

#Generate folders if nonexistent
directories = ["Vorlesungsaufzeichnungen/LinAlg", "Vorlesungsaufzeichnungen/EProg"]

for i in directories:
    if not os.path.isdir(i):
        os.makedirs(i)
        print("This folder was generated:   ",i)
    else:
        print("This folder already exists:  ",i)
print("\n\n")


def LA():
    #START LinAlg
    global user_agent
    global link_counter
    global download_counter
    global link_list
    global filename_list
    global alles
    #Check main site for all available lectures
    print("LinAlg")
    linalg_link = 'https://www.video.ethz.ch/lectures/d-math/2018/autumn/401-0131-00L.html'
    linalg_link_dict = {}
    linalg_date_dict = {}
    linalg_counter = 0

    request = Request(linalg_link, headers={'User-Agent' : user_agent})
    soup = BeautifulSoup(urllib.request.urlopen(request), 'html.parser')

    for div in soup.find_all('div', class_='newsListBox'):
        link = 'http://www.video.ethz.ch'+str(div).partition('\n<a href="')[-1].rpartition('"><h2>Lineare')[0]
        date = str(div).partition('<p>')[-1].strip().rpartition(', Imamoglu')[0]
        linalg_link_dict[linalg_counter] = link
        linalg_date_dict[linalg_counter] = date
        print('['+str(linalg_counter)+']',date,'\n',link,'\n')
        linalg_counter += 1

    if not alles:
        try:
            choice = [int(x) for x in input("Enter numbers of lectures, separated by space (e.g. 0 3 5 7)\nJust press enter if you don't want to download anything\n").split()]
        except:
            print("You done fucked up")
            sys.exit()
    else:
        choice = linalg_link_dict

    print('')

    #Get video url from each site choosen
    for c in choice:
        request = Request(linalg_link_dict[c], headers={'User-Agent' : user_agent})
        soup = BeautifulSoup(urllib.request.urlopen(request), 'html.parser')

        link = soup.find('li', class_='video')
        link = link.find('a').get('href')

        split = urllib.parse.urlsplit(link)
        filename = 'Vorlesungsaufzeichnungen/LinAlg/'+str(linalg_date_dict[c])+".mp4"
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

    link_counter += linalg_counter

    print("\n\n")
    #end LinAlg


def EP():
    #START EProg
    global user_agent
    global link_counter
    global download_counter
    global link_list
    global filename_list
    global alles
    #Check main site for all available lectures
    print("EProg")
    eprog_link = 'https://www.video.ethz.ch/lectures/d-infk/2018/autumn/252-0027-00L.html'
    eprog_link_dict = {}
    eprog_date_dict = {}
    eprog_counter = 0
    eprog_links = []

    request = Request(eprog_link, headers={'User-Agent': user_agent})
    soup = BeautifulSoup(urllib.request.urlopen(request), 'html.parser')

    for div in soup.find_all('div', class_='newsListBox'):
        link = 'http://www.video.ethz.ch'+str(div).partition('\n<a href="')[-1].rpartition('"><h2>Einf')[0]
        date = str(div).partition('<p>')[-1].strip().rpartition(', Gross')[0]
        eprog_link_dict[eprog_counter] = link
        eprog_date_dict[eprog_counter] = date
        print('['+str(eprog_counter)+']',date,'\n',link,'\n')
        eprog_counter += 1

    if not alles:
        try:
            choice = [int(x) for x in input("Enter numbers of lectures, separated by space (e.g. 0 3 5 7)\nJust press enter if you don't want to download anything\n").split()]
        except:
            print("You done fucked up")
            sys.exit()
    else:
        choice = eprog_link_dict

    print('')

    #open every chosen lecture
    for c in choice:
        request = Request(eprog_link_dict[c], headers={'User-Agent' : user_agent})
        soup = BeautifulSoup(urllib.request.urlopen(request), 'html.parser')

        link = soup.find('li', class_='video')
        link = link.find('a').get('href')

        split = urllib.parse.urlsplit(link)
        filename = 'Vorlesungsaufzeichnungen/EProg/'+str(eprog_date_dict[c])+".mp4"
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

    link_counter += eprog_counter

    print("\n\n")
    #end PP


if alles:
    mt_start = time.time()
    tep = threading.Thread(target = EP)
    tla = threading.Thread(target = LA)

    tep.start()
    tla.start()

    tep.join()
    tla.join()
    print("Parallel time: ", time.time()-mt_start)

else:
    EP()
    LA()

print()
print(link_counter,"Files Found and",download_counter,"Files downloaded")
if len(filename_list) != 0:
    print("Lectures downloaded into: ")
    for fn in filename_list:
        print(fn)
if platform == "win32":
    input('\nEOF') #Just so Windows users don't get butthurt about not seeing the output
