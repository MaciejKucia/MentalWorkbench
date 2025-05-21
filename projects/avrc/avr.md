---
title: Co to jest AVR?
layout: "base.njk"
---

## Co to jest AVR?

![alt](/projects/avrc/avr.svg)

AVR jest rodziną 8 bitowych mikrokontrolerów RISC opartych na zmodyfikowanej architekturze harwardzkiej stworzonych przez firmę Atmel w 1996 roku. Mikrokontrolery te bardzo szybko stały się popularne, ponieważ zawierały pamięć [flash](https://pl.wikipedia.org/wiki/Pami%C4%99%C4%87_flash) co wówczas było rzadkością.

## Co te terminy oznaczają?

- 8 bitów oznacza że układ jest w stanie w trakcie jednej instrukcji przeliczyć 8 bitową liczbę. Dopóki nie będziemy chcieli bawić się liczbami zmiennoprzecinkowymi nie powinno być z tym ograniczeniem problemu.
- RISC (ang. Reduced Instruction Set Computer) układ realizuje małą liczbę instrukcji ale za to w jednym takcie (np. Intel posiada całą masę instrukcji jednak niektóre potrzebują kilku taktów aby zostały wykonane). Rozwiązanie ma swoje plusy, mniejszy stopień skomplikowania układu to niższy koszt produkcji i niższe zużycie energii.
- Zmodyfikowana architektura harwardzka. Dociekliwych odsyłam do [Wikipedii](https://pl.wikipedia.org/wiki/Zmodyfikowana_architektura_harwardzka)
- Dlaczego flash jest taki fajny? Początkowo układy były programowane za pomocą maski w trakcie produkcji ([MROM](https://handwiki.org/wiki/Mask_ROM)), potem można było programować układ już po produkcji, pamięć składała się z zintegrowanych rezystorów które wystarczyło przepalić aby zapisać informację ([PROM](https://en.wikipedia.org/wiki/Programmable_ROM)). Jeżeli zaistniałaby potrzeba zmiany programu, należałoby wymienić układ, więc rozwiązanie kosztowne. W pewnym momencie pojawiły się pamięci [EPROM](https://en.wikipedia.org/wiki/EPROM), wreszcie można było skasować program i nagrać nowy, jednak kasowanie wymagało  naświetlania ultrafioletem (układy z szybką, niektóre sklepy elektroniczne oferowały jeszcze niedawno takie kasowanie). Następnie pojawiły się pamięci [EEPROM](https://en.wikipedia.org/wiki/EEPROM) (Electrically Erasable Programmable ROM) oraz [Flash](https://en.wikipedia.org/wiki/Flash_memory) (Flash jest pamięcią EEPROM, jednak w pamięci flash nie kasuje się całej pamięci na raz. Pamięć ta jest podzielona na sektory, a kasowanie usuwa informacje tylko z jednego sektora). Możliwość łatwego programowania i zmiany programu jest bardzo ważnym aspektem podczas pracy z uC.

## Dlaczego akurat AVR?

uC firmy Atmel są popularne w Polsce a więc: łatwo dostępne, stosunkowo tanie*, sporo projektów na elektrodzie jest oparte na avr'ach i stosunkowo dużo informacji na ich temat jest po polsku. Czasopisma branżowe również mocno wpłynęły na popularność akurat tych układów.
Pomimo różnic w budowie wewnętrznej większość mikroprocesorów jest podobnych a więc wiedza zdobyta na avr'ach będzie wykorzystywana przy innych układach.

## Warianty układów AVR

Układy z rodziny avr występują w przyrodzie w następujących wariantach (od największej mocy obliczeniowej, pamięci, częstotliwości taktowania):

* AVR32 - 32 bitowa wersja, zaawansowane układy dla urządzeń multimedialnych.
* Xmega - 16/8 bitowe układy wypełniające lukę pomiędzy zaawansowanymi AVR32 a ATmega.
* ATmega - seria układów o szerokim wachlarzu zastosowań. Interesująca nas rodzina, wersje różnią się wielkością pamięci i peryferiami.
* ATtiny - najprostsze układy, zastosowanie w prostych układach.

## Środowisko programistyczne

Podczas pracy z układem będziemy korzystać z zestawu narzędzi gnu avr-gcc. Konkretnie WinAVR (windows) oraz edytora eclipse.

* [Strona projektu WinAVR](http://sourceforge.net/projects/winavr/)
* [Strona pobierania eclipse dla C/C++](http://www.eclipse.org/downloads/)
* [Strona rozszerzenia eclipse AVR Eclipse](http://avr-eclipse.sourceforge.net/wiki/index.php/Plugin_Download)

## Programator

Układy AVR posiadają możliwość programowania w systemie (ang. [ISP In-system programming](https://en.wikipedia.org/wiki/In-system_programming)) Jeżeli ktoś posiada komputer ze złączem LPT (szeregowym) to może programować avr'y wprost z tego portu (programator szeregowy), jednak najlepiej zrealizować programator USB np. bardzo dobry AVRISPMKII lub USBasp. Programator pełni rolę "tłumacza interfejsów" pomiędzy komputerem (USB) a układem docelowym (SPI).

* [Strona domowa projektu USBasp](http://www.fischl.de/usbasp/)
* [Strona domowa projektu AVRISP mkII](https://web.archive.org/web/20241108081242/http://www.fourwalledcubicle.com/AVRISP.php)

## Złącze programatora

Zdjęcie przedstawia standardowe złącze programowania używane przy mikrokontrolerach AVR. Jest to złącze wprowadzone przez firmę [Kanda](http://www.kanda.com/) stąd często nazywa się je złączem Kanda lub złączem ISPod funkcji jaką pełni. Warto wiedzieć że wtyk  nazywa się złączem [IDC](https://en.wikipedia.org/wiki/IDC_(electrical_connector)) a gniazdo nazywamy "gniazdem wannowym" lub "wanienkowym".

Programowanie odbywa się przez interfejs [SPI](http://en.wikipedia.org/wiki/Serial_Peripheral_Interface_Bus) który składa się z następujących sygnałów:
  * MOSI - (Master Output Slave Input) Sygnał danych z kierunkiem przesyłu od programatora (master) do układu (slave).
  * MISO - (Master Input Slave Output) Sygnał danych z kierunkiem przesyłu od układu do programatora.
  * SCK - (Serial ClocK) Sygnał zegarowy.
  * RST - Reset, aktywny stanem niskim. Układy AVR pracują w trybie programowania ISP tylko w "stanie resetu". (W zwykłym interfejsie SPI, sygnał ten nazywa się SS [Slave Selct])
Dodatkowo w złączu występują następujące sygnały:
  * LED - Nie używane w USBasp, w niektórych programatorach podczas programowania pojawia się na tym złączu stan wysoki dzięki czemu można sygnalizowac (np. za pomoca LEDa) że układ jest aktualnie programowany. Można pozostawić niepodłączone.
  * VCC - Zasilanie.
  * GND - Masa

## Programowanie

### Schemat połączenia

![alt](/projects/avrc/avr_schematic.svg)

Uwaga! Zasilanie przez programator może nie wystarczyć (Ograniczenie prądowe na USB do 50mA wynikające z konfiguracji USBasp!), mi nie udało się zaprogramować układu korzystając z zasilania z szyny. Układ należy zasilać tylko napięciem __stabilizowanym__ 5V. W przypadku korzystania z zewnętrznego napięcia zasilania najlepiej odłączyć linię zasilającą programatora!

## avrdude

Avrdude (AVR Downloader/UploaDEr) jest programem wchodzącym w skład pakietu WinAVR (gnu avr-gcc). Jest to aplikacja konsolowa (chociaż istnieją niezbyt dobre nakładki graficzne) i warto poznać sposób pracy z tym programem, pomimo iż pracując w środowisku eclipse jego praca nie będzie widoczna.

Użycie komendy avrdude w konsoli wyświetli nam listę argumentów jakie on przyjmuje. Ponieważ skupimy się na programowaniu układu ATmega8 programatorem AVRISPmkII należy zapamiętać podstawową listę argumentów:
``` avrdude -pm8 -cavrispmkii -Pusb``` 
(Lub dla USBasp):
``` avrdude -pm8 -cusbasp``` 

Co powinno nam zwrócić następującą informację:

``` avrdude: AVR device initialized and ready to accept instructions

Reading | ################################################## | 100% 0.02s

avrdude: Device signature = 0x1e9307

avrdude: safemode: Fuses OK

avrdude done.  Thank you.
```

Informacja ta oznacza że układ odpowiedział i jest prawidłowo rozpoznany. Parametr -p służy do wyboru układu jaki programujemy a -c programatora.

Mogą się jednak zdarzyć błędy np:

``` 
avrdude: error: programm enable: target doesn't answer. 1 
avrdude: initialization failed, rc=-1
         Double check connections and try again, or use -F to override
         this check.
``` 

Lub:

``` 
avrdude: Device signature = 0x000000 
avrdude: Yikes!  Invalid device signature. 
         Double check connections and try again, or use -F to override 
      
         this check.
``` 
Takie komunikaty najczęściej oznaczają problem z połączeniem pomiędzy programatorem a układem docelowym.

Kolejnym ważnym parametrem jest -U który definiuje zadanie dla programu.

```
avrdude -pm8 -cavrispmkii -Pusb -U flash:r:PLIKPROGRAMUfl.hex
avrdude -pm8 -cavrispmkii -Pusb -U eeprom:w:PLIKPROGRAMUee.hex
avrdude -pm8 -cavrispmkii -Pusb -U hfuse:w:0x{wartość}:m -U lfuse:w:0x{wartość}:m 
``` 

Pierwsza linijka odczytuje zawartość pamięci flash uC i zapisuje ją w pliku PLIKPROGRAMUfl.hex. Druga linijka zapisuje zawartość pliku PLIKPROGRAMUee.hex do pamięci EEPROM mikrokontrolera. Trzecia linijka zapisuje górne (hfuse) i dolne (lfuse) fusebity do uC. Jak widać możemy definiować więcej niż jedno zadanie na raz. AVRdude podczas zapisu dodatkowo sprawdza jego poprawność (odczytuje to co zapisał i porównuje). Podczas zapisu fusebitów warto kożystać z gotowego tekstu generowanego przez skrypt na stronie [fusecalc](http://www.engbedded.com/fusecalc/).

## fuse bits

Wielu początkujących nieświadomie (z niewiedzy) blokuje sobie układy więc warto zwrócić uwagę na kwestię fusebitów.

Fusebity to po polsku bity konfiguracyjne. Służą do zmiany parametrów pracy układu takich jak:

* __Źródło sygnału zegarowego.__
* Regulacja pracy układu nadzorującego zasilanie (niskie napięcia powodują nieprawidłową pracę uC, więc jest możliwe ustawienie układu tak aby samoczynnie resetował się w momencie zaniku napięcia [przydatne np. przy zasilaniu bateryjnym]).
* Ustawianie adresu początku programu.
* Włączanie/wyłączanie możliwości odczytywania programu przez ISP (zabezpieczenie przed piraceniem oprogramowania uC np. przez konkurencję)
* Włączanie/wyłączanie watchdoga (resetuje uC jeżeli się zawiesi)
* __Regulacja funkcji pinu 1 (reset lub pin logiczny)__
* Oraz inne

Podkreślone parametry są bardzo ważne, jeżeli ustawimy źródło sygnału zegarowego na zewnętrzne to jeżeli nie mamy kwarcu, nasz układ nie ruszy (i nie będzie się dało go programować!). Jeżeli pin nr.1 zostanie ustawiony jako pin logiczny a nie reset to programowanie przez ISP nie będzie w ogóle możliwe! (Istnieją inne metody programowania dzięki którym można odblokować taki zablokowany reset np [programatorem szeregowym wysokonapięciowym](http://www.scienceprog.com/avr-serial-and-parallel-high-voltage-programmer/))

Na szczęście fusebity możemy policzyć za pomocą skryptu na stronie [fusecalc](http://www.engbedded.com/fusecalc/). Polecam zajrzeć choćby żeby zobaczyć o co chodzi z tymi fusebitami. Problematyka fusebitów jest przedstawiona w artykule na stronie [elportalu](http://elportal.pl/index.php?module=ContentExpress&func=display&ceid=243) jednak przedstawione tam rozwiązania praktyczne dotyczą programatora szeregowego.
