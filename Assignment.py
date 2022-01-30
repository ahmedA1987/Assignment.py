"""
Ahmed Abdulsahib
Tampere university
Student number 293895

task description:
this task is about the function (control_signal) that takes the linear and angular velocities
and calculate the needed loader turn then convert the turning angle to steering signal then return
the signal
"""
from math import *


def control_signal(linear_velocity, angular_velocity, f1=0.6, f2=0.6, max_turn=42, Beta_angle=0):
    """
    passed parameters
        linear_velocity: type float:
        f1: type float: distance from the loader center to the center of the front body tires.
            the initial value from the assignment paper but it is possible to pass new value.
        f2: type float: distance from the loader center to the center of the rear body tires
            the initial value from the assignment paper but it is possible to pass new value.
        max_turn: type int: this represent the maximum loader turning angle and if it is not
                passed the function then from the assignment paper it is 42 degree
        Beta: type float: represent the actual turn angle from the Loader center
        :var
        direction: type int: represent the direction of the turn and it is either -1 or 1
        f3 : the distance from the loader center and turn circle center
        alpha_1: type float: represent the angle between f1 and f3
        alpha_2: type float: represent the angle between f2 and f3
        theata: is the turn angle in degree

        :return
        the function will return signal ( number in  [-1 : 1]

    """
    if angular_velocity == 0 or linear_velocity == 0:
        return -1 * Beta_angle / max_turn
    direction = int(angular_velocity / abs(angular_velocity))
    radius = linear_velocity / abs(angular_velocity)
    f3 = sqrt(pow(radius, 2) + pow(f1, 2))
    alpha_1 = acos((pow(f1, 2) + pow(f3, 2) - pow(radius, 2)) / (2 * f1 * f3))
    alpha_2 = acos((pow(f2, 2) + pow(f3, 2) - pow(radius, 2)) / (2 * f2 * f3))
    theata = 180 - degrees(alpha_1) - degrees(alpha_2)
    if theata > max_turn:
        theata = max_turn
    if abs(Beta_angle - theata * direction) >= max_turn:
        return direction
    elif Beta_angle > theata * direction:
        return -1 * abs(Beta_angle - theata * direction) / max_turn
    else:
        abs(Beta_angle - theata * direction) / max_turn
