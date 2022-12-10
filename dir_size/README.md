
A helper designed for Windows, dec.2022.

     This simple python script helps to find largest used diskspace.
     Not fast, not smart. Does not scan files on disks.
     Reads a.txt and calculates sizes of folders and subfolders.
     Writes b.txt with sizes (see "Directory of.." only)

 Steps:

 1.     dir C:\ /s /a  >a.txt

          C:\ is the starting folder to list
          /s means recursive subdirectories
          /a means to show hidden files and folders too
          >a.txt outputs stdout to file not screen

 2.     python dir_size.py

 3.  View b.txt for folder sizes.
 
  Result b.txt sample:
 
        127.9Gb! c:\
          13.8Gb! c:\Program Files\
           6.8Gb! c:\Program Files (x86)\
          24.8Gb! c:\Users\
             4.2Gb! All Users\
	           ....
          76.6Gb! c:\Windows\
             3.1Gb! assembly\
            58.1Gb! Installer\
             1.0Gb! servicing\
             3.2Gb! System32\
             1.2Gb! SysWOW64\
             6.9Gb! WinSxS\

