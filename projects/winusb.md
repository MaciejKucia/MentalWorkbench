# USB CDC + Microsoft descriptors

## Project Abstract

The aim of this project is to extend [TI StellarisWare](http://www.ti.com/tiva) USB CDC Device demo with 
[Microsoft OS Descriptors](http://msdn.microsoft.com/en-us/library/windows/hardware/gg463179.aspx). 
By doing so one turn device WCID((Windows Compatible ID)) compliant.
Using this optional, vendor specific extension to USB specification is supposed to have numerous advantages. 
The most important is true plug-and-play without use of *.inf* descriptor files. 
Moreover MS OS Descriptors can provide other data usually shipped with *.inf* file.

Windows has numerous drivers for basic USB classes, for example:
* CDC
* HID
* MSC
* Audio
* Bluetooth
* Content Secourity
* Imaging
* Hub Device
* Media Transfer Protocol
* Printer
* Smart Card
* Video

WinUSB also allow for using USB raw transfers: control, bulk, interrupt.

> Automated driver installation is natively supported in Windows 8. Previous versions of windows down to Windows XP can benefit from it as long as user has access to the internet and Windows Update service can download drivers. If this service is blocked user must provide *.inf* therefore automated installation and true plug and play is non-functional.

## Hardware

[TI Stellaris Launchpad](http://processors.wiki.ti.com/index.php/Stellaris_LaunchPad) with no modifications will be used in this project.

## Software

The project is accessible for download through [GitHub page](https://github.com/MaciejKucia/OS_Descriptors). 
Project is based on TI StellarisWare USB CDC Device demo code modified by lawrence_jeff for Stellaris Launchpad 
support. Please see Stellarisiti 
[thread](http://forum.stellarisiti.com/topic/453-launchpad-usb-example-and-documentation-additionslabs/).

Below steps to follow implementing OS descriptors.

### Step 1 - USB version

> If the USB Device Descriptor’s bcdUSB field is equal to 0x0100 or 0x0110, the hub driver will skip the query for the MS OS Descriptor and move to the “Serial Number String Descriptor Query” state.
I changed *USBShort(0x110),* to *USBShort(0x200),* in *g_pCDCSerDeviceDescriptor* in *usbdcdc.c*

### Step 2 - Microsoft OS String Descriptor

If the device reports USB version 2.0 or higher Windows is sending request for non-standard string descriptor. The descriptor has a index-number of *0xEE*. Appropriate condition must be added to *usbdenum.c* under line *1789: case USB_DTYPE_STRING:*.

User must return speciall MS-defined string descriptor. The only value that can be changed is vendor code. Vendor code is used during further non-standard requests but in the end it does not have any relevance.

```
const unsigned char g_pOSDescriptorPresentString[] =
{
    0x14,
    USB_DTYPE_STRING,
    'M', 0, 'S', 0, 'F', 0, 'T', 0, '1', 0, '0', 0, '0', 0,
    0xBE, // Vendor code
    0
};
```

### Step 3 - Microsoft Compatible ID Feature Descriptor

Windows asks for OS feature descriptor (0xC0) that falls into non-standard request in Stellaris USB stack.

Those two request fall into CDC *HandleRequests* code (*usbcdc.c*). I catch *0xC0* request in this function.
First only header is requested to determine size of whole descriptor.

### Step 4 - Microsoft Extended Properties Feature Descriptor

Extended properties descriptor provides additional information that is added to Windows registry upon device enumeration. 
Unfortunately it seems that both Label and Icon properties have no effect. 

Handling is same as in step 3 with the exception for request type is *0xC1*.

### Summary

Below comparison of hot plugged USB device

#### Without OS descriptors

![alt](/media/winusb_usb.png)

#### With OS descriptors

![alt](/media/winusb_usb2.png)

## Notes

When you are developing your application it is convenient to have open regedit((Windows registry editor)) and have 2 paths saved in favourites:
* `*HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\usbflags*` - Stores information if device with specific VID PID has OS descriptors or not.
* `*HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Enum\USB*` - Stores information on class and other (this key is removed on device uninstall in Device Manager).

Removing appropriate sub keys from preceding path allows for re-enumeration of device. 

## References

* <https://github.com/pbatard/libwdi/wiki/WCID-Devices>
* MSDN <http://blogs.msdn.com/b/usbcoreblog/archive/2009/10/31/how-does-usb-stack-enumerate-a-device.aspx>
* MSDN <http://msdn.microsoft.com/en-us/library/ff553426.aspx>
* MSDN [Microsoft-Defined USB Descriptors](http://msdn.microsoft.com/en-us/library/windows/hardware/ff537430(v=vs.85).aspx)
* MSDN [WHCK USB MS OS Descriptor related test fail](http://social.msdn.microsoft.com/Forums/en-US/whck/thread/8cbda6d4-87d5-4549-95c4-e4bc86532bb4/)
* MSDN [Windows Hardware Certification Kit (HCK)](http://msdn.microsoft.com/en-us/library/windows/hardware/hh833788.aspx)
* MSDN <http://msdn.microsoft.com/en-us/library/windows/hardware/jj151573(v=vs.85).aspx>
* MSDN [System-Defined Device Setup Classes Available to Vendors](http://msdn.microsoft.com/en-us/library/windows/hardware/ff553426(v=vs.85).aspx)
* MSDN [How to install WinUSB.sys without a custom INF?](http://blogs.msdn.com/b/usbcoreblog/archive/2012/09/26/how-to-install-winusb-sys-without-a-custom-inf.aspx)

## Project TODOs

* Better comments in code
* Make a more complex example - composite device
* Implementing Container ID descriptors
* MSP430 code?
* Validating if different classes work (currently only CDC confirmed)
