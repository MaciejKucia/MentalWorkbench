# Programming AVR with ADA programming language


The purpose of this page is to provide information on building and running embedded software on [Atmel AVR](http://www.atmel.com/products/microcontrollers/avr/default.aspx) family devices using [Ada programming language](https://en.wikipedia.org/wiki/Ada_(programming_language)). Some information can be obtained in sourceforge project [AVR-Ada](http://sourceforge.net/projects/avr-ada/). Unfortunately AVR-Ada project is no longer being developed. [AdaCore](https://pl.wikipedia.org/wiki/AdaCore), the company maintaining GNAT compiler recently released [cross compiler](https://en.wikipedia.org/wiki/Cross_compiler) version of GNAT for AVR. All tools are cross-platform, if binaries are not available they can be compiled to run on any platform as sources are attainable to download.

January 2012

## Software

To start writing embedded code in Ada, several software packages are required:
  * [GNAT AVR](http://libre.adacore.com/libre/download2?config=avr-elf-windows&version=2011#)
  * AdaCore GPS (part of GNAT AVR package)
  * [WinAVR](http://sourceforge.net/projects/winavr/) GNU gcc tools and libraries for AVR
  * [Atmel AVR Studio 5](http://www.atmel.com/tools/ATMELAVRSTUDIO5_0.aspx) (Only for device XML description file)

## CRT - C Run-Time Library

Usually programs written in Ada comes with extensive run-time library. In embedded environment especially such low-end as in AVR8 platform, memory cost of such RTL is very high. Additionally there's no OS and [HAL](https://pl.wikipedia.org/wiki/Warstwa_abstrakcji_sprz%C4%99towej). In embedded world initialization code is device-specific and CRT((C Run-Time Library)) must consist:

  * Program entry point
  * Vector table
  * Stack initialization
  * Global variables initialization

AdaCore provides sample initialization code written in assembler for ATmega2560. Instead of writing code for other chips it is easier (and safer) to use CRT code from WinAvr. Compiled CRT files can be found in `\avr\lib\` subdirectory of WinAvr distribution. For example: AtMega8 uses following file: `\avr\lib\avr4\crtm8.o`. It is advised to compile WinAvr rather than using pre-compiled files.

## Device specyfication package

Each AVR device has a number of internal peripherals and registers associated with them. Registers are located at various memory locations specific to the type of the device. AdaCore provides tool (avr_gen) for generating Ada package based on Atmel XML device specification files, but only in redundant AVRStudio 4 format. I rewritten similar tool which works with current device specification format (AVRStudio 5). Please note that tool is designed to work with AVR8 device description files (using it with AVR32 and Xmega families will require modifications).

  * [Source](/projects/avrada/tool_src)
  * [Windows binaries](/media/avrada/avr_gen_avrs5.zip)
  * [Sample output file for AtMega8](/projects/avrada/tool_sampleM8)
  * [Sample output file for AtMega2560](/projects/avrada/tool_sampleM2560)

To build this tool following software is required:

  * GNAT x86 (for your OS)
  * XMLAda (Both software packages are available on <http://libre.adacore.com>)

To build device specification package:
  - Build or unzip tool
  - Copy device specification file from `<Program Files>\Atmel\AVR Studio 5.0\devices\` into tool directory
  - Run `main device.xml >avr-device.ads` where `device` is changed into appropriate name. Ex: `main atmega8.xml >avr-atmega8.ads`

## Makefile

When all required files and tools are installed, machine code can be compiled using `avr-gnatmake` tool. It's handy to keep compilation and programming scripts in makefile and invoke them using `make`.

Sample makefile for AtMega8 is:

```makefile
all: main.hex main.lss sizedummy

program:
	avrdude -pm8 <PROGRAMMER SPECIFIC> -Uflash:w:"main.hex"

main.elf: force
	avr-gnatmake main -o $@ -Os -mmcu=avr4 --RTS=zfp -largs crtm8._o -nostdlib -lgcc -mavr4 -Tdata=0x00800200

main.lss: main.elf
	-avr-objdump -h -S main.elf  >"main.lss"

main.hex: main.elf
	avr-objcopy -O ihex $< $@

sizedummy: main.elf
	-avr-size --format=avr --mcu=atmega8 main.elf

clean:
	$(RM) *.o leds  *.ihex *.ali *.elf *.hex *.lss *.map
```

The most important line is:

```avr-gnatmake main -o $@ -Os -mmcu=avr4 --RTS=zfp -largs crtm8._o -nostdlib -lgcc -mavr4 -Tdata=0x00800200```

  * `-Os` turns on size optimization  
  * `--RTS=zfp` sets Ada RTL to 'Zero FootPrint' 
  * `-mmcu=avr4` and `-mavr4` sets device architecture to avr4 (AtMega8 specific, change for other devices)
  * `-largs` allows passing arguments to linker
  * `crtm8._o` forces linker to link Ada code with CRT. Please note that the **file extension was changed** from `.o` to `._o`, if the extension remained unchanged file would be **removed** when using `make clean`
  * `-nostdlib` forces linker not to attach any libraries by itself
  * `-lgcc` required when using `-nostdlib`, allows resolving reference to procedure `main`
  * `-Tdata=0x00800200` sets data code section to appropriate address

## Setting up GPS

GPS (GNAT Programming Studio) is an editor maintained by AdaCore and it's default editor for software written in Ada. If makefile is present it is easy to use it to develop embedded software in Ada.
  - Select `Build->Settings->Targets`
  - Select `Run->Run Main` and change `Target model` to `make`
  - Select `Clean->Clean All` and change `Target model` to `make`
  - Assure that command in text box is `make clean`
  - Select `Project->Build *` and change `Target model` to `make`
  - Assure that command in text box is `make all`
  - Now code can be generated and run just like in any other Ada project.

## Useful code samples
Following code samples are written and tested for ATmega8 device.

### Lighting LED

Assuming LED anode is connected to AtMega8 PORTB pin 0 and cathode is connected to the power rail trough appropriate resistor.

```
with Interfaces; use Interfaces;
with AVR.AtMega8; use AVR.AtMega8;

procedure Main is

   -- LED
   LedPort : Unsigned_8;
   for LedPort'Address use AVR.atmega8.PORTB'Address;
   LedPin : constant := 2#00000001#;

begin

   -- Initialize
   DDRB := 1; -- only pin 0 is output
   
   -- turn on
   LedPort := LedPort or LedPin;
   
   -- turn off
   LedPort := LedPort and not LedPin;
   
   -- toogle
   LedPort := LedPort xor LedPin;

   -- infinite loop: end of program
   loop end loop;

end Main;
```

### Using interrupts

avr-interrupts.adb

```
-- AVR ATMEGA8 - Interrupts
-- Maciej Kucia Krakow 2012
-- MIT/X11 license 

with System.Machine_Code;

package body AVR.Interrupts is

   procedure Enable is
   begin
      System.Machine_Code.Asm ("sei", Volatile => True);
   end Enable;

   procedure Disable is
   begin
      System.Machine_Code.Asm ("cli", Volatile => True);
   end Disable;

end AVR.Interrupts;
```

avr-interrupts.ads

```
-- AVR ATMEGA8 - Interrupts
-- Maciej Kucia Krakow 2012
-- MIT/X11 license

package AVR.Interrupts is

   -- Enables interrupts
   procedure Enable;
   -- Disables interrupts
   procedure Disable;

private
   pragma Inline(Disable);
   pragma Inline(Enable);

end AVR.Interrupt;
```

### Buffered interrupt driven UART

avr-uart.ads

```
with Interfaces; use Interfaces;
with AVR.strings; use AVR.strings;
with System;

package AVR.UART is

   Flaga_A : boolean := False;

   --  Initialize timer and port B.
   procedure Init;

   -- wypisuje znak
   procedure WriteChar (char : Character);
   procedure Write(d : Unsigned_8);

   -- zwraca ilosc znakow w
   function BufferCnt return Integer;

   -- wczytuje znakow w buforze wejsciowym
   function Read return Unsigned_8;
   function ReadChar return Character;

   -- wypisuje lancuch znakow
   procedure WriteString( str: AVR_String);
   procedure WriteStringP( str: AVR_String);

   -- wypisuje liczbe
   procedure WriteInteger (i : Integer; b:  Integer);

   -- Wysyla znaki z bufora
   procedure ProcessWrite;

private
   pragma Volatile(Flaga_A);
   pragma Inline_Always( BufferCnt);
   pragma Inline_Always(processWrite);
   procedure Last_Chance_Handler
     (Source_Location : System.Address;
      Line            : Integer);
   pragma Export (C, Last_Chance_Handler, "__gnat_last_chance_handler");

end AVR.UART;
```

avr-uart.adb

```
with System.Machine_Code; use System.Machine_Code;
with AVR.atmega8; use AVR.atmega8;
with AVR.strings; use AVR.strings;
with AVR.Interrupt;
with Environment;

package body AVR.UARTis

   type Unsigned_3  is mod 2 **  3;
   for Unsigned_3'Size use  8;

   type Unsigned_4  is mod 2 **  4;
   for Unsigned_4'Size use  8;

   -- Bufory cykliczne

   type TablicaUART8 is array (0..7) of Unsigned_8;
   type TablicaUART16 is array (0..15) of Unsigned_8;

   BuffWe : TablicaUART8;
   pragma Volatile(BuffWe);
   BuffWeP : Unsigned_3  :=0 ; -- poczatek
   pragma Volatile(BuffWeP);
   BuffWeK : Unsigned_3  :=0 ; -- koniec
   pragma Volatile(BuffWeK);
   BuffWeC : Integer range 0..8  :=0 ; -- ile
   pragma Volatile(BuffWeC);

   BuffWy : TablicaUART16;
   pragma Volatile(BuffWy);
   BuffWyP : Unsigned_4  :=0 ; -- poczatek
   pragma Volatile(BuffWyP);
   BuffWyK : Unsigned_4  :=0 ; -- koniec
   pragma Volatile(BuffWyK);
   BuffWyC : Integer range 0..16  :=0 ; -- ile
   pragma Volatile(BuffWyC);

   --  Przerwania
   procedure USART_RxComplete;
   pragma Machine_Attribute (USART_RxComplete, "signal");
   pragma Export (C, USART_RxComplete, AVR.Interrupt.vec_uart_rx);
   procedure USART_RxComplete is
      rec : Unsigned_8;
   begin
      while (UCSRA and UCSRA_RXC) = 0 loop null; end loop;
      rec := UDR;
      --UDR := rec; --echo

      if BuffWeC <= 8 then
         BuffWe(Integer(BuffWeK)) := rec;
         BuffWeK:=BuffWeK + 1;
         BuffWeC:=BuffWeC+1;
      end if;
      Flaga_A := True;
   end USART_RxComplete;

   procedure USART_TxComplete;
   pragma Machine_Attribute (USART_TxComplete, "signal");
   pragma Export (C, USART_TxComplete, AVR.Interrupt.vec_uart_dree);
   procedure USART_TxComplete is
   begin
      if BuffWyC > 0 then
         while (UCSRA and UCSRA_UDRE) = 0 loop null; end loop;
         UDR := BuffWy(Integer(BuffWyK));
         BuffWyK:=BuffWyK + 1; -- ada dba o zaokraglanie
         BuffWyC:=BuffWyC-1;
      else
         UCSRB := UCSRB and not (UCSRB_UDRIE);
      end if;
   end USART_TxComplete;


   function BufferCnt return Integer is
   begin
      return Integer(BuffWeC);
   end;

   -- Zamiany typow
   function To_Char is new Ada.Unchecked_Conversion (Target => Character,
                                                     Source => Unsigned_8);


   function To_Uint8 is new Ada.Unchecked_Conversion (Target =>  Unsigned_8,
                                                      Source => Character);

   procedure Write (d : Unsigned_8) is
   begin
      if BuffWyC < 16 then
         BuffWy(Integer(BuffWyP)) := d;
         BuffWyP := BuffWyP + 1;
         BuffWyC := BuffWyC + 1;
      end if;
   end Write;

   procedure WriteChar (char : Character) is
   begin
      Write(To_Uint8(char));
   end WriteChar;

   characters : constant array (0 .. 15) of Character := ('0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F');

   procedure WriteInteger (i : Integer; b:  Integer) is
      help : Integer range 0..9 :=0;
      tmp : Integer := i;
      arr : array (0..9) of Character;
   begin

      if tmp < 0 then WriteChar('-'); tmp := -tmp; end if;

      if tmp = 0 then WriteChar('0');
      else

         while tmp /= 0 loop
            arr(help) := characters( tmp mod b );
            tmp := tmp / b;

            help := help+1;
         end loop;

         while help /=0 loop
            WriteChar(arr(help-1));
            help := help - 1;
         end loop;

      end if;

   end WriteInteger;

   procedure ProcessWrite is
   begin
      -- Aktywacja przerwania
      if ( BuffWyC > 0) then
         UCSRB := UCSRB or UCSRB_UDRIE;
      end if;
   end ProcessWrite;

   -- wypisuje lancuch znakow na uart
   procedure WriteString( str: AVR_String) is
   begin
      for I in str'Range loop
         WriteChar (str(I));
      end loop;
   end WriteString;

   -- odczyt z pamieci
   function Get_PGM_Byte (Addr : System.Address) return Unsigned_8 is
      Result : Unsigned_8;
   begin
      Asm ("lpm %0, Z",
           Outputs => Unsigned_8'Asm_Output ("=r", Result),
           Inputs  => System.Address'Asm_Input ("z", Addr));
      return Result;
   end Get_PGM_Byte;

   function Get_PGM_Char (Addr : System.Address) return Character is
      U : Unsigned_8;
   begin
      U := Get_PGM_Byte (Addr);
      return Character'Val (U);
   end Get_PGM_Char;

   -- wypisuje lancuch znakow z pamieci programu
   procedure WriteStringP( str: AVR_String ) is
      C : Character;
   begin
      for U in str'Range loop
         C := Get_PGM_Char (str (U)'Address);
         WriteChar (C);
      end loop;
   end WriteStringP;

   function Read return Unsigned_8 is
      ret : Unsigned_8;
   begin
      if BuffWeC > 0 then
         ret := BuffWe(Integer(BuffWeP));
         BuffWeP:= BuffWeP+1;
         BuffWeC:= BuffWeC-1;
         return ret;
      else
         return 0;
      end if;
   end Read;

   -- Odczyt znaku z bufora
   function ReadChar return Character is
   begin
	return To_Char(Read);
   end ReadChar;

   -- Initializacja UART
   procedure Init is
   begin
      -- Uruchamiam moduly odbiorczy i nadawczy USART
      UCSRB := UCSRB or UCSRB_RXEN or UCSRB_TXEN or UCSRB_RXCIE  or UCSRB_UDRIE;
      -- 8 bit 1 bit stopu
      UCSRC := UCSRC or UCSRC_URSEL or UCSRC_UCSZ0 or UCSRC_UCSZ1;
      -- Wczytuje poprzednio obliczone wartosci baud
      --UBRRH := 0;
      UBRRL := 51; !!!!!!!!!!!!!!!!1

      BuffWe(0):=0;
      BuffWy(0):=0;
   end;


   procedure Last_Chance_Handler
     (Source_Location : System.Address;
      Line            : Integer)
   is begin
     null;
     -- error handling here
   end Last_Chance_Handler;

end AVR.UART;
```

Example:
```
with AVR.UART; use AVR.UART;
```

### Storing strings in program memory

```
-- AVR ATMEGA8 - Strings
-- Maciej Kucia Krakow 2012
-- 

with Interfaces; use Interfaces;

package AVR.strings is

   type AVR_String is array (Unsigned_8 range <>) of Character;
   type Progmem_String is new AVR_String;
   subtype PStr is Progmem_String;

   --  Strings stored in flash memory:
   Flash_String_HELLOADA : AVR_String := "Hello Ada!" & ASCII.LF;
   pragma Linker_Section (Flash_String_HELLOADA, ".progmem");

   Flash_String1 : AVR_String := "This is string nr.1 " & ASCII.LF;
   pragma Linker_Section (Flash_String1, ".progmem");

   Flash_String2 : AVR_String := "There is no new line after this";
   pragma Linker_Section (Flash_String2, ".progmem");

end AVR.strings;
```

### Timer0 PWM

avr-timer0pwm.ads

```
with Interfaces; use Interfaces;

package AVR.TIMER0PWM is

   -- inicjalizuje timer0 w trybie PWM
   procedure InitPWM;

   -- ustawia wypelnienie PWM
   procedure SetPWM(val: Unsigned_8);
   
private
   pragma Inline(SetPWM);
   pragma Inline(InitPWM);

end AVR.TIMER0PWM;
```

ada-timer0pwm.adb

```
with AVR.AtMega8; use AVR.AtMega8;

package body AVR.TIMER0PWM is

   procedure InitPWM is
   begin
      -- Tumer setup
      OCR1AH :=0;
      OCR1AL :=0;
      OCR1BH :=0;
      OCR1BL :=0;
      TCCR1A := TCCR1A_WGM10 or TCCR1A_COM1A1;
      TCCR1B := TCCR1B_WGM12 or TCCR1B_CS10;
   end InitPWM;

   procedure SetPWM(val:  Unsigned_8) is
   begin
      OCR1AH := val;
      OCR1AL := val;
   end SetPWM;

end AVR.TIMER0PWM;
```

### TWI interface

avr-twi.ads

```
package AVR.TWI is

   TW_READ  : constant := 1;
   TW_WRITE : constant := 0;

   TWI_FREQ  : constant := 100_000;

   procedure Init;

   function Start(address : Unsigned_8) return Boolean;

   procedure Stop;

   function Write( data : Unsigned_8 ) return Boolean;

   function ReadAck return Unsigned_8;

   function ReadNak return Unsigned_8;

private
   pragma Inline_Always(Init);

end AVR.TWI;
```

avr-twi.adb

```
with AVR.AtMega8; use AVR.AtMega8;
with Environment;

package body AVR.TWI is

   -- Start
   TW_START        : constant := 16#08#;
   TW_REP_START    : constant := 16#10#;

   TW_STATUS_MASK  : constant := 248;

   -- trans
   TW_MT_SLA_ACK   : constant := 16#18#; -- SLA+W transmitted, ACK got
   TW_MT_SLA_NACK  : constant := 16#20#; -- SLA+W transmitted, NACK got

   TW_MT_DATA_ACK  : constant := 16#28#; -- data transmitted, ACK got
   TW_MT_DATA_NACK : constant := 16#30#; -- data transmitted, NACK got


   -- rec
   TW_MR_SLA_ACK   : constant := 16#40#; -- SLA+R transmitted, ACK got
   TW_MR_SLA_NACK  : constant := 16#48#; -- SLA+R transmitted, NACK got

   TW_MR_DATA_ACK  : constant := 16#50#; -- data transmitted, ACK got
   TW_MR_DATA_NACK : constant := 16#58#; -- data transmitted, NACK got


   function To_Char is new Ada.Unchecked_Conversion (Target => Character,
                                                     Source => Unsigned_8);

   procedure Init is
   begin
      -- Init twi prescaler and bitrate
      TWSR := 0;
      TWBR := Interfaces.Unsigned_8 ( ((Environment.F_CPU / TWI_FREQ) - 16 ) /2 );
   end Init;

   -- zwraca false gdy failed
   function Start(address : Unsigned_8) return Boolean is
      twst : Unsigned_8;
   begin

      --Send start
      TWCR := TWCR_TWINT or TWCR_TWSTA or TWCR_TWEN;

      -- czekaj
      while ( (TWCR and TWCR_TWINT) = 0) loop null; end loop;

      twst := TWSR and TW_STATUS_MASK and 16#F8#;

      -- sprawdzam odpowiedz
      if ( twst /= TW_START) and ( twst /= TW_REP_START ) then return false; end if;

      -- Wysylam adress
      TWDR := address;
      TWCR := TWCR_TWINT or TWCR_TWEN;

      -- czekam
      while ( (TWCR and TWCR_TWINT) =0 ) loop null; end loop;

      -- sprawdzam
      twst :=  TWSR and TW_STATUS_MASK and 16#F8#;

      if ( (twst /= TW_MT_SLA_ACK) and (twst /= TW_MR_SLA_ACK) ) then return false; end if;

      return true;

   end Start;

   procedure Stop is
   begin
      TWCR := TWCR_TWINT or TWCR_TWEN or TWCR_TWSTO;
      while (( TWCR and TWCR_TWSTO ) /= 0) loop null; end loop;
   end Stop;

   -- true jezeli sie powiodlo
   function Write( data : Unsigned_8 ) return Boolean is
      twst : Unsigned_8;
   begin

      TWDR := data;

      TWCR := TWCR_TWINT or TWCR_TWEN;

      while ( (TWCR and TWCR_TWINT) = 0 ) loop null; end loop;

      twst := TWSR and TW_STATUS_MASK and 16#F8#;
      if (twst /= TW_MT_DATA_ACK) then
         return false;
      end if;

      return true;

   end Write;

   function ReadAck return Unsigned_8 is
   begin

      TWCR := TWCR_TWINT or TWCR_TWEN or TWCR_TWEA;

      while ( (TWCR and TWCR_TWINT) = 0 ) loop null; end loop;

      return TWDR;

   end ReadAck;

   function ReadNak return Unsigned_8 is
   begin

      TWCR := TWCR_TWINT or TWCR_TWEN;

      while ( (TWCR and TWCR_TWINT) = 0 ) loop null; end loop;

      return TWDR;

   end ReadNak;

end AVR.TWI;
```

### Watchdog

avr-watchdog.ads

```
package AVR.Watchdog is

   type Watchdog_Timeout is
     (
      WT16k,
      WT32k,
      WT64k,
      WT128k,
      WT256k,
      WT512k,
      WT1024k,
      WT2048k
     );
   for Watchdog_Timeout'Size use 8;

   --  init watchdog reset/interrupt
   procedure Enable(tout:Watchdog_Timeout);

   --  reset watchdog timer
   procedure Wdr;
   procedure Reset renames Wdr;

   --  disable watchdog reset/interrupt
   procedure Disable;

private
   pragma Inline_Always (Wdr);
   pragma Inline_Always (Reset);
   pragma Inline_Always (Enable);
   pragma Inline_Always (Disable);
end AVR.Watchdog;
```

avr-watchdog.adb

```
with System.Machine_Code;  use System.Machine_Code;
with AVR.AtMega8;          use AVR.AtMega8;

package body AVR.Watchdog is

   function WT2Uint8 is
     new Ada.Unchecked_Conversion (Watchdog_Timeout, Unsigned_8);

   procedure Enable(tout : Watchdog_Timeout) is
   begin
      WDTCR := WDTCR or WDTCR_WDCE or WDTCR_WDE or WT2Uint8(tout);
      WDTCR := WDTCR or WDTCR_WDCE or WDTCR_WDE or WT2Uint8(tout);
   end Enable;

   procedure Disable is
   begin
      WDTCR := WDTCR or WDTCR_WDCE or WDTCR_WDE;
      WDTCR := 0;
   end Disable;

   procedure Wdr is
   begin
      Asm ("wdr", Volatile => True);
   end Wdr;

end AVR.Watchdog;
```