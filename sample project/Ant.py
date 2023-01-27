from MobileCritter import MobileCritter
from Insect import Insect


class Ant(Insect, MobileCritter):

    def __init__(self):
        Insect.__init__(self)

    def move_right(self):
        """moves this ant's position 1 unit right"""
        x = self.get_position()[0]
        y = self.get_position()[1]
        self.position = [x+1, y]

    def move_left(self):
        """moves this ant's position 1 unit left"""
        x = self.get_position()[0]
        y = self.get_position()[1]
        self.position = [x-1, y]

    def move_up(self):
        """moves this ant's position 2 units up"""
        x = self.get_position()[0]
        y = self.get_position()[1]
        self.position = [x, y+2]

    def move_down(self):
        """moves this ant's position 2 units down"""
        x = self.get_position()[0]
        y = self.get_position()[1]
        self.position = [x, y-2]

    def __str__(self):
        return u'\u1F41C'
