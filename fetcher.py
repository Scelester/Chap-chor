import urllib.request
import beautify as b
import os
import sys
import time

folder_name = "Nine Star Hegemon Body Arts p8"
links_folder = "chapterLinks new.txt"

def fetch_and_save(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}

    # chapter_name = url.split('/')[-1]
    
    # # for nine start 
    # chapter_name = chapter_name[1:]

    chapter_name = False

    try:
        req = urllib.request.Request(url, headers=headers)
        response = urllib.request.urlopen(req)
        data = response.read()
        text_data = data.decode("utf-8")
        chapter_name = b.non_rawing(chapter_name,text_data,folder_name)

        print(chapter_name,"saved successfully")

    except urllib.error.URLError as e:
        print(f"Failed to fetch data. Error: {e}")
        sys.exit()






with open(links_folder,'r') as file:
    
    if os.path.exists(folder_name):
        print("Directory exists.")
    else:
        print("Directory not found, creating one...")
    
        
        try:
            os.makedirs(folder_name)
            print("Directory created successfully.")
        except OSError as e:
            print(f"Error: {e}")

    links = file.readlines()
    # startx = 3767
    # endx = 4138
    enumx = 0

    # for nine star
    # startx = startx - 2

    for l in links:

        enumx = enumx + 1

        # if enumx % 15 == 0:
        #     time.sleep(30)

        print(" \nsaving chapter: ",enumx)
        fetch_and_save(l.strip())   
