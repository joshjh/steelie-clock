#!/usr/bin/env python3
from ABE_ServoPi import PWM
from ABE_helpers import ABEHelpers
from time import sleep

def init_servos(address):
    i2c_helper = ABEHelpers()
    bus = i2c_helper.get_smbus()
    pwm = PWM(bus, address)
    pwm.set_pwm_freq(60)
    pwm.output_enable()

    # cycle the arms on channels 0, 2, 4
    print('cycling through all valid positions')
    for x in (175, 300, 425, 550):
        pwm.set_pwm(0, 0, x)
        sleep(1)
        pwm.set_pwm(2, 0, x)
        sleep(1)
        pwm.set_pwm(4, 0, x)
        sleep(2)
    return pwm

def error_lamp(setting):
    pass

def steelie_move_arms(pwm, temp_arm, wind_arm, rain_arm):
    temp_arm_channel, wind_arm_channel, rain_arm_channel = 0, 2, 4
    servoPosn1 = 175  # Min pulse length out of 4096
    servoPosn2 = 300  # Min pulse length out of 4096
    servoPosn3 = 425  # Max pulse length out of 4096
    ServoPosn4 = 550  # Max pulse length out of 4096
    # loop  assumes that temp arm is chan 0, wind arm chan 1, rain arm chan 2
    setting_arm = 0
    arms = (temp_arm, wind_arm, rain_arm)
    for x in (temp_arm_channel,  wind_arm_channel, rain_arm_channel):
        sleep(1) # don't try to set everything at once as it will spike the power supply
        if arms[setting_arm] == 0:
            print('setting arm {} to servoPosn1'.format(x)) 
            pwm.set_pwm(x, 0, servoPosn1)
        elif arms[setting_arm] == 1: 
            print('setting arm {} to servoPosn2'.format(x)) 
            pwm.set_pwm(x, 0, servoPosn2)
        elif arms[setting_arm] == 2: 
            print('setting arm {} to servoPosn3'.format(x)) 
            pwm.set_pwm(x, 0, servoPosn3)
        elif arms[setting_arm] == 3: 
            print('setting arm {} to servoPosn4'.format(x)) 
            pwm.set_pwm(x, 0, servoPosn4)
        setting_arm += 1

