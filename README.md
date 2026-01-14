# Hardware for Upkie wheeled bipeds

<img align="right" height="150" src="https://github.com/user-attachments/assets/c4875d4b-3a93-4938-8836-7221ded15141">

This repository provides FreeCAD and STL files to 3D print the mechanical parts of [Upkie wheeled bipeds](https://github.com/upkie/upkie).

## Getting started

This repository uses Git LFS to distribute large files, as the full revision history of CAD files would be memory-consuming. You will need to install Git LFS for your operating system. For instance, on a Debian-based Linux distribution:

```console
sudo apt install git-lfs
```

If you cloned this repository with Git LFS installed, all files will be in your working directory. If you cloned the repository without Git LFS, you can pull large files by `git lfs pull`.

## Add-ons

### Earflap

Provisional connector to attach a [60x60x25 mm, 24 V DC fan](https://www.amazon.fr/Ventilateur-60x60x25mm-22dBA-Sunon-MF60252V21000UA99/dp/B07ZBSBP33/) to Upkie's head. Helps avoid thermal throttling when the robot actively balances for more than one hour.

* [STL file](add-ons/earflap/earflap.stl)

### Handle

Regular handle to grab the robot and move it around.

* [STL file](add-ons/handle/handle.stl)
* [Blender project](add-ons/handle/handle.blend)

<img align="right" src="https://github.com/upkie/upkie_parts/assets/1189580/0c6855b4-e5e8-41a2-86e3-0561b63a771f" height="150">

## See also

- [Build instructions](https://github.com/upkie/upkie/wiki): printing and assembling a new Upkie
- [Discussions](https://github.com/upkie/upkie/discussions): around Upkie's hardware and software
- [mjbots/quad](https://github.com/mjbots/quad/tree/main/hw/chassis/3dprint): an open-source quadruped from which torso meshes in Upkie were initially imported
