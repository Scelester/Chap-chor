from ebooklib import epub
import os
import natsort

class Create_EPUB:
    def __init__(self,folder_path):

        self.name = os.path.basename(os.path.dirname(folder_path)) + "_0-2029"

        self.book = epub.EpubBook()
        self.book.set_identifier("SLS_CC_0")
        self.book.set_title(self.name)
        self.book.set_language("en")
        self.book.add_author("Scelester")
        self.book.set_cover("Xia Qingyue.png",open("/home/scelester/ProjectD/fetcher/STORAGE/Against the gods/Xia Qingyue.png",'rb').read())
        self.book.add_item(epub.EpubNcx())
        self.book.add_item(epub.EpubNav())
        self.chapter_list = []

        self.book.spine = ['nav']

        if os.path.isdir(folder_path):
            # Get a list of all files and directories in the folder
            all_items = os.listdir(folder_path)

            # Sort the list of items by name
            sorted_items = natsort.natsorted(all_items)

            # Iterate over the sorted list
            for filename in sorted_items:
                # Construct the full file path
                file_path = os.path.join(folder_path, filename)

                # Check if the item is a file (not a subdirectory)
                if os.path.isfile(file_path):
                    # Process the file as needed
                    file = open(file_path)
                    self.add_chapter(file)
        else:
            print("The specified path is not a directory.")

    def add_chapter(self,file):
        file_content = file.read().strip().split('\n')
        title = file_content[0]
        
        formatted_body_array = []
        old_line = "Some()"
        for line in file_content[1:]:
            if line == old_line == "":
                pass
            else:
                formatted_body_array.append(line)
            old_line = line


        body = '<br>'.join(formatted_body_array) 
        

        xht_title = ''.join(title.split(' '))

        chapter = epub.EpubHtml(title=f'{title}', file_name=f'{xht_title}.xhtml', lang='en')
        chapter.content =  f"<html><head></head><body><h1>{title}</h1><p>{body}</p></body></html>"

        self.book.add_item(chapter)

        self.chapter_list.append(chapter)
        self.book.spine.append(chapter)
        self.book.toc.append(epub.Link(href=f"{xht_title}.xhtml",title=title,uid=chapter.id))
            

    def finilize(self):
        epub.write_epub('Against The Gods 0-2029.epub',self.book,{})



x = Create_EPUB("/home/scelester/ProjectD/fetcher/STORAGE/Against the gods/Chapter_upto")
x.finilize()