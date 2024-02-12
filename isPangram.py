# -*- coding: utf-8 -*-
""" Checks if a given sentence is a pangram.
A pangram is a sentence that contains all the letters of the English alphabet
at least once. 
Here, the case of the every letter is ignored i.e. a lowercase letter is 
treated same as an uppercase letter.
e.g. <1> "The quick brown fox jumps over the lazy dog."
"""

import sys

__moduleName__ = ""
__args__ = ""
__expln__ =""

def printUsage():
    print('python {0}'.format(__moduleName__) )



def run(s):
    """ Checks if s is a pangram 
    params:
        s - input sentence
    ret:
        True if s is a pangram, False otherwise

    IMPORTANT: You should use dict Python data type to solve this problem        
    HINT:
        1. Initialize counters for ascii lowercase character. To do this, use
           dict, where key is ascii lowercase character and value = 0
        2. Now, scan every alpahbet in the input sentence (ignore case), and 
           increment the counter for that alphabet in the dict object
        3. Finally, scan the values of all keys in the dict object. If all the
           values are greater than 0, then the input sentence is pangram        
    """
    # Your code here
    
    
    import string
    d = dict.fromkeys(string.ascii_lowercase, 0)
    s1=s.lower()
    #print(s1)
    #print(d)
    h1={}
    for ch in s1:
        if ch.isalpha():
            h1[ch]=h1.get(ch,0)+1
   # print(h1)
   #for key,value in d.items():
       
    if (len(h1)==26):
      #print (key)
      return True
    else:
       return False
       

def test():
    ''' Test function for run() '''
    
    # Test data in the format input-value:expected-value
    testData =  {
        "The quick brown fox jumps over the lazy dog.":True,
        "Pack my box with five dozen liquor jugs.":True,
        "Pack my box with five dozen liquor.":False
    }
    
    for k,v in testData.items():
        res = run(k)
        print('Ran isPangram with \"{0}\"\n\texpecting {1}\n\tgot {2}\n\tstatus: {3}'.format( 
        k, v, res, ('FAIL','PASS')[res==v] ) )

    
def main(argv):
    s = ''
    try:
        # expecting a single argument
        if len(argv)==1 and argv[0]=='test':
            test()
            return
        elif len(argv)>=1:
            raise Exception('ArgumentCountError')
            
        s = input("Enter sentence: ")

    except:
        # In case of exception, print usage and exit
        printUsage()
        return
        
    pangram = run(s)
    print('\"{0}\" is{1} a pangram'.format(s,' NOT' if not pangram else ''))
    return
        
    
if __name__ == "__main__":
    main(sys.argv[1:])
# -*- coding: utf-8 -*-

