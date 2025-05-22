# Setting up wireless LAN in Sitara starter kit

[Sitara starter](http://processors.wiki.ti.com/index.php/AM335x_Starter_Kit) kit is a great tool for embedded Linux development.
I do not want to use Ethernet cable and I have no spare keyboard to use therefore I needed to configure connection manually. 

By default device have enabled tty0 console at serial line connected to on-board USB hub. When board is connected to PC it should see new virtual COM port.
The only user on the device is root without password. I am using unmodified stock firmware.

1. Connect board to PC using USB cable. Power the board.
1. Connect to board using PuTTY (Serial 11500) COM port number depends on user system.
1. Start or re-boot board
1. Login as root
1. Create psk hex using [wpa_passphrase](http://linux.die.net/man/8/wpa_passphrase) and put it in */etc/wpasupplicant.conf* (*<nowiki>wpa_passphrase network_ssid password >> /etc/wpasupplicant.conf</nowiki>*). 
1. Edit */etc/network/interfaces* (use [vi](http://www.rru.com/~meo/useful/vi/))
1. Comment out current *wlan0* interface definition
1. Add new *wlan0* interface definition: ```auto wlan0
iface wlan0 inet dhcp
    wpa-conf /etc/wpa_supplicant.conf```
1. Reset network interface */etc/init.d/networking restart*
1. Now device should connect to AP. User can reset device to check if connection is acquired on boot.

If the network connection is successful user can telnet or ssh into board. USB connection is no more needed.

## Static IP

User might want to set static IP. It is possible to set static IP in AP((Access Point)) DHCP settings. To set static IP in embedded device
use following changes for */etc/network/interfaces*:

```
auto wlan0
iface wlan0 inet static
    wpa-conf /etc/wpa_supplicant.conf
    address 192.168.1.10
    netmask 255.255.255.0
    gateway 192.168.1.1
```
