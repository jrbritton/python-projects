#-------------------------------------------------------------------------------
# Name:        time format
# Purpose:     Takes a time in seconds and makes it readable
#
#
# Author:      jrbritt
#
# Created:     02/04/2023
# Copyright:   (c) jrbritt 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def format_duration(seconds):
    if seconds == 1:
        print(f'{seconds} second')
    elif seconds > 1 and seconds < 60:
        print(f'{seconds} seconds')
    elif seconds == 60:
        print('1 minute')
    elif seconds == 61:
        print('1 minute and 1 second')
    elif seconds >= 62 and seconds < 120:
        minutes = int(seconds / 60)
        seconds = seconds % 60
        print(f'{minutes} minute and {seconds} seconds')
    elif seconds == 120:
        print('1 hour')
    elif seconds >= 120 and seconds < 3600:
        minutes = int(seconds % 60)
        seconds = int(seconds % 3600)
        if seconds == 1:
            print(f'{minutes} minutes and {seconds} second')
        elif seconds > 1 and seconds < 60:
            print(f'{minutes} minutes and {seconds} seconds')
        elif seconds >= 60:
            minutes = int(seconds/60)
            seconds = seconds % 60
            print(f'{minutes} minutes and {seconds} seconds')
    elif seconds >= 3600 and seconds < 7200:
        hours = int(seconds / 3600)
        minutes = int(seconds / 60)
        seconds = seconds % 60
        print(f'{hours} hour {minutes} minutes and {seconds} seconds')


format_duration(123)