# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 19:38:03 2017

@author: Felix
"""

'''
Given: an array containing hashes of names

Return: a string formatted as a list of names separated by commas except for the last two names, which should be separated by an ampersand.

Example:

namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# returns 'Bart, Lisa & Maggie'

namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
# returns 'Bart & Lisa'

namelist([ {'name': 'Bart'} ])
# returns 'Bart'

namelist([])
# returns ''

'''


a = [ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}, {'name': 'tom'}, {'name': 'jerry'} ]


### testing
list_of_names = []

for dicts in a:
    #print ( dicts.items() )
    for key, value in dicts.items():
        #print (value)
        #temp = [key, value]
        list_of_names.append( value )
    
    
list_of_names     

if len(list_of_names) == 1:
    print ( list_of_names[0] )
    
elif len(list_of_names) == 2:
    print ( list_of_names[0] + ' & ' + list_of_names[1] )
    
elif len(list_of_names) > 2:
    for i in range(len(list_of_names)-2):    
        print ( list_of_names[i] + ', ' + list_of_names[-2] + ' & ' + list_of_names[-1] )    

else:
    print ( [] )

    
### function        
def namelist(names):   
    list_of_names = []
    
    for dicts in names:
        for key, value in dicts.items():
            list_of_names.append( value )  
                       
    if len(list_of_names) == 1:
        return ( list_of_names[0] )
    
    elif len(list_of_names) == 2:
        return ( list_of_names[0] + ' & ' + list_of_names[1] )
        
    elif len(list_of_names) > 2:
        return ( ', '.join( list_of_names[0:len(list_of_names)-2] ) + ', ' + list_of_names[-2] + ' & ' + list_of_names[-1] )    
    
    else:
        return ( '' )
        
        
namelist(a)        