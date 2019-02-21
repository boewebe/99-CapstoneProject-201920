
import rosebot
import time



##############################################################
#
#   This file contains all the functional code to guide
#   the robot through solving the mazes.
#
##############################################################


def Mazesolver():

    '''Walks the robot through solving the maze, by stopping at each intersection,
     determining which way is the longest path, orienting itself in the direction of that path,
     and then moving in that direction until it reaches another intersection. The program ends
     when the robot crosses over a black finish line'''

    robot = rosebot.RoseBot()
    robot.arm_and_claw.calibrate_arm()
    while True:
        go_down_hallway(robot)
        time.sleep(0.5)
        if robot.sensor_system.color_sensor.get_color_as_name() == 'Green':
            break
        path_choosing(robot)
        time.sleep(0.5)
        if robot.sensor_system.color_sensor.get_color_as_name() == 'Green':
            break
    robot.sound_system.speech_maker.speak('Congratulations')
    print('You did it! You solved this maze!')



def go_down_hallway(robot):

    '''Makes the robot go down the hallway, stopping when it reaches blue, signaling an intersection,
    or black, signaling the finish line and end of the maze'''

    robot.drive_system.go(50, 50)
    time.sleep(1.0)      # this is to allow the robot to get off of the tape marker it is currently on to prevent getting stuck on the same tape marker
    while True:
        if robot.sensor_system.color_sensor.get_color_as_name() == 'Blue':
            robot.drive_system.stop()
            break
        elif robot.sensor_system.color_sensor.get_color_as_name() == 'Green':
            robot.drive_system.stop()
            break
        else:
            time.sleep(0.1)



def path_choosing(robot):

    '''The robot determines which direction from an intersection is the longest path,
    and orients itself to go in that direction'''

    while True:
        sleep_time = 1.45
        greatest_distance = 0


        robot.drive_system.go(-50, 50)
        time.sleep(sleep_time)
        robot.drive_system.stop()
        left_path_distance = average_distance_data(robot)

        if left_path_distance > greatest_distance:
            greatest_distance = left_path_distance


        robot.drive_system.go(50, -50)
        time.sleep(sleep_time)
        robot.drive_system.stop()
        straight_path_distance = average_distance_data(robot)

        if straight_path_distance > greatest_distance:
            greatest_distance = straight_path_distance


        robot.drive_system.go(50, -50)
        time.sleep(sleep_time)
        robot.drive_system.stop()
        right_path_distance = average_distance_data(robot)

        if right_path_distance > greatest_distance:
            greatest_distance = right_path_distance


        # Now to Re-orient the Robot in the proper direction

        if greatest_distance == right_path_distance:
            break

        if greatest_distance == straight_path_distance:
            robot.drive_system.go(-50, 50)
            time.sleep(sleep_time)
            robot.drive_system.stop()
            break

        if greatest_distance == left_path_distance:
            robot.drive_system.go(-50, 50)
            time.sleep(sleep_time)
            robot.drive_system.stop()

            robot.drive_system.go(-50, 50)
            time.sleep(sleep_time)
            robot.drive_system.stop()
            break



def average_distance_data(robot):

    '''This averages several readings of proximity data, so the robot can choose the correct path'''

    first_reading = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
    time.sleep(0.2)
    second_reading = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
    time.sleep(0.2)
    third_reading = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
    time.sleep(0.2)
    fourth_reading = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
    time.sleep(0.1)
    average_distance = (first_reading + second_reading + third_reading + fourth_reading) / 4
    return average_distance