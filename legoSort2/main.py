#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from pybricks import ev3brick as brick

import ubinascii, urequests, ujson, utime

Key = 'zZn5lZCJeeOQ1qhDOzO1QsJem8nFUTkSNL268RZGkY'

# Write your program here
ev3 = EV3Brick()
speed = 50
twist = Motor(Port.A)
dump = Motor(Port.B)

pos0 = 15 # 1x1
pos1 = 48 # 1x2
pos2 = 88 # 2x2
pos3 = 118 # 2x3
pos4 = 150 # 2x4
pos5 = 182 # 1x3
pos6 = 220 # unknown



def SL_setup():
     urlBase = "https://api.systemlinkcloud.com/nitag/v2/tags/"
     headers = {"Accept":"application/json","x-ni-api-key":Key}
     return urlBase, headers
     
def Put_SL(Tag, Type, Value):
     urlBase, headers = SL_setup()
     urlValue = urlBase + Tag + "/values/current"
     propValue = {"value":{"type":Type,"value":Value}}
     try:
          reply = urequests.put(urlValue,headers=headers,json=propValue).text
     except Exception as e:
          print(e)         
          reply = 'failed'
     return reply

def Get_SL(Tag):
     urlBase, headers = SL_setup()
     urlValue = urlBase + Tag + "/values/current"
     try:
          value = urequests.get(urlValue,headers=headers).text
          data = ujson.loads(value)
          #print(data)
          result = data.get("value").get("value")
     except Exception as e:
          print(e)
          result = 'failed'
     return result
     
def Create_SL(Tag, Type):
     urlBase, headers = SL_setup()
     urlTag = urlBase + Tag
     propName={"type":Type,"path":Tag}
     try:
          urequests.put(urlTag,headers=headers,json=propName).text
     except Exception as e:
          print(e) 

def TurnMotor(pos):
    if pos == 0:
         twist.run_target(speed, pos0, stop_type = Stop.COAST, wait = True)
         dump.run_target(speed, 180, stop_type = Stop.COAST, wait = True)
         dump.run_target(speed, 0, stop_type = Stop.COAST, wait = True)
         twist.run_target(speed, 0, stop_type = Stop.COAST, wait = True)
    if pos == 1:
         twist.run_target(speed, pos1, stop_type = Stop.COAST, wait = True)
         dump.run_target(speed, 180, stop_type = Stop.COAST, wait = True)
         dump.run_target(speed, 0, stop_type = Stop.COAST, wait = True)
         twist.run_target(speed, 0, stop_type = Stop.COAST, wait = True)
    if pos == 2:
         twist.run_target(speed, pos2, stop_type = Stop.COAST, wait = True)
         dump.run_target(speed, 180, stop_type = Stop.COAST, wait = True)
         dump.run_target(speed, 0, stop_type = Stop.COAST, wait = True)
         twist.run_target(speed, 0, stop_type = Stop.COAST, wait = True)
    if pos == 3:
         twist.run_target(speed, pos3, stop_type = Stop.COAST, wait = True)
         dump.run_target(speed, 180, stop_type = Stop.COAST, wait = True)
         dump.run_target(speed, 0, stop_type = Stop.COAST, wait = True)
         twist.run_target(speed, 0, stop_type = Stop.COAST, wait = True)
    if pos == 4:
         twist.run_target(speed, pos4, stop_type = Stop.COAST, wait = True)
         dump.run_target(speed, 180, stop_type = Stop.COAST, wait = True)
         dump.run_target(speed, 0, stop_type = Stop.COAST, wait = True)
         twist.run_target(speed, 0, stop_type = Stop.COAST, wait = True)
    if pos == 5:
         twist.run_target(speed, pos5, stop_type = Stop.COAST, wait = True)
         dump.run_target(speed, 180, stop_type = Stop.COAST, wait = True)
         dump.run_target(speed, 0, stop_type = Stop.COAST, wait = True)
         twist.run_target(speed, 0, stop_type = Stop.COAST, wait = True)
    if pos == 6:
         twist.run_target(speed, pos6, stop_type = Stop.COAST, wait = True)
         dump.run_target(speed, 180, stop_type = Stop.COAST, wait = True)
         dump.run_target(speed, 0, stop_type = Stop.COAST, wait = True)
         twist.run_target(speed, 0, stop_type = Stop.COAST, wait = True)

justDone = 0
ev3.speaker.beep()
while True:
     twist.run_target(speed, 290, stop_type = Stop.COAST, wait = True)
     if Button.CENTER in brick.buttons():
          Put_SL("take_pic", "STRING", '1')
          takepic = Get_SL("take_pic")
          while takepic == '1':
               wait(100)
               takepic = Get_SL("take_pic")

          twist.run_target(speed, 0, stop_type = Stop.COAST, wait = True)

          bricktype = Get_SL("brick_type")
          if bricktype != 'none':
               TurnMotor(int(bricktype))
               Put_SL("brick_type", "STRING", 'none')
               twist.run_target(speed, 290, stop_type = Stop.COAST, wait = True)
               Put_SL("take_pic", "STRING", '1')
               wait(2000)
               twist.run_target(speed, 0, stop_type = Stop.COAST, wait = True)

# twist.run_target(speed, pos0, stop_type = Stop.COAST, wait = True)
# print(pos0)
# wait(2000)
# twist.run_target(speed, 0, stop_type = Stop.COAST, wait = True)
# twist.run_target(speed, pos1, stop_type = Stop.COAST, wait = True)
# print(pos1)
# wait(2000)
# twist.run_target(speed, 0, stop_type = Stop.COAST, wait = True)
# twist.run_target(speed, pos2, stop_type = Stop.COAST, wait = True)
# print(pos2)
# wait(2000)
# twist.run_target(speed, 0, stop_type = Stop.COAST, wait = True)
# twist.run_target(speed, pos3, stop_type = Stop.COAST, wait = True)
# print(pos3)
# wait(2000)
# twist.run_target(speed, 0, stop_type = Stop.COAST, wait = True)
# twist.run_target(speed, pos4, stop_type = Stop.COAST, wait = True)
# print(pos4)
# wait(2000)
# twist.run_target(speed, 0, stop_type = Stop.COAST, wait = True)
# twist.run_target(speed, pos5, stop_type = Stop.COAST, wait = True)
# print(pos5)
# wait(2000)
# twist.run_target(speed, 0, stop_type = Stop.COAST, wait = True)
# twist.run_target(speed, pos6, stop_type = Stop.COAST, wait = True)
# print(pos6)
# wait(2000)
# twist.run_target(speed, 0, stop_type = Stop.COAST, wait = True)
