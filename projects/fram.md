# Smart City Batteryless, Wireless and Serviceless Sensor Node

## Design assumptions

The aim of this project is to build batteryless and serviceless device for measuring passing cars count and speed.

> The project is not finished due to lack of essential parts (radio quartz and inductor for boost converter).
> Still I think it is cool therefore I am posting it.

## Applications

* Intelligent traffic control
* Industrial sensor networks
* Security systems
* Intelligent lighting
* Crowd management

System does not have to be limited to the cars. Piezo sensors can detect any moving mass including both vehicles and humans.

## Location

![alt](/projects/fram1.svg)

Device can be located under asphalt. The piezo generators will be located under track of car wheels. The wireless link with local wired node allows for minimum invasion into road structure.

## Block diagram

![alt](/projects/fram2.svg)

The mechanical energy from the passing cars is transformed using piezoelectric transducers into electric power. The current is rectified and boosted in high-efficiency, low input voltage boost converter.
The energy is stored in capacitor. Other sources of energy can be connected as well. 

MSP430 is in deep sleep until external interrupt wakes it up. Radio is completely cut off from the power unless MCU opens MOSFET.

## Experiments

Alongside hardware development I am experimenting with the piezoelectric power generation.

I am using 35 [mm] Piezo plates:
![alt](https://lh3.googleusercontent.com/-5d7HnvwaeTE/USd7OeQ3vbI/AAAAAAAAES8/QCuAoHb52-Q/s902/IMG_20130222_150722.jpg)

![alt](https://lh6.googleusercontent.com/-XCjBSjsFnE4/USd5swk-Q2I/AAAAAAAAESk/X4wXPneSHOM/s1059/IMG_20130222_111941.jpg)
Test setup consist of piezo, diode rectifier, 100 [μF] capactor, diode and 2 [kΩ] resistor. Few gentle bends charge the capacitor allowing diode to light after button press.

![alt](https://lh5.googleusercontent.com/-o2wvy7cN_v8/USd5wCh8jgI/AAAAAAAAES4/Y1lgP-SVBgs/s1059/IMG_20130222_141554.jpg)
In this setup 4 piezos were connected in parallel to increase power. Rigid bar applies force to the centers of piezos. Piezos are mounted on soft base allowing them to bend slightly.
This setup produces much higher voltage on capacitor.
![alt](https://lh6.googleusercontent.com/-uEVRCAlN_Cw/USd5wJ91q8I/AAAAAAAAES4/MhQSphodH9Q/s1059/IMG_20130222_141525.jpg)
I was able to charge capacitor easily up to 6V.

> Piezos are made of solid material and will break if applied force is too high. Broken piezo will produce much less power if any at all.

![alt](https://lh5.googleusercontent.com/-aRyN30Ysb9g/USd5wAhSk-I/AAAAAAAAES4/TOF0w-WysdY/s1059/IMG_20130222_141740.jpg)
Close-up of the setup. The LED is bright.

> Maybe this simple method of energy generation could be used for powering "active" cat's eyes on roads?

## Hardware

Hardware design considerations:
* Low leakage current capacitors
* Maximum radio power - folded dipole antenna
* Low cost - minimal board size, components on one side

### Schematics

* [fram_wsn.pdf](/media/fram_wsn.pdf)
* [fram_wsn2.pdf](/media/fram_wsn2.pdf)

### Layout

![alt](/media/fram_layout.png)

## Software

Application is simple and can be represented by following flow diagram:

![alt](/projects/fram3.svg)

After power-up MCU initializes all peripherals and goes into deep sleep. Two external interrupts are responsible for measuring the vehicle speed. First interrupt starts timer, the second one stops it and stores time in FRAM. 
If timer overflow occur measurement is discarded. After several measurements MCU activates radio, sets it and burst data stored in FRAM.

## Summary

* GHz radio might be attenuated by asphalt. More experiments are required to estimate the best radio settings for minimal power and usability. 

### Prototype

![alt](/media/fram_wsn_dbg.jpg)

The device is connected to [MSP-EXP430FR5739](http://www.ti.com/tool/msp-exp430fr5739) for debugging and control signals emulation.
## References

### Datasheet
* [MSP430FR57xx Family User's Guide](http://www.ti.com/lit/ug/slau272b/slau272b.pdf)
* [MSP430FR572x](http://www.ti.com/lit/ds/symlink/msp430fr5720.pdf)
* [CC2550 Low-Cost Low-Power 2.4 GHz RF Transmitter](http://www.ti.com/lit/ds/symlink/cc2550.pdf)
* [bq25504 Ultra Low Power Boost Converter with Battery Management for Energy Harvester Applications](http://www.ti.com/lit/ds/symlink/bq25504.pdf)
 
### Application note

* [TI Low Power RF Designer’s Guide to LPRF](http://www.ti.com/lit/sg/slya020a/slya020a.pdf)
* [TI Antenna Selection Guide](http://www.ti.com/lit/an/swra161b/swra161b.pdf)
* [TI Folded dipole antenna for CC2500](http://www.ti.com/lit/an/swra118/swra118.pdf)
* [Self-Powered, Ambient Light Sensor Using bq25504](http://www.ti.com.cn/cn/lit/an/slua629/slua629.pdf)

### Other

* [LTC3588-1 - Piezoelectric Energy  Harvesting Power Supply](http://cds.linear.com/docs/Datasheet/35881fa.pdf)
* [TI Powering Low-Power RF Products](http://www.ti.com/lit/an/swra173b/swra173b.pdf)
* [Estimation of Electric Charge output for Piezoelectric Energy Harvesting](http://institutes.lanl.gov/ei/pdf_files/Strain2004.pdf) - Henry A. Sodano and Daniel J. Inman Center for Intelligent Material Systems and Structures Virginia Polytechnic Institute and State University 2004
* <http://www.digikey.com/us/en/techzone/energy-harvesting/resources/articles/power-management-ics.html>
* <http://electronicdesign.com/energy/boost-charger-ic-completes-energy-harvesting-puzzle>
* [Maximizing FRAM Write Speed on the MSP430FR573x](http://www.ti.com/lit/an/slaa498/slaa498.pdf)

### Tools

* <http://www.ti.com/product/cc2550>
* <http://www.ti.com/product/msp430fr5720>
* <http://www.ti.com/product/bq25504>
* <http://www.nxp.com/products/diodes/switching_diodes/BAS45AL.html> - low forward drop voltage