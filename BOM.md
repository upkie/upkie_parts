# Bill of materials

* Comms cable: see [CABLES.md](CABLES.md)
* Power cable: see [CABLES.md](CABLES.md)
* UPE: Unit Price Estimate (retrieved: February 2023)

| Short name         | Part name                   | Requirements  | Quantity  | UPE (USD) | Suppliers     |
|--------------------|-----------------------------|---------------|-----------|-----------|---------------|
| hex wrench         | 17 mm RC Hex Wrench         | -             | 1         | 1         | [3D print](https://www.printables.com/model/59120-17mm-rc-hex-wrench/comments/151854) |
| leg power cable    | female-female power cable   | length: 40 cm | 4         |           | |
| M2 inserts         | M2x4x3.5 heat set inserts   | M2x4x3.5      | 10        | 0.02      | online retail |
| raspi heat sink    | Aluminum Heatsink           | for rpi 4b+   | 1         | 5         | online retail |
| M2 screws          | M2x8 socket head screws     | M2x8          | 10        | 0.02      | online retail |
| M3 inserts         | M3x4x5 heat set inserts     | M3x4x5        | 20        | 0.02      | online retail |
| M3 screws          | M3x8 socket head screws     | M3x8          | 50        | 0.02      | online retail |
| microSD card       | microSDXC card              | U3, V30, A2   | 1         | 20        | online retail |
| pi3hat             | mjbots pi3hat               | r4.4b+        | 1         | 150       | [mjbots](https://mjbots.com/products/mjbots-pi3hat-r4-4b) |
| power dist         | mjbots power dist           | r4.3b+        | 1         | 140       | [mjbots](https://mjbots.com/products/mjbots-power-dist-r4-3b) |
| qdd100             | mjbots qdd100 servo         | beta 2+       | 4         | 540       | [mjbots](https://mjbots.com/products/qdd100-beta-3) |
| raspi              | Raspberry Pi 4 Model B      | -             | 1         | 100       | see [raspberrypi.com](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/#find-reseller) |
| torso power cable  | male-female power cable     | length: 30 cm | 3         | 2         | |
| wheel              | RC 1:8 rubber tyre          | see [Wheels](#wheels) | 2 | 7         | online retail |
| wheel actuator     | moteus developer kit        | r4.11+        | 2         | 230       | [mjbots](https://mjbots.com/products/moteus-r4-11-developer-kit) |
| wheel hex coupler  | 17 mm Wheel Hex Coupler     | -             | 2         | 1.5       | online retail |

Summing up unit price estimates multiplied by part quantities, the total price estimate for this BOM is waitforcompletebom USD.

## Specifications

## Wheels

* Outer diameter: 112 mm
* Inner diameter: 83 mm
* Wheel drive hex: 17 mm
* Axle hole diameter: 12 mm

Changing the outer diameter is super easy (barely an inconvenience), you will only need to update your agent's configuration. Most agents are robust to cm-wide variations of this diameter.

Changing the inner diameter, wheel drive hex or axle hole diameter will require a corresponding update to the 3D printed [wheel hub](3d_printing/legs/hollow/wheel_hub_v6.3mf). The wheel hub should be a tight fit into the wheel, which usually takes a few iterations to get right. If you select a different wheel drive hex or axle hole diameter, make sure to buy a matching hex coupler.
