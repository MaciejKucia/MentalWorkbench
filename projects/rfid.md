# RFID booster pack

![alt](/projects/rfid/rfid_rockets.png)

The aim of this project is to design and build a breakout board for TI RFID transceiver chip TRF7970a compatible with Stellaris Launchpad.

TRF7970a supports following radio standards:

| | | | | | | |
| --- | --- | --- | --- | --- | --- | --- |
|  ISO14443A/B  ||||  ISO15693 ISO18000-3 (Mode 1)  |  FeliCa  |  NFC  |
|  106 [kbps]  |  212 [kbps]  |  424 [kbps]  |  848 [kbps]  | ::: |  213 [kbps] \\ 424 [kbps]  |  Type 1-4  |

Additional project considerations:
* Simple layout
* Low cost (2 layer board)
* Focus on parallel interface and ISO 15693

> This is a research project without deadline. I have created the board to explore RFID technology, NOT develop a full product. Do not use for commercial applications. Please visit GitHub for most recent software. 

> Currently supported technology: 
> * ISO15693 single slot anticollision and block read.

![alt](/projects/rfid/rfid_image.jpg)

## Schematics

* [nfc_boosterpack.zip](/projects/rfid/nfc_boosterpack.zip)
* [Board layout PDF](/projects/rfid/rfid_booster_pack.pdf)
* [Schematic PDF](/projects/rfid/frid_booster_pack_-_schematic.pdf)

## Hardware

* Operating voltage 3.3 [V] (Remember to set __Chip Status Control Register__)
* Device was designed for use with Launchpad's emulator serial connection. Please do not use DEVICE USB. Pin PD7 is used to sense DEVICE USB bus voltage. If you need to use DEVICE USB please remove resistor R15.
* Clock output is unused as Stellaris Launchpad does have it's own clocking source.
* TRF7970a EN2 is permanently pulled high (sleep mode)

### RFID Booster pinout

| Left header ||||
| --- | --- | --- | --- |
|  Desc  |   Pin A  |  Pin B   |  Desc  | 
| 3V3 VCC|  1  |  1  | |
| ASK/OOK|  2  |  2  | GND |
| |  3  |  3  | |
| |  4  |  4  | |
| IRQ |  5  |  5  | |
| |  6  |  6  | |
| |  7  |  7  | |
| Led1 |  8  |  8  | |
| Led2 |  9  |  9  | |
| |  10  |  10  | |


|  Right header ||||
|  --- | --- | --- | --- |
|  Desc  |   Pin A  |  Pin B   |  Desc  | 
| EN1 |  1  |  1  | GND |
| T1|  2  |  2  | MOD |
| T2|  3  |  3  | DATA_CLK |
| T3|  4  |  4  | |
| T4|  5  |  5  | |
| T5|  6  |  6  | |
| T6|  7  |  7  | |
| T7|  8  |  8  | |
| T8|  9  |  9  | |
| |  10  |  10  | |

> Please take note that naming is a bit misleading. T8 is the least significant bit and T1 most significant bit.

### Pin MUX

| BP Pin | MCU Pin | LP Pin | **Parallel** | **SPI SS** | **SPI** | LP Pin 2 |
|  --- | --- | --- | --- | --- | --- | --- |
| ASK/OOK | PB5 | A2 |  -  |  -  |  -  | 
| IRQ | PE4 | A5 |  Interrupt request  |||
| LED1 | PA5 | A8 |  User LED 1  |||
| LED2 | PA6 | A9 |  User LED 2  |||
| EN1 | PF2 | D1 |  Chip enable  |||
| MOD | PB2 | B2 |  -  |  -  |  -  |
| DATA<sub>CLK</sub> | PE0 | A3 |  CLK  |||   C3 (PD0)  |
| T1 | PF3 | D2 |  I/O 7  |  MOSI   ||  C6 (PD3)  |
| T2 | PB3 | D3 |  I/O 6  |  MISO   || C5 (PD2)  |
| T3 | PC4 | D4 |  I/O 5  |  -  |  -  |
| T4 | PC5 | D5 |  I/O 4  |  SS  |  -   |  C4 (PD1)  |
| T5 | PC6 | D6 |  I/O 3  |  -  |  -  | 
| T6 | PC7 | D7 |  I/O 2  |  V<sub>DD</sub>  |  V<sub>DD</sub>  |
| T7 | PD6 | D8 |  I/O 1  |  V<sub>DD</sub>  |  V<sub>SS</sub>  |
| T8 | PD7 | D9 |  I/O 0  |  V<sub>SS</sub>  |  V<sub>SS</sub>  |

Additionally:

| MCU Pin | Function |
|  --- | --- |
| PA0 | UART RX |
| PA1 | UART TX |

