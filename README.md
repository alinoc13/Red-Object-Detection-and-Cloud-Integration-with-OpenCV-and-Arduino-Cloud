# Red-Object-Detection-and-Cloud-Integration-with-OpenCV-and-Arduino-Cloud
Uploading data obtained from machine vision to Arduino IOT Cloud using NodeMCU.


This repository contains a simple project that explores the use of machine vision technology to detect the presence and area of a red object (tomato) using OpenCV and Python and upload the data onto Arduino Cloud using NodeMCU via serial communication. The goal of this project is to learn about the integration of different technologies and to share the process with others.

The project consists of four main steps:
  1.	Creation of a red color detector using Python IDLE.
  2.	Calculation of the area of the red color detected.
  3.	Transmission of the area data to the NodeMCU board through serial communication.
  4.	Uploading of the data onto the Arduino Cloud platform.

This project is designed to offer an opportunity for learning and experimentation in the field of electronics and programming. It provides insights into the process of capturing and processing image data, transferring it across devices, and visualizing the data in the cloud. Whether you are a beginner or an experienced maker, this project can help you gain a deeper understanding of the technologies involved and encourage you to explore new possibilities.


*Program description*

Python:
Program is written and executed in Python IDLE (3.7) to detect red color and send data to NodeMCU.
Steps:
  1.	Red color boundary is defined in HSV color space.
  2.	Live image is feed in using webcam and converted to HSV.
  3.	Red color is extracted and the area of the red color is detected using getContours function.
  4.	Area data output is then sent to NodeMCU via serial communication using write_read function

Arduino:
Program is written and executed in Arduino IDE and data is uploaded onto Arduino IOT Cloud.
Steps:
1.	Create your own simple Arduino IOT Cloud dashboard with value display widget.
2.	Read input from serial communication using getData function.
3.	Upload data to Arduino IOT Cloud every 1.5 seconds.


*Reference website*
Serial communication: https://www.hackster.io/ansh2919/serial-communication-between-python-and-arduino-e7cce0

Arduino Cloud set up: https://docs.arduino.cc/arduino-cloud/getting-started/iot-cloud-getting-started

I would like to express my appreciation to the author for the reference website above for their valuable resources and inspiration that contributed to the development of this project.
