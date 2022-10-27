# importing libraries
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from datetime import datetime
import numpy as np
from scipy.io.wavfile import read
from PyQt5.QtWidgets import QMainWindow, QPushButton
import sounddevice as sd
import sys

# create dictionaries to store path to audio files in
number_dict = {}
number_dict_Dutch = {}

def numberSounds():
    path = r"add the path to the audio files here" # path to audio files

    for i in range(1, 60): # Create a dictionary with paths to the Farsi audio files
        number = i
        number_dict[i] = fr'{path}\{number}.wav'
    number_dict['half_past'] = fr'{path}\half_past.wav'
    number_dict['quarter_past'] = fr'{path}\quarter_past.wav'
    number_dict['quarter_to'] = fr'{path}\quarter_to.wav'
    number_dict['and'] = fr'{path}\and.wav'
    number_dict['it is'] = fr'{path}\it_is.wav'
    number_dict['minute'] = fr'{path}\minute.wav'
    number_dict['hour'] = fr'{path}\hour.wav'

    for i in range(1, 21): # Create a dictionary with paths to the Dutch audio files
        number = i
        number_dict_Dutch[i] = fr'{path}\{number}_Dutch.wav'
    number_dict_Dutch['half'] = fr'{path}\half_Dutch.wav'
    number_dict_Dutch['quarter_past'] = fr'{path}\quarter_past_Dutch.wav'
    number_dict_Dutch['quarter_to'] = fr'{path}\quarter_to_Dutch.wav'
    number_dict_Dutch['it is'] = fr'{path}\It_is_Dutch.wav'
    number_dict_Dutch['hour'] = fr'{path}\hour_Dutch.wav'
    number_dict_Dutch['past'] = fr'{path}\past_Dutch.wav'
    number_dict_Dutch['to'] = fr'{path}\To_Dutch.wav'

def check_hours_Dutch(hour): # function to make the clock say 'one' even when the clock says 13
    if hour > 12:
        hour -= 12
    h_sr, h_audio = read(number_dict_Dutch[hour])
    return h_sr, h_audio

def concatSoundsDutch(time): # function to create Dutch spoken segment of clock
    hour = int(time[0:2])
    minute = int(time[3:5])
    sr, hour_text = read(number_dict_Dutch['hour'])
    sr, it_is = read(number_dict_Dutch['it is'])
    h_sr, h_audio = check_hours_Dutch(hour)
    if minute == 00:
        audio1 = np.concatenate((it_is, h_audio, hour_text))
        sd.play(audio1, h_sr, blocking=True)
    elif minute == 15:
        sr, q_past = read(number_dict_Dutch['quarter_past'])
        audio2 = np.concatenate((it_is, q_past, h_audio))
        sd.play(audio2, h_sr, blocking=True)
    elif 1 <= minute <= 17:
        m_sr, m_audio = read(number_dict_Dutch[minute])
        p_sr, past = read(number_dict_Dutch['past'])
        audio3 = np.concatenate((it_is, m_audio, past, h_audio))
        sd.play(audio3, h_sr, blocking=True)
    hour += 1
    h_sr, h_audio = check_hours_Dutch(hour)
    if 18 <= minute <= 29:
        minute = 30 - minute
        m_sr, m_audio = read(number_dict_Dutch[minute])
        t_sr, to = read(number_dict_Dutch['to'])
        hp_sr, half = read(number_dict_Dutch['half'])
        audio4 = np.concatenate((it_is, m_audio, to, half, h_audio))
        sd.play(audio4, h_sr, blocking=True)
    elif minute == 30:
        hp_sr, half = read(number_dict_Dutch['half'])
        audio5 = np.concatenate((it_is, half, h_audio))
        sd.play(audio5, h_sr, blocking=True)
    elif 31 <= minute <= 44:
        minute -= 30
        m_sr, m_audio = read(number_dict_Dutch[minute])
        t_sr, past = read(number_dict_Dutch['past'])
        hp_sr, half = read(number_dict_Dutch['half'])
        audio6 = np.concatenate((it_is, m_audio, past, half, h_audio))
        sd.play(audio6, h_sr, blocking=True)
    elif minute == 45:
        q_sr, q_to = read(number_dict_Dutch['quarter_to'])
        audio7 = np.concatenate((it_is, q_to, h_audio))
        sd.play(audio7, h_sr, blocking=True)
    elif 46 <= minute <= 59:
        minute = 60 - minute
        m_sr, m_audio = read(number_dict_Dutch[minute])
        t_sr, to = read(number_dict_Dutch['to'])
        audio8 = np.concatenate((it_is, m_audio, to, h_audio))
        sd.play(audio8, h_sr, blocking=True)

