from MobileCritter import MobileCritter
from Insect import Insect


class Spider(Insect, MobileCritter):
    def __init__(self):
        Insect.__init__(self)

    def move_right(self):
        """moves this spider's position 1 unit right"""
        # todo
        raise NotImplementedError()

    def move_left(self):
        """moves this spider's position 2 units left"""
        # todo
        raise NotImplementedError()

    def move_up(self):
        """moves this spider's position 1 unit up"""
        # todo
        raise NotImplementedError()

    def move_down(self):
        """moves this spider's position 2 units down"""
        # todo
        raise NotImplementedError()

    def __str__(self):
        return u'\u1F577'
