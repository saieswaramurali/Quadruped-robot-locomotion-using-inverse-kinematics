from gpiozero import AngularServo
from time import sleep

servo1 = AngularServo(8, min_pulse_width = 0.0006, max_pulse_width = 0.0023)
servo2 = AngularServo(7, min_pulse_width = 0.0006, max_pulse_width = 0.0023)
servo3 = AngularServo(12, min_pulse_width = 0.0006, max_pulse_width = 0.0023)

'''
t1 = [0, 45, 15, 0, -15, -45]
t2 = [0, 59, 59, 60, 59.2069903918657, 0]
t3 = [0, 90.7547761909206, 94.45951748347302, 98.18306938002281, 94.45951748347302, 90.7547761909206]
'''
t1 = [0, 0, -15, -45]
t2 = [0, 60, 59.2069903918657, 0]
t3 = [90, 98.18306938002281, 94.45951748347302, 90.7547761909206] # changed 0 to 90 on first index
'''
      servo1.angle = 0
      sleep(2)
      servo2.angle = 0
      sleep(2)
      servo3.angle = 0
      sleep(3)
'''
while True :
    
   
      for i in range(4) :
          delay = 0.1 # before it was 0.5 -> 0.1
          servo1.angle = int(t1[i])
          sleep(delay)
          print(int(t1[i]))
          servo2.angle = int(-t2[i])
          sleep(delay)
          print(int(-t2[i]))
          servo3.angle = int(90 - t3[i])
          sleep(delay)
          print(int(t3[i]))
          
              
                
          
          