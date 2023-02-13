# Build Upkie

Instructions and resource files to build Upkie.

## 3D printing

3D printing project (3MF) files were configured using [PrusaSlicer](https://github.com/prusa3d/PrusaSlicer). They should work with other slicers, but your mileage may vary.

* Print all chassis parts from [3d\_printing/chassis](3d_printing/chassis).
* Print all leg parts from [3d\_printing/legs/hollow](3d_printing/legs/hollow).
    - Optionally, if you don't mind hanging cables and prefer a lower print time, you can print [wooden leg](3d_printing/legs/wooden) parts instead.

## Assembly

### Torso

...

### Left leg

...

### Right leg

...

### Final assembly

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
