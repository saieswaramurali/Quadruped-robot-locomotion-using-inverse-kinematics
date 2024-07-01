import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

servo_pin = 18
GPIO.setup(servo_pin, GPIO.OUT)

pwm_frequency = 100

pwm_duty_cycle_min = 2.5
pwm_duty_cycle_max = 12.5

pwm = GPIO.PWM(servo_pin, pwm_frequency)
pwm.start(7.5)


try :
    while True :
        
       # duty_cycle = (270 / 360.0) * (pwm_duty_cycle_max - pwm_duty_cycle_min) + 2.5
        for duty_cycle in range(int(pwm_duty_cycle_min), int(pwm_duty_cycle_max) + 1, 1) :
            
            pwm.ChangeDutyCycle(duty_cycle)
            time.sleep(0.5)

except KeyboardInterrupt :
    
    pwm.stop()
    GPIO.cleanup()