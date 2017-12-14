# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# =============================================================================
# testing codes
# =============================================================================

#int(str(89)[0])**1 + int(str(89)[1])**2


def sum_dig_pow(a, b):
    the_list = []
    for i in range(a, b+1):
        if len(str(i)) == 1:
            if i**1 == i:
                the_list.append(i)
                
        elif len(str(i)) == 2:
                if int(str(i)[0])**1 + int(str(i)[1])**2 == i:
                    the_list.append(i)
                    
        elif len(str(i)) == 3:
                if int(str(i)[0])**1 + int(str(i)[1])**2  + int(str(i)[2])**3 == i:
                    the_list.append(i)
                    
        elif len(str(i)) == 4:
                if int(str(i)[0])**1 + int(str(i)[1])**2  + int(str(i)[2])**3 + int(str(i)[3])**4 == i:
                    the_list.append(i)
                    
    return the_list
            
sum_dig_pow(89, 135)          
            
# =============================================================================
# BELOW CODE IS THE ONES
# =============================================================================

def sum_num(i):
    a_num = 0
    for N in range( 1, len(str(i)) + 1 ):
        a_num += int(str(i)[N-1]) ** N
        
    if a_num == i:
        return a_num
    
    
def sum_dig_pow(a, b):
    the_list = []
    
    for i in range(a, b+1):
        the_list.append( sum_num(i) )
                   
    return [x for x in the_list if x is not None]      

sum_dig_pow(1, 1000)           







        