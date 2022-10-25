#!/usr/bin/python3
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import notify2


class PlayMusic:

    def __init__(self):
        notify2.init('Music')
        self.n=notify2.Notification('A.L.F.R.E.D.',message='Opening Requested Webpage !',icon='/home/tbarik/Documents/PythonP/projects/alfred.png')
        options=webdriver.ChromeOptions()
        options.headless=True
        self.driver = webdriver.Chrome('/home/tbarik/Documents/PythonP/projects/chromedriver',options=options) 

    def play(self,query):
        if query=="exit":
            self.driver.close()
            exit()
        query=query+" song"
        query.replace(" ","+")
        url ="https://www.youtube.com/results?search_query="+query
        url = url[:23]+'.'+url[23:]
        self.driver.get(url)
        videos=self.driver.find_elements_by_id('video-title')
        href=videos[0].get_attribute("href")
        self.driver.get(href)
        self.n.message="Playing song : "+ self.driver.title+"\n"
        self.n.show()
        self.control()
    def control(self):
        element = self.driver.find_element_by_xpath("//button[@class='ytp-play-button ytp-button']")
        element.click()


if __name__ == "__main__":
    p=PlayMusic()
    while True:
        inpquery=input("Enter Song Name : ")
        p.play(inpquery)


