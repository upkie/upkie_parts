# Build Upkie

Instructions and resource files to build the [Upkie](https://hackaday.io/project/185729-upkie-wheeled-biped-robot) wheeled biped.

## Table of contents

0. [Bill of materials](BOM.md)
1. [Order parts](#1-order-parts)
2. [3D printing](#2-3d-printing)
3. [Assembly](#3-assembly)
4. [Raspberry Pi setup](#4-raspberry-pi-setup)
5. [Power the robot up](#5-power-the-robot-up)
6. [Motion control software](#6-motion-control-software)
7. [Balancing test](#7-balancing-test)
8. [Unleash the beast!](#8-unleash-the-beast)

## 1) Order parts

Order parts listed in the [bill of materials](BOM.md). It is better to do this first as shipping will take some time.

## 2) 3D printing

3D printing project (3MF) files are provided for each part. They include all configuration details (speed, infill, layer height, etc.) required for printing. All parts were printed multiple times with a [Prusa i3 MK3S+](https://www.prusa3d.com/product/original-prusa-i3-mk3s-kit-3/).

Parts should be printed in PETG (which has better impact resistance than PLA) with a 0.2 mm layer height. Infill varies from 15% to 30%, but most of these values are guesstimates that don't come from observing parts breaking after robot falls. The only exception to this is the wheel hub, where there is an explicit infill modifier on the hex coupler connector.

### 2.1) Torso

Print all torso parts from [3d\_printing/torso](3d_printing/torso).

### 2.2) Legs

Print all leg parts from [3d\_printing/legs/hollow](3d_printing/legs/hollow). (Optionally, if you don't mind hanging cables and prefer a lower print time, you can print [wooden leg](3d_printing/legs/wooden) parts instead.)

## 3) Assembly

---

### 3.1) Torso

... [Comments on this step](...).

---

### 3.1.1) Head plate

- Mount the Raspberry Pi to the plate using the four M2 hex spacers. USB ports should be on the side of the “USB” printed text.
- Mount the pi3hat on top of the Pi using the four M2 screws that come with it.
- Mount the head to the left and right plates so that the USB side is to the robot's right (eyes are front, battery is back).

Pay extra care to the last point. If the head is mounted the opposite way, you will have (1) a hard time plugging in XT-30 power cables and (2) to update the IMU frame orientation in the robot's URDF, a.k.a., more trouble than necessary ;-)

- Optionally, 3D print the [handle](3d_printing/extras/handle_v1.3mf) and screw it to the head plate using four M3x8 screws (this can always be done at any later stage).

---

### 3.1.2) Buttocks plate

- Screw the power dist board to the buttocks plate using four M2 screws

---

### 3.1.3) Complete the torso

- Screw the left and right plates to the buttocks plate using M3x8 screws
- Screw the front plate to the left and right plates using M3x8 screws
- Screw the two stiffeners to the front plate using M3x8 screws
- (Leave out the internal covers for now)
- Screw the two internal covers using the ten M2.5 screws
- Plug the battery to the connector, it should make a satisfying click

---

### 3.2) Left leg

...

---

### 3.3) Right leg

...

---

### 3.4) Final assembly

Parts:

| Short name         | Quantity |
|--------------------|----------|
| torso              | 1        |
| left leg           | 1        |
| right leg          | 1        |
| comms cable, 20 cm | 2        |
| torso power cable  | 2        |

1. Connect the **right**-hip qdd100 CAN to the pi3hat **JC1** CAN using a comms cable
    - Add a label "JC1" to the comms cable
2. Connect the **left**-hip qdd100 CAN to the pi3hat **JC2** CAN using a comms cable
    - Add a label "JC2" to the comms cable
3. Connect the left qdd100 to the power dist board using a torso power cable
4. Connect the right qdd100 to the power dist board using a torso power cable

---

## 4) Raspberry Pi setup

...

## 5) Power the robot up

...

## 6) Motion control software

...

## 7) Balancing test

...

## 8) Unleash the beast!

...
