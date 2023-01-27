from MobileCritter import MobileCritter
from Insect import Insect


class Ant(Insect, MobileCritter):

    def __init__(self):
        Insect.__init__(self)

    def move_right(self):
        """moves this ant's position 1 unit right"""
        MobileCritter.move_right()

    def move_left(self):
        """moves this ant's position 1 unit right"""
        MobileCritter.left()

    def move_up(self):
        """moves this ant's position 2 units up"""
        MobileCritter.up()

    def move_down(self):
        """moves this ant's position 2 units down"""
        MobileCritter.down()

    def __str__(self):
        return u'\u1F41C'
