import numpy as np 
import skfuzzy as fuzz
#import random
import matplotlib.pyplot as plt

"""
step1 : create input and output variables
step2: create membership functions of each variable
step3: create rules set
"""


'''
Problem: Car 0 - 100 km/h
         distance: 0 - 100m

         define the break pressure
'''


break_pressure = np.arange(0, 101)
speed = np.arange(0, 101)
x_distance = np.arange(0, 101)

#define better mesures
x_short_distance = fuzz.trimf(x_distance,[0, 10, 20])
x_average_distace = fuzz.trimf(x_distance, [15, 45, 60])
x_long_distance = fuzz.trimf(x_distance,[50, 75, 100])

#define better mesures
v_fast = fuzz.trimf(speed, [80, 90, 100])
v_avg = fuzz.trimf(speed, [40, 60, 80])
v_slow = fuzz.trimf(speed, [1, 20, 40])

#define better mesures
light_break_pressure = fuzz.trimf(break_pressure, [0, 15, 30])
medium_break_pessure = fuzz.trimf(break_pressure, [20, 40, 55])
heavy_break_pressure = fuzz.trimf(break_pressure, [50, 75, 100])

plt.figure()

plt.plot(x_distance, x_short_distance, 'b', linewidth=1.5, label='Short')
plt.plot(x_distance, x_average_distace, 'k', linewidth=1.5, label='AVG')
plt.plot(x_distance, x_long_distance, 'm', linewidth=1.5, label='Long')
plt.title('Distance')

plt.show()


# Rules membership
#rule1 = np.fmax(x_long_distance, v_fast)
#activate_pressure








