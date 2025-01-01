# TUKE OpenLab Screen Controller

This is a simple Python program to control and manage the screens in the TUKE OpenLab environment. It allows resetting the screens to their default state or setting screens from a predefined list. **The program is available exclusively for students of TUKE (Technical University of Košice) connected to the university network.**

## Features
- Reset screens to their default content.
- Display screens on:
  1. Ascii Art (`http://ukazky.kpi.fei.tuke.sk:8080/ascii/ola`)
  2. Matrix Code Rain (`https://pranx.com/matrix-code-rain/`)
  3. Custom Matrix (`http://ukazky.kpi.fei.tuke.sk:8080/matrix.html`)

## Prerequisites
- **Python 3.8 or later**
- **tuke_openlab Python module**: Ensure this library is installed and available in your Python environment.
- Connection to the TUKE university network.

## How to Use
1. Clone or download this repository to your local machine.
2. Navigate to the project directory.
3. Run the script with one of the following commands:
   
   ```bash
   python controller.py 1
   python controller.py 2
   python controller.py 3
   python controller.py 0
   
