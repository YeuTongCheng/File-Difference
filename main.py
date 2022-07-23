"""
Project for Week 4 of "Python Data Representations".
Find differences in file contents.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

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
    if line1!=line2:
        for index in range(len(min(line1,line2))) :
            difference= line1[index] != line2[index]
            if difference:
                diff= index
                break
            else:
                diff=len(min(line1,line2))
    if len(line1)==len(line2):
        for index in range(len(line1)):
            difference= line1[index] != line2[index]
            if difference:
                diff= index
                break
            else:
                diff=IDENTICAL
            
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
    if ("\n" in line1 or "\n" in line2) or ("\r" in line1 or "\r" in line2) or (idx not in range(len(min(line1,line2)))):
        result=" "
    else :
        result=line1+"\n"+ "="*(idx)+"^"+"="*((len(min(line1,line2))-1)-idx)+"\n"+line2+"\n"
    
    return result