Current revision of the board requires SPI and interface select pins to be connected externally. Code uses SSI1 peripheral for SPI control.

BP - boosterpack; LP - launchpad

## Software

All necessary software is located in the MCU. The PC communicates with the kit trough USB UART.

![alt](/projects/rfid/rfid.svg)

Software stack consists of 4 layers:
* Hardware abstraction layer
* Chip support layer 
* RF protocol layer 
* User layer
* Project [github repository](https://github.com/MaciejKucia/BP_RFID)

## Booster pack in action

The sample application is a simple playback control device. Stellaris Launchpad acts as HID USB device sending "Consumer" commands (see USB documentation) to host.
Resistor R15 was removed therefore device can be powered without debug USB connection. 

Three different tags have different values written in memory. Device is looking for tags in range around every second. If it finds tag, memory content readout is performed. 
One byte defines tag function (play pause, next track, previous track). If tag remains in the field for more than one read cycle, it is ignored. To use tag function second time in a row just move tag out of range, so device can detect "no tag" condition. After that tag will not be ignored.

This will also work with Linux and Android!

<http://www.youtube.com/v/dAkR1WXPeXE?.swf>

* [Zipped CCS project](/projects/rfid/rfid_control_example.zip)

## Next board revision notes

* SPI only? SS switch?
* SPI Buffer for tristate line?
* EN2 pull down for poweroff
* Fully compatible with small Launchpad
* Bigger antenna to fit components "inside"

## References

* [TI processors.wiki Build Your Own Boosterpack](http://processors.wiki.ti.com/index.php/BYOB)
* [TI processors.wiki BoosterPack Design Guide](http://processors.wiki.ti.com/index.php/BoosterPack_Design_Guide)
* [TI TRF7970a products page](http://www.ti.com/product/trf7970a)
* [Antenna Matching for the TRF7960 RFID Reader](http://www.ti.com/lit/an/sloa135/sloa135.pdf)
* [TRF7960TB HF RFID Reader Module User's Guide](http://www.ti.com/lit/ug/slou297/slou297.pdf)
* [TRF7970A Evaluation Module (EVM)](http://www.ti.com/lit/ug/slou321a/slou321a.pdf)
* [TRF7970A Firmware Design Hints](http://www.ti.com/lit/an/sloa159/sloa159.pdf)
* [TRF7970A Reference Firmware Description](http://www.ti.com/lit/an/sloa157/sloa157.pdf)
* [TI TRF7970A C Code Samples](http://www.ti.com/litv/zip/sloc250)
* [Implementation of the ISO15693 Protocol in the TI TRF796x](http://www.ti.com/lit/an/sloa138/sloa138.pdf)

### NFC

* <http://apps4android.org/nfc-specifications/NFCForum-TS-Type-4-Tag_2.0.pdf>
* <http://apps4android.org/nfc-specifications/NFCForum-TS-Type-3-Tag_1.1.pdf>
* <http://www.ecma-international.org/publications/standards/Ecma-340.htm>
* <http://www.adafruit.com/datasheets/Introduction_to_NFC_v1_0_en.pdf>
* <http://www.developer.nokia.com/Community/Wiki/Understanding_NFC_Data_Exchange_Format_(NDEF)_messages>
* <http://www.nfc-forum.org/specs/spec_list/#tagtypes>

### ISO 15693

* [TRF7960 Evaluation Module ISO 15693 Host Commands](http://www.ti.com/lit/an/sloa141/sloa141.pdf)
* [Identification cards — Contactless integrated circuit(s) cards - Vicinity cards — Part 3: Anti-collision and transmission protocol](http://www.waazaa.org/download/fcd-15693-3.pdf)
* [Tag-it™ HF-I Plus Transponder Inlays Reference Guide](http://www.ti.com/lit/ug/scbu004b/scbu004b.pdf)
* [13.56-MHz ENCAPSULATED STANDARD TRANSPONDER](http://www.ti.com/lit/ds/symlink/rf-hdt-dvbe.pdf)

### ISO 14443

* <http://wg8.de/wg8n1496_17n3613_Ballot_FCD14443-3.pdf>
* <http://www.waazaa.org/download/fcd-14443-4.pdf>

### Other

* <http://static.googleusercontent.com/external_content/untrusted_dlcp/www.google.com/pl//events/io/2011/static/presofiles/how_to_nfc.pdf>

#### Sample project references

* <http://forum.stellarisiti.com/topic/453-launchpad-usb-example-and-documentation-additionslabs/>
* [Universal Serial Bus (USB) HID Usage Tables](http://www.usb.org/developers/devclass_docs/Hut1_11.pdf)
* [ MSDN Enhanced Keyboards and Windows](http://msdn.microsoft.com/en-us/library/windows/hardware/gg463446.aspx)