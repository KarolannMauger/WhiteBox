# WhiteBox
**WhiteBox is a wearable and interactive project designed to raise awareness of interpersonal distance through visual and auditory feedback. Using a dual Raspberry Pi setup, ultrasonic sensors, a buzzer, and addressable LEDs, the system represents "proxemic bubbles" through light and sound depending on how close someone is to the wearer.

---

## Table of Contents

-[Overview](#overview)
-[Features](#features)
-[Required Materials](#required-materials)
-[How it Works](#how-it-works)
-[Installation](#installation)
  -[Client (Distance Sensor & Buzzer)](#client-distance-sensor--buzzer)
  -[Server (LEDs)](#server-leds)
-[Hardware Setup](#hardware-setup)
-[Usage](#usage)
-[Project Structure](#project-structure)
-[Demo](#demo)
-[Credits](#credits)
-[License](#license)

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













