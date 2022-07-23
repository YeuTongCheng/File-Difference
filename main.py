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
        x=0
        for char in min(line1,line2) :
            difference= char != max(line1,line2)[x]
            if difference:
                diff= x
                break
            else:
                diff=len(min(line1,line2))
                x+=1
    if len(line1)==len(line2):
        x=0
        for char in line1:
            difference= char != line2[x]
            if difference:
                diff= x
                break
            else:
                diff=IDENTICAL
                x+=1
            
    return diff





