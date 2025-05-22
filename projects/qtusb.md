# Developing multi-platform USB applications with Qt

_Germany 24.05.2013_

![alt](/projects/qtusb.svg)

USB is very popular and user-friendly computer interface. Unfortunately it is far from the most easy ones to use. 
This article is meant to provide a guidelines and samples on building multi-platform application from the 
side of device and host as well.

In many cases CDC(virtual serial) class device is enough but there might be situations where user wan to avoid using it (for example to obscure communication and block third part software access).
I will show how to create true plug and play generic bulk device on Windows and how to create Linux version of the same software.
I believe that this way is much more professional than HID "hack" (using HID class for both way communication).


The application will allow to control Launchpad RGB led colour using simple GUI on PC.

There are several software projects involved:

* [TI StellarisWARE](http://www.ti.com/tool/sw-lm3s) - provides embedded USB stack and basic examples. 
* [Qt](https://qt-project.org/) - provides multi platform application framework and widget toolkit.
* [libusbX](http://libusbx.org/) - provides generic access to USB devices on multiple platforms.

There are multiple USB libraries available. For example:

* Microsoft [winusb](http://msdn.microsoft.com/en-us/library/windows/hardware/ff540174(v=vs.85).aspx) - Native for windows (platform-dependent)
* [libusb 0.1](http://www.libusb.org/wiki/APIs) - Now legacy. Unix (platform-dependent)
* [libusb-win32](http://www.libusb.org/wiki/libusb-win32) - Now legacy. Windows (platform-dependent)
* [libusb 1.0](http://www.libusb.org/wiki/libusb-1.0) - multi platform solution, alternative to libusbX

#### What are the advantages of libusbx over libusb?

Quoting <http://libusbx.org/>:
> Apart from frequent releases, which include regular bugfixes as well as exciting new features (please check our roadmap), you should find that we are a lot more responsive and that, rather than focus our efforts on elements that are of little interest to you, or an ever delayed promise of "better" features that fail to materialize, we strive to bring you the best possible user and developer experience today.
> Also, unlike libusb, we fully subscribe to the Release Early, Release Often (RERO) philosophy, upon which the success of the Linux kernel and countless other Open Source projects is based.
> Finally, if there's anything the failure of libusb has taught us, it's that a project should never fail to listen to you, its user... As such, libusbx is as much your library as it is ours, and we hope that you will engage with us to help make it even greater!

libusbx supports Windows, Linux, MacOS X, OpenBSD and NetBSD. Multiple language bindings exist including Python and C<sup>#</sup>.

> 2014-07-06: libusbx was merged back to libusb project. See [ this post](http://libusbx.1081486.n5.nabble.com/Libusbx-devel-Announcing-libusb-1-0-18-as-well-as-libusbx-1-0-18-FINAL-td2375.html).


#### What about VID/PID?
If you are planning commercial product you need to have custom VID((Vendor ID))/PID((Product ID)). You may buy your VID from USB Implementers Forum or use one from MCU manufacturer.
* [ USB.org How do I get a USB VID, TID and PID?](http://www.usb.org/developers/usbfaq#12)
* [ TI Stellaris USB VID/PID Sublicense Application](http://www.ti.com/mcu/docs/mcuorphan.tsp?contentId=72713&DCMP=STELLARIS&)
# Software

## Embedded
Code for embedded device is based on Generic Bulk example provided by TI. 
Instead of echoing data back to PC data is processed and LEDs are set according to it. 
Additionally device provide OS Descriptors unlike TI example.
Please view my [winusb](/projects/winusb) project for more information on what OS Descriptors are and how to use them with TI StellarisWARE.
Software for MCU does not change for any PC platform.

There are 4 commands that MCU can understand:
1. *0x0E* - **E**nable LEDs 
1. *0x0D* - **D**isable LEDs
1. *0x0C* - Set **c**olour of LEDs (followed by 6 bytes: 2x Red, 2x Green, 2x Blue)
1. *0x0A* - Host **a**sk for status. Device will reply with 1 byte indicating LED current state
* [qtusb_led_bulk.zip](/media/qtusb_led_bulk.zip)

## Windows

![alt](/media/qtusb_gui.png) GUI with device connected under Windows.

This sample application was written in Qt 5. GUI controls are disabled as long as device is not connected. Connection/disconnection is fully automatic. Program pools device status every 500[ms] to check if user disabled LED by pressing on-board switch (SW1). Button LEDs ON is toogle-type. When LEDs are active button glows.

[usb_windows_gui.zip](/media/usb_windows_gui.zip)

### Linking libusbx

I have downloaded the most recent release of library (http://sourceforge.net/projects/libusbx/) and decompressed it.
There are 2 options on linking it: static or dynamic.
I am choose static to reduce output file count.

Now we need to:
1. Add header file to our project by coping `*[...]\include\libusbx-1.0\libusb.h*` to our project
1. Copy compiled library to our project folder `*[...]\MinGW32\static\libusb-1.0.a*`
1. Add library binary by adding following line to `****.pro*` file of our project ```LIBS += -L$$PWD -lusb-1.0```

### Detecting device mount/remove

It is possible to get a notification from Windows when our device is connected or disconnected from the system.

```
#include <dbt.h>

[...]

//
// Register for device connect notification
//
DEV_BROADCAST_DEVICEINTERFACE devInt;
ZeroMemory( &devInt, sizeof(devInt) );
devInt.dbcc_size        = sizeof(DEV_BROADCAST_DEVICEINTERFACE);
devInt.dbcc_devicetype  = DBT_DEVTYP_DEVICEINTERFACE;
devInt.dbcc_classguid   = GUID_DEVINTERFACE_LAUNCHPAD;
//
HDEVNOTIFY m_hDeviceNotify =
            RegisterDeviceNotification((HANDLE)winId(),&devInt, DEVICE_NOTIFY_WINDOW_HANDLE );
//
if(m_hDeviceNotify == NULL)
{
    qDebug() << "Error: Failed to register device notification!";
    qApp->quit();
}
```

Structure *devInt* consists variable *GUID_DEVINTERFACE_LAUNCHPAD*. This variable stores [GUID](https://en.wikipedia.org/wiki/Universally_unique_identifier) of device interface.

```
static const GUID GUID_DEVINTERFACE_LAUNCHPAD =
{ 0xfd96fadb, 0x9246, 0x4017, { 0x8d, 0x76, 0x3e, 0x30, 0x77, 0x80, 0xf6, 0xeb } };
//![alt](fd96fadb-9246-4017-8d76-3e307780f6eb)
```

Device interface GUID usually is stored in driver *.inf* file. Since we are using OS Descriptors we can define it in OS Properties descriptor

```
const g_sOSProperties g_pOSProperties =
{
 dwLength: 			sizeof(g_pOSProperties),
 bcdVersion:			0x0100,
 wIndex:			5,
 wCount:			3,

 dwSize:			sizeof(L"DeviceInterfaceGUID")+sizeof(L"{4d36e978-e325-11ce-bfc1-08002be10318}")+14,//132,
 dwPropertyDataType: 		1,	//(Unicode string
 wPropertyNameLength: 		sizeof(L"DeviceInterfaceGUID"),
 bPropertyName: 		L"DeviceInterfaceGUID",
 dwPropertyDataLength:		sizeof(L"{fd96fadb-9246-4017-8d76-3e307780f6eb}"),
 bPropertyData: 		L"{fd96fadb-9246-4017-8d76-3e307780f6eb}", 
[...]
```

Handling of the messages is being performed in a standard way. In case message is interesting for us we emit signal.

```
// Function that receive messages 
// This is windows-specific
bool MainWindow::nativeEvent(const QByteArray& eventType, void* message,
                             long* result)
{
    Q_UNUSED( result );
    Q_UNUSED( eventType );

    MSG* msg = reinterpret_cast<MSG*>(message);

    // Does this specific message interest us?
    if(msg->message == WM_DEVICECHANGE)
    {
        switch(msg->wParam)
        {
        case DBT_DEVICEARRIVAL:
            emit signal_DeviceConnected();
            break;

        case DBT_DEVICEREMOVECOMPLETE:
            emit signal_DeviceDisconnected();
            break;
        }
    }

    // Qt handles the rest
    return false;
}
```

## Linux

![alt](/media/qt_usb_linux.png)

I am using Debian 7 with LXDE. 

We cannot use windows-specific routines under Linux. To check if device is connected or not we will pool udev monitor. 
Additionally we need to set udev rules to allow non-root users access device.

At this moment Linux requires user action to install device unlike Windows. It is possible to add udev rules through GUI (root obviously needed). 
If true plug-and-play is required it is better to use standard USB class (for example CDC).

[usb_gui.zip](/media/usb_gui.zip)

### Linking libraries

If your system is up-to-date you will most likely have both libraries installed. You can link them using following qmake code:

```
LIBS += -L/usr/local/lib/ -lusb-1.0
LIBS += -L/usr/lib/ -ludev
```

### udev rules

Create a rule for device by making a new file:

`  nano /etc/udev/rules.d/usb_led_bulk.rules`

with following content:

`  SUBSYSTEMS=="usb", ATTRS{idVendor}=="1cbe", ATTRS{idProduct}=="0003", GROUP="users", MODE="0666", SYMLINK+="rgb_led"`

This will allow non-root users to access the device. Also device will be accessible through path */dev/rgb_led*

Restart udev service for changes to take effect */etc/init.d/udev restart*

There are more actions that udev rules can implement. For example launching application when device is connected.

### Detecting device mount/remove

udev allow user applications to receive messages on changes in devices filesystem. 
One can filter messages by subsystem and type. 
In our case we want to receive USB device notifications from USB subsystem (it also emits USB interface messages).
Finally monitor is activated and file descriptor ([socket file](https://en.wikipedia.org/wiki/Unix_file_types)) retrieved. 

```
// Create the udev object
if (!(udev = udev_new()))
[..]

// Set up a monitor to monitor usb devices
mon = udev_monitor_new_from_netlink(udev, "udev");
// We want only to receive information about usb devices
udev_monitor_filter_add_match_subsystem_devtype(mon, "usb", "usb_device");
udev_monitor_enable_receiving(mon);
fd = udev_monitor_get_fd(mon);
```

The messages need to be pooled periodically. I created timer that fires every 250 [ms].

```
// Start timer that will periodicaly check if hardware is connected
monitorTimer = new QTimer(this);
connect(monitorTimer, &QTimer::timeout, this, &MainWindow::monitorTimerTick );
monitorTimer->start(250);
```

Timer code checks if there is a new message. select() returns amount of messages. In this case function is non-blocking but one can implement timeout easy here.

```
void MainWindow::monitorTimerTick()
{
    // Set up select
    fd_set fds;
    struct timeval tv;
    int ret;
    FD_ZERO(&fds);
    FD_SET(fd, &fds);
    tv.tv_sec = 0;
    tv.tv_usec = 0;

    ret = select(fd+1, &fds, NULL, NULL, &tv);

    // Check if our file descriptor has received data.
    if (ret > 0 && FD_ISSET(fd, &fds))
    {
```

When new message is confirmed code check if it from our hardware by looking into vendor id and product id.
If device matches, code checks type of event and emits appropriate Qt signal.

```
// Get the device
if ( (dev = udev_monitor_receive_device(mon)) == NULL)
[...]
// Now check if the device is our rgb_led launchpad

const char* str_action = udev_device_get_action(dev);
const char* str_PID = udev_device_get_property_value(dev, "ID_MODEL_ID");
const char* str_VID = udev_device_get_property_value(dev, "ID_VENDOR_ID");

[...]
// Compare strings and send signals
if ( (strcmp(STR_PRODUCT_ID,str_PID) == 0) && (strcmp(STR_VENDOR_ID,str_VID) == 0) )
{
   if (strcmp("add",str_action) == 0)
   {
      emit signal_DeviceConnected();
   }
   else if (strcmp("remove",str_action) == 0)
   {
      emit signal_DeviceDisconnected();
   }
[...]

    // If there are more events to process, do not wait for next tick!
    if (ret-1 > 0)
        monitorTimerTick();
```

# References

* <http://libusbx.sourceforge.net/api-1.0/>
* <http://www.signal11.us/oss/udev/>
* <http://www.freedesktop.org/software/systemd/libudev/>
* <http://linux.die.net/man/8/udevadm>
* <http://www.linuxforu.com/2012/06/some-nifty-udev-rules-and-examples/>
* <http://www.reactivated.net/writing_udev_rules.html>
* <http://hackaday.com/2009/09/18/how-to-write-udev-rules/>
* <http://msdn.microsoft.com/en-us/library/windows/hardware/gg463179.aspx>

> TODO: Build single software package for MCU, Win and Linux
