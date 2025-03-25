# WhiteBox
**WhiteBox** is a wearable and interactive project designed to raise awareness of interpersonal distance through visual and auditory feedback. Using a dual Raspberry Pi setup, ultrasonic sensors, a buzzer, and addressable LEDs, the system represents "proxemic bubbles" through light and sound depending on how close someone is to the wearer.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Required Materials](#required-materials)
- [How it Works](#how-it-works)
- [Installation](#installation)
  - [Client (Distance Sensor & Buzzer)](#client-distance-sensor--buzzer)
  - [Server (LEDs)](#server-leds)
- [Hardware Setup](#hardware-setup)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Demo](#demo)
- [Credits](#credits)
- [License](#license)

---

## Overview
WhiteBox explores human interaction zone through a wearable clothe that changes color and emits sounds based on proximity. It's a reactive piece that visualizes social comfort zones in real-time.

The project consists of:
- A **client Raspberry Pi** with an ultrasonic sensor and buzzer
- A **server Raspberry Pi** with an Alitove addressable LED strip DC 5V (WS2811)

The client measures the distance and sends it to the server over UDP every 0.5 seconds. Simultaneously, it controls the buzzer frequency depending on proximity. The server then changes the LED colors according to the distance using a JSON configuration file.

---

## Features

- Real-time distance measurement using an ultrasonic sensor
- Visual feedback with a WS2811 addressables LED strip
- Audio feedback with a buzzer - beeps increase as distance decreases
- Wireless UDP communication between client and server
- Distance-to-color mapping via JSON configuration
- Educational and wearable design to promote personal space awareness

---

## Required Materials

- 2 x Raspberry Pi (client + server)
- 1 x Ultrasonic sensor (HC-SR04)
- 1 x Buzzer
- 1 x Alitove addressable LED strip 50pcs (WS2811, 5V)
- 2 x External battery
- Access to Wi-Fi network (for UDP communication)

---

## How it works

- **Distance zones** are defined from **200 cm to 0 cm**, in 10 cm increments.
- Each distance range maps to a specific **LED color**, defined in `colors.json` file.
- The **buzzer** starts beeping from **25 cm**, increasing in frequency as distance decreases - becoming a constant tone when someone is **<10 cm** away.
- The **LED colors** visually represent different *proxemic bubbles* (safe distance, social zone, personal zone, etc.).

---

## Installation

You'll need **Python** and **Git** installed on both Raspberry Pis.

### Common Preparation

Run the following commands on both devices:

```bash
$ sudo apt update
$ sudo apt upgrade -y
$ sudo apt install git python3-pip
```

Then clone the repository:

```bash
$ git clone https://github.com/KarolannMauger/WhiteBox
$ cd WhiteBox
```

### Client (Distance Sensor & Buzzer)
1. Install and start pigpio:
   ```bash
   $ sudo apt install pigpio
   $ sudo systemctl enable pigpiod
   $ sudo sytemctl start pigpiod
   ```
2. Run the client:
   ```bash
   $ cd client
   $ python3 main.py
   ```
### Server (LEDs)
1. Install the rpi_ws2811x library:
   ```bash
   $ pip3 install rpi_ws281x
   ```
2. Run the server:
   ```bash
   $ cd server
   $ sudo python3 main.py
   ```

---

---

## Hardware Setup

### Client GPIO (Ultrasonic Sensor + Buzzer)

| Component         | GPIO Pin                      | Power   |
|------------------|-------------------------------|---------|
| Ultrasonic Sensor | GPIO 14 (Trig), GPIO 15 (Echo) | 5V, GND |
| Buzzer            | GPIO 18                       | 5V, GND |

### Server GPIO (Addressable LED Strip)

| Component          | GPIO Pin | Power   |
|-------------------|----------|---------|
| Alitove LED Strip | GPIO 12  | 5V, GND |

> **Note:** Make sure the LED strip supports 5V logic and is properly powered using a suitable external power supply if needed.

---

## Usage

Once both Raspberry Pis are powered on and scripts are running:

- **Client**:
  - Measures the distances every 0.5 seconds
  - Controls the buzzer sound based on distance
  - Sends the measured value via UDP to the server
- **Server**:
  - Receives the distance
  - Looks up the corresponding RGB color in `colors.json`
  - Updates the LED strip to reflect the distance zone

You can modify `server/colors.json` to change the color associated with each distance zone.

---

## Project Structure

WhiteBox/
│
├── client/
│   ├── main.py               # Measures distance, handles buzzer, sends data via UDP
│   ├── buzzer.py             # Manages buzzer frequency based on distance
│   └── distance_sensor.py    # Reads ultrasonic sensor values        
│
├── server/
│   ├── main.py               # Receives UDP data and controls the LED strip
│   ├── led_controller.py     # Converts distance to RGB and controls the LED
│   └── colors.json       # Defines RGB colors for each 10cm range (200-0 cm)
│
└── README.md                 # Project documentation

---






































