from gpiozero import AngularServo
import time
import math
import numpy as np
from time import sleep 

A = 7.5
B = 17.6
C = 12.3874
stride_length = 10
a = stride_length / 2

theta_1 = 0
theta_2 = 0
theta_3 = 0

print("ellipse")

def ellipse_generation() :
    x_coords = []
    y_coords = []
    z_coords = []
    k = 1
    theta_range = np.linspace(0, np.pi, num=5)
    for theta in theta_range :
        x = a*math.cos(theta)
        z = k*math.sin(theta)
        y = a*math.sin(theta)
        x_coords.append(x)
        y_coords.append(y)
        z_coords.append(z)
    
    return x_coords, y_coords, z_coords


x_coords, y_coords, z_coords = ellipse_generation()
#print(x_coords)



def inverse_kinematics(x,y,z) :
    
    theta1 = []
    theta2 = []
    theta3 = []
    
    for i in range(len(x_coords)) :
        H = math.sqrt(x[i] ** 2 + (y[i] ) ** 2)
       # H = math.sqrt(x[i] ** 2 + (y[i]) ** 2)

        L = math.sqrt(H ** 2 + z[i] ** 2)
        print("length of L is", L)
        theta_1 = math.atan2(x[i], H)
        theta_2 =  np.arccos((L ** 2 + A ** 2 - C ** 2) / (2 * L * A))-math.atan2(z[i],H)
        theta_3 = np.pi -  np.arccos((A ** 2 + C ** 2 - L ** 2) / (2 * A * C))
        theta1.append(theta_1 * 180 / np.pi)
        theta2.append(theta_2 * 180 / np.pi)
        theta3.append(theta_3 * 180 / np.pi)
    '''
    for i in range(len(x_coords)) :
        theta1 = math.atan2(y[i],x[i])
        theta2 = np.arccos(-(C**2) + A ** 2 + x[i] ** 2 + y[i] ** 2 + z[i] ** 2) + math.atan2(z[i], math.sqrt(x[i] ** 2 + y[i] **2 ))
        theta3 = - np.arccos((x[i] ** 2 + y[i] ** 2 + z[i] ** 2 - A ** 2 - C ** 2)/ (2 * A * C))
    '''
    return theta1, theta2, theta3


# here theta3 maybe theta3 or pi - theta3 depending upon the configuration 
theta1, theta2, theta3 = inverse_kinematics(x_coords, y_coords, z_coords)
print(theta1)
print(theta2)
print(theta3)

for i in theta1 :
    if i > 180 :
        print("work agaathu")
        break
for i in theta2 :
    if i > 180 :
        print(" jfjfjfjfj")
        break
for i in theta3 :
    if i > 180 :
        print(" 515 ")
        break 
#theta values for the fourth leg
# here x can be negative x or 360 - x

theta1R = [-x for x in theta1]
theta2R = [-x for x in theta2]
theta3R = [-x for x in theta3]

dist_diff = 5.83744 ;

L_y_coords = [(x - dist_diff) for x in y_coords]

# theta values for left sided legs 1, 5
L_theta1, L_theta2, L_theta3 = inverse_kinematics(x_coords, L_y_coords, z_coords)


# now taking the inverse of the left leg values for the right legs
# here x can be negative of x or 360 -x

R_theta1 = [-x for x in L_theta1]
R_theta2 = [-x for x in L_theta2]
R_theta3 = [-x for x in L_theta3]

servo = AngularServo(18, min_pulse_width = 0.0006, max_pulse_width = 0.0023)
while True :
    servo.angle = 90
    sleep(2)
'''

def servo_initialise(servoPin) :
    
    servo = machine.PWM(machine.Pin(servoPin))
    servo.freq(50)
    return servo

def servo_write(servo, angle) :
    
    writeVal = 6553/360 * (angle) + 1638
    servo.duty_u16(int(writeVal))
    time.sleep(.02)
    
    ServoPin = 15
servo = machine.PWM(machine.Pin(servoPin))
servo.freq(50)
angle = 30
        
'''

'''
Servo_1 = servo_initialise(15)

while True :
    servo_write(Servo_1, 30) 
    
    
'''

servo1 = AngularServo(14, min_pulse_width = 0.0006, max_pulse_width = 0.0023)
servo2 = AngularServo(18, min_pulse_width = 0.0006, max_pulse_width = 0.0023)
servo3 = AngularServo(15, min_pulse_width = 0.0006, max_pulse_width = 0.0023)



while True :
    
     # for i in len(theta1) :
          servo1.angle = int(theta1[0])
          sleep(0.5)
          