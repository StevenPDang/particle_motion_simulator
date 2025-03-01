import numpy as numpy
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

#define constants
mass = 1
charge = 1
dt = .01 #time interval
t_max = 10 #simulation time
steps = int(t_max / dt)

#input for mass and charge, and Fields
mass = int(input('Mass of particle: '))
charge = int(input('Charge of particle: '))
str_in = input("Electric Field (Enter numbers seperated by spaces): ")
str_list = str_in.split()
EField = numpy.array(str_list, dtype=int)
str_in = input("Magnetic Field (Enter numbers seperated by spaces): ")
str_list = str_in.split()
BField = numpy.array(str_list, dtype=int)

#test input
print(EField)
print(BField)
#define electric field and magnetic fields


#initial conditons
r = numpy.array([0.0,0.0,0.0], dtype = float)
v = numpy.array([1.0,0.0,0.0], dtype = float) 

#plotting
trajectory = []

#eulers method
for step in range(steps):
    force = charge * (EField + numpy.cross(v,BField))  
    a = force/mass
    v += a * dt
    r += v * dt
    trajectory.append(r.copy())

#convert tracjetory to numpy array for plotting

trajectory = numpy.array(trajectory)

fig = plt.figure()
ax = fig.add_subplot(111, projection = "3d")    
ax.plot(trajectory[:, 0], trajectory[:, 1], trajectory[:,2])
ax.set_xlabel("X")
ax.set_xlabel("Y")
ax.set_xlabel("Z")
plt.show()
