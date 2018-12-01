#Basic Crawler from a Youtube Tutorial
#os lib
import os

#each time the project runs, a new folder will be created to store the crawled files
def create_project_dir(directory):
    if not os.path.exists(directory):
        print('creating project' + directory)
        os.makedirs(directory)
        
#create a queue and crawled files (if crawled files do not already exist)
def create_data_files(project_name, base_url):
        #a list of links on the waiting list, waiting to be crawled
        #the process of file writing is relatively slow, so watch out
        queue = project_name + '/que.txt'
        crawled = project_name + '/crawled.txt'
        #if the file doesn't exist, make it
        if not os.path.isfile(queue):
                write_file(queue, base_url)
        if not os.path.isfile(crawled):
                write_file(crawled,'')

#create a new file
def write_file(path, data):
        #w for write mode
        f = open(path, 'w')
        f.write(data)
        #close the file to free up memory resources
        f.close()

#add data to an existing file
def append_to_file(path, data):
        #open a file in append mode
        with open(path, 'a') as file:
                #write link on a new line
                file.write(data + '\n')

#delete existing data if needed. Creates a file of the same name, but "deletes" the content of it.
def delete_file_contents(path):
        with open(path, 'w'):
                #pass means do nothin; kind of like just having a comment. When you want a loop, but do nothing..
                pass

#store the urls in a set, which can only contain unique elements (vs duplicates in a list)

#convert links in a file to a set
#read a file and convert each line to set items
def file_to_set(file_name):
        #create an empty set
        results = set()
        #open file; rt = read text file as file
        with open(file_name,'rt') as f:
                #for each line in the file
                for line in f:
                        #delete the new line from read file in, and replace it with blank info
                        results.add(line.replace('\n',''))
        return results

#convert the links in a set to a file
#iterate through a set. each item will be a new line in a file
#file to set and set to file are to speed things up
def set_to_file(links,file):
        #you don't need the files anymore, just the contents (links)
        delete_file_contents(file)
        #sort the links in alphabetical order
        for link in sorted(links):
                #add them to the end of the file
                append_to_file(file,link)
