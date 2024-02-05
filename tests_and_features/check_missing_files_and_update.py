import os

def extract_digits(filename):
    # Extract and return digits from the given filename
    filename = ''.join(filename.split(' ')[:2])
    return ''.join(char for char in filename if char.isdigit())

def check_files_in_folder(folder_path):
    re_list = []

    # Get the list of files in the specified folder
    files = os.listdir(folder_path)

    # Extract digits from each filename and convert them to integers
    numeric_file_numbers = [int(extract_digits(filename)) for filename in files if extract_digits(filename)]

    # Find the total number of files in the folder
    total_files = len(numeric_file_numbers)

    # Check if there is a file for each number from 0 to total_files
    n = 0
    for i in range(total_files):
        
        i += 1
        if i not in numeric_file_numbers:
            n+=1
            print(f"{n}). File for number {i} is missing.")
            re_list.append(i)
            
    
    print("File check completed.")
    return re_list

# Specify the folder path here
folder_path = "/home/scelester/ProjectD/fetcher/STORAGE/Against the gods/Chapter_upto"

# Call the function to check files in the folder
a = check_files_in_folder(folder_path)

x = open("/home/scelester/ProjectD/fetcher/STORAGE/Against the gods/chapterLinks_ATG.txt",'r')
y = x.readlines()

chapter_link_to_download = []
for z in y:
    m =  ''.join(z.split('/')[-1]).split('-')[1].strip()
    print("m = ",m)
    if int(m) in a:
        chapter_link_to_download.append(z)

x.close()

x = open('rem_chapters.txt','w')
x.write(''.join(chapter_link_to_download))