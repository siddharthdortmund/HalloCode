# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 19:19:10 2016

@author: siddharth
"""

# -*- coding: utf-8 -*-
'''5r5fr
This module computes the histogram for a given sentence.
That is, the character frequency count is computed for the given sentence
'''

def getHistogram( sentence ):
    ''' Generates the character histogram for the given sentence
    params:
        sentence - str object - input sentence
    ret:
        dict object containing the character histogram
    '''
    histogram = {}
    for ch in sentence:
        if ch.isalpha():
            histogram[ch] = histogram.get( ch, 0 ) + 1

    return histogram
    
def testHistogramGenerator():
    ''' Tests the getHistogram() function with sample inputs
    params:
        
    ret:
        
    '''
    test_data = [ 'Welcome to Anveshana Education!',
                'The name of the course is Programming With Python',
                'abcdefghijklmnopqrstuvwxyz'*3 ]
    
    for data in test_data:
        print('*'*90)
        print()
        print( 'Testing with sentence:\n{0}'.format(data) )
        print('Histogram:')
        i = 0
        for k,v in getHistogram(data).items():
            print( 'char: {0:<2}, count: {1:<3}'.format(k,v), end='\t' )
            i += 1
            if i%3==0:
                print()
        print()
        print('*'*90)
        
if __name__ == '__main__':
    testHistogramGenerator()




#def histogramV2():
    #d= getHistogram('Samsung IS SMARTP')
   # result = {}
   # for key, value in d.items():

     #   lower_key = key.lower()
      #  result[lower_key] = result.get(lower_key, 0) + value
   # return result
# add changes
                
def histogramV2():
    d= {'a':2,'A':12,'c':11}
    result = {}
    for key, value in d.items():
       lower_key = key.lower()
       result[lower_key] = result.get(lower_key, 0) + value
    return result
   
    
  
                
    return histv2,sorted_list  
    
    '''As I am not sure of the sorted list I am returning the normal list'''
                
            
            
