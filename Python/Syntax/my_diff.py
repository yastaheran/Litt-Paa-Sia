"""
The program compares two files. It will open the files in read only mode and 
reads one line at a time and compares them after stripping off any trailing 
whitespaces (it ignores new-line and spaces at the end of the line).
"""
#!/usr/bin/python
import sys

def main (original, modified):
    # Open file for reading in text mode    
    o = open(original)
    m = open(modified)
    
    # Print confirmation
    print("-----------------------------------")
    print("Comparing files ", original + " and " + modified, sep='\n')
    print("-----------------------------------")
    
    # Goes through the files line by line
    for o_line, m_line in o, m:
        # Strip the leading whitespaces
        o_line = o_line.rstrip()
        m_line = m_line.rstrip()        
        
        #if a line has not been modified, a 0 is added in front
        if o_line == m_line:
            print('0', '%s' % o_line)
            # If a line has been modified
            # = a deletion (-) of the original line
            # = an addition (+) of the modified line
        elif o_line != m_line:
            print('-', '%s' % o_line)
            print('+', '%s' % m_line)
    
    # Close the files
    o.close()
    m.close()

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])