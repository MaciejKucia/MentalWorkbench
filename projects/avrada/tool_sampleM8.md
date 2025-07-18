```ada
with Interfaces; use Interfaces;
with System;

  -- architecture = AVR8
  -- AVR Studio 5 XML avr register definition generator 
  -- Maciej Kucia, Krakow 2012 

package AVR.ATmega8 is

  --
  --  ANALOG_COMPARATOR
  --

  -- Special Function IO Register
  SFIOR : Unsigned_8;
  for SFIOR'Address	 use System'To_Address (16#50#);

   SFIOR_ACME		: constant := 16#08#; -- Analog Comparator Multiplexer Enable


  --
  --  SFIOR
  --

  -- Analog Comparator Control And Status Register
  ACSR : Unsigned_8;
  for ACSR'Address	 use System'To_Address (16#28#);

   ACSR_ACD		: constant := 16#80#; -- Analog Comparator Disable
   ACSR_ACBG		: constant := 16#40#; -- Analog Comparator Bandgap Select
   ACSR_ACO		: constant := 16#20#; -- Analog Compare Output
   ACSR_ACI		: constant := 16#10#; -- Analog Comparator Interrupt Flag
   ACSR_ACIE		: constant := 16#08#; -- Analog Comparator Interrupt Enable
   ACSR_ACIC		: constant := 16#04#; -- Analog Comparator Input Capture Enable
   ACSR_ACIS		: constant := 16#03#; -- Analog Comparator Interrupt Mode Select bits


  --
  --  SPI
  --

  -- SPI Data Register
  SPDR : Unsigned_8;
  for SPDR'Address	 use System'To_Address (16#2F#);



  --
  --  SPDR
  --

  -- SPI Status Register
  SPSR : Unsigned_8;
  for SPSR'Address	 use System'To_Address (16#2E#);

   SPSR_SPIF		: constant := 16#80#; -- SPI Interrupt Flag
   SPSR_WCOL		: constant := 16#40#; -- Write Collision Flag
   SPSR_SPI2X		: constant := 16#01#; -- Double SPI Speed Bit


  --
  --  SPSR
  --

  -- SPI Control Register
  SPCR : Unsigned_8;
  for SPCR'Address	 use System'To_Address (16#2D#);

   SPCR_SPIE		: constant := 16#80#; -- SPI Interrupt Enable
   SPCR_SPE		: constant := 16#40#; -- SPI Enable
   SPCR_DORD		: constant := 16#20#; -- Data Order
   SPCR_MSTR		: constant := 16#10#; -- Master/Slave Select
   SPCR_CPOL		: constant := 16#08#; -- Clock polarity
   SPCR_CPHA		: constant := 16#04#; -- Clock Phase
   SPCR_SPR		: constant := 16#03#; -- SPI Clock Rate Selects


  --
  --  EXTERNAL_INTERRUPT
  --

  -- General Interrupt Control Register
  GICR : Unsigned_8;
  for GICR'Address	 use System'To_Address (16#5B#);

   GICR_INT		: constant := 16#C0#; -- External Interrupt Request 1 Enable
   GICR_IVSEL		: constant := 16#02#; -- Interrupt Vector Select
   GICR_IVCE		: constant := 16#01#; -- Interrupt Vector Change Enable


  --
  --  GICR
  --

  -- General Interrupt Flag Register
  GIFR : Unsigned_8;
  for GIFR'Address	 use System'To_Address (16#5A#);

   GIFR_INTF		: constant := 16#C0#; -- External Interrupt Flags


  --
  --  GIFR
  --

  -- MCU Control Register
  MCUCR : Unsigned_8;
  for MCUCR'Address	 use System'To_Address (16#55#);

   MCUCR_ISC1		: constant := 16#0C#; -- Interrupt Sense Control 1 Bits
   MCUCR_ISC0		: constant := 16#03#; -- Interrupt Sense Control 0 Bits


  --
  --  TIMER_COUNTER_0
  --

  -- Timer/Counter Interrupt Mask Register
  TIMSK : Unsigned_8;
  for TIMSK'Address	 use System'To_Address (16#59#);

   TIMSK_TOIE0		: constant := 16#01#; -- Timer/Counter0 Overflow Interrupt Enable


  --
  --  TIMSK
  --

  -- Timer/Counter Interrupt Flag register
  TIFR : Unsigned_8;
  for TIFR'Address	 use System'To_Address (16#58#);

   TIFR_TOV0		: constant := 16#01#; -- Timer/Counter0 Overflow Flag


  --
  --  TIFR
  --

  -- Timer/Counter0 Control Register
  TCCR0 : Unsigned_8;
  for TCCR0'Address	 use System'To_Address (16#53#);

   TCCR0_CS02		: constant := 16#04#; -- Clock Select0 bit 2
   TCCR0_CS01		: constant := 16#02#; -- Clock Select0 bit 1
   TCCR0_CS00		: constant := 16#01#; -- Clock Select0 bit 0


  --
  --  TCCR0
  --

  -- Timer Counter 0
  TCNT0 : Unsigned_8;
  for TCNT0'Address	 use System'To_Address (16#52#);



  --
  --  TIMER_COUNTER_1
  --

  -- Timer/Counter Interrupt Mask Register
  TIMSK : Unsigned_8;
  for TIMSK'Address	 use System'To_Address (16#59#);

   TIMSK_TICIE1		: constant := 16#20#; -- Timer/Counter1 Input Capture Interrupt Enable
   TIMSK_OCIE1A		: constant := 16#10#; -- Timer/Counter1 Output CompareA Match Interrupt Enable
   TIMSK_OCIE1B		: constant := 16#08#; -- Timer/Counter1 Output CompareB Match Interrupt Enable
   TIMSK_TOIE1		: constant := 16#04#; -- Timer/Counter1 Overflow Interrupt Enable


  --
  --  TIMSK
  --

  -- Timer/Counter Interrupt Flag register
  TIFR : Unsigned_8;
  for TIFR'Address	 use System'To_Address (16#58#);

   TIFR_ICF1		: constant := 16#20#; -- Input Capture Flag 1
   TIFR_OCF1A		: constant := 16#10#; -- Output Compare Flag 1A
   TIFR_OCF1B		: constant := 16#08#; -- Output Compare Flag 1B
   TIFR_TOV1		: constant := 16#04#; -- Timer/Counter1 Overflow Flag


  --
  --  TIFR
  --

  -- Timer/Counter1 Control Register A
  TCCR1A : Unsigned_8;
  for TCCR1A'Address	 use System'To_Address (16#4F#);

   TCCR1A_COM1A		: constant := 16#C0#; -- Compare Output Mode 1A, bits
   TCCR1A_COM1B		: constant := 16#30#; -- Compare Output Mode 1B, bits
   TCCR1A_FOC1A		: constant := 16#08#; -- Force Output Compare 1A
   TCCR1A_FOC1B		: constant := 16#04#; -- Force Output Compare 1B
   TCCR1A_WGM1		: constant := 16#03#; -- Waveform Generation Mode


  --
  --  TCCR1A
  --

  -- Timer/Counter1 Control Register B
  TCCR1B : Unsigned_8;
  for TCCR1B'Address	 use System'To_Address (16#4E#);

   TCCR1B_ICNC1		: constant := 16#80#; -- Input Capture 1 Noise Canceler
   TCCR1B_ICES1		: constant := 16#40#; -- Input Capture 1 Edge Select
   TCCR1B_WGM1		: constant := 16#18#; -- Waveform Generation Mode
   TCCR1B_CS1		: constant := 16#07#; -- Prescaler source of Timer/Counter 1


  --
  --  TCCR1B
  --

  -- Timer/Counter1  Bytes
  TCNT1 : Unsigned_8;
  for TCNT1'Address	 use System'To_Address (16#4C#);



  --
  --  TCNT1
  --

  -- Timer/Counter1 Output Compare Register  Bytes
  OCR1A : Unsigned_8;
  for OCR1A'Address	 use System'To_Address (16#4A#);



  --
  --  OCR1A
  --

  -- Timer/Counter1 Output Compare Register  Bytes
  OCR1B : Unsigned_8;
  for OCR1B'Address	 use System'To_Address (16#48#);



  --
  --  OCR1B
  --

  -- Timer/Counter1 Input Capture Register  Bytes
  ICR1 : Unsigned_8;
  for ICR1'Address	 use System'To_Address (16#46#);



  --
  --  TIMER_COUNTER_2
  --

  -- Timer/Counter Interrupt Mask register
  TIMSK : Unsigned_8;
  for TIMSK'Address	 use System'To_Address (16#59#);

   TIMSK_OCIE2		: constant := 16#80#; -- Timer/Counter2 Output Compare Match Interrupt Enable
   TIMSK_TOIE2		: constant := 16#40#; -- Timer/Counter2 Overflow Interrupt Enable


  --
  --  TIMSK
  --

  -- Timer/Counter Interrupt Flag Register
  TIFR : Unsigned_8;
  for TIFR'Address	 use System'To_Address (16#58#);

   TIFR_OCF2		: constant := 16#80#; -- Output Compare Flag 2
   TIFR_TOV2		: constant := 16#40#; -- Timer/Counter2 Overflow Flag


  --
  --  TIFR
  --

  -- Timer/Counter2 Control Register
  TCCR2 : Unsigned_8;
  for TCCR2'Address	 use System'To_Address (16#45#);

   TCCR2_FOC2		: constant := 16#80#; -- Force Output Compare
   TCCR2_WGM20		: constant := 16#40#; -- Waveform Genration Mode
   TCCR2_COM2		: constant := 16#30#; -- Compare Output Mode bits
   TCCR2_WGM21		: constant := 16#08#; -- Waveform Generation Mode
   TCCR2_CS2		: constant := 16#07#; -- Clock Select bits


  --
  --  TCCR2
  --

  -- Timer/Counter2
  TCNT2 : Unsigned_8;
  for TCNT2'Address	 use System'To_Address (16#44#);



  --
  --  TCNT2
  --

  -- Timer/Counter2 Output Compare Register
  OCR2 : Unsigned_8;
  for OCR2'Address	 use System'To_Address (16#43#);



  --
  --  OCR2
  --

  -- Asynchronous Status Register
  ASSR : Unsigned_8;
  for ASSR'Address	 use System'To_Address (16#42#);

   ASSR_AS2		: constant := 16#08#; -- Asynchronous Timer/counter2
   ASSR_TCN2UB		: constant := 16#04#; -- Timer/Counter2 Update Busy
   ASSR_OCR2UB		: constant := 16#02#; -- Output Compare Register2 Update Busy
   ASSR_TCR2UB		: constant := 16#01#; -- Timer/counter Control Register2 Update Busy


  --
  --  ASSR
  --

  -- Special Function IO Register
  SFIOR : Unsigned_8;
  for SFIOR'Address	 use System'To_Address (16#50#);

   SFIOR_PSR2		: constant := 16#02#; -- Prescaler Reset Timer/Counter2


  --
  --  USART
  --

  -- USART I/O Data Register
  UDR : Unsigned_8;
  for UDR'Address	 use System'To_Address (16#2C#);



  --
  --  UDR
  --

  -- USART Control and Status Register A
  UCSRA : Unsigned_8;
  for UCSRA'Address	 use System'To_Address (16#2B#);

   UCSRA_RXC		: constant := 16#80#; -- USART Receive Complete
   UCSRA_TXC		: constant := 16#40#; -- USART Transmitt Complete
   UCSRA_UDRE		: constant := 16#20#; -- USART Data Register Empty
   UCSRA_FE		: constant := 16#10#; -- Framing Error
   UCSRA_DOR		: constant := 16#08#; -- Data overRun
   UCSRA_UPE		: constant := 16#04#; -- Parity Error
   UCSRA_U2X		: constant := 16#02#; -- Double the USART transmission speed
   UCSRA_MPCM		: constant := 16#01#; -- Multi-processor Communication Mode


  --
  --  UCSRA
  --

  -- USART Control and Status Register B
  UCSRB : Unsigned_8;
  for UCSRB'Address	 use System'To_Address (16#2A#);

   UCSRB_RXCIE		: constant := 16#80#; -- RX Complete Interrupt Enable
   UCSRB_TXCIE		: constant := 16#40#; -- TX Complete Interrupt Enable
   UCSRB_UDRIE		: constant := 16#20#; -- USART Data register Empty Interrupt Enable
   UCSRB_RXEN		: constant := 16#10#; -- Receiver Enable
   UCSRB_TXEN		: constant := 16#08#; -- Transmitter Enable
   UCSRB_UCSZ2		: constant := 16#04#; -- Character Size
   UCSRB_RXB8		: constant := 16#02#; -- Receive Data Bit 8
   UCSRB_TXB8		: constant := 16#01#; -- Transmit Data Bit 8


  --
  --  UCSRB
  --

  -- USART Control and Status Register C
  UCSRC : Unsigned_8;
  for UCSRC'Address	 use System'To_Address (16#40#);

   UCSRC_URSEL		: constant := 16#80#; -- Register Select
   UCSRC_UMSEL		: constant := 16#40#; -- USART Mode Select
   UCSRC_UPM		: constant := 16#30#; -- Parity Mode Bits
   UCSRC_USBS		: constant := 16#08#; -- Stop Bit Select
   UCSRC_UCSZ		: constant := 16#06#; -- Character Size
   UCSRC_UCPOL		: constant := 16#01#; -- Clock Polarity


  --
  --  UCSRC
  --

  -- USART Baud Rate Register Hight Byte
  UBRRH : Unsigned_8;
  for UBRRH'Address	 use System'To_Address (16#40#);



  --
  --  UBRRH
  --

  -- USART Baud Rate Register Low Byte
  UBRRL : Unsigned_8;
  for UBRRL'Address	 use System'To_Address (16#29#);



  --
  --  TWI
  --

  -- TWI Bit Rate register
  TWBR : Unsigned_8;
  for TWBR'Address	 use System'To_Address (16#20#);



  --
  --  TWBR
  --

  -- TWI Control Register
  TWCR : Unsigned_8;
  for TWCR'Address	 use System'To_Address (16#56#);

   TWCR_TWINT		: constant := 16#80#; -- TWI Interrupt Flag
   TWCR_TWEA		: constant := 16#40#; -- TWI Enable Acknowledge Bit
   TWCR_TWSTA		: constant := 16#20#; -- TWI Start Condition Bit
   TWCR_TWSTO		: constant := 16#10#; -- TWI Stop Condition Bit
   TWCR_TWWC		: constant := 16#08#; -- TWI Write Collition Flag
   TWCR_TWEN		: constant := 16#04#; -- TWI Enable Bit
   TWCR_TWIE		: constant := 16#01#; -- TWI Interrupt Enable


  --
  --  TWCR
  --

  -- TWI Status Register
  TWSR : Unsigned_8;
  for TWSR'Address	 use System'To_Address (16#21#);

   TWSR_TWS		: constant := 16#F8#; -- TWI Status
   TWSR_TWPS		: constant := 16#03#; -- TWI Prescaler


  --
  --  TWSR
  --

  -- TWI Data register
  TWDR : Unsigned_8;
  for TWDR'Address	 use System'To_Address (16#23#);



  --
  --  TWDR
  --

  -- TWI (Slave) Address register
  TWAR : Unsigned_8;
  for TWAR'Address	 use System'To_Address (16#22#);

   TWAR_TWA		: constant := 16#FE#; -- TWI (Slave) Address register Bits
   TWAR_TWGCE		: constant := 16#01#; -- TWI General Call Recognition Enable Bit


  --
  --  WATCHDOG
  --

  -- Watchdog Timer Control Register
  WDTCR : Unsigned_8;
  for WDTCR'Address	 use System'To_Address (16#41#);

   WDTCR_WDCE		: constant := 16#10#; -- Watchdog Change Enable
   WDTCR_WDE		: constant := 16#08#; -- Watch Dog Enable
   WDTCR_WDP		: constant := 16#07#; -- Watch Dog Timer Prescaler bits


  --
  --  PORTB
  --

  -- Port B Data Register
  PORTB : Unsigned_8;
  for PORTB'Address	 use System'To_Address (16#38#);



  --
  --  PORTB
  --

  -- Port B Data Direction Register
  DDRB : Unsigned_8;
  for DDRB'Address	 use System'To_Address (16#37#);



  --
  --  DDRB
  --

  -- Port B Input Pins
  PINB : Unsigned_8;
  for PINB'Address	 use System'To_Address (16#36#);



  --
  --  PORTC
  --

  -- Port C Data Register
  PORTC : Unsigned_8;
  for PORTC'Address	 use System'To_Address (16#35#);



  --
  --  PORTC
  --

  -- Port C Data Direction Register
  DDRC : Unsigned_8;
  for DDRC'Address	 use System'To_Address (16#34#);



  --
  --  DDRC
  --

  -- Port C Input Pins
  PINC : Unsigned_8;
  for PINC'Address	 use System'To_Address (16#33#);



  --
  --  PORTD
  --

  -- Port D Data Register
  PORTD : Unsigned_8;
  for PORTD'Address	 use System'To_Address (16#32#);



  --
  --  PORTD
  --

  -- Port D Data Direction Register
  DDRD : Unsigned_8;
  for DDRD'Address	 use System'To_Address (16#31#);



  --
  --  DDRD
  --

  -- Port D Input Pins
  PIND : Unsigned_8;
  for PIND'Address	 use System'To_Address (16#30#);



  --
  --  EEPROM
  --

  -- EEPROM Address Register  Bytes
  EEAR : Unsigned_8;
  for EEAR'Address	 use System'To_Address (16#3E#);



  --
  --  EEAR
  --

  -- EEPROM Data Register
  EEDR : Unsigned_8;
  for EEDR'Address	 use System'To_Address (16#3D#);



  --
  --  EEDR
  --

  -- EEPROM Control Register
  EECR : Unsigned_8;
  for EECR'Address	 use System'To_Address (16#3C#);

   EECR_EERIE		: constant := 16#08#; -- EEPROM Ready Interrupt Enable
   EECR_EEMWE		: constant := 16#04#; -- EEPROM Master Write Enable
   EECR_EEWE		: constant := 16#02#; -- EEPROM Write Enable
   EECR_EERE		: constant := 16#01#; -- EEPROM Read Enable


  --
  --  CPU
  --

  -- Status Register
  SREG : Unsigned_8;
  for SREG'Address	 use System'To_Address (16#5F#);

   SREG_I		: constant := 16#80#; -- Global Interrupt Enable
   SREG_T		: constant := 16#40#; -- Bit Copy Storage
   SREG_H		: constant := 16#20#; -- Half Carry Flag
   SREG_S		: constant := 16#10#; -- Sign Bit
   SREG_V		: constant := 16#08#; -- Two's Complement Overflow Flag
   SREG_N		: constant := 16#04#; -- Negative Flag
   SREG_Z		: constant := 16#02#; -- Zero Flag
   SREG_C		: constant := 16#01#; -- Carry Flag


  --
  --  SREG
  --

  -- Stack Pointer 
  SP : Unsigned_8;
  for SP'Address	 use System'To_Address (16#5D#);



  --
  --  SP
  --

  -- MCU Control Register
  MCUCR : Unsigned_8;
  for MCUCR'Address	 use System'To_Address (16#55#);

   MCUCR_SE		: constant := 16#80#; -- Sleep Enable
   MCUCR_SM		: constant := 16#70#; -- Sleep Mode Select
   MCUCR_ISC1		: constant := 16#0C#; -- Interrupt Sense Control 1 Bits
   MCUCR_ISC0		: constant := 16#03#; -- Interrupt Sense Control 0 Bits


  --
  --  MCUCR
  --

  -- MCU Control And Status Register
  MCUCSR : Unsigned_8;
  for MCUCSR'Address	 use System'To_Address (16#54#);

   MCUCSR_WDRF		: constant := 16#08#; -- Watchdog Reset Flag
   MCUCSR_BORF		: constant := 16#04#; -- Brown-out Reset Flag
   MCUCSR_EXTRF		: constant := 16#02#; -- External Reset Flag
   MCUCSR_PORF		: constant := 16#01#; -- Power-on reset flag


  --
  --  MCUCSR
  --

  -- Oscillator Calibration Value
  OSCCAL : Unsigned_8;
  for OSCCAL'Address	 use System'To_Address (16#51#);



  --
  --  OSCCAL
  --

  -- Store Program Memory Control Register
  SPMCR : Unsigned_8;
  for SPMCR'Address	 use System'To_Address (16#57#);

   SPMCR_SPMIE		: constant := 16#80#; -- SPM Interrupt Enable
   SPMCR_RWWSB		: constant := 16#40#; -- Read-While-Write Section Busy
   SPMCR_RWWSRE		: constant := 16#10#; -- Read-While-Write Section Read Enable
   SPMCR_BLBSET		: constant := 16#08#; -- Boot Lock Bit Set
   SPMCR_PGWRT		: constant := 16#04#; -- Page Write
   SPMCR_PGERS		: constant := 16#02#; -- Page Erase
   SPMCR_SPMEN		: constant := 16#01#; -- Store Program Memory Enable


  --
  --  SPMCR
  --

  -- Special Function IO Register
  SFIOR : Unsigned_8;
  for SFIOR'Address	 use System'To_Address (16#50#);

   SFIOR_ADHSM		: constant := 16#10#; -- ADC High Speed Mode
   SFIOR_PUD		: constant := 16#04#; -- Pull-up Disable
   SFIOR_PSR10		: constant := 16#01#; -- Prescaler Reset Timer/Counter1 and Timer/Counter0


  --
  --  AD_CONVERTER
  --

  -- The ADC multiplexer Selection Register
  ADMUX : Unsigned_8;
  for ADMUX'Address	 use System'To_Address (16#27#);

   ADMUX_REFS		: constant := 16#C0#; -- Reference Selection Bits
   ADMUX_ADLAR		: constant := 16#20#; -- Left Adjust Result
   ADMUX_MUX		: constant := 16#0F#; -- Analog Channel and Gain Selection Bits


  --
  --  ADMUX
  --

  -- The ADC Control and Status register
  ADCSRA : Unsigned_8;
  for ADCSRA'Address	 use System'To_Address (16#26#);

   ADCSRA_ADEN		: constant := 16#80#; -- ADC Enable
   ADCSRA_ADSC		: constant := 16#40#; -- ADC Start Conversion
   ADCSRA_ADFR		: constant := 16#20#; -- ADC  Free Running Select
   ADCSRA_ADIF		: constant := 16#10#; -- ADC Interrupt Flag
   ADCSRA_ADIE		: constant := 16#08#; -- ADC Interrupt Enable
   ADCSRA_ADPS		: constant := 16#07#; -- ADC  Prescaler Select Bits


  --
  --  ADCSRA
  --

  -- ADC Data Register  Bytes
  ADC : Unsigned_8;
  for ADC'Address	 use System'To_Address (16#24#);


end AVR.ATmega8;
```