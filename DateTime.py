import time
import pygame
import datetime

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    sound_file = r"C:\Users\Lenovo\Music\musique.mp3" 

    pygame.mixer.init() 
    is_running = True

    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)

        if current_time == alarm_time:
            print("⏰ Wake up!")
       

            try:
                pygame.mixer.music.load(sound_file)
                pygame.mixer.music.play()

                while pygame.mixer.music.get_busy():
                    time.sleep(1)

            except Exception as e:
                print("Error playing sound:", e)

            is_running = False

        time.sleep(1)

if _name_ == "_main_":
    alarm_time = input("Enter the alarm time (HH:MM:SS): ")
    set_alarm(alarm_time)