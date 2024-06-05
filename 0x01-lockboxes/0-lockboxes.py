#!/usr/bin/python3

""" Method to determine if all the boxes can be opened """

def canUnlockAll(boxes):
    """ Returns True if all the boxes can be opened or False if not """
    for key in range(1, len(boxes)):
        flag = False
        for box in range(len(boxes)):
            if key in boxes[box] and key != box:
                flag = True
                break
        if not flag:
            return False
    
    return True