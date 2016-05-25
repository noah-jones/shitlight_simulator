#!/usr/bin/env python3



import time


import Main


x_size = 8
y_size = 8

refresh_rate = 0.02

light = Main.Light(x_size, y_size)


light.set_color((0,255,0))
time.sleep(2)


while True:
    for i in range (256):
        colors = [(i,i,i)] * x_size * y_size
        light.set_color(colors)
        time.sleep(refresh_rate)
