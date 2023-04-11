#!/usr/bin/python3


'''My list '''


class MyList(list):
    ''' Inherits from in-built list class '''

    def print_sorted(self):
        ''' returns a sorted list '''
        return sorted(self)
