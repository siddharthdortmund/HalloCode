# -*- coding: utf-8 -*-
""" Checks if two strings are anagrams of each other 
e.g. <1> 'north' and 'thorn'
e.g. <2> 'west' and 'stew'
e.g. <3> 'pole' and 'lope'
e.g. <4> 'eastern' and 'nearest'
"""

import sys

__moduleName__ = ""
__args__ = "s1 s2"
__expln__ ="s1 and s2 are input words"

def printUsage():
    print('python {0} {1}\nWhere,\n{2}'.format(__moduleName__,
          __args__,__expln__ ) )
    
    
def run(s1,s2):
    """ Checks if s1 and s2 are anagrams of each other

    params:
        s1 and s2 - two input words
    ret:
        True if s1 and s2 are anagrams, False otherwise
        
    IMPORTANT: You should use dict Python data type to solve this problem
    HINT:
        1. Create two character histograms, one each for s1 and s2
        2. if the histograms of s1 and s2 are equal, then s1 and s2 are anagrams
    """
    # Your code here
    h1 = {};h2={}
    for ch in s1:
        if ch.isalpha():
            h1[ch] = h1.get( ch, 0 ) + 1

    for ch in s2:
        if ch.isalpha():
            h2[ch] = h2.get( ch, 0 ) + 1
    for key,value in h1.items():
        if h2.get(key)==h1.get(key) and (len(h1)==len(h2)):
            return True
        else:
            return False
        
def test():
    ''' Test function for run() '''
    
    testData =  [ 
        ('north','thorn', True ),
        ('eastern','nearest', True),
        ('west','stew', True),
        ('pole', 'lope', True),
        ('latitude', 'altitude', True ),
        ('lattitude', 'altitude', False ),
        ('aabc', 'abbc', False )
    ]
    
    for testItem in testData:
        res = run(testItem[0],testItem[1])
        print('Ran isAnagram with {0} and {1}, expecting {2}, got {3}, status: {4} '.format( 
        testItem[0], testItem[1], testItem[2], res, ('FAIL','PASS')[res==testItem[2]] ) )

    
def main(argv):
    s1 = s2 = ''
    try:
        if len(argv)==1 and argv[0]=='test':
            test()
            return
        elif len(argv)!=2:
            raise Exception('ArgumentCountError')

        s1 = argv[0]
        s2 = argv[1]
    except:
        # In case of exception, print usage and exit
        printUsage()
        return
        
    anagram = run(s1,s2)
    print('{0} and {1} are{2} anagrams'.format(s1,s2,' NOT' if not anagram else ''))
    return
        
    
if __name__ == "__main__":
    main(sys.argv[1:])
# -*- coding: utf-8 -*-

