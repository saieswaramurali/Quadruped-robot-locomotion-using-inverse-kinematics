from gpiozero import AngularServo
from time import sleep

servo1_1 = AngularServo(14, min_pulse_width = 0.0006, max_pulse_width = 0.0023)
servo2_1 = AngularServo(15, min_pulse_width = 0.0006, max_pulse_width = 0.0023)
servo3_1 = AngularServo(18, min_pulse_width = 0.0006, max_pulse_width = 0.0023)

servo1_2 = AngularServo(17, min_pulse_width = 0.0006, max_pulse_width = 0.0023)
servo2_2 = AngularServo(27, min_pulse_width = 0.0006, max_pulse_width = 0.0023)
servo3_2 = AngularServo(22, min_pulse_width = 0.0006, max_pulse_width = 0.0023)

servo1_3 = AngularServo(26, min_pulse_width = 0.0006, max_pulse_width = 0.0023)
servo2_3 = AngularServo(13, min_pulse_width = 0.0006, max_pulse_width = 0.0023)
servo3_3 = AngularServo(5, min_pulse_width = 0.0006, max_pulse_width = 0.0023)

servo1_4 = AngularServo(16, min_pulse_width = 0.0006, max_pulse_width = 0.0023)
servo2_4 = AngularServo(20, min_pulse_width = 0.0006, max_pulse_width = 0.0023)
servo3_4 = AngularServo(21, min_pulse_width = 0.0006, max_pulse_width = 0.0023)

servo1_5 = AngularServo(25, min_pulse_width = 0.0006, max_pulse_width = 0.0023)
servo2_5 = AngularServo(3, min_pulse_width = 0.0006, max_pulse_width = 0.0023)
servo3_5 = AngularServo(4, min_pulse_width = 0.0006, max_pulse_width = 0.0023)

servo1_6 = AngularServo(7, min_pulse_width = 0.0006, max_pulse_width = 0.0023)
servo2_6 = AngularServo(8, min_pulse_width = 0.0006, max_pulse_width = 0.0023)
servo3_6 = AngularServo(1, min_pulse_width = 0.0006, max_pulse_width = 0.0023)
'''
t1 = [0, 45, 15, 0, -15, -45]
t2 = [0, 59, 59, 60, 59.2069903918657, 0]
t3 = [0, 90.7547761909206, 94.45951748347302, 98.18306938002281, 94.45951748347302, 90.7547761909206]
'''
t1 = [0, 0, -15, -45,-45,0]
t2 = [0, 20, 19.2069903918657,10 ,0, 0]
t3 = [90, 98.18306938002281, 94.45951748347302, 91.5,90.7547761909206, 90] # changed 0 to 90 on first index

#t1 = [0, 0, -36, -14, 0]
#t2 = [0, 50, 50, -5, -5] # 0 82 78 0 0 
#t3 = [53, 86, 87, 90, 90]
'''
      servo1.angle = 0
      sleep(2)
      servo2.angle = 0
      sleep(2)
      servo3.angle = 0
      sleep(3)
'''

def iniatilise_zero(servo1, servo2, servo3) :
    delay=0.05
    servo1.angle = 0
    sleep(delay) # previous 0.1->0.08
    servo2.angle = 0
    sleep(delay)
    servo3.angle = 0
    sleep(delay)
    

def move_forward_L(servo1, servo2, servo3) : 
    for i in range(len(t1)) :
              delay = 0.05 # before it was 0.5 -> 0.1->0.08
              servo1.angle = int(t1[i])
              sleep(delay)
              print(int(t1[i]))
              servo2.angle = int(-t2[i])
              sleep(delay)
              print(int(-t2[i]))
              servo3.angle = int(70 - t3[i])
              sleep(delay)
              print(int(t3[i]))
    sleep(0.01) # delay 0.2-> 0.01
    
def move_forward_R(servo1, servo2, servo3) : 
    for i in range(len(t1)) :
              delay = 0.05 # before it was 0.5 -> 0.1 ->0.8
              servo1.angle = -int(t1[i])
              sleep(delay)
              print(int(t1[i]))
              servo2.angle = int(-t2[i])
              sleep(delay)
              print(int(-t2[i]))
              servo3.angle = -int(70 - t3[i])
              sleep(delay)
              print(int(t3[i]))
    sleep(0.01) #delay 0.2 ->0.01
    
while True :
     delay  =0.05
      # wave gait to move the bot forward
     move_forward_L(servo1_6, servo2_6, servo3_6)
     sleep(delay)
     move_forward_L(servo1_4, servo2_4, servo3_4)
     sleep(delay)
     move_forward_L(servo1_2, servo2_2, servo3_2)
     sleep(delay)
     move_forward_R(servo1_5, servo2_5, servo3_5)
     sleep(delay)
     move_forward_R(servo1_3, servo2_3, servo3_3)
     sleep(delay)
     move_forward_R(servo1_1, servo2_1, servo3_1)
     sleep(delay)
     

      
          
                
                
           
          
