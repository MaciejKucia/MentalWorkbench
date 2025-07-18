```ada
with Interfaces; use Interfaces;
with System;

  -- architecture = AVR8
  -- AVR Studio 5 XML avr register definition generator 
  -- Maciej Kucia, Krakow 2012 

package AVR.ATmega2560 is

  --
  --  ANALOG_COMPARATOR
  --

  -- ADC Control and Status Register B
  ADCSRB : Unsigned_8;
  for ADCSRB'Address	 use System'To_Address (16#7B#);

   ADCSRB_ACME		: constant := 16#40#; -- Analog Comparator Multiplexer Enable


  --
  --  ADCSRB
  --

  -- Analog Comparator Control And Status Register
  ACSR : Unsigned_8;
  for ACSR'Address	 use System'To_Address (16#50#);

   ACSR_ACD		: constant := 16#80#; -- Analog Comparator Disable
   ACSR_ACBG		: constant := 16#40#; -- Analog Comparator Bandgap Select
   ACSR_ACO		: constant := 16#20#; -- Analog Compare Output
   ACSR_ACI		: constant := 16#10#; -- Analog Comparator Interrupt Flag
   ACSR_ACIE		: constant := 16#08#; -- Analog Comparator Interrupt Enable
   ACSR_ACIC		: constant := 16#04#; -- Analog Comparator Input Capture Enable
   ACSR_ACIS		: constant := 16#03#; -- Analog Comparator Interrupt Mode Select bits


  --
  --  ACSR
  --

  -- Digital Input Disable Register 1
  DIDR1 : Unsigned_8;
  for DIDR1'Address	 use System'To_Address (16#7F#);

   DIDR1_AIN1D		: constant := 16#02#; -- AIN1 Digital Input Disable
   DIDR1_AIN0D		: constant := 16#01#; -- AIN0 Digital Input Disable


  --
  --  USART0
  --

  -- USART I/O Data Register
  UDR0 : Unsigned_8;
  for UDR0'Address	 use System'To_Address (16#C6#);



  --
  --  UDR0
  --

  -- USART Control and Status Register A
  UCSR0A : Unsigned_8;
  for UCSR0A'Address	 use System'To_Address (16#C0#);

   UCSR0A_RXC0		: constant := 16#80#; -- USART Receive Complete
   UCSR0A_TXC0		: constant := 16#40#; -- USART Transmitt Complete
   UCSR0A_UDRE0		: constant := 16#20#; -- USART Data Register Empty
   UCSR0A_FE0		: constant := 16#10#; -- Framing Error
   UCSR0A_DOR0		: constant := 16#08#; -- Data overRun
   UCSR0A_UPE0		: constant := 16#04#; -- Parity Error
   UCSR0A_U2X0		: constant := 16#02#; -- Double the USART transmission speed
   UCSR0A_MPCM0		: constant := 16#01#; -- Multi-processor Communication Mode


  --
  --  UCSR0A
  --

  -- USART Control and Status Register B
  UCSR0B : Unsigned_8;
  for UCSR0B'Address	 use System'To_Address (16#C1#);

   UCSR0B_RXCIE0		: constant := 16#80#; -- RX Complete Interrupt Enable
   UCSR0B_TXCIE0		: constant := 16#40#; -- TX Complete Interrupt Enable
   UCSR0B_UDRIE0		: constant := 16#20#; -- USART Data register Empty Interrupt Enable
   UCSR0B_RXEN0		: constant := 16#10#; -- Receiver Enable
   UCSR0B_TXEN0		: constant := 16#08#; -- Transmitter Enable
   UCSR0B_UCSZ02		: constant := 16#04#; -- Character Size
   UCSR0B_RXB80		: constant := 16#02#; -- Receive Data Bit 8
   UCSR0B_TXB80		: constant := 16#01#; -- Transmit Data Bit 8


  --
  --  UCSR0B
  --

  -- USART Control and Status Register C
  UCSR0C : Unsigned_8;
  for UCSR0C'Address	 use System'To_Address (16#C2#);

   UCSR0C_UMSEL0		: constant := 16#C0#; -- USART Mode Select
   UCSR0C_UPM0		: constant := 16#30#; -- Parity Mode Bits
   UCSR0C_USBS0		: constant := 16#08#; -- Stop Bit Select
   UCSR0C_UCSZ0		: constant := 16#06#; -- Character Size
   UCSR0C_UCPOL0		: constant := 16#01#; -- Clock Polarity


  --
  --  UCSR0C
  --

  -- USART Baud Rate Register  Bytes
  UBRR0 : Unsigned_8;
  for UBRR0'Address	 use System'To_Address (16#C4#);



  --
  --  TWI
  --

  -- TWI (Slave) Address Mask Register
  TWAMR : Unsigned_8;
  for TWAMR'Address	 use System'To_Address (16#BD#);

   TWAMR_TWAM		: constant := 16#FE#; -- 


  --
  --  TWAMR
  --

  -- TWI Bit Rate register
  TWBR : Unsigned_8;
  for TWBR'Address	 use System'To_Address (16#B8#);



  --
  --  TWBR
  --

  -- TWI Control Register
  TWCR : Unsigned_8;
  for TWCR'Address	 use System'To_Address (16#BC#);

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
  for TWSR'Address	 use System'To_Address (16#B9#);

   TWSR_TWS		: constant := 16#F8#; -- TWI Status
   TWSR_TWPS		: constant := 16#03#; -- TWI Prescaler


  --
  --  TWSR
  --

  -- TWI Data register
  TWDR : Unsigned_8;
  for TWDR'Address	 use System'To_Address (16#BB#);



  --
  --  TWDR
  --

  -- TWI (Slave) Address register
  TWAR : Unsigned_8;
  for TWAR'Address	 use System'To_Address (16#BA#);

   TWAR_TWA		: constant := 16#FE#; -- TWI (Slave) Address register Bits
   TWAR_TWGCE		: constant := 16#01#; -- TWI General Call Recognition Enable Bit


  --
  --  SPI
  --

  -- SPI Control Register
  SPCR : Unsigned_8;
  for SPCR'Address	 use System'To_Address (16#4C#);

   SPCR_SPIE		: constant := 16#80#; -- SPI Interrupt Enable
   SPCR_SPE		: constant := 16#40#; -- SPI Enable
   SPCR_DORD		: constant := 16#20#; -- Data Order
   SPCR_MSTR		: constant := 16#10#; -- Master/Slave Select
   SPCR_CPOL		: constant := 16#08#; -- Clock polarity
   SPCR_CPHA		: constant := 16#04#; -- Clock Phase
   SPCR_SPR		: constant := 16#03#; -- SPI Clock Rate Selects


  --
  --  SPCR
  --

  -- SPI Status Register
  SPSR : Unsigned_8;
  for SPSR'Address	 use System'To_Address (16#4D#);

   SPSR_SPIF		: constant := 16#80#; -- SPI Interrupt Flag
   SPSR_WCOL		: constant := 16#40#; -- Write Collision Flag
   SPSR_SPI2X		: constant := 16#01#; -- Double SPI Speed Bit


  --
  --  SPSR
  --

  -- SPI Data Register
  SPDR : Unsigned_8;
  for SPDR'Address	 use System'To_Address (16#4E#);



  --
  --  PORTA
  --

  -- Port A Data Register
  PORTA : Unsigned_8;
  for PORTA'Address	 use System'To_Address (16#22#);



  --
  --  PORTA
  --

  -- Port A Data Direction Register
  DDRA : Unsigned_8;
  for DDRA'Address	 use System'To_Address (16#21#);



  --
  --  DDRA
  --

  -- Port A Input Pins
  PINA : Unsigned_8;
  for PINA'Address	 use System'To_Address (16#20#);



  --
  --  PORTB
  --

  -- Port B Data Register
  PORTB : Unsigned_8;
  for PORTB'Address	 use System'To_Address (16#25#);



  --
  --  PORTB
  --

  -- Port B Data Direction Register
  DDRB : Unsigned_8;
  for DDRB'Address	 use System'To_Address (16#24#);



  --
  --  DDRB
  --

  -- Port B Input Pins
  PINB : Unsigned_8;
  for PINB'Address	 use System'To_Address (16#23#);



  --
  --  PORTC
  --

  -- Port C Data Register
  PORTC : Unsigned_8;
  for PORTC'Address	 use System'To_Address (16#28#);



  --
  --  PORTC
  --

  -- Port C Data Direction Register
  DDRC : Unsigned_8;
  for DDRC'Address	 use System'To_Address (16#27#);



  --
  --  DDRC
  --

  -- Port C Input Pins
  PINC : Unsigned_8;
  for PINC'Address	 use System'To_Address (16#26#);



  --
  --  PORTD
  --

  -- Port D Data Register
  PORTD : Unsigned_8;
  for PORTD'Address	 use System'To_Address (16#2B#);



  --
  --  PORTD
  --

  -- Port D Data Direction Register
  DDRD : Unsigned_8;
  for DDRD'Address	 use System'To_Address (16#2A#);



  --
  --  DDRD
  --

  -- Port D Input Pins
  PIND : Unsigned_8;
  for PIND'Address	 use System'To_Address (16#29#);



  --
  --  PORTE
  --

  -- Data Register, Port E
  PORTE : Unsigned_8;
  for PORTE'Address	 use System'To_Address (16#2E#);



  --
  --  PORTE
  --

  -- Data Direction Register, Port E
  DDRE : Unsigned_8;
  for DDRE'Address	 use System'To_Address (16#2D#);



  --
  --  DDRE
  --

  -- Input Pins, Port E
  PINE : Unsigned_8;
  for PINE'Address	 use System'To_Address (16#2C#);



  --
  --  PORTF
  --

  -- Data Register, Port F
  PORTF : Unsigned_8;
  for PORTF'Address	 use System'To_Address (16#31#);



  --
  --  PORTF
  --

  -- Data Direction Register, Port F
  DDRF : Unsigned_8;
  for DDRF'Address	 use System'To_Address (16#30#);



  --
  --  DDRF
  --

  -- Input Pins, Port F
  PINF : Unsigned_8;
  for PINF'Address	 use System'To_Address (16#2F#);



  --
  --  PORTG
  --

  -- Data Register, Port G
  PORTG : Unsigned_8;
  for PORTG'Address	 use System'To_Address (16#34#);



  --
  --  PORTG
  --

  -- Data Direction Register, Port G
  DDRG : Unsigned_8;
  for DDRG'Address	 use System'To_Address (16#33#);



  --
  --  DDRG
  --

  -- Input Pins, Port G
  PING : Unsigned_8;
  for PING'Address	 use System'To_Address (16#32#);



  --
  --  PORTH
  --

  -- PORT H Data Register
  PORTH : Unsigned_8;
  for PORTH'Address	 use System'To_Address (16#02#);



  --
  --  PORTH
  --

  -- PORT H Data Direction Register
  DDRH : Unsigned_8;
  for DDRH'Address	 use System'To_Address (16#01#);



  --
  --  DDRH
  --

  -- PORT H Input Pins
  PINH : Unsigned_8;
  for PINH'Address	 use System'To_Address (16#00#);



  --
  --  PORTJ
  --

  -- PORT J Data Register
  PORTJ : Unsigned_8;
  for PORTJ'Address	 use System'To_Address (16#05#);



  --
  --  PORTJ
  --

  -- PORT J Data Direction Register
  DDRJ : Unsigned_8;
  for DDRJ'Address	 use System'To_Address (16#04#);



  --
  --  DDRJ
  --

  -- PORT J Input Pins
  PINJ : Unsigned_8;
  for PINJ'Address	 use System'To_Address (16#03#);



  --
  --  PORTK
  --

  -- PORT K Data Register
  PORTK : Unsigned_8;
  for PORTK'Address	 use System'To_Address (16#08#);



  --
  --  PORTK
  --

  -- PORT K Data Direction Register
  DDRK : Unsigned_8;
  for DDRK'Address	 use System'To_Address (16#07#);



  --
  --  DDRK
  --

  -- PORT K Input Pins
  PINK : Unsigned_8;
  for PINK'Address	 use System'To_Address (16#06#);



  --
  --  PORTL
  --

  -- PORT L Data Register
  PORTL : Unsigned_8;
  for PORTL'Address	 use System'To_Address (16#0B#);



  --
  --  PORTL
  --

  -- PORT L Data Direction Register
  DDRL : Unsigned_8;
  for DDRL'Address	 use System'To_Address (16#0A#);



  --
  --  DDRL
  --

  -- PORT L Input Pins
  PINL : Unsigned_8;
  for PINL'Address	 use System'To_Address (16#09#);



  --
  --  TIMER_COUNTER_0
  --

  -- Timer/Counter0 Output Compare Register
  OCR0B : Unsigned_8;
  for OCR0B'Address	 use System'To_Address (16#48#);



  --
  --  OCR0B
  --

  -- Timer/Counter0 Output Compare Register
  OCR0A : Unsigned_8;
  for OCR0A'Address	 use System'To_Address (16#47#);



  --
  --  OCR0A
  --

  -- Timer/Counter0
  TCNT0 : Unsigned_8;
  for TCNT0'Address	 use System'To_Address (16#46#);



  --
  --  TCNT0
  --

  -- Timer/Counter Control Register B
  TCCR0B : Unsigned_8;
  for TCCR0B'Address	 use System'To_Address (16#45#);

   TCCR0B_FOC0A		: constant := 16#80#; -- Force Output Compare A
   TCCR0B_FOC0B		: constant := 16#40#; -- Force Output Compare B
   TCCR0B_WGM02		: constant := 16#08#; -- 
   TCCR0B_CS0		: constant := 16#07#; -- Clock Select


  --
  --  TCCR0B
  --

  -- Timer/Counter  Control Register A
  TCCR0A : Unsigned_8;
  for TCCR0A'Address	 use System'To_Address (16#44#);

   TCCR0A_COM0A		: constant := 16#C0#; -- Compare Output Mode, Phase Correct PWM Mode
   TCCR0A_COM0B		: constant := 16#30#; -- Compare Output Mode, Fast PWm
   TCCR0A_WGM0		: constant := 16#03#; -- Waveform Generation Mode


  --
  --  TCCR0A
  --

  -- Timer/Counter0 Interrupt Mask Register
  TIMSK0 : Unsigned_8;
  for TIMSK0'Address	 use System'To_Address (16#6E#);

   TIMSK0_OCIE0B		: constant := 16#04#; -- Timer/Counter0 Output Compare Match B Interrupt Enable
   TIMSK0_OCIE0A		: constant := 16#02#; -- Timer/Counter0 Output Compare Match A Interrupt Enable
   TIMSK0_TOIE0		: constant := 16#01#; -- Timer/Counter0 Overflow Interrupt Enable


  --
  --  TIMSK0
  --

  -- Timer/Counter0 Interrupt Flag register
  TIFR0 : Unsigned_8;
  for TIFR0'Address	 use System'To_Address (16#35#);

   TIFR0_OCF0B		: constant := 16#04#; -- Timer/Counter0 Output Compare Flag 0B
   TIFR0_OCF0A		: constant := 16#02#; -- Timer/Counter0 Output Compare Flag 0A
   TIFR0_TOV0		: constant := 16#01#; -- Timer/Counter0 Overflow Flag


  --
  --  TIFR0
  --

  -- General Timer/Counter Control Register
  GTCCR : Unsigned_8;
  for GTCCR'Address	 use System'To_Address (16#43#);

   GTCCR_TSM		: constant := 16#80#; -- Timer/Counter Synchronization Mode
   GTCCR_PSRSYNC		: constant := 16#01#; -- Prescaler Reset Timer/Counter1 and Timer/Counter0


  --
  --  TIMER_COUNTER_2
  --

  -- Timer/Counter Interrupt Mask register
  TIMSK2 : Unsigned_8;
  for TIMSK2'Address	 use System'To_Address (16#70#);

   TIMSK2_OCIE2B		: constant := 16#04#; -- Timer/Counter2 Output Compare Match B Interrupt Enable
   TIMSK2_OCIE2A		: constant := 16#02#; -- Timer/Counter2 Output Compare Match A Interrupt Enable
   TIMSK2_TOIE2		: constant := 16#01#; -- Timer/Counter2 Overflow Interrupt Enable


  --
  --  TIMSK2
  --

  -- Timer/Counter Interrupt Flag Register
  TIFR2 : Unsigned_8;
  for TIFR2'Address	 use System'To_Address (16#37#);

   TIFR2_OCF2B		: constant := 16#04#; -- Output Compare Flag 2B
   TIFR2_OCF2A		: constant := 16#02#; -- Output Compare Flag 2A
   TIFR2_TOV2		: constant := 16#01#; -- Timer/Counter2 Overflow Flag


  --
  --  TIFR2
  --

  -- Timer/Counter2 Control Register A
  TCCR2A : Unsigned_8;
  for TCCR2A'Address	 use System'To_Address (16#B0#);

   TCCR2A_COM2A		: constant := 16#C0#; -- Compare Output Mode bits
   TCCR2A_COM2B		: constant := 16#30#; -- Compare Output Mode bits
   TCCR2A_WGM2		: constant := 16#03#; -- Waveform Genration Mode


  --
  --  TCCR2A
  --

  -- Timer/Counter2 Control Register B
  TCCR2B : Unsigned_8;
  for TCCR2B'Address	 use System'To_Address (16#B1#);

   TCCR2B_FOC2A		: constant := 16#80#; -- Force Output Compare A
   TCCR2B_FOC2B		: constant := 16#40#; -- Force Output Compare B
   TCCR2B_WGM22		: constant := 16#08#; -- Waveform Generation Mode
   TCCR2B_CS2		: constant := 16#07#; -- Clock Select bits


  --
  --  TCCR2B
  --

  -- Timer/Counter2
  TCNT2 : Unsigned_8;
  for TCNT2'Address	 use System'To_Address (16#B2#);



  --
  --  TCNT2
  --

  -- Timer/Counter2 Output Compare Register B
  OCR2B : Unsigned_8;
  for OCR2B'Address	 use System'To_Address (16#B4#);



  --
  --  OCR2B
  --

  -- Timer/Counter2 Output Compare Register A
  OCR2A : Unsigned_8;
  for OCR2A'Address	 use System'To_Address (16#B3#);



  --
  --  OCR2A
  --

  -- Asynchronous Status Register
  ASSR : Unsigned_8;
  for ASSR'Address	 use System'To_Address (16#B6#);

   ASSR_EXCLK		: constant := 16#40#; -- Enable External Clock Input
   ASSR_AS2		: constant := 16#20#; -- Asynchronous Timer/Counter2
   ASSR_TCN2UB		: constant := 16#10#; -- Timer/Counter2 Update Busy
   ASSR_OCR2AUB		: constant := 16#08#; -- Output Compare Register2 Update Busy
   ASSR_OCR2BUB		: constant := 16#04#; -- Output Compare Register 2 Update Busy
   ASSR_TCR2AUB		: constant := 16#02#; -- Timer/Counter Control Register2 Update Busy
   ASSR_TCR2BUB		: constant := 16#01#; -- Timer/Counter Control Register2 Update Busy


  --
  --  ASSR
  --

  -- General Timer Counter Control register
  GTCCR : Unsigned_8;
  for GTCCR'Address	 use System'To_Address (16#43#);

   GTCCR_TSM		: constant := 16#80#; -- Timer/Counter Synchronization Mode
   GTCCR_PSRASY		: constant := 16#02#; -- Prescaler Reset Timer/Counter2


  --
  --  WATCHDOG
  --

  -- Watchdog Timer Control Register
  WDTCSR : Unsigned_8;
  for WDTCSR'Address	 use System'To_Address (16#60#);

   WDTCSR_WDIF		: constant := 16#80#; -- Watchdog Timeout Interrupt Flag
   WDTCSR_WDIE		: constant := 16#40#; -- Watchdog Timeout Interrupt Enable
   WDTCSR_WDP		: constant := 16#27#; -- Watchdog Timer Prescaler Bits
   WDTCSR_WDCE		: constant := 16#10#; -- Watchdog Change Enable
   WDTCSR_WDE		: constant := 16#08#; -- Watch Dog Enable


  --
  --  USART1
  --

  -- USART I/O Data Register
  UDR1 : Unsigned_8;
  for UDR1'Address	 use System'To_Address (16#CE#);



  --
  --  UDR1
  --

  -- USART Control and Status Register A
  UCSR1A : Unsigned_8;
  for UCSR1A'Address	 use System'To_Address (16#C8#);

   UCSR1A_RXC1		: constant := 16#80#; -- USART Receive Complete
   UCSR1A_TXC1		: constant := 16#40#; -- USART Transmitt Complete
   UCSR1A_UDRE1		: constant := 16#20#; -- USART Data Register Empty
   UCSR1A_FE1		: constant := 16#10#; -- Framing Error
   UCSR1A_DOR1		: constant := 16#08#; -- Data overRun
   UCSR1A_UPE1		: constant := 16#04#; -- Parity Error
   UCSR1A_U2X1		: constant := 16#02#; -- Double the USART transmission speed
   UCSR1A_MPCM1		: constant := 16#01#; -- Multi-processor Communication Mode


  --
  --  UCSR1A
  --

  -- USART Control and Status Register B
  UCSR1B : Unsigned_8;
  for UCSR1B'Address	 use System'To_Address (16#C9#);

   UCSR1B_RXCIE1		: constant := 16#80#; -- RX Complete Interrupt Enable
   UCSR1B_TXCIE1		: constant := 16#40#; -- TX Complete Interrupt Enable
   UCSR1B_UDRIE1		: constant := 16#20#; -- USART Data register Empty Interrupt Enable
   UCSR1B_RXEN1		: constant := 16#10#; -- Receiver Enable
   UCSR1B_TXEN1		: constant := 16#08#; -- Transmitter Enable
   UCSR1B_UCSZ12		: constant := 16#04#; -- Character Size
   UCSR1B_RXB81		: constant := 16#02#; -- Receive Data Bit 8
   UCSR1B_TXB81		: constant := 16#01#; -- Transmit Data Bit 8


  --
  --  UCSR1B
  --

  -- USART Control and Status Register C
  UCSR1C : Unsigned_8;
  for UCSR1C'Address	 use System'To_Address (16#CA#);

   UCSR1C_UMSEL1		: constant := 16#C0#; -- USART Mode Select
   UCSR1C_UPM1		: constant := 16#30#; -- Parity Mode Bits
   UCSR1C_USBS1		: constant := 16#08#; -- Stop Bit Select
   UCSR1C_UCSZ1		: constant := 16#06#; -- Character Size
   UCSR1C_UCPOL1		: constant := 16#01#; -- Clock Polarity


  --
  --  UCSR1C
  --

  -- USART Baud Rate Register  Bytes
  UBRR1 : Unsigned_8;
  for UBRR1'Address	 use System'To_Address (16#CC#);



  --
  --  EEPROM
  --

  -- EEPROM Address Register Low Bytes
  EEAR : Unsigned_8;
  for EEAR'Address	 use System'To_Address (16#41#);



  --
  --  EEAR
  --

  -- EEPROM Data Register
  EEDR : Unsigned_8;
  for EEDR'Address	 use System'To_Address (16#40#);



  --
  --  EEDR
  --

  -- EEPROM Control Register
  EECR : Unsigned_8;
  for EECR'Address	 use System'To_Address (16#3F#);

   EECR_EEPM		: constant := 16#30#; -- EEPROM Programming Mode Bits
   EECR_EERIE		: constant := 16#08#; -- EEPROM Ready Interrupt Enable
   EECR_EEMPE		: constant := 16#04#; -- EEPROM Master Write Enable
   EECR_EEPE		: constant := 16#02#; -- EEPROM Write Enable
   EECR_EERE		: constant := 16#01#; -- EEPROM Read Enable


  --
  --  TIMER_COUNTER_5
  --

  -- Timer/Counter5 Control Register A
  TCCR5A : Unsigned_8;
  for TCCR5A'Address	 use System'To_Address (16#20#);

   TCCR5A_COM5A		: constant := 16#C0#; -- Compare Output Mode 1A, bits
   TCCR5A_COM5B		: constant := 16#30#; -- Compare Output Mode 5B, bits
   TCCR5A_COM5C		: constant := 16#0C#; -- Compare Output Mode 5C, bits
   TCCR5A_WGM5		: constant := 16#03#; -- Waveform Generation Mode


  --
  --  TCCR5A
  --

  -- Timer/Counter5 Control Register B
  TCCR5B : Unsigned_8;
  for TCCR5B'Address	 use System'To_Address (16#21#);

   TCCR5B_ICNC5		: constant := 16#80#; -- Input Capture 5 Noise Canceler
   TCCR5B_ICES5		: constant := 16#40#; -- Input Capture 5 Edge Select
   TCCR5B_WGM5		: constant := 16#18#; -- Waveform Generation Mode
   TCCR5B_CS5		: constant := 16#07#; -- Prescaler source of Timer/Counter 5


  --
  --  TCCR5B
  --

  -- Timer/Counter 5 Control Register C
  TCCR5C : Unsigned_8;
  for TCCR5C'Address	 use System'To_Address (16#22#);

   TCCR5C_FOC5A		: constant := 16#80#; -- Force Output Compare 5A
   TCCR5C_FOC5B		: constant := 16#40#; -- Force Output Compare 5B
   TCCR5C_FOC5C		: constant := 16#20#; -- Force Output Compare 5C


  --
  --  TCCR5C
  --

  -- Timer/Counter5  Bytes
  TCNT5 : Unsigned_8;
  for TCNT5'Address	 use System'To_Address (16#24#);



  --
  --  TCNT5
  --

  -- Timer/Counter5 Output Compare Register A  Bytes
  OCR5A : Unsigned_8;
  for OCR5A'Address	 use System'To_Address (16#28#);



  --
  --  OCR5A
  --

  -- Timer/Counter5 Output Compare Register B  Bytes
  OCR5B : Unsigned_8;
  for OCR5B'Address	 use System'To_Address (16#2A#);



  --
  --  OCR5B
  --

  -- Timer/Counter5 Output Compare Register B  Bytes
  OCR5C : Unsigned_8;
  for OCR5C'Address	 use System'To_Address (16#2C#);



  --
  --  OCR5C
  --

  -- Timer/Counter5 Input Capture Register  Bytes
  ICR5 : Unsigned_8;
  for ICR5'Address	 use System'To_Address (16#26#);



  --
  --  ICR5
  --

  -- Timer/Counter5 Interrupt Mask Register
  TIMSK5 : Unsigned_8;
  for TIMSK5'Address	 use System'To_Address (16#73#);

   TIMSK5_ICIE5		: constant := 16#20#; -- Timer/Counter5 Input Capture Interrupt Enable
   TIMSK5_OCIE5C		: constant := 16#08#; -- Timer/Counter5 Output Compare C Match Interrupt Enable
   TIMSK5_OCIE5B		: constant := 16#04#; -- Timer/Counter5 Output Compare B Match Interrupt Enable
   TIMSK5_OCIE5A		: constant := 16#02#; -- Timer/Counter5 Output Compare A Match Interrupt Enable
   TIMSK5_TOIE5		: constant := 16#01#; -- Timer/Counter5 Overflow Interrupt Enable


  --
  --  TIMSK5
  --

  -- Timer/Counter5 Interrupt Flag register
  TIFR5 : Unsigned_8;
  for TIFR5'Address	 use System'To_Address (16#3A#);

   TIFR5_ICF5		: constant := 16#20#; -- Input Capture Flag 5
   TIFR5_OCF5C		: constant := 16#08#; -- Output Compare Flag 5C
   TIFR5_OCF5B		: constant := 16#04#; -- Output Compare Flag 5B
   TIFR5_OCF5A		: constant := 16#02#; -- Output Compare Flag 5A
   TIFR5_TOV5		: constant := 16#01#; -- Timer/Counter5 Overflow Flag


  --
  --  TIMER_COUNTER_4
  --

  -- Timer/Counter4 Control Register A
  TCCR4A : Unsigned_8;
  for TCCR4A'Address	 use System'To_Address (16#A0#);

   TCCR4A_COM4A		: constant := 16#C0#; -- Compare Output Mode 1A, bits
   TCCR4A_COM4B		: constant := 16#30#; -- Compare Output Mode 4B, bits
   TCCR4A_COM4C		: constant := 16#0C#; -- Compare Output Mode 4C, bits
   TCCR4A_WGM4		: constant := 16#03#; -- Waveform Generation Mode


  --
  --  TCCR4A
  --

  -- Timer/Counter4 Control Register B
  TCCR4B : Unsigned_8;
  for TCCR4B'Address	 use System'To_Address (16#A1#);

   TCCR4B_ICNC4		: constant := 16#80#; -- Input Capture 4 Noise Canceler
   TCCR4B_ICES4		: constant := 16#40#; -- Input Capture 4 Edge Select
   TCCR4B_WGM4		: constant := 16#18#; -- Waveform Generation Mode
   TCCR4B_CS4		: constant := 16#07#; -- Prescaler source of Timer/Counter 4


  --
  --  TCCR4B
  --

  -- Timer/Counter 4 Control Register C
  TCCR4C : Unsigned_8;
  for TCCR4C'Address	 use System'To_Address (16#A2#);

   TCCR4C_FOC4A		: constant := 16#80#; -- Force Output Compare 4A
   TCCR4C_FOC4B		: constant := 16#40#; -- Force Output Compare 4B
   TCCR4C_FOC4C		: constant := 16#20#; -- Force Output Compare 4C


  --
  --  TCCR4C
  --

  -- Timer/Counter4  Bytes
  TCNT4 : Unsigned_8;
  for TCNT4'Address	 use System'To_Address (16#A4#);



  --
  --  TCNT4
  --

  -- Timer/Counter4 Output Compare Register A  Bytes
  OCR4A : Unsigned_8;
  for OCR4A'Address	 use System'To_Address (16#A8#);



  --
  --  OCR4A
  --

  -- Timer/Counter4 Output Compare Register B  Bytes
  OCR4B : Unsigned_8;
  for OCR4B'Address	 use System'To_Address (16#AA#);



  --
  --  OCR4B
  --

  -- Timer/Counter4 Output Compare Register B  Bytes
  OCR4C : Unsigned_8;
  for OCR4C'Address	 use System'To_Address (16#AC#);



  --
  --  OCR4C
  --

  -- Timer/Counter4 Input Capture Register  Bytes
  ICR4 : Unsigned_8;
  for ICR4'Address	 use System'To_Address (16#A6#);



  --
  --  ICR4
  --

  -- Timer/Counter4 Interrupt Mask Register
  TIMSK4 : Unsigned_8;
  for TIMSK4'Address	 use System'To_Address (16#72#);

   TIMSK4_ICIE4		: constant := 16#20#; -- Timer/Counter4 Input Capture Interrupt Enable
   TIMSK4_OCIE4C		: constant := 16#08#; -- Timer/Counter4 Output Compare C Match Interrupt Enable
   TIMSK4_OCIE4B		: constant := 16#04#; -- Timer/Counter4 Output Compare B Match Interrupt Enable
   TIMSK4_OCIE4A		: constant := 16#02#; -- Timer/Counter4 Output Compare A Match Interrupt Enable
   TIMSK4_TOIE4		: constant := 16#01#; -- Timer/Counter4 Overflow Interrupt Enable


  --
  --  TIMSK4
  --

  -- Timer/Counter4 Interrupt Flag register
  TIFR4 : Unsigned_8;
  for TIFR4'Address	 use System'To_Address (16#39#);

   TIFR4_ICF4		: constant := 16#20#; -- Input Capture Flag 4
   TIFR4_OCF4C		: constant := 16#08#; -- Output Compare Flag 4C
   TIFR4_OCF4B		: constant := 16#04#; -- Output Compare Flag 4B
   TIFR4_OCF4A		: constant := 16#02#; -- Output Compare Flag 4A
   TIFR4_TOV4		: constant := 16#01#; -- Timer/Counter4 Overflow Flag


  --
  --  TIMER_COUNTER_3
  --

  -- Timer/Counter3 Control Register A
  TCCR3A : Unsigned_8;
  for TCCR3A'Address	 use System'To_Address (16#90#);

   TCCR3A_COM3A		: constant := 16#C0#; -- Compare Output Mode 1A, bits
   TCCR3A_COM3B		: constant := 16#30#; -- Compare Output Mode 3B, bits
   TCCR3A_COM3C		: constant := 16#0C#; -- Compare Output Mode 3C, bits
   TCCR3A_WGM3		: constant := 16#03#; -- Waveform Generation Mode


  --
  --  TCCR3A
  --

  -- Timer/Counter3 Control Register B
  TCCR3B : Unsigned_8;
  for TCCR3B'Address	 use System'To_Address (16#91#);

   TCCR3B_ICNC3		: constant := 16#80#; -- Input Capture 3 Noise Canceler
   TCCR3B_ICES3		: constant := 16#40#; -- Input Capture 3 Edge Select
   TCCR3B_WGM3		: constant := 16#18#; -- Waveform Generation Mode
   TCCR3B_CS3		: constant := 16#07#; -- Prescaler source of Timer/Counter 3


  --
  --  TCCR3B
  --

  -- Timer/Counter 3 Control Register C
  TCCR3C : Unsigned_8;
  for TCCR3C'Address	 use System'To_Address (16#92#);

   TCCR3C_FOC3A		: constant := 16#80#; -- Force Output Compare 3A
   TCCR3C_FOC3B		: constant := 16#40#; -- Force Output Compare 3B
   TCCR3C_FOC3C		: constant := 16#20#; -- Force Output Compare 3C


  --
  --  TCCR3C
  --

  -- Timer/Counter3  Bytes
  TCNT3 : Unsigned_8;
  for TCNT3'Address	 use System'To_Address (16#94#);



  --
  --  TCNT3
  --

  -- Timer/Counter3 Output Compare Register A  Bytes
  OCR3A : Unsigned_8;
  for OCR3A'Address	 use System'To_Address (16#98#);



  --
  --  OCR3A
  --

  -- Timer/Counter3 Output Compare Register B  Bytes
  OCR3B : Unsigned_8;
  for OCR3B'Address	 use System'To_Address (16#9A#);



  --
  --  OCR3B
  --

  -- Timer/Counter3 Output Compare Register B  Bytes
  OCR3C : Unsigned_8;
  for OCR3C'Address	 use System'To_Address (16#9C#);



  --
  --  OCR3C
  --

  -- Timer/Counter3 Input Capture Register  Bytes
  ICR3 : Unsigned_8;
  for ICR3'Address	 use System'To_Address (16#96#);



  --
  --  ICR3
  --

  -- Timer/Counter3 Interrupt Mask Register
  TIMSK3 : Unsigned_8;
  for TIMSK3'Address	 use System'To_Address (16#71#);

   TIMSK3_ICIE3		: constant := 16#20#; -- Timer/Counter3 Input Capture Interrupt Enable
   TIMSK3_OCIE3C		: constant := 16#08#; -- Timer/Counter3 Output Compare C Match Interrupt Enable
   TIMSK3_OCIE3B		: constant := 16#04#; -- Timer/Counter3 Output Compare B Match Interrupt Enable
   TIMSK3_OCIE3A		: constant := 16#02#; -- Timer/Counter3 Output Compare A Match Interrupt Enable
   TIMSK3_TOIE3		: constant := 16#01#; -- Timer/Counter3 Overflow Interrupt Enable


  --
  --  TIMSK3
  --

  -- Timer/Counter3 Interrupt Flag register
  TIFR3 : Unsigned_8;
  for TIFR3'Address	 use System'To_Address (16#38#);

   TIFR3_ICF3		: constant := 16#20#; -- Input Capture Flag 3
   TIFR3_OCF3C		: constant := 16#08#; -- Output Compare Flag 3C
   TIFR3_OCF3B		: constant := 16#04#; -- Output Compare Flag 3B
   TIFR3_OCF3A		: constant := 16#02#; -- Output Compare Flag 3A
   TIFR3_TOV3		: constant := 16#01#; -- Timer/Counter3 Overflow Flag


  --
  --  TIMER_COUNTER_1
  --

  -- Timer/Counter1 Control Register A
  TCCR1A : Unsigned_8;
  for TCCR1A'Address	 use System'To_Address (16#80#);

   TCCR1A_COM1A		: constant := 16#C0#; -- Compare Output Mode 1A, bits
   TCCR1A_COM1B		: constant := 16#30#; -- Compare Output Mode 1B, bits
   TCCR1A_COM1C		: constant := 16#0C#; -- Compare Output Mode 1C, bits
   TCCR1A_WGM1		: constant := 16#03#; -- Waveform Generation Mode


  --
  --  TCCR1A
  --

  -- Timer/Counter1 Control Register B
  TCCR1B : Unsigned_8;
  for TCCR1B'Address	 use System'To_Address (16#81#);

   TCCR1B_ICNC1		: constant := 16#80#; -- Input Capture 1 Noise Canceler
   TCCR1B_ICES1		: constant := 16#40#; -- Input Capture 1 Edge Select
   TCCR1B_WGM1		: constant := 16#18#; -- Waveform Generation Mode
   TCCR1B_CS1		: constant := 16#07#; -- Prescaler source of Timer/Counter 1


  --
  --  TCCR1B
  --

  -- Timer/Counter 1 Control Register C
  TCCR1C : Unsigned_8;
  for TCCR1C'Address	 use System'To_Address (16#82#);

   TCCR1C_FOC1A		: constant := 16#80#; -- Force Output Compare 1A
   TCCR1C_FOC1B		: constant := 16#40#; -- Force Output Compare 1B
   TCCR1C_FOC1C		: constant := 16#20#; -- Force Output Compare 1C


  --
  --  TCCR1C
  --

  -- Timer/Counter1  Bytes
  TCNT1 : Unsigned_8;
  for TCNT1'Address	 use System'To_Address (16#84#);



  --
  --  TCNT1
  --

  -- Timer/Counter1 Output Compare Register A  Bytes
  OCR1A : Unsigned_8;
  for OCR1A'Address	 use System'To_Address (16#88#);



  --
  --  OCR1A
  --

  -- Timer/Counter1 Output Compare Register B  Bytes
  OCR1B : Unsigned_8;
  for OCR1B'Address	 use System'To_Address (16#8A#);



  --
  --  OCR1B
  --

  -- Timer/Counter1 Output Compare Register C  Bytes
  OCR1C : Unsigned_8;
  for OCR1C'Address	 use System'To_Address (16#8C#);



  --
  --  OCR1C
  --

  -- Timer/Counter1 Input Capture Register  Bytes
  ICR1 : Unsigned_8;
  for ICR1'Address	 use System'To_Address (16#86#);



  --
  --  ICR1
  --

  -- Timer/Counter1 Interrupt Mask Register
  TIMSK1 : Unsigned_8;
  for TIMSK1'Address	 use System'To_Address (16#6F#);

   TIMSK1_ICIE1		: constant := 16#20#; -- Timer/Counter1 Input Capture Interrupt Enable
   TIMSK1_OCIE1C		: constant := 16#08#; -- Timer/Counter1 Output Compare C Match Interrupt Enable
   TIMSK1_OCIE1B		: constant := 16#04#; -- Timer/Counter1 Output Compare B Match Interrupt Enable
   TIMSK1_OCIE1A		: constant := 16#02#; -- Timer/Counter1 Output Compare A Match Interrupt Enable
   TIMSK1_TOIE1		: constant := 16#01#; -- Timer/Counter1 Overflow Interrupt Enable


  --
  --  TIMSK1
  --

  -- Timer/Counter1 Interrupt Flag register
  TIFR1 : Unsigned_8;
  for TIFR1'Address	 use System'To_Address (16#36#);

   TIFR1_ICF1		: constant := 16#20#; -- Input Capture Flag 1
   TIFR1_OCF1C		: constant := 16#08#; -- Output Compare Flag 1C
   TIFR1_OCF1B		: constant := 16#04#; -- Output Compare Flag 1B
   TIFR1_OCF1A		: constant := 16#02#; -- Output Compare Flag 1A
   TIFR1_TOV1		: constant := 16#01#; -- Timer/Counter1 Overflow Flag


  --
  --  JTAG
  --

  -- On-Chip Debug Related Register in I/O Memory
  OCDR : Unsigned_8;
  for OCDR'Address	 use System'To_Address (16#51#);



  --
  --  OCDR
  --

  -- MCU Control Register
  MCUCR : Unsigned_8;
  for MCUCR'Address	 use System'To_Address (16#55#);

   MCUCR_JTD		: constant := 16#80#; -- JTAG Interface Disable


  --
  --  MCUCR
  --

  -- MCU Status Register
  MCUSR : Unsigned_8;
  for MCUSR'Address	 use System'To_Address (16#54#);

   MCUSR_JTRF		: constant := 16#10#; -- JTAG Reset Flag


  --
  --  EXTERNAL_INTERRUPT
  --

  -- External Interrupt Control Register A
  EICRA : Unsigned_8;
  for EICRA'Address	 use System'To_Address (16#69#);

   EICRA_ISC3		: constant := 16#C0#; -- External Interrupt Sense Control Bit
   EICRA_ISC2		: constant := 16#30#; -- External Interrupt Sense Control Bit
   EICRA_ISC1		: constant := 16#0C#; -- External Interrupt Sense Control Bit
   EICRA_ISC0		: constant := 16#03#; -- External Interrupt Sense Control Bit


  --
  --  EICRA
  --

  -- External Interrupt Control Register B
  EICRB : Unsigned_8;
  for EICRB'Address	 use System'To_Address (16#6A#);

   EICRB_ISC7		: constant := 16#C0#; -- External Interrupt 7-4 Sense Control Bit
   EICRB_ISC6		: constant := 16#30#; -- External Interrupt 7-4 Sense Control Bit
   EICRB_ISC5		: constant := 16#0C#; -- External Interrupt 7-4 Sense Control Bit
   EICRB_ISC4		: constant := 16#03#; -- External Interrupt 7-4 Sense Control Bit


  --
  --  EICRB
  --

  -- External Interrupt Mask Register
  EIMSK : Unsigned_8;
  for EIMSK'Address	 use System'To_Address (16#3D#);

   EIMSK_INT		: constant := 16#FF#; -- External Interrupt Request 7 Enable


  --
  --  EIMSK
  --

  -- External Interrupt Flag Register
  EIFR : Unsigned_8;
  for EIFR'Address	 use System'To_Address (16#3C#);

   EIFR_INTF		: constant := 16#FF#; -- External Interrupt Flags


  --
  --  EIFR
  --

  -- Pin Change Mask Register 2
  PCMSK2 : Unsigned_8;
  for PCMSK2'Address	 use System'To_Address (16#6D#);



  --
  --  PCMSK2
  --

  -- Pin Change Mask Register 1
  PCMSK1 : Unsigned_8;
  for PCMSK1'Address	 use System'To_Address (16#6C#);



  --
  --  PCMSK1
  --

  -- Pin Change Mask Register 0
  PCMSK0 : Unsigned_8;
  for PCMSK0'Address	 use System'To_Address (16#6B#);



  --
  --  PCMSK0
  --

  -- Pin Change Interrupt Flag Register
  PCIFR : Unsigned_8;
  for PCIFR'Address	 use System'To_Address (16#3B#);

   PCIFR_PCIF		: constant := 16#07#; -- Pin Change Interrupt Flags


  --
  --  PCIFR
  --

  -- Pin Change Interrupt Control Register
  PCICR : Unsigned_8;
  for PCICR'Address	 use System'To_Address (16#68#);

   PCICR_PCIE		: constant := 16#07#; -- Pin Change Interrupt Enables


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

   MCUCR_JTD		: constant := 16#80#; -- JTAG Interface Disable
   MCUCR_PUD		: constant := 16#10#; -- Pull-up disable
   MCUCR_IVSEL		: constant := 16#02#; -- Interrupt Vector Select
   MCUCR_IVCE		: constant := 16#01#; -- Interrupt Vector Change Enable


  --
  --  MCUCR
  --

  -- MCU Status Register
  MCUSR : Unsigned_8;
  for MCUSR'Address	 use System'To_Address (16#54#);

   MCUSR_JTRF		: constant := 16#10#; -- JTAG Reset Flag
   MCUSR_WDRF		: constant := 16#08#; -- Watchdog Reset Flag
   MCUSR_BORF		: constant := 16#04#; -- Brown-out Reset Flag
   MCUSR_EXTRF		: constant := 16#02#; -- External Reset Flag
   MCUSR_PORF		: constant := 16#01#; -- Power-on reset flag


  --
  --  MCUSR
  --

  -- External Memory Control Register A
  XMCRA : Unsigned_8;
  for XMCRA'Address	 use System'To_Address (16#74#);

   XMCRA_SRE		: constant := 16#80#; -- External SRAM Enable
   XMCRA_SRL		: constant := 16#70#; -- Wait state page limit
   XMCRA_SRW1		: constant := 16#0C#; -- Wait state select bit upper page
   XMCRA_SRW0		: constant := 16#03#; -- Wait state select bit lower page


  --
  --  XMCRA
  --

  -- External Memory Control Register B
  XMCRB : Unsigned_8;
  for XMCRB'Address	 use System'To_Address (16#75#);

   XMCRB_XMBK		: constant := 16#80#; -- External Memory Bus Keeper Enable
   XMCRB_XMM		: constant := 16#07#; -- External Memory High Mask


  --
  --  XMCRB
  --

  -- Oscillator Calibration Value
  OSCCAL : Unsigned_8;
  for OSCCAL'Address	 use System'To_Address (16#66#);



  --
  --  OSCCAL
  --

  -- Sleep Mode Control Register
  SMCR : Unsigned_8;
  for SMCR'Address	 use System'To_Address (16#53#);

   SMCR_SM		: constant := 16#0E#; -- Sleep Mode Select bits
   SMCR_SE		: constant := 16#01#; -- Sleep Enable


  --
  --  SMCR
  --

  -- Extended Indirect Register
  EIND : Unsigned_8;
  for EIND'Address	 use System'To_Address (16#5C#);



  --
  --  EIND
  --

  -- RAM Page Z Select Register
  RAMPZ : Unsigned_8;
  for RAMPZ'Address	 use System'To_Address (16#5B#);



  --
  --  RAMPZ
  --

  -- General Purpose IO Register 2
  GPIOR2 : Unsigned_8;
  for GPIOR2'Address	 use System'To_Address (16#4B#);

   GPIOR2_GPIOR		: constant := 16#FF#; -- General Purpose IO Register 2 bis


  --
  --  GPIOR2
  --

  -- General Purpose IO Register 1
  GPIOR1 : Unsigned_8;
  for GPIOR1'Address	 use System'To_Address (16#4A#);

   GPIOR1_GPIOR		: constant := 16#FF#; -- General Purpose IO Register 1 bis


  --
  --  GPIOR1
  --

  -- General Purpose IO Register 0
  GPIOR0 : Unsigned_8;
  for GPIOR0'Address	 use System'To_Address (16#3E#);

   GPIOR0_GPIOR07		: constant := 16#80#; -- General Purpose IO Register 0 bit 7
   GPIOR0_GPIOR06		: constant := 16#40#; -- General Purpose IO Register 0 bit 6
   GPIOR0_GPIOR05		: constant := 16#20#; -- General Purpose IO Register 0 bit 5
   GPIOR0_GPIOR04		: constant := 16#10#; -- General Purpose IO Register 0 bit 4
   GPIOR0_GPIOR03		: constant := 16#08#; -- General Purpose IO Register 0 bit 3
   GPIOR0_GPIOR02		: constant := 16#04#; -- General Purpose IO Register 0 bit 2
   GPIOR0_GPIOR01		: constant := 16#02#; -- General Purpose IO Register 0 bit 1
   GPIOR0_GPIOR00		: constant := 16#01#; -- General Purpose IO Register 0 bit 0


  --
  --  GPIOR0
  --

  -- Power Reduction Register1
  PRR1 : Unsigned_8;
  for PRR1'Address	 use System'To_Address (16#65#);

   PRR1_PRTIM5		: constant := 16#20#; -- Power Reduction Timer/Counter5
   PRR1_PRTIM4		: constant := 16#10#; -- Power Reduction Timer/Counter4
   PRR1_PRTIM3		: constant := 16#08#; -- Power Reduction Timer/Counter3
   PRR1_PRUSART		: constant := 16#07#; -- Power Reduction USART3


  --
  --  PRR1
  --

  -- Power Reduction Register0
  PRR0 : Unsigned_8;
  for PRR0'Address	 use System'To_Address (16#64#);

   PRR0_PRTWI		: constant := 16#80#; -- Power Reduction TWI
   PRR0_PRTIM2		: constant := 16#40#; -- Power Reduction Timer/Counter2
   PRR0_PRTIM0		: constant := 16#20#; -- Power Reduction Timer/Counter0
   PRR0_PRTIM1		: constant := 16#08#; -- Power Reduction Timer/Counter1
   PRR0_PRSPI		: constant := 16#04#; -- Power Reduction Serial Peripheral Interface
   PRR0_PRUSART0		: constant := 16#02#; -- Power Reduction USART
   PRR0_PRADC		: constant := 16#01#; -- Power Reduction ADC


  --
  --  AD_CONVERTER
  --

  -- The ADC multiplexer Selection Register
  ADMUX : Unsigned_8;
  for ADMUX'Address	 use System'To_Address (16#7C#);

   ADMUX_REFS		: constant := 16#C0#; -- Reference Selection Bits
   ADMUX_ADLAR		: constant := 16#20#; -- Left Adjust Result
   ADMUX_MUX		: constant := 16#1F#; -- Analog Channel and Gain Selection Bits


  --
  --  ADMUX
  --

  -- ADC Data Register  Bytes
  ADC : Unsigned_8;
  for ADC'Address	 use System'To_Address (16#78#);



  --
  --  ADC
  --

  -- The ADC Control and Status register A
  ADCSRA : Unsigned_8;
  for ADCSRA'Address	 use System'To_Address (16#7A#);

   ADCSRA_ADEN		: constant := 16#80#; -- ADC Enable
   ADCSRA_ADSC		: constant := 16#40#; -- ADC Start Conversion
   ADCSRA_ADATE		: constant := 16#20#; -- ADC  Auto Trigger Enable
   ADCSRA_ADIF		: constant := 16#10#; -- ADC Interrupt Flag
   ADCSRA_ADIE		: constant := 16#08#; -- ADC Interrupt Enable
   ADCSRA_ADPS		: constant := 16#07#; -- ADC  Prescaler Select Bits


  --
  --  ADCSRA
  --

  -- The ADC Control and Status register B
  ADCSRB : Unsigned_8;
  for ADCSRB'Address	 use System'To_Address (16#7B#);

   ADCSRB_ACME		: constant := 16#40#; -- 
   ADCSRB_MUX5		: constant := 16#08#; -- Analog Channel and Gain Selection Bits
   ADCSRB_ADTS		: constant := 16#07#; -- ADC Auto Trigger Source bits


  --
  --  ADCSRB
  --

  -- Digital Input Disable Register
  DIDR2 : Unsigned_8;
  for DIDR2'Address	 use System'To_Address (16#7D#);

   DIDR2_ADC15D		: constant := 16#80#; -- 
   DIDR2_ADC14D		: constant := 16#40#; -- 
   DIDR2_ADC13D		: constant := 16#20#; -- 
   DIDR2_ADC12D		: constant := 16#10#; -- 
   DIDR2_ADC11D		: constant := 16#08#; -- 
   DIDR2_ADC10D		: constant := 16#04#; -- 
   DIDR2_ADC9D		: constant := 16#02#; -- 
   DIDR2_ADC8D		: constant := 16#01#; -- 


  --
  --  DIDR2
  --

  -- Digital Input Disable Register
  DIDR0 : Unsigned_8;
  for DIDR0'Address	 use System'To_Address (16#7E#);

   DIDR0_ADC7D		: constant := 16#80#; -- 
   DIDR0_ADC6D		: constant := 16#40#; -- 
   DIDR0_ADC5D		: constant := 16#20#; -- 
   DIDR0_ADC4D		: constant := 16#10#; -- 
   DIDR0_ADC3D		: constant := 16#08#; -- 
   DIDR0_ADC2D		: constant := 16#04#; -- 
   DIDR0_ADC1D		: constant := 16#02#; -- 
   DIDR0_ADC0D		: constant := 16#01#; -- 


  --
  --  BOOT_LOAD
  --

  -- Store Program Memory Control Register
  SPMCSR : Unsigned_8;
  for SPMCSR'Address	 use System'To_Address (16#57#);

   SPMCSR_SPMIE		: constant := 16#80#; -- SPM Interrupt Enable
   SPMCSR_RWWSB		: constant := 16#40#; -- Read While Write Section Busy
   SPMCSR_SIGRD		: constant := 16#20#; -- Signature Row Read
   SPMCSR_RWWSRE		: constant := 16#10#; -- Read While Write section read enable
   SPMCSR_BLBSET		: constant := 16#08#; -- Boot Lock Bit Set
   SPMCSR_PGWRT		: constant := 16#04#; -- Page Write
   SPMCSR_PGERS		: constant := 16#02#; -- Page Erase
   SPMCSR_SPMEN		: constant := 16#01#; -- Store Program Memory Enable


  --
  --  USART2
  --

  -- USART I/O Data Register
  UDR2 : Unsigned_8;
  for UDR2'Address	 use System'To_Address (16#D6#);



  --
  --  UDR2
  --

  -- USART Control and Status Register A
  UCSR2A : Unsigned_8;
  for UCSR2A'Address	 use System'To_Address (16#D0#);

   UCSR2A_RXC2		: constant := 16#80#; -- USART Receive Complete
   UCSR2A_TXC2		: constant := 16#40#; -- USART Transmitt Complete
   UCSR2A_UDRE2		: constant := 16#20#; -- USART Data Register Empty
   UCSR2A_FE2		: constant := 16#10#; -- Framing Error
   UCSR2A_DOR2		: constant := 16#08#; -- Data overRun
   UCSR2A_UPE2		: constant := 16#04#; -- Parity Error
   UCSR2A_U2X2		: constant := 16#02#; -- Double the USART transmission speed
   UCSR2A_MPCM2		: constant := 16#01#; -- Multi-processor Communication Mode


  --
  --  UCSR2A
  --

  -- USART Control and Status Register B
  UCSR2B : Unsigned_8;
  for UCSR2B'Address	 use System'To_Address (16#D1#);

   UCSR2B_RXCIE2		: constant := 16#80#; -- RX Complete Interrupt Enable
   UCSR2B_TXCIE2		: constant := 16#40#; -- TX Complete Interrupt Enable
   UCSR2B_UDRIE2		: constant := 16#20#; -- USART Data register Empty Interrupt Enable
   UCSR2B_RXEN2		: constant := 16#10#; -- Receiver Enable
   UCSR2B_TXEN2		: constant := 16#08#; -- Transmitter Enable
   UCSR2B_UCSZ22		: constant := 16#04#; -- Character Size
   UCSR2B_RXB82		: constant := 16#02#; -- Receive Data Bit 8
   UCSR2B_TXB82		: constant := 16#01#; -- Transmit Data Bit 8


  --
  --  UCSR2B
  --

  -- USART Control and Status Register C
  UCSR2C : Unsigned_8;
  for UCSR2C'Address	 use System'To_Address (16#D2#);

   UCSR2C_UMSEL2		: constant := 16#C0#; -- USART Mode Select
   UCSR2C_UPM2		: constant := 16#30#; -- Parity Mode Bits
   UCSR2C_USBS2		: constant := 16#08#; -- Stop Bit Select
   UCSR2C_UCSZ2		: constant := 16#06#; -- Character Size
   UCSR2C_UCPOL2		: constant := 16#01#; -- Clock Polarity


  --
  --  UCSR2C
  --

  -- USART Baud Rate Register  Bytes
  UBRR2 : Unsigned_8;
  for UBRR2'Address	 use System'To_Address (16#D4#);



  --
  --  USART3
  --

  -- USART I/O Data Register
  UDR3 : Unsigned_8;
  for UDR3'Address	 use System'To_Address (16#36#);



  --
  --  UDR3
  --

  -- USART Control and Status Register A
  UCSR3A : Unsigned_8;
  for UCSR3A'Address	 use System'To_Address (16#30#);

   UCSR3A_RXC3		: constant := 16#80#; -- USART Receive Complete
   UCSR3A_TXC3		: constant := 16#40#; -- USART Transmitt Complete
   UCSR3A_UDRE3		: constant := 16#20#; -- USART Data Register Empty
   UCSR3A_FE3		: constant := 16#10#; -- Framing Error
   UCSR3A_DOR3		: constant := 16#08#; -- Data overRun
   UCSR3A_UPE3		: constant := 16#04#; -- Parity Error
   UCSR3A_U2X3		: constant := 16#02#; -- Double the USART transmission speed
   UCSR3A_MPCM3		: constant := 16#01#; -- Multi-processor Communication Mode


  --
  --  UCSR3A
  --

  -- USART Control and Status Register B
  UCSR3B : Unsigned_8;
  for UCSR3B'Address	 use System'To_Address (16#31#);

   UCSR3B_RXCIE3		: constant := 16#80#; -- RX Complete Interrupt Enable
   UCSR3B_TXCIE3		: constant := 16#40#; -- TX Complete Interrupt Enable
   UCSR3B_UDRIE3		: constant := 16#20#; -- USART Data register Empty Interrupt Enable
   UCSR3B_RXEN3		: constant := 16#10#; -- Receiver Enable
   UCSR3B_TXEN3		: constant := 16#08#; -- Transmitter Enable
   UCSR3B_UCSZ32		: constant := 16#04#; -- Character Size
   UCSR3B_RXB83		: constant := 16#02#; -- Receive Data Bit 8
   UCSR3B_TXB83		: constant := 16#01#; -- Transmit Data Bit 8


  --
  --  UCSR3B
  --

  -- USART Control and Status Register C
  UCSR3C : Unsigned_8;
  for UCSR3C'Address	 use System'To_Address (16#32#);

   UCSR3C_UMSEL3		: constant := 16#C0#; -- USART Mode Select
   UCSR3C_UPM3		: constant := 16#30#; -- Parity Mode Bits
   UCSR3C_USBS3		: constant := 16#08#; -- Stop Bit Select
   UCSR3C_UCSZ3		: constant := 16#06#; -- Character Size
   UCSR3C_UCPOL3		: constant := 16#01#; -- Clock Polarity


  --
  --  UCSR3C
  --

  -- USART Baud Rate Register  Bytes
  UBRR3 : Unsigned_8;
  for UBRR3'Address	 use System'To_Address (16#34#);


end AVR.ATmega2560;
```