# CarND-Controls-PID
Self-Driving Car Engineer Nanodegree Program

---

## Dependencies
* cmake >= 3.5
 * All OSes: [click here for installation instructions](https://cmake.org/install/)
* make >= 4.1
  * Linux: make is installed by default on most Linux distros
  * Mac: [install Xcode command line tools to get make](https://developer.apple.com/xcode/features/)
  * Windows: [Click here for installation instructions](http://gnuwin32.sourceforge.net/packages/make.htm)
* gcc/g++ >= 5.4
  * Linux: gcc / g++ is installed by default on most Linux distros
  * Mac: same deal as make - [install Xcode command line tools]((https://developer.apple.com/xcode/features/)
  * Windows: recommend using [MinGW](http://www.mingw.org/)
* [uWebSockets](https://github.com/uWebSockets/uWebSockets) == 0.13, but the master branch will probably work just fine
  * Follow the instructions in the [uWebSockets README](https://github.com/uWebSockets/uWebSockets/blob/master/README.md) to get setup for your platform. You can download the zip of the appropriate version from the [releases page](https://github.com/uWebSockets/uWebSockets/releases). Here's a link to the [v0.13 zip](https://github.com/uWebSockets/uWebSockets/archive/v0.13.0.zip).
  * If you run OSX and have homebrew installed you can just run the ./install-mac.sh script to install this
* Simulator. You can download these from the [project intro page](https://github.com/udacity/CarND-PID-Control-Project/releases) in the classroom.

## Basic Build Instructions
1. Clone this repo.
2. Make a build directory: `mkdir build && cd build`
3. Compile: `cmake .. && make`
4. Run it: `./pid`. 

## Basic Plot Visualization Instructions
1. Edit the column name in visualize.py
2. run `python visualize.py <csvfilename>`

## Summary

First, I implemented the PID error calculation and its update mechanism in *PID.cpp*. By printing out the CTE and the error value or the steering value, I can see and follow the impact of parameter changes. For the first experiment, I tuned the P parameter. After several experiments, I found out that with 0.05 as the P parameter, the vehicle can pass the first left curve. The bellow figures shows the comparison between 0.1, 0.05, and 0.2. The left graphs plots the CTE values and the right graph plots the steering values in respect to the time.

![image1]

Afterwards, I started to vary the D parameter with values 1, 2, and 0.5. 0.5 as the D value causes that the current control will react half of the current error difference. It means that the vehicle cannot response a high error difference that can be caused by curves. On the other hand, if KD is equal to 2, then the vehicle is overresponsive to a small error change. Thus, I chose KP=0.05 and KD=1 as the reference to tune the I parameter.

![image2]

The below figures shows several experiments using difference I parameters. KI=0.001 (see green and blue lines) generates a good results compared to 0.0001 (orange line).

![image3]

With the above results, the vehicle still drives out side the road and yelow line at the curves (CTE is larger than 3.0). Thus, I try to assign a zero value for the trottle in order to slow down the vehicle if the current CTE exceeds a threshold value. Next, I need to re-tune the parameters. I found out that KP = 0.12, KD=2.1 and KI[0.002:0.005] keep the vehicle on the road. 

![image4]

These two figures show some refinement of the parameter tuning and limit the steering value between range -1 and 1. We can observe the steering values of these figures, that by increasing the I-parameter , we can control the vehicle to be more stable.

![image5]
![image6]

As the final result, I choose KP=0.12, KI=0.009, and KD=1.8. The last figures shows that even without assigning a negative trottle, the vehicle can deal with the circuit curves without leaving the road (CTE < 3.0).

![image7]


[//]: # (Image References)

[image1]: ./results/P_experiments.png "Tuning P parameter"
[image2]: ./results/PD_experiments.png "Tuning Pand D parameter"
[image3]: ./results/PID_experiments.png "Tuning P, D ,and I parameter"
[image4]: ./results/PID_experiments_diffI.png "Tuning I parameter"
[image5]: ./results/Finalexperiments.png "Applying maximum range [-1,1]"
[image6]: ./results/Finalexperiments2.png "Tuning P parameter"
[image7]: ./results/NoBreakexperiments.png "Tuning P parameter"





