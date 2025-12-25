# Parking Lot Management Project
This is a simulation of a parking lot management, where my goal was to create a minimalistic portal to perform the basic functions a parking lot managemnt portal should do such as :
- keep a tab on vehicle and it's assigned slot(if available) and generate a ticket
- calculate a fee using entry and exit time of vehicle using a predeterimed hourly rate to be paid by customer

I created a simple gui using Tkinter as well to utilize the portal.

Note: I purposely coded such that ticket id is not accessible by GUI as in real life the customer will give back his actual ticket to pay fee and then only slot is free

## Structure of Directory
- py_files
  - model.py
  - services.py
  - gui.py
  - main.py
- Dockerfile

## How to Use the project
Download the contents of the git as it is and use the following commands:
- docker build -t parking-lot .
- xhost + localhost: docker  ##important for GUI Display, don't skip
- docker run --rm -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix parking-lot

## Weekwise work
- Week1: Coded the py_files content
- Week2: Applied the containerizer process using Dockerfile
     

