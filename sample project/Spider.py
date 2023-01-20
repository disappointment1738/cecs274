from MobileCritter import MobileCritter
from Insect import Insect


class Spider(Insect, MobileCritter):
    def __init__(self):
        Insect.__init__(self)

    def move_right(self):
        """moves this spider's position 1 unit right"""
        # need to check if ant touches border, if yes, end.
        # if no, continue and move one
        raise NotImplementedError()

    def move_left(self):
        """moves this spider's position 2 units left"""
        # need to check if ant touches border, if yes, end.
        # if no, continue and move one
        raise NotImplementedError()

    def move_up(self):
        """moves this spider's position 1 unit up"""
        # need to check if ant touches border, if yes, end.
        # if no, continue and move one
        raise NotImplementedError()

    def move_down(self):
        """moves this spider's position 2 units down"""
        # need to check if ant touches border, if yes, end.
        # if no, continue and move one
        raise NotImplementedError()

    def __str__(self):
        return u'\u1F577'
