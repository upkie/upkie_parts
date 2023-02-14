# Build Upkie

Instructions and resource files to build the [Upkie](https://hackaday.io/project/185729-upkie-wheeled-biped-robot) wheeled biped.

## 1) Order parts

Order parts listed in the [bill of materials](BOM.md). It is better to do this first as shipping will take some time.

## 2) 3D printing

Parts are printed in PETG with a 0.2 mm layer height. 3D printing project (3MF) files include all configuration details (speed, infill, layer height, ...) used to print them with a [Prusa i3 MK3S+](https://www.prusa3d.com/product/original-prusa-i3-mk3s-kit-3/). Printing should work out with other printers too.

Infill varies from 15% to 30%, but most of these values are guesstimates that don't come from observing parts breaking after robot falls. The only exception to this is the wheel hub, where there is an explicit infill modifier on the hex coupler connector.

### 1.1) Torso

Print all torso parts from [3d\_printing/torso](3d_printing/torso).

### 1.2) Legs

Print all leg parts from [3d\_printing/legs/hollow](3d_printing/legs/hollow). (Optionally, if you don't mind hanging cables and prefer a lower print time, you can print [wooden leg](3d_printing/legs/wooden) parts instead.)

## 2) Assembly

### 2.1) Torso

...

### 2.2) Left leg

...

### 2.3) Right leg

...

### 2.4) Final assembly

Parts:

| Item        | Number |
|-------------|--------|
| Torso       | 1 |
| Left leg    | 1 |
| Right leg   | 1 |
| CAN cable, 20 cm | 2 |
| PWR cable, male-female connectors, 20 cm | 2 |

1. Connect the **right**-hip qdd100 CAN to the pi3hat **JC1** CAN using a CAN cable
    - Add a label "JC1" to the CAN cable
2. Connect the **left**-hip qdd100 CAN to the pi3hat **JC2** CAN using a CAN cable
    - Add a label "JC2" to the CAN cable
3. Connect the left qdd100 to the power dist board using a PWR cables
4. Connect the right qdd100 to the power dist board using a PWR cables

## 3) Enjoy!

...
