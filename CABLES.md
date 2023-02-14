# Cables

## Comms cables

- Connectors: JST PH-3 (*i.e.* 3-pin JST connectors with 2.0 mm (PH) pin-to-pin pitch)
- Wire gauge: 26 AWG (24 AWG to 32 AWG should work)

Comms cable have female-female connectors, that is, female connectors on both sides. Pins inside are ordered as follows when looking from the cable to the JST connector:

- Left: ``CAN_H`` (typically blue)
- Center: ``CAN_L`` (typically green)
- Right: ``GND`` (typically black)

See also: [JST PH-3 CAN](https://github.com/mjbots/power_dist/blob/main/docs/reference.md#jst-ph-3-can) in the power dist reference.

## Power cables

- Connectors: XT-30
- Wire gauge: 14 or 16 AWG

Power cables from one actuator to the next have female-female connectors, while power cables to the power dist board have female-male connectors.
