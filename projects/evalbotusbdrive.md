# Evalbot Chronos USB Control

Evalbot ([EKB-UCOS3-EVM](https://www.ti.com/lit/po/spmt213/spmt213.pdf) from Texas Instruments) is a simple, jet fun robotic development platform for ARM® Cortex™-M3 Stellaris ([LM3S9B92](https://www.ti.com/product/lm3s9b92)) microcontroller. Another great tool from TI is a MSP430 [Chronos](https://processors.wiki.ti.com/index.php/EZ430-Chronos) a programmable sport watch with radio-enabled MSP430 microcontroller ([CC430F6137](http://www.ti.com/product/cc430f6137)).
Evalbot has a headers for TI's standard radio modules. You can plug the [CC1101EMK](https://www.ti.com/tool/cc1101emk868-915) module and use sample code from [StellarisWARE](https://ti.com/stellarisware) (''StellarisWare\boards\ek-evalbot\chronos_drive\'') to drive your Evalbot remotely.

Operation in such configuration can be seen on the following video (Property of [Elektor International Media](http://www.youtube.com/user/ElektorIM)):

<https://www.youtube.com/v/zixo3dkpsTA?.swf?400×333>

Evalbot also has a [USB OTG](https://en.wikipedia.org/wiki/USB_On-The-Go) functionality. I was curious if is it possible to use a CC1101 USB dongle shipped with Chronos to drive Evalbot. What I found was that the dongle is just a simple [CDC Class](https://en.wikipedia.org/wiki/USB_communications_device_class) device. I was able to write a very simple CDC Host driver and receive packets from Chronos. 
Chronos is using stock unmodified firmware. Simply start accelerometer mode just like in the TI Control Center demo.

## Wave playback

There is even more! Evalbot has an build in micro SD card slot and audio coded with small speaker. The V2 binaries allow to play wave files. 

  * Wav file format: MONO 16 bit 11025 [Hz]
  * SD card file system: Fat
  * File naming: 3 digit hex:  ''000.wav, 001.wav 002.wav, ..., 00A.wav, 010.wav ...''

Files are being played in a loop. You can play next file using __SW2__ button on Evalbot, or Chronos' __# button__ in acc mode. The __* button__ selects next file without playing. 

## Binaries

You can flash following binaries using LM Flash Programmer. 

  * [BIN file](/media/evalbotusbdrive.zip)
  * [V2 BIN file](/media/evb_sound.zip)

Source code is currently not available.

## Operation
The effect of the program can be seen on the following video:

<http://www.youtube.com/v/XfTkw6fsvPU&?.swf?400×333>

After powering the device on USB dongle is enumerated automatically. The radio link is inactive until user press __SW 1__ button. Pressing this button toggles [SimpliciTI](http://www.ti.com/tool/simpliciti) link.

The Chronos uses stock software in accelerometer mode. Tilting watch forward makes robot drive forward. Tilting sideways causes robot to turn. To stop the robot simply move your hand upwards.

  * Yellow LED on the Ethernet socket signals successful enumeration of USB device.
  * Orange LED on the Ethernet socket signals SipliciTI packets reception.

## Future development perspective

This project can be extended. I doubt I will return into it as my design assumptions were fulfilled. Some of the possibilities are:

  - Creating Chronos-specific USB CDC Host driver and publishing source code for it.
  - Making drive control more fluid (variable speed of wheels during turning)

**Note:** All trademarks are the property of their respective owners.
