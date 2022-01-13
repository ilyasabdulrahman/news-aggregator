#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 03:10:46 2021
@author: ilyasabdulrahman
"""

#Web Content Aggregator
#step1: initialize web server
#step2: create function home()
#step3: request HTML content from websites
#step4: iterate through website HTML code
#step5: format web application

from flask import Flask
from bs4 import BeautifulSoup
import requests


app = Flask(__name__)

@app.route("/")

def home():
    '''
    This function executes the code to be displayed on the home page of the
    web application
    Returns: display of the web application
    '''
    #make HTTP requests to receive raw HTML content from websites
    source = requests.get('https://www.nytimes.com').text
    soup = BeautifulSoup(source, 'lxml')
    nyt_list = []
    for section in soup.find_all('section', class_='story-wrapper')[0:7]:
        try:
            #iterate through the website's HTML code
            headline = section.a.h3.text
            nyt_list.append(headline)
        except:
            pass
    nyt1 = nyt_list[0]
    nyt2 = nyt_list[1]
    nyt3 = nyt_list[2]
    nyt4 = nyt_list[3]
    
    
    source = requests.get('https://www.foxnews.com').text
    soup = BeautifulSoup(source, 'lxml')
    fox_list = []
    for article in soup.find_all('article')[10:15]:
        try:
            headline = article.header.h2.a.text
            fox_list.append(headline)
        except:
            pass
    fox1 = fox_list[0]
    fox2 = fox_list[1]
    fox3 = fox_list[2]
    fox4 = fox_list[3]
    fox5 = fox_list[4]
    
    
    source = requests.get('https://www.theguardian.com/us').text
    soup = BeautifulSoup(source, 'lxml')
    gau_list = []
    for div in soup.find_all('div', class_='fc-item__container')[0:6]:
        try:
            headline = div.a.text
            gau_list.append(headline)
        except:
            pass
    gau1 = gau_list[0]
    gau2 = gau_list[1]
    gau3 = gau_list[2]
    gau4 = gau_list[3]
    gau5 = gau_list[4]
    
    
    source = requests.get('https://www.cnbc.com').text
    soup = BeautifulSoup(source, 'lxml')
    cnbc_list = []
    for div in soup.find_all('div', class_='LatestNews-headlineWrapper'):
        try:
            headline = div.a.text
            if headline == "":
                pass
            else:
                cnbc_list.append(headline)
        except:
            pass
    cnbc1 = cnbc_list[0]
    cnbc2 = cnbc_list[1]
    cnbc3 = cnbc_list[2]
    cnbc4 = cnbc_list[3]
    cnbc5 = cnbc_list[4]
    
    
    source = requests.get('https://www.ndtv.com/trends/most-popular-news').text
    soup = BeautifulSoup(source, 'lxml')
    ndtv_list = []
    for div in soup.find_all('div', class_='trend-list')[0:6]:
        try:
            headline = div.h3.a.text
            ndtv_list.append(headline)
        except:
            pass
    ndtv1 = ndtv_list[0]
    ndtv2 = ndtv_list[1]
    ndtv3 = ndtv_list[2]
    ndtv4 = ndtv_list[3]
    ndtv5 = ndtv_list[4]
    
    
    source = requests.get('https://www.lansingstatejournal.com/news/').text
    soup = BeautifulSoup(source, 'lxml')
    lsj_list = []
    for a in soup.find_all('a', class_='gnt_m_th_a'):
        try:
            headline = a.text
            lsj_list.append(headline)
        except:
            pass
    lsj1 = lsj_list[0]
    lsj2 = lsj_list[1]
    lsj3 = lsj_list[2]
    lsj4 = lsj_list[3]
    
    
    source = requests.get('https://news.un.org/en/').text
    soup = BeautifulSoup(source, 'lxml')
    un_list = []
    for h3 in soup.find_all(class_='story-title'):
        try:
            headline = h3.a.text
            un_list.append(headline)
        except:
            pass
    un1 = un_list[0]
    un2 = un_list[1]
    un3 = un_list[2]
    un4 = un_list[3]
    un5 = un_list[4]
    un6 = un_list[5]
    un7 = un_list[6]
    un8 = un_list[7]
    
    
    source = requests.get('https://www.detroitnews.com').text
    soup = BeautifulSoup(source, 'lxml')
    det_list = []
    for a in soup.find_all('a', class_='gnt_m_th_a'):
        headline = a.text
        det_list.append(headline)
    det1 = det_list[0]
    det2 = det_list[1]
    det3 = det_list[2]
    det4 = det_list[3]
    det5 = det_list[4]
    
    return '''
        <html>
            
            <body style='background-color:#87CEFA'>
                <h1 style='text-align: center; font-family: Arial'>
                News Aggregator
                </h2>
                <h2>
                    <span  style="font-size: 22px; color: red; font-family: Arial">NYT Front Page</span>
                    <span style="font-size: 10px; color: orange"><a href="https://www.nytimes.com">(https://www.nytimes.com)</a></span>
                </h2>
                <ul style='font-family: Arial'>
                    <li>{nyt1}</li>
                    <li>{nyt2}</li>
                    <li>{nyt3}</li>
                    <li>{nyt4}</li>
                </ul>
                <h2>
                    <span  style="font-size: 22px; color: red; font-family: Arial">Fox News</span>
                    <span style="font-size: 10px; color: orange"><a href="https://www.foxnews.com">(https://www.foxnews.com)</a></span>
                </h2>
                <ul style='font-family: Arial'>
                    <li>{fox1}</li>
                    <li>{fox2}</li>
                    <li>{fox3}</li>
                    <li>{fox4}</li>
                    <li>{fox5}</li>
                </ul>
                <h2>
                    <span  style="font-size: 22px; color: red; font-family: Arial">The Gaurdian</span>
                    <span style="font-size: 10px; color: orange"><a href="https://www.theguardian.com/us">(https://www.theguardian.com/us)</a></span>
                </h2>
                <ul style='font-family: Arial'>
                    <li>{gau1}</li>
                    <li>{gau2}</li>
                    <li>{gau3}</li>
                    <li>{gau4}</li>
                    <li>{gau5}</li>
                </ul>
                <h2>
                <h2>
                    <span  style="font-size: 22px; color: red; font-family: Arial">CNBC News</span>
                    <span style="font-size: 10px; color: orange"><a href="https://www.cnbc.com">(https://www.cnbc.com)</a></span>
                </h2>
                <ul style='font-family: Arial'>
                    <li>{cnbc1}</li>
                    <li>{cnbc2}</li>
                    <li>{cnbc3}</li>
                    <li>{cnbc4}</li>
                    <li>{cnbc5}</li>
                </ul>
                <h2>
                    <span  style="font-size: 22px; color: red; font-family: Arial">NDTV Most Popular News</span>
                    <span style="font-size: 10px; color: orange"><a href="https://www.ndtv.com/trends/most-popular-news">(https://www.ndtv.com/trends/most-popular-news)</a></span>
                </h2>
                 <ul style='font-family: Arial'>
                    <li>{ndtv1}</li>
                    <li>{ndtv2}</li>
                    <li>{ndtv3}</li>
                    <li>{ndtv4}</li>
                    <li>{ndtv5}</li>
                </ul>
                <h2>
                    <span  style="font-size: 22px; color: red; font-family: Arial">Lansing State Journal News</span>
                    <span style="font-size: 10px; color: orange"><a href="https://www.lansingstatejournal.com/news/">(https://www.lansingstatejournal.com/news/)</a></span>
                </h2>
                <ul style='font-family: Arial'>
                    <li>{lsj1}</li>
                    <li>{lsj2}</li>
                    <li>{lsj3}</li>
                    <li>{lsj4}</li>
                </ul>
                <h2>
                    <span  style="font-size: 22px; color: red; font-family: Arial">UN News Front Page</span>
                    <span style="font-size: 10px; color: orange"><a href="https://news.un.org/en/">(https://news.un.org/en/)</a></span>
                </h2>
                 <ul style='font-family: Arial'>
                    <li>{un1}</li>
                    <li>{un2}</li>
                    <li>{un3}</li>
                    <li>{un4}</li>
                    <li>{un5}</li>
                    <li>{un6}</li>
                    <li>{un7}</li>
                    <li>{un8}</li>
                </ul>
                <h2>
                    <span  style="font-size: 22px; color: red; font-family: Arial">The Detroit News Top Headlines</span>
                    <span style="font-size: 10px; color: orange"><a href="https://www.detroitnews.com">(https://www.detroitnews.com)</a></span>
                </h2>
                 <ul style='font-family: Arial'>
                    <li>{det1}</li>
                    <li>{det2}</li>
                    <li>{det3}</li>
                    <li>{det4}</li>
                    <li>{det5}</li>
                </ul>
            </body>
        </html>
    '''.format(**locals())
        
    
 
if __name__ == "__main__":
    app.run()