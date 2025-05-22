# DIY Xbox 360 PC wireless receiver with MSP430 control

_Germany 15.06.2013_

## Abstract

Xbox 360 wireless controller can be used with PC when special adapter is used. 
Xbox 360 itself has a separate RF module that communicates with motherboard through USB interface. 
Additional interface is used to initialize module LEDs and start sync process. 
One can create adapter for a fraction of cost using only several elements. 

![alt](/projects/xbr.jpg)

## Description

Required parts:
* Xbox360 RF board
* USB cable
* MCU
* LDO (3.3 [V])
* Capacitor/resistor for MCU

Pinout of the RF board from top:

![alt](/projects/xbr.svg)

Board must be powered by 3v3 so I decided to use LDO. 
Furthermore to start pairing process specific serial command must be sent. I have used MSP430G2231 for this task.
MCU need reset pull-up resistor and decoupling capacitor.
Pins 1 and 8 are connected to RF board.

Pairing process starts few seconds after device is powered. No external button needed.


```
#include <msp430.h> 
#include <stdbool.h>

#define DATA 1
#define CLOCK 8

#define DTA_INPUT P1DIR &= ~DATA;
#define DTA_OUTPUT P1DIR |= DATA;

#define DTA_HI P1OUT |= DATA;
#define DTA_LO P1OUT &= ~DATA;

volatile signed   short bit_counter	=0;
volatile unsigned short command		=0;

 //Port 1 interrupt service routine
#pragma vector=PORT1_VECTOR
__interrupt void Port_1(void)
{
 P1IFG &= ~CLOCK;

 // are we sending or receiving?
 if (bit_counter>0)
 {
	 DTA_OUTPUT
	 if (command & (1<<(bit_counter-1)))
		 DTA_HI
	 else
		 DTA_LO
 }
 // stop bit!
 else if (bit_counter == 0)
 {
	 P1OUT |= DATA;
	 command=0;
 }
 else
 {
	 DTA_INPUT
	 if (P1IN&DATA)
		 command |= (1<<((11+bit_counter)));
	 else
		 command &= ~(1<<((11+bit_counter)));
 }

 bit_counter--;
}

inline void send(char s)
{
	DTA_OUTPUT
	command = s;
	bit_counter = 10;
	DTA_LO				// Send start bit
}

//------------------------------------------------------------------------------

int main(void)
{
    unsigned short delay=0;

    //
    // CLOCK
    //
    WDTCTL = WDTPW | WDTHOLD;		// Stop watchdog timer
    if (CALBC1_1MHZ==0xFF)		// If calibration constants erased
    {
      while(1);                     	// do not load, trap CPU!!
    }
    DCOCTL = 0;                     	// Select lowest DCOx and MODx settings
    BCSCTL1 = CALBC1_1MHZ;
    DCOCTL = CALDCO_1MHZ;

    //
    // Serial Interface
    //
    P1OUT |= DATA; 			// DTA HIGH
    P1DIR |= (1<<6);
    DTA_OUTPUT 				// DTA OUTPUT

    P1IES |= CLOCK;			// fires on falling edge~
    P1IFG &= ~CLOCK; 			// int cleared
    P1IE |= CLOCK; 			// int enabled

    //
    // Start
    //
    __enable_interrupt();
    __delay_cycles(2000000);

    send(132);				// LEDs active with power button on
    while(--delay);			// Delay for a while
    send(0x085);			// Start animation
    while(--delay);
    while(--delay);
    send(0x004);			// Start sync

    __delay_cycles(5000000);		// Give some extra time to finish cmd send

    __disable_interrupt();		// Turn off MCU
    _BIS_SR(LPM4_bits);

}
```

## Notes

* There is no way to detect if controller is connected without snooping USB. Current and serial responses do not change after connection.
* RF board should be easy to get as repair shops have huge stock from broken Xboxs

## References

* [STM LD1117xx datasheet](http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/CD00000544.pdf)
* [TI MSP430G2x31 Mixed Signal Microcontroller](http://www.ti.com/product/msp430g2231)
* TI Application Report [PCB-Based Capacitive Touch Sensing With MSP430 Zack Albus](http://www.ti.com/lit/an/slaa363a/slaa363a.pdf)
* TI Application Report [Capacitive Touch Sensing, MSP430™ Button Gate Time Optimization and Tuning Guide](http://www.ti.com/lit/an/slaa574/slaa574.pdf)
* [XBOX 360 Motherboard Headers and Connector](http://www.oocities.org/xbox.360@rogers.com/Public/Xbox360HC14.pdf)
* <http://web12.ger2.x-ex.com/viewtopic.php?f=13&t=4029&sid=69aff04e1efbaf199411f8dbfb315e2d>