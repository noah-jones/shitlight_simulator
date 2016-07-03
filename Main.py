#!/usr/bin/env python3



import threading




class Light(threading.Thread):


    def __init__(self, x_size=None, y_size=None):
        super(Light, self).__init__()

        self.app = None
        self.canvas = None

        self.running = False

        self.x_size = x_size
        self.y_size = y_size

        self.start()

        while self.running == False:
            pass

        
    def run(self):

        from PyQt5 import QtCore, QtGui, QtWidgets

        from .Gui import Canvas

        self.app = QtWidgets.QApplication(['shitlight'])
        self.canvas = Canvas(self.x_size, self.y_size)
        self.canvas.show()

        self.running = True

        self.app.exec_()


    def set_color(self, colors):

        if self.canvas:   # wait until initilized
            self.canvas.queue.put(colors)
            self.canvas.trigger.emit()

