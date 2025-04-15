import time
import threading

def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        time_format = '{:02d}:{:02d}'.format(mins, secs)
        print("Time Left:", time_format, end='\r')
        time.sleep(1)
        seconds -= 1
    print("Time's up!               ")

def get_timer_input():
    while True:
        try:
            total_time = int(input("Enter countdown time in seconds: "))
            if total_time > 0:
                return total_time
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Enter a valid number.")

def main():
    print("=== Countdown Timer ===")
    total_seconds = get_timer_input()
    timer_thread = threading.Thread(target=countdown_timer, args=(total_seconds,))
    timer_thread.start()
    timer_thread.join()
    print("=== Timer Finished ===")

if __name__ == "__main__":
    main()
