import pygame
import time
import datetime

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    sound_file = "Projects\\17.Alarm Clock\\drums_of_liberation.mp3"
    is_running = True

    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)
        # if current_time > alarm_time:
        #     print("Alarm to be set for future ")
        #     break
        if current_time == alarm_time:
            print("WAKE UP ! 😒")

            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                cmd = input("Type 'Stop' if you are awake now: ")
                if cmd != True :
                    pygame.mixer.music.stop()
                    break
                time.sleep(1)
            is_running = False
        time.sleep(1)

if __name__ == "__main__":
    alarm_time = input ("Enter the alarm time(HH:MM:SS): ")
    set_alarm(alarm_time)