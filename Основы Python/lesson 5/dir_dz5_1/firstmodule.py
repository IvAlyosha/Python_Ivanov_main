import os

def adddir(first,end):
    path = os.getcwd()
    for i in range(first,end):
         os.mkdir(f'{path}\dir_{i}')
def removedir(first,end):
    path = os.getcwd()
    for i in range(first,end):
        os.removedirs(f'{path}\dir_{i}')

