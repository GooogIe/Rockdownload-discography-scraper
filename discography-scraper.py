#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re			# Some regular expressions to carry out some readable data from html
import requests
import sys
"""
Use this lil script to get full artist's album links from http://rd-13.blogspot.it
Author: A Sad Loner, t.me/eigoog
Usage: run in terminal -> python scraper.py
"""

def getUrls(query):
	data = requests.get("http://rd-13.blogspot.it/search?q=%s" % (query)).content

	results = re.findall(r"<h3 class='post-title entry-title' itemprop='name'>\n<a href='(http://rd-13\.blogspot\.it.*?\.html)'>(.*?)<",data)
	return results

def getCollected(url):
	collected = []
	data = requests.get(url).content
	titles = re.findall(r'<span style="font-size: large;">(\[.*?)<',data)

	while "[" in titles: titles.remove("[")

	links = re.findall(r'\[<b><a href="(.*?)"',data)
	for i in range(0,len(titles)-1):
		print ("Album: %s - %s" % (titles[i],links[i]))
		collected.append("Album: %s - %s" % (titles[i],links[i]))
	#return collected

def getPassword(url):
	return re.findall(r', sans-serif;"><b><span style="font-size: x-large;"><u>(.*?)</u>',data)[0]


query = raw_input("Artist name: ")

results = getUrls(query)

if len(results) == 0:
 sys.exit("No artist found")

for i in range(0,len(results)):
	print str(i+1) +" - "+results[i][1]

choice = 0

while True:
	choice = int(raw_input("Type the number of the artist you want: "))
	if choice>0 and choice<len(results)+1:
		break
	print("Invalid choice.")

getCollected(results[choice-1][0])
	
