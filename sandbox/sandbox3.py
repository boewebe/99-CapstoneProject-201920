# Put whatever you want in this module and do whatever you want with it.
# It exists here as a place where you can "try out" things without harm.

# This sandbox is for use by Colin Browne.

"""it's gotta have cool background music. it should definite;y play the mario end-of-level theme when
we complete the objective, possibly have some actiion music go while it's doing stuff."""

'Locker code is 38-16-2  locker 1'

"""

Idea: print out some ppink cardboard faces and make small boxes. Robot picks up and finds the pink boxes. 
It finds if it's oriented towards that box via a block of color in front of the box.

make a piano in the GUI

arrange things by color

make art

mazes that it solves on it's own. When it passes over a blue strip, the solve maze function is activated. it looks at
what direction is the farthest using the IR sensor and goes until that direction(from a wall) is at some small set value.
then it turns 90 degrees to the left and 90 degrees to the right, recording the maximum distance of the IR sensor on each side
It turns back to whatever distance is the farthest, and then goes in that direction until that direction is again minimized.

"""
import rosebot
import time

def increasing_beeps_as_approach(speed, initial_beep_rate, rate_of_beep_increase):
    robot = rosebot.RoseBot()
    initial_distance = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
    robot.drive_system.go(speed, speed)
    initial_beep_rate = int(initial_beep_rate)
    rate_of_beep_increase = int(rate_of_beep_increase)

    while True:
        percent_distance = (initial_distance - robot.sensor_system.ir_proximity_sensor.get_distance_in_inches())/(initial_distance)
        pause_time = (percent_distance) / ((initial_beep_rate) + ((rate_of_beep_increase) * (1/10)*(100 - percent_distance)))
        robot.sound_system.beeper.beep().wait()
        time.sleep(pause_time)
        if robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() <=2:
            robot.drive_system.stop()
            break