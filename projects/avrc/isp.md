---
title: ISP
layout: "base.njk"
---

8 bitowe mikrokontrolery AVR posiadają możliwość programowania w systemie (ISP). Programowanie odbywa się za pomocą interfejsu SPI((Serial Perypherial Interface)) umożliwiając modyfikację pamięci nieulotnej układu. Programowanie w systemie umożliwia szybkie zaprogramowanie pamięci bez konieczności wyjmowania MCU z urządzenia.

## Interfejs

  * MCU zawsze slave
  * Konieczna wspólna masa
  * Reset aktywny (LOW)
  * Chip erase wymaga przełączenia Reset
  * Programowanie w zakresie napięć 2.7 - 6.0 [V]
  * Reset MCU - wszystko jako wejście
  * Taktowanie jest kluczowe, zgubiony tak to konieczność resetu procesu

Sygnały:
  * SCK (Serial ClocK) - zegar: każdy impuls to przekazanie 1 bitu danych z (MISO) i równocześnie do (MOSI) układu (generuje master)
  * MISO (Master In Slave Out)
  * MOSI (Master Out Slave In)
  * RST (ReSeT)

## Komendy

### Enable Memory Access

Po resecie układ oczekuje na polecenie żeby cokolwiek zacząć. Wszystkie inne komendy są ignorowane.

| | do | z |
| --- | --- | --- |
|Programming Enable| AC 53 xx yy | zz AC 53 xx |
|Read Device Code | 30 nn 00 mm | yy 30 nn 1E |

### Device code

| | do | z |
| --- | --- | --- |
|Read Vendor at 00| 30 xx 00 yy | zz 30 xx /1E/ |
|Read Familly and Mem size at 01 | 30 nn 01 mm | yy 30 nn /90/ |
|Read Part Number at 02 | 30 xx 02 yy | mm 30 xx /01/ |

```
Vendor: 1E-Atmel 00-Device Locked
Familly, Part - 
```
