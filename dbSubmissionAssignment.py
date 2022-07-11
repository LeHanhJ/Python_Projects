

import sqlite3

#this will connect to class sqlite3 and will connect by using the method; will make dbAssignment.db if it hasn't been created yet
conn = sqlite3.connect('dbAssignment.db') 


with conn: #while we are connected to the database...
    cur = conn.cursor() #cursor object
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_asignFiles( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_string TEXT \
        )")
    conn.commit()
conn.close() #closes the connection

conn = sqlite3.connect('dbAssignment.db')

#fileList in assignment
fileList = ('information.docx','Hello.txt','myImage.png', \
           'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

#loop through each object in the tuple to find files ending in .txt
for x in fileList: #for each element in fileList
    if x.endswith('.txt'): #if the element ends in .txt...
        with conn: #connect to dbAssignment.db
            cur = conn.cursor()
        #(?) denotes a wildcard, which the program will go through each element
        #to pull out x (aka any file that ends in .txt)
        #adding a comma at the end of x in (x,) will denote it as an individual tuple,
        #thereby printing it in its own line
            cur.execute("INSERT INTO tbl_asignFiles(col_string) VALUES(?)", (x,)) 
            print(x)

conn.close()

"""
note: when I try to use the triple quotation marks in the multiple lined comment above, it says that the following cur.execute had an unexpected indent
but the line of code was unchanged besides adding the triple quotes. Are triple quotes only viable in the beginning and ending of a code?
"""
