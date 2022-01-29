# Assignment.py
to use this function please copy the file Assignment.py to your project directory
and import the control_signal function by typing
from Assignment.py import control_signal
then to get the steering signal create signal variable as example
steering_signal = control_signal(linear_speed, angular_speed)
note if the direction of loader turn to the left then angular_velosity must be posative value other wise it must be negative
the function can take other three parameters f1, f2, max_turn these parameters can be optained from loader manufacturer
in this code if you dont change it then it is set to f1=0.6 m, f2=0.6 m, max_turn=42 degree

important note
please pay attention that giving invalid and un realistic values that leads to turn the loader in its position or giving any
values types other than numbers it will lead to error so to use it without any crash you need to pay attention to your inputs.
error problems will be fixed later.
