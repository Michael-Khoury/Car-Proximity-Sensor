from engi1020.arduino.api import*
from time import sleep
def Turn_Off_Car(): #This function is called while the car is in "drive" mode to completely turn it off
    rgb_lcd_clear() #Clears LCD screen to prepare for shutdown
    rgb_lcd_colour(0,0,0)
    quit() #Quits the python script completely to prevent further interactions
   

def Turn_On_Car(): #This function is defined so that it is called when the user wants to turn his car

                
    while True: #Code is placed in this while loop to ensure it takes inputs indefinitely
        temp=pressure_get_temp()# Gets the temperature
        
        while analog_read(0)==1023:# Puts the car in park mode when the rotary dial is at 1023
            rgb_lcd_clear()
            rgb_lcd_colour(100,100,0)
            rgb_lcd_print("Park",0,6)
            buzzer_stop(5)
            if analog_read(6)>20:# Using the light sensor if the light level is at a specific level (above 20) the message will be good morning
                rgb_lcd_print("Good morning",1,1)
                sleep(0.5)
            if analog_read(6)<=20:# Using the light sensor if the light level is at a specific level (less than or equal to20) the message will be good evening
                rgb_lcd_print("Good evening",1,1)
                sleep(0.5)
            if digital_read(6)==True: #This will stop the car by holding down the button when the car is in "Park" mode
                Turn_Off_Car() #Calling the function turn off car
                
        while 0<analog_read(0)<1023: #This puts the car in drive mode when the rotary dial is not in "drive" or "reverse" mode
            rgb_lcd_clear()
            rgb_lcd_colour(0,100,0)
            rgb_lcd_print('Drive',0,6)
            buzzer_stop(5)
            rgb_lcd_print(f"Outside temp {temp}",1,1)# Prints the outside temperature with the previously defined "temp"
            sleep(0.5)
             
            '''
             this next line ensures an initial distance reading is taken
             after exiting the first loop and before entering the next while loop '''
       
        d=ultra_get_centimeters(7)
        while analog_read(0)==0: #Code in this while loop only occurs if rotary dial is set to 0
            rgb_lcd_clear()
            rgb_lcd_print('Reverse',0,5) #If rotary dial is set to 0, lcd prints 'reverse'
            if d>=150:
                rgb_lcd_print(f'{d} cm away',1,1)
                d=ultra_get_centimeters(7)
                buzzer_note(5,100,1)
                rgb_lcd_colour(100,00,0)
                sleep(1)
                rgb_lcd_colour(0,0,0)
                sleep(1)
                rgb_lcd_colour(100,0,0)
                '''
                if nearest object is further away, distance is printed, and frequency of buzzer's
                sound as well as frequency of flashing of LCD is low. Screen flashes red'''

            elif d>=50:
                rgb_lcd_print(f'{d} cm away',1,1)
                d=ultra_get_centimeters(7)
                buzzer_note(5,100,0.5)
                rgb_lcd_colour(100,00,0)
                sleep(0.1)
                rgb_lcd_colour(0,0,0)
                sleep(0.1)
                rgb_lcd_colour(100,0,0)
                '''
                if nearest object is a medium distance away, distance is printed, and frequency of buzzer's
                sound as well as frequency of flashing of LCD is faster. Screen flashes red'''      

            elif d<50:
                rgb_lcd_print(f'{d} cm away',1,1)
                d=ultra_get_centimeters(7)
                buzzer_note(5,100,0.0)
                rgb_lcd_colour(100,00,0)
                sleep(0)
                rgb_lcd_colour(0,0,0)
                sleep(0)
                rgb_lcd_colour(100,0,0)
                '''
                if nearest object is close, distance is printed, and buzzer plays a constant sound.
                Screen flashes red at a very high frequency.'''          

while True:
    if digital_read(6)==True: #When the button is pressed the car is turned on and automatically put in "Park" mode
        Turn_On_Car()
        break #If break is not used here the function will only be called when the button is held this exits the while loop
