# template for "Stopwatch: The Game"
import simplegui

# define global variables

stopwatch_timer = 0
Number_of_stops = 0
Number_of_successful_stops = 0
stopwatch_running = True

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    A = t / 600
    B = ((t / 100)) % 6
    C = ((t / 10)) % 10
    D = t % 10
    return str(A) + ":" + str(B) + str(C) + "." + str(D)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global stopwatch_running
    timer.start()
    stopwatch_running = True

# define event handler for timer with 0.1 sec interval
def stop():
    global Number_of_stops, Number_of_successful_stops, stopwatch_running
    timer.stop()
    if stopwatch_running == True:
        Number_of_stops += 1
        if (stopwatch_timer % 10) == 0:
            Number_of_successful_stops += 1
        stopwatch_running = False

def reset():
    global stopwatch_timer
    global Number_of_stops
    global Number_of_successful_stops
    stopwatch_timer = 0
    Number_of_stops = 0
    Number_of_successful_stops = 0
    timer.stop()

# define event handler for timer with 0.1 sec interval
def increment_timer():
    global stopwatch_timer
    stopwatch_timer += 1

# define draw handler
def draw(canvas):
    canvas.draw_text(format(stopwatch_timer), (80, 65), 20, "White")
    canvas.draw_text(str(Number_of_successful_stops) + "/" + str(Number_of_stops), (170, 20), 20, "White")
    
# create frame
frame = simplegui.create_frame("Stopwatch: The Game", 200, 120)
start_button = frame.add_button ("Start", start)
stop_button = frame.add_button("Stop", stop)
reset_button = frame.add_button("Reset", reset)

# register event handlers
frame.set_draw_handler(draw)
timer = simplegui.create_timer(100, increment_timer)

# start frame
frame.start()

# Please remember to review the grading rubric
