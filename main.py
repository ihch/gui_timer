# -*- coding:utf-8 -*-
import kivy
kivy.require('1.9.2')
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
import pygame.mixer as mixer
import datetime
import time
import threading
from logging import getLogger, StreamHandler, DEBUG

logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)

ZeroTime = datetime.datetime.strptime("00:00:00", "%H:%M:%S")

class TimerWidget(Widget):
#    labeldatetime = ObjectProperty(None)
#    start1 = ObjectProperty(None)
    pass

class MyApp(App):
    f_timer = False
    def timer(self, t=None):
        logger.debug("ttype: {}".format(type(t)))
        s = datetime.datetime.now()
        mixer.init()
        mixer.music.load("./trumpet2.mp3")

        while True:
            now = datetime.datetime.now()
            delta = now - s
            self.root.labeldatetime.text = "{}".format(delta)[:-7]
            logger.debug("now - s: {}".format(delta))
            if (t - ZeroTime <= delta):
                break
            time.sleep(1)
        mixer.music.play(-1)
        time.sleep(10)
        self.root.labeldatetime.text = "(´・ω・｀)"
        mixer.music.stop()

    def start1_clicked(self, src):
        logger.info("button_clicked")
        #self.root.labeldatetime.text = str(datetime.datetime.now())
        t = datetime.datetime.strptime("00:00:10", "%H:%M:%S")
        logger.debug("ttype: {}, t: {}".format(type(t), t))
        th = threading.Thread(target=self.timer, name="th", args=([t]))
        th.setDaemon(True)
        th.start()

    def start2_clicked(self, src):
        logger.info("button_clicked")
        #self.root.labeldatetime.text = str(datetime.datetime.now())
        t = datetime.datetime.strptime("00:05:00", "%H:%M:%S")
        logger.debug("ttype: {}, t: {}".format(type(t), t))
        th = threading.Thread(target=self.timer, name="th", args=([t]))
        th.setDaemon(True)
        th.start()

    def build(self):
        self.root = TimerWidget()
        self.root.start1.bind(on_press=self.start1_clicked)
        self.root.start2.bind(on_press=self.start2_clicked)
        return self.root


if __name__ == '__main__':
    MyApp().run()

