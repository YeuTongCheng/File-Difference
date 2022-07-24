IDENTICAL = -1

def singleline_diff(line1, line2):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
    Output:
      Returns the index where the first difference between
      line1 and line2 occurs.

      Returns IDENTICAL if the two lines are the same.
    """
    if (line1=='') or (line2==''):
        diff=0
    if (line1=='') and (line2==''):
        diff=IDENTICAL        
    if line1!=line2:
        for index in range(len(min(line1,line2))) :
            difference= line1[index] != line2[index]
            if not difference:
                diff=len(min(line1,line2))
            else:
                diff= index
                break
                
    if len(line1)==len(line2):
        for index in range(len(line1)):
            difference= line1[index] != line2[index]
            if not difference:
                diff=IDENTICAL
            else:
                diff= index
                break
                
            
    return diff

def singleline_diff_format(line1, line2, idx):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
      idx   - index at which to indicate difference
    Output:
      Returns a three line formatted string showing the location
      of the first difference between line1 and line2.

      If either input line contains a newline or carriage return,
      then returns an empty string.

      If idx is not a valid index, then returns an empty string.
    """
        
    if ("\n" in line1 or "\n" in line2) or ("\r" in line1 or "\r" in line2)\
       or (idx not in range(len(min(line1,line2))+1)):
        result1=""
    else :
        result1=line1+"\n"+ "="*(idx)+"^"+"\n"+line2+"\n"
    
    return result1

def multiline_diff(lines1, lines2):
    """
    Inputs:
      lines1 - list of single line strings
      lines2 - list of single line strings
    Output:
      Returns a tuple containing the line number (starting from 0) and
      the index in that line where the first difference between lines1
      and lines2 occurs.
      
      Returns (IDENTICAL, IDENTICAL) if the two lists are the same.
    """
    if (lines1==[]) or (lines2==[]):
        result2=(0,0)
    if (lines1==[]) and (lines2==[]):
        result2=(IDENTICAL,IDENTICAL)     
        
    for index in range(min(len(lines1),len(lines2))):
        compare=singleline_diff(lines1[index], lines2[index])
        if compare==-1 and lines1==lines2:
            result2=(IDENTICAL,IDENTICAL)
        elif compare==-1 and lines1!=lines2:
            result2=(index+1,0)
        else:
            result2=(index,compare)
            break
    return result2

def get_file_lines(filename):
    """
    Inputs:
      filename - name of file to read
    Output:
      Returns a list of lines from the file named filename.  Each
      line will be a single line string with no newline ('\n') or 
      return ('\r') characters.

      If the file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    with open(filename,"rt") as file:
        list_of_file=[]
        for line in file.readlines():
            clean=line.replace("\n","")
            list_of_file.append(clean)
    return list_of_file
def file_diff_format(filename1, filename2):
    """
    Inputs:
      filename1 - name of first file
      filename2 - name of second file
    Output:
      Returns a four line string showing the location of the first
      difference between the two files named by the inputs.

      If the files are identical, the function instead returns the
      string "No differences\n".

      If either file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    file1=get_file_lines(filename1)
    file2=get_file_lines(filename2)
    if file1==file2:
        return "No differences\n"
    else:
        line_number=multiline_diff(file1, file2)[0]
        return "Line "+str(line_number)+":\n"+\
singleline_diff_format(file1[line_number], file2[line_number],multiline_diff(file1, file2)[1] )
    




