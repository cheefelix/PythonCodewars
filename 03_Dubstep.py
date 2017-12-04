# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 00:35:06 2017

@author: Felix
"""

# https://www.codewars.com/kata/dubstep/train/python

'''
song = "WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB"
song = "AWUBWUBWUBBWUBWUBWUBC"
song = 'WUBAWUBBWUBCWUB'
'''

# solution
def song_decoder2(song):
    import re
    return re.sub('(WUB)+', ' ', song).strip()
    

# Pass all test except the last
def song_decoder(song):

    a = "  "
    b = "   "
    c = ""
    
    song = song.replace('WUB', ' ')
    song = song.replace('W', ' W')
                
    if a in song:
        song = song.replace(a,c)
    elif b in song:
        song = song.replace(b,c)
    
    if song[0] == ' ' and song[-1] == ' ':
        song = song[1:-1]
        
    elif song[0] == ' ':
        song = song[1::]
        
    elif song[-1] == ' ':
        song = song[0:-1]
    
    return song

    
    