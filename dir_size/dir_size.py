#
# A helper designed for Windows, dec.2022.
#
# This simple python script helps to find largest used diskspace.
# Not fast, not smart. Does not scan files on disks.
# Reads a.txt and calculates sizes of folders and subfolders.
# Writes b.txt with sizes (see "Directory of.." only)
# 
# Steps:
#
# 1.     dir C:\ /s /a  >a.txt
#
#          C:\ is the starting folder to list
#          /s means recursive subdirectories
#          /a means to show hidden files and folders too
#          >a.txt outputs stdout to file not screen
#          
# 2.     python dir_size.py
#
# 3.  View b.txt for folder sizes.
 
if True:

  #
  # Sum totals and show sizes.
  # 
  
  fileIn = "a.txt";
  fileOut = "b.txt";


  KB = 1024;
  MB = KB * KB;
  GB = MB * KB;
  TB = GB * GB;
  M = [TB,GB,MB,KB];
  Ms = ["Tb!!","Gb!","Mb","Kb"];
    
  # display above 200 Mb folders only
  dispAbove = 200 *MB; 

  # our tables
  
  # folders
  A = [];
  # node up
  B = [];
  # size on disk
  C = [];
  # folder path
  V = [];
  
  #current folder  
  F = "";
  
  print("Reading file:" + fileIn);
  
  fh = open(fileIn, "r", encoding="latin-1");

  # index of current item in our table
  k = 0;
  # node up index
  kF = -1;
  
  # status 1= reading folder files under Directory of...
  St = 0;

  # read from dir output file and calculate sizes  
  while True:
    buf = fh.readline();
    if not buf:
      break;
    A.append(buf);
    B.append(-1);
    C.append(0);
    V.append("");
    
    if St==0:
     # it is a new folder in the list
     a = buf.find("Directory of");
     if a>0:
       St=1;
       F = buf[a+13:];
       # obtain folder path
       v = s = z = "";
       for t in range(0,len(F)):
         s = F[t];
         if s!=chr(10) and s!=chr(13):
           v = v + s;
           z = s;
       if z!="\\":
         v = v + "\\";
       V[k] = v;

       kF = k;
      
       # find parent upper folder in our table 
       if k>0:
         p = k-1;
         while p>=0:
          if len(V[p])>0 and F.startswith( V[p] ):
            B[k]=p;
            break;
          p = p-1;        
         
       print(V[k]);

    k=k+1;
    
    if St==1:
     # obtain size of current folder (in bytes) from total
     a = buf.find("File(s)");
     if a>0:
       St=0;
       S = buf[a+7:];
       Q = "";
       for j in range(0,len(S)):
         c = S[j];
         if( ("0123456789").find(c)>=0 ):
           Q=Q+c;
       Size = int(Q);
       C[kF] = Size;
      
       # update size to all upper folders
       f = kF;
       while True:
         f = B[f];
         if( f<0 ):
           break;
         C[f]=C[f] + Size;

  fh = fh.close();
  
  print("Writing file:" + fileOut);
  
  fh = open(fileOut, "wt");
  
  fh.write("Directories above " + str(dispAbove) + " bytes" + chr(13));
  
  T = "";
  
  # display to file
  for i in range(0,len(A)):
    N = C[i];
    S = "";     # str(N)
    # format bytes to Tb,Gb,Mb
    if True:
     for w in range(0,3):
      k = N / M[w];
      if k>=1:
        S = ("%0.1f" % k) + Ms[w];
        break;  
    
    s = V[i];
    z = "";
    l = 0;
    
    # tab spaces
    if len(s)>0:
      T = "";
      for j in range(0,len(s)):
       if l>0:
        l = 0;
        z = "";
        
       z = z + s[j];
       if s[j]=="\\":
         T = T + "  ";
         if j>0 and s[j-1]!=":":
          l = 1;
    
    O = T + S + " " + z + chr(13);
    
    if N > dispAbove:
      fh.write(O);
  
  fh = fh.close();
