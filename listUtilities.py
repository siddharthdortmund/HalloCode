''' This module contains utility functions for an integer list '''

from random import randint
from sys import maxsize

NOT_FOUND = -maxsize - 1


def generateIntList(length):
    '''
    Generates a list of random integers and returns the same
    params:
        length - length of the list which must be generated
    ret:
        list object of len = length
        
    NOTE: the random integers generated are in the range (0,500)
    '''
    list1 = []
    for i in range(length):
        list1.append(randint(0,20))
    
    return list1


def getIntListFromUser(length):
    '''
    Generates a list of integers by inputting values from user and returns the
    same
    params:
        length - length of the list which must be generated
    ret:
        list object of len = length
    exception:
        ValueError if input is not an integer or not in the range(0,20)        
    '''
    list1 = []
    gotException = False
    val = 0
    print('Enter {0} integers for the list.\
 Each integer must be in the range (0,20)'.format(length) )
    
    for i in range(length):
        try:
            val = int(input("Enter integer for index {0}: ".format(i)) )
        except:
            gotException = True
        finally:
            if gotException or not(0<=val<=20):
                raise ValueError("Entered value not integer or not in range(0,20)" )
            else:
                list1.append(val)
                    
    return list1
    
def printIntList(l1):
    '''
    prints the input list of integers
    params:
        l1- input list
    ret:
        
    '''
    for item in l1:
        print( '{0:03d}'.format(item),end=' ')
    
    print()

def kThUniqueElement( listObj, kTh ):
    '''
    This function returns the kTh unique element in the list.
    params:
        listObj - list of int objects
        kTh - int object - positive number
    ret:
        int object - value of the kTh unique element in the list, if present.
        NOT_FOUND, if kTh unique element not found
    
    IMPORTANT: use dict Python data type for this problem    
    
    NOTE: After you complete coding this function, for testing purpose, 
    generate a large size list of int objects. For this, you can use the 
    already available generateIntList() function
    
    Example:
        #1:
            if listObj = [1,2,3,4,5,6,7], kTh = 5.
            Since all the elements are unique (no repitition), 
            1 is the first unique element
            2 is the second unique element,
            so on,
            
            5 is the 5th unique element i.e. kTh unique element. 
            Hence 5 is to be returned
        
        #2:
            if listObj = [1,2,3,1,1,2,2,7,9,7,13,17], kTh = 3.
            values 1, 2, 7 all repeat themselves at least two times,
            3 is the first unique element,
            9 is the second unique element,
            13 is the third unique element i.e kth.
            Hence 13 is to be returned
        
        #3:
            if listObj = [1,2,3,1,1,2,2,7,9,7,13,17], kTh = 5.
            values 1, 2, 7 all repeat themselves at least two times,
            3 is the first unique element,
            9 is the second unique element,
            13 is the third unique element,
            17 is the forth unique element.
            There are no more unique elements.
            Hence NOT_FOUND is to be returned
            
    '''
    # Your code here
            
    data=listObj[:];count=0;v=0
    
    d=dict((x, data.count(x)) for x in data)
    #d.sort()
    #print(d)
    for i,c in enumerate( data):
        if d[c]==1:
            count+=1
            if count==kTh:
                return c
    else:
       return NOT_FOUND
          