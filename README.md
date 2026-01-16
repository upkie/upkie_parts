# Hardware for Upkie wheeled bipeds

<img align="right" width="200" src="https://github.com/user-attachments/assets/6c9b24ed-2439-414a-94e7-167b035e9f6f">

This repository provides FreeCAD and STL files to 3D print the mechanical parts of [Upkie wheeled bipeds](https://github.com/upkie/upkie).

### Getting started

This repository uses Git LFS to distribute large files, as the full revision history of CAD files would be memory-consuming. You will need to install Git LFS for your operating system. For instance, on a Debian-based Linux distribution:

```console
sudo apt install git-lfs
```

If you cloned this repository with Git LFS installed, all files will be in your working directory. If you cloned the repository without Git LFS, you can pull large files by `git lfs pull`.

## Legs

- **Hip support** ([FreeCAD](legs/hip_support/hip_support.FCStd) | [STL](legs/hip_support/hip_support.stl)): Optional 3D printed part with a bearing to reduce play and "protect" knee actuators from radial load.
    - Bearing reference: 40x52x7mm [Amazon](https://amzn.eu/d/3NPo64S).
- **Upper leg** ([FreeCAD](legs/upper_leg/upper_leg.FCStd) | [STL](legs/upper_leg/upper_leg.stl)): Upper segment of the leg assembly.
- **Knee support** ([FreeCAD](legs/knee_support/knee_support.FCStd) | [STL](legs/knee_support/knee_support.stl)): Optional 3D printed part with a bearing to reduce play and "protect" knee actuators from radial load.
    - Bearing reference: 40x52x7mm [Amazon](https://amzn.eu/d/3NPo64S).
- **Lower leg** ([FreeCAD](legs/lower_leg/lower_leg.FCStd) | [STL](legs/lower_leg/lower_leg.stl)): Lower segment connecting to the wheel hub.
- **Wheel hub** ([FreeCAD](legs/wheel_hub/wheel_hub.FCStd) | [STL](legs/wheel_hub/wheel_hub.stl)): Integrated wheel and hub assembly for mounting tires.
    - There is also a [hex variant](legs/wheel_hub/hex_variant/) for 17 mm wheel hex driver RC cars. It is easier to adapt to various RC wheels, but more brittle.

## Torso

- **Case** ([FreeCAD](torso/case/case.FCStd) | [STL](torso/case/case.stl)): Main torso enclosure.
- **Battery shore plug** ([STL](torso/battery_shore_plug/battery_shore_plug.stl)): Plug where two leaf springs can be connected to the battery via an XT90-S cable.
- **Battery stud** ([STL top](torso/battery_stud/battery_stud_top.stl) | [STL bottom](torso/battery_stud/battery_stud_bottom.stl)): Two-part hold for securing the battery inside the Upkie.
- **Raspberry Pi support** ([FreeCAD](torso/raspberry_support/raspberry_support.FCStd) | [STL](torso/raspberry_support/Raspberry_support.stl)): Mounting bracket for the Raspberry Pi.
- **Power dist board support** ([FreeCAD](torso/powerboard_support/powerboard_support.FCStd) | [STL](torso/powerboard_support/Powerboard_support.stl)): Mounting bracket for the power distribution board.

## Add-ons

- **Camera support** ([FreeCAD](add-ons/camera_support/camera_support.FCStd) | [STL](add-ons/camera_support/camera_support.stl)): Mounting bracket for an OAK-D Lite camera.
- **Handle** ([STL](add-ons/handle/handle.stl)): Regular handle to grab the robot and move it around.

## See also

- [Build instructions](https://github.com/upkie/upkie/wiki): printing and assembling a new Upkie.
- [Discussions](https://github.com/upkie/upkie/discussions): around Upkie's hardware and software.
- [mjbots/quad](https://github.com/mjbots/quad/tree/main/hw/chassis/3dprint): an open-source quadruped from which torso meshes in Upkie were initially imported.
