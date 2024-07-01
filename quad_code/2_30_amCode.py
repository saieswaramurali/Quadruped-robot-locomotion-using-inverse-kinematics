
from gpiozero import AngularServo
from time import sleep
'''
servo1 = AngularServo(25, min_pulse_width = 0.0006, max_pulse_width = 0.0023)
servo2 = AngularServo(3, min_pulse_width = 0.0006, max_pulse_width = 0.0023)
servo3 = AngularServo(4, min_pulse_width = 0.0006, max_pulse_width = 0.0023)
'''

servo1_1 = AngularServo(14, min_pulse_width = 0.0006, max_pulse_width = 0.0023)
servo2_1 = AngularServo(15, min_pulse_width = 0.0006, max_pulse_width = 0.0023)
servo3_1 = AngularServo(18, min_pulse_width = 0.0006, max_pulse_width = 0.0023)

servo1_3 = AngularServo(26, min_pulse_width = 0.0006, max_pulse_width = 0.0023)
servo2_3 = AngularServo(13, min_pulse_width = 0.0006, max_pulse_width = 0.0023)
servo3_3 = AngularServo(5, min_pulse_width = 0.0006, max_pulse_width = 0.0023)

servo1_5 = AngularServo(25, min_pulse_width = 0.0006, max_pulse_width = 0.0023)
servo2_5 = AngularServo(3, min_pulse_width = 0.0006, max_pulse_width = 0.0023)
servo3_5 = AngularServo(4, min_pulse_width = 0.0006, max_pulse_width = 0.0023)




t1 = [0, 0, -15, -45]
t2 = [0, 60, 59.2069903918657, 0]
t3 = [90, 98.18306938002281, 94.45951748347302, 90.7547761909206]
'''
t1 = [0, 0,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 , -1.751023740288441, -5.173855718283394, -8.37135804252406, -11.229513598983766, -13.674754257402034, -15.670796339659512, -17.208520409530603, -18.294138910340152, -18.93907223162459, -19.1528482278982]
t2 = [0, 58.85159790329807, 58.634336684437564, 58.6775109864224, 58.92687015151685, 59.311574021054305, 59.75208508148069, 60.168879596659266, 60.49147175364128, 60.66696821407798, 60.66696821407798, 60.49147175364128, 60.168879596659266, 59.75208508148069, 59.311574021054334, 58.92687015151685, 58.6775109864224, 58.634336684437564, 58.85159790329807, 59.360367737478064]
t3 = [90.7547761909206, 90.9552890132437, 91.53517336845364, 92.43189493399773, 93.54892450065273, 94.76607601039252, 95.95209433402563, 96.97837565103274, 97.7327530219982, 98.13208676528232, 98.13208676528232, 97.7327530219982, 96.97837565103274, 95.95209433402563, 94.76607601039257, 93.54892450065273, 90, 90, 90, 90] # changed 0 to 90 on first index
'''
      
'''
'''
while True :
    
   
      for i in range(len(t1)) :
          delay = 0.1
          servo1_1.angle = 0
          sleep(delay)
          servo2_1.angle = 0
          sleep(delay)
          
          servo3_1.angle = 0
          sleep(delay)
          
          servo1_3.angle = 0
          sleep(delay)
          
          servo2_3.angle = 0
          sleep(delay)

          servo3_3.angle = 0
          sleep(delay)

          servo1_5.angle = 0
          sleep(delay)

          servo2_5.angle = 0
          sleep(delay)

          servo3_5.angle = 0
          sleep(delay)

        
          
                
                
          
          
