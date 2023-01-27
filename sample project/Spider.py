from MobileCritter import MobileCritter
from Insect import Insect


class Spider(Insect, MobileCritter):
    def __init__(self):
        Insect.__init__(self)

    def move_right(self):
        """moves this spider's position 1 unit right"""
        MobileCritter.move_right()

    def move_left(self):
        """moves this spider's position 2 units left"""
        MobileCritter.move_left()

    def move_up(self):
        """moves this spider's position 1 unit up"""
        MobileCritter.move_up()

    def move_down(self):
        """moves this spider's position 2 units down"""
        MobileCritter.move_down()

    def __str__(self):
        return u'\u1F577'
