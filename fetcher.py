import urllib.request
import extraction as b
import os
import sys
import time
import threading
import math

# forder and link setup here and for text and data extraction see beautify.py


folder_name = "Nine Star Hegemon Body Arts p8 test"
links_folder = "chapterLinks new.txt"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
counter = 0

def fetch_and_save(url):
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



def indi_thread_call(links:list):
    global counter
    # startx = 3767
    # endx = 4138
    enumx = 0

    
    thread_name = threading.current_thread().name

    # for nine star
    # startx = startx - 2

    for l in links:
        counter += 1
        enumx = enumx + 1

        if enumx % 15 == 0:
            time.sleep(30)

        print(f"\nTotal_counter: {counter} Thread no:{thread_name} saving chapter: ",enumx)
        fetch_and_save(l.strip())   


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
    each_slice = math.floor(len(links)/8)
    
    l1 = links[:each_slice-1]
    l2 = links[each_slice-1:(each_slice)*2-1]
    l3 = links[each_slice*2-1:each_slice*3-1]
    l4 = links[each_slice*3-1:each_slice*4-1]
    l5 = links[each_slice*4-1:each_slice*5-1]
    l6 = links[each_slice*5-1:each_slice*6-1]
    l7 = links[each_slice*6-1:each_slice*7-1]
    l8 = links[each_slice*7-1:]

    T1 = threading.Thread(name="t1",target=indi_thread_call,args=(l1,))
    T2 = threading.Thread(name="t2",target=indi_thread_call,args=(l2,))
    T3 = threading.Thread(name="t3",target=indi_thread_call,args=(l3,))
    T4 = threading.Thread(name="t4",target=indi_thread_call,args=(l4,))
    T5 = threading.Thread(name="t5",target=indi_thread_call,args=(l5,))
    T6 = threading.Thread(name="t6",target=indi_thread_call,args=(l6,))
    T7 = threading.Thread(name="t7",target=indi_thread_call,args=(l7,))
    T8 = threading.Thread(name="t8",target=indi_thread_call,args=(l8,))

    T1.start()
    T2.start()
    T3.start()
    T4.start()
    T5.start()
    T6.start()
    T7.start()
    T8.start()

    T1.join()
    T2.join()
    T3.join()
    T4.join()
    T5.join()
    T6.join()
    T8.join()
