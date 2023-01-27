from MobileCritter import MobileCritter
from Insect import Insect


class Spider(Insect, MobileCritter):
    def __init__(self):
        Insect.__init__(self)

    def move_right(self):
        """moves this spider's position 1 unit right"""
        x = self.get_position()[0]
        y = self.get_position()[1]
        self.position = [x+1, y]

    def move_left(self):
        """moves this spider's position 2 units left"""
        x = self.get_position()[0]
        y = self.get_position()[1]
        self.position = [x-2, y]

    def move_up(self):
        """moves this spider's position 1 unit up"""
        x = self.get_position()[0]
        y = self.get_position()[1]
        self.position = [x, y+1]

    def move_down(self):
        """moves this spider's position 2 units down"""
        x = self.get_position()[0]
        y = self.get_position()[1]
        self.position = [x, y-2]

    def __str__(self):
        return u'\u1F577'
