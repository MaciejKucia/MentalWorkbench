---
title: Kurs AVR C
layout: "base.njk"
---

## Kurs AVR C

* [Mikrokontrolery AVR](/projects/avrc/avr)

## Rozdziały

* [00 Przygotowanie warsztatu pracy](/projects/avrc/art/0x00)
* [01 Podstawy elektroniki](/projects/avrc/art/0x01)
* [02 Porty We/Wy migająca dioda](/projects/avrc/art/0x02)
* [03 Przyciski, podstawowe przerwania](/projects/avrc/art/0x03)
* [04 Przetwornik ADC i komparator](/projects/avrc/art/0x04)
* [05 Fusebity, biblioteka avr-libc](/projects/avrc/art/0x05)
* [06 Układy czasowe](/projects/avrc/art/0x06)
* [07 UARTc](/projects/avrc/art/0x07)
* [08 PROGMEM](/projects/avrc/art/0x08)
* [10 EEPROM](/projects/avrc/art/0x0a)

## Miniprojekty

* [00 Zamek szyfrowy z tarczą numeryczną](/projects/avrc/mp/mp0)
* [Przejściówka IDC10](/projects/avrc/mp/przejsciowka)

## Wyprowadzenia

![wyprowadzenia](/projects/wyprowadzenia.svg)

## Uwagi

### F_CPU

Czasami można spotkać się z następującą dyrektywą preprocesora:

```
#define F_CPU
```

Dyrektywa ta służy do poinformowania wszelakich makr i podprogramów w naszym kodzie o szybkości taktowania układu (np. funkcja delay z tego korzysta do obliczenia ilość pętli potrzebnych do odczekania podanego odcinka czasu). W naszym przypadku nie możemy dodać tej komendy w kodzie, ponieważ jest ona wysyłana "przez eclipse" do kompilatora jako argument linii poleceń (deklaracja tej wartości znajduje się w pliku makefile), zdublowana deklaracja doprowadziłaby do konfliktu. Jedynym miejscem w jakim podajemy częstotliwość są ustawienia projektu. Zmiana częstotliwości taktowania jest możliwa tylko poprzez zmianę fusebitów i dodaniu zewnętrznego kwarcu (lub generatora) oraz podania częstotliwości tego sygnału taktującego w ustawieniach projektu (pliku makefile).

## Pozostałe

* [Tabele z elementami oraz parametry elementów. (Zakupy grupowe 2012)](/projects/avrc/zestaw2012)
* [Tabela z elementami oraz parametry elementów. (Zakupy grupowe 2011)](/projects/avrc/zestaw2011)
* **[Programator AVRISP-MKII Clone](/projects/avrc/programator)**
* [Dodatki](/projects/avrc/dodatki)
