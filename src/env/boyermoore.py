# Reference from https://www.geeksforgeeks.org/boyer-moore-algorithm-for-pattern-searching/
# Modified the data structure and the number of args

# NO_OF_CHARS = 256
 
def badCharHeuristic(string):
    '''
    The preprocessing function for
    Boyer Moore's bad character heuristic
    '''
    
    badCharDict = {}

    # Store last occurence with respective chars
    for i in range(len(string)):
        badCharDict.update({string[i]:i})
 
    # return the dict
    return badCharDict

def search(txt, pat):
    '''
    A pattern searching function that uses Bad Character
    Heuristic of Boyer Moore Algorithm
    '''
    m = len(pat)
    n = len(txt)
 
    # create the bad character dict by calling
    # the preprocessing function badCharHeuristic()
    # for given pattern
    badChar = badCharHeuristic(pat)

    # s is shift of the pattern with respect to text
    s = 0
    while(s <= n-m):
        j = m-1
 
        # Keep reducing index j of pattern while
        # characters of pattern and text are matching
        # at this shift s
        while j>=0 and pat[j] == txt[s+j]:
            j -= 1
 
        # If the pattern is present at current shift,
        # then index j will become -1 after the above loop
        if j<0:
            print("Pattern occur at shift = "+str(s))
 
            '''   
                Shift the pattern so that the next character in text
                      aligns with the last occurrence of it in pattern.
                The condition s+m < n is necessary for the case when
                   pattern occurs at the end of text
            '''
            # Handling when the key is not in the dict
            if badChar.get(txt[s+m]) is not None:
                s += (m-badChar[txt[s+m]] if s+m<n else 1)
            else:
                s += (m-(-1) if s+m<n else 1)
        else:
            '''
               Shift the pattern so that the bad character in text
               aligns with the last occurrence of it in pattern. The
               max function is used to make sure that we get a positive
               shift. We may get a negative shift if the last occurrence
               of bad character in pattern is on the right side of the
               current character.
            '''
            # Handling when the key is not in the dict
            if badChar.get(txt[s+m]) is not None:
                s += max(1, j-badChar[txt[s+j]])
            else:
                s += max(1, j-(-1))
 
# Driver program to test above function
def main():
    txt = "EIFSFDEIEF STIMA OJRFJF"
    pat = "STIMA"
    search(txt, pat)
 
if __name__ == '__main__':
    main()