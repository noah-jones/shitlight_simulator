

try:
    import queue
except ImportError:
    import Queue as queue   # python2.7
        

from PyQt5 import QtCore, QtGui, QtWidgets

class Canvas(QtWidgets.QWidget):


    trigger = QtCore.pyqtSignal()
    

    def __init__(self, x_size, y_size):
        super(Canvas, self).__init__()

        if x_size == None:
            self.x_size = 8
        else:
            self.x_size = x_size
        if y_size == None:
            self.y_size = 8
        else:
            self.y_size = y_size

        self.color = QtGui.QColor(128, 128, 128)
        self.colors = None
        
        self.initUI()

        self.trigger.connect(self.set_color)

        self.queue = queue.Queue()
        
        
    def initUI(self):      

        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle('Lights')


        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Background, QtCore.Qt.black)
        self.setAutoFillBackground(True)
        self.setPalette(palette)

        self.show()


    def paintEvent(self, e):

        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawPoints(qp)
        qp.end()
        
        
    def drawPoints(self, qp):
      
        #qp.setPen(QtCore.Qt.NoPen)
        #gradient = QtGui.QRadialGradient(50,50,50,50,50)
        color0 = self.color
        #color1 = QtGui.QColor(0, 0, 255)
        #gradient.setColorAt(0, color0)
        #gradient.setColorAt(1, color1)
        brush = QtGui.QBrush() #gradient)
        brush.setStyle(QtCore.Qt.SolidPattern)
        size = self.size()

        if self.colors == None:

            brush.setColor(color0)
            qp.setBrush(brush)
        
            for i in range(self.x_size):
                for j in range(self.y_size):
                    x = size.width() / self.x_size * ( i + .5)
                    y = size.height() / self.y_size * (j + .5)
                    #gradient.setCenter(QtCore.QPoint(x, y))
                    qp.drawEllipse(QtCore.QPoint(x, y), 20, 20)
  
        elif self.color == None:

            assert len(self.colors) == self.x_size * self.y_size

            for i in range(self.x_size):
                for j in range(self.y_size):
                    color1 = self.colors[i*self.y_size+j]
                    brush.setColor(QtGui.QColor(*color1))
                    qp.setBrush(brush)
                    x = size.width() / self.x_size * ( i + .5)
                    y = size.height() / self.y_size * (j + .5)
                    #gradient.setCenter(QtCore.QPoint(x, y))
                    qp.drawEllipse(QtCore.QPoint(x, y), 20, 20)


    def set_color(self):
        colors = self.queue.get(False)
        if isinstance(colors, tuple):
            self.color = QtGui.QColor(*colors)
            self.colors = None
        if isinstance(colors, list):
            self.colors = colors
            self.color = None
        self.update()

