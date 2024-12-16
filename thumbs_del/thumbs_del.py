#
#
#  Windows makes hidden Thumbs.db files.
#
#  This python script deletes them.
#
#  Prepare by:
#   dir Thumbs.db /s /a:h > thumbs.txt
#
#

if True:

  import os

  # dir batch prepared file contains list of Thumbs.db
  dirfile = "thumbs.txt"

  slash = "\\"

  file = open(dirfile, "r")
  content = file.read()
  file.close()

  S = content.split('\n')  
  path = ""

  for s in S:
   
   i = s.find("Directory of")
   if(i>0):
     path = s[14:]

   if( s.find("Thumbs.db")>0 ):
     x = path + slash + "Thumbs.db"
     file = x.replace(slash,"/")

     if( os.path.exists(file) ):
       print(file)

       #remove Thumbs.db
       os.remove(file)



