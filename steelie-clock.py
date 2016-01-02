#!/usr/bin/env python3
# Josh Harney 2015

# functions needs: get weather.  Get position.  Adjust Position.
import weatherget
import RANGES
import sys
import move_arm
from time import sleep  

def main_loop(pwm):
    
    weather_tup = weatherget.weatherget()
    # returns tuple (temp, wind_mph, precip (1hr)
    # use the range of figures in the tuple to figure where to put the arms
    
    # set temp arm position (0 - 3)
    if round(weather_tup[0]) in range(RANGES.temp_baltic_range[0], RANGES.temp_baltic_range[1]):
        temp_arm = 0
    elif round(weather_tup[0]) in range(RANGES.temp_chilly_range[0], RANGES.temp_chilly_range[1]):
        temp_arm = 1
    elif round(weather_tup[0]) in range(RANGES.temp_warm_range[0], RANGES.temp_warm_range[1]):
        temp_arm = 2
    elif round(weather_tup[0]) in range(RANGES.temp_redders_range[0], RANGES.temp_redders_range[1]):
        temp_arm = 3
    else:
        error_str = 'TEMP value {} outside defined ranges!'.format(weather_tup[0])
        print(error_str) # send this to PC maybe??
    # set wind_arm position (0 - 3)
    if round(weather_tup[1]) in range(RANGES.wind_calm_range[0], RANGES.wind_calm_range[1]):
        wind_arm = 0
    elif round(weather_tup[1]) in range(RANGES.wind_bit_blowly_range[0], RANGES.wind_bit_blowly_range[1]):
        wind_arm = 1
    elif round(weather_tup[1]) in range(RANGES.wind_windy_range[0], RANGES.wind_windy_range[1]):
        wind_arm = 2
    elif round(weather_tup[1]) in range(RANGES.wind_hurricane_range[0], RANGES.wind_hurricane_range[1]):
        wind_arm = 3
    else:
        error_str = 'WIND value {} outside defined ranges!'.format(weather_tup[0])
        print(error_str) # send this to PC maybe??
    
    # set rain_arm position (0 - 3)
    if round(weather_tup[2]) in range(RANGES.precip_dry_range[0], RANGES.precip_dry_range[1]):
        rain_arm = 0
    elif round(weather_tup[2]) in range(RANGES.precip_rainy_range[0], RANGES.precip_rainy_range[1]):
        rain_arm = 1
    elif round(weather_tup[2]) in range(RANGES.precip_wet_range[0], RANGES.precip_wet_range[1]):
        rain_arm = 2
    elif round(weather_tup[2]) in range(RANGES.precip_monsoon_range[0], RANGES.precip_monsoon_range[1]):
        rain_arm = 3
    else:
        error_str = 'WIND value {} outside defined ranges!'.format(weather_tup[0])
        print(error_str) # send this to PC maybe??
    print('processed weather_tup (temp {} wind {} rain {})'.format(weather_tup[0], weather_tup[1], weather_tup[2]))
    print('setting temp arm to ', temp_arm)
    print('setting wind arm to ', wind_arm)
    print('setting rain arm to ', rain_arm)
    
    move_arm.steelie_move_arms(pwm, temp_arm, wind_arm, rain_arm)

# do this once.
pwm = move_arm.init_servos(0x40)

while True:
    
    main_loop(pwm)
    sleep(3600)






    

    
        
    