def concatSounds(time): # function to create Farsi spoken segment of clock
    hour = int(time[0:2])
    minute = int(time[3:5])
    sr, hour_text = read(number_dict['hour'])
    sr, minute_text = read(number_dict['minute'])
    sr, it_is = read(number_dict['it is'])
    if minute == 45:
        hour += 1
        if hour > 12:
            hour -= 12
        h_sr, h_audio = read(number_dict[hour])
        sr, q_to = read(number_dict['quarter_to'])
        audio1 = np.concatenate((hour_text, q_to, h_audio, it_is))
        sd.play(audio1, h_sr, blocking=True)
    elif hour > 12:
        hour -= 12
    h_sr, h_audio = read(number_dict[hour])
    if minute == 15:
        sr, q_past = read(number_dict['quarter_past'])
        audio2 = np.concatenate((hour_text, h_audio, q_past, it_is))
        sd.play(audio2, h_sr, blocking=True)
    elif minute == 30:
        sr, half_past = read(number_dict['half_past'])
        audio3 = np.concatenate((hour_text, h_audio, half_past, it_is))
        sd.play(audio3, h_sr, blocking=True)
    elif minute == 00:
        audio3 = np.concatenate((hour_text, h_audio, it_is))
        sd.play(audio3, h_sr, blocking=True)
    elif minute != 15 and minute != 30 and minute != 45 and minute != 00:
        sr, and_text = read(number_dict['and'])
        m_sr, m_audio = read(number_dict[minute])
        audio4 = np.concatenate((hour_text, h_audio, and_text, m_audio, minute_text, it_is))
        sd.play(audio4, h_sr, blocking=True)

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        # creating clock window
        self.setWindowOpacity(0.7)
        self.setMinimumSize(QSize(300, 200))
        self.setWindowTitle("Speaking Clock")

        #creating buttons to make the clock speak
        self.pybutton = QPushButton('!صحبت کن', self) # speak in Farsi
        self.pybutton.setFont(QFont('Courier New', 11))
        self.pybutton2 = QPushButton('Spreek!', self) # speak in Dutch
        self.pybutton2.setFont(QFont('Courier New', 11))
        self.pybutton.resize(100, 50)
        self.pybutton2.resize(100, 50)
        self.pybutton.move(0,80)

        # setting colors for the window and buttons
        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
        self.setStyleSheet("border: 2px solid rgb(4, 61, 30); background-color: rgb(6, 69, 34); color: rgb(245, 245, 245)")
        self.setFixedSize(700, 500)

        #making the buttons work
        now = datetime.now()
        nowString = now.strftime(('%H:%M:%S'))

        self.pybutton.clicked.connect(lambda: concatSounds(nowString))
        self.pybutton2.clicked.connect(lambda: concatSoundsDutch(nowString))


        # The code below comes from https://www.geeksforgeeks.org/create-analog-clock-using-pyqt5-in-python/.
        # We only changed some aestetic features of this clock

        timer = QTimer(self)

        # adding action to the timer
        # update the whole code
        timer.timeout.connect(self.update)

        # setting start time of timer i.e 1 second
        timer.start(1000)

        # setting window title
        self.setWindowTitle('Clock')

        # setting window geometry
        self.setGeometry(200, 200, 300, 300)

        # creating hour hand
        self.hPointer = QtGui.QPolygon([QPoint(3, 2),
                                        QPoint(-3, 2),
                                        QPoint(0, -50)])

        # creating minute hand
        self.mPointer = QPolygon([QPoint(3, 2),
                                  QPoint(-3, 2),
                                  QPoint(0, -70)])

        # creating second hand
        self.sPointer = QPolygon([QPoint(1, 1),
                                  QPoint(-1, 1),
                                  QPoint(0, -90)])
        # colors
        # color for minute and hour hand
        self.hColor = QColor(52, 235, 134)
        self.mColor = QColor(39, 171, 98)

        # color for second hand
        self.sColor = QColor(8, 94, 47)

        # color for minute markers
        self.bColor = QColor(31, 153, 86)

        # method for paint event

    def paintEvent(self, event):

        # getting minimum of width and height
        # so that clock remain square
        rec = min(self.width(), self.height())

        # getting current time
        tik = QTime.currentTime()

        # creating a painter object
        painter = QPainter(self)
        # painter.setOpacity(0.7)

        # method to draw the hands
        # argument : color rotation and which hand should be pointed
        def drawPointer(color, rotation, pointer):

            # setting brush
            painter.setBrush(QBrush(color))

            # saving painter
            painter.save()

            # rotating painter
            painter.rotate(rotation)

            # draw the polygon i.e hand
            painter.drawConvexPolygon(pointer)

            # restore the painter
            painter.restore()

        # tune up painter
        painter.setRenderHint(QPainter.Antialiasing)

        # translating the painter
        painter.translate(self.width() / 2, self.height() / 2)

        # scale the painter
        painter.scale(rec / 200, rec / 200)

        # set current pen as no pen
        painter.setPen(QtCore.Qt.NoPen)

        # draw each hand
        drawPointer(self.hColor, (30 * (tik.hour() + tik.minute() / 60)), self.hPointer)
        drawPointer(self.mColor, (6 * (tik.minute() + tik.second() / 60)), self.mPointer)
        drawPointer(self.sColor, (6 * tik.second()), self.sPointer)

        # drawing background
        painter.setPen(QPen(self.bColor))

        # for loop
        for i in range(0, 60):

            # drawing background lines
            if (i % 5) == 0:
                painter.drawLine(87, 0, 97, 0)

            # rotating the painter
            painter.rotate(6)

        # ending the painter

        painter.end()


# Driver code; this makes the code run
if __name__ == '__main__':
    numberSounds()
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())