---
title: Programator
layout: "base.njk"
---

## Programator

## Wstęp

Dawno temu kiedy komputery posiadały jeszcze [[wp>Parallel_port|pory równoległe]] programowanie układów AVR wymagało jedynie kilku rezystorów. Dzisiaj w erze laptopów konieczne jest zbudowanie dodatkowego urządzenia pośredniczącego: programatora. Zadaniem urządzenia jest wysyłanie komend do układu docelowego w celu wykorzystania wbudowanego modułu [[wp>In-system_programming|ISP]] układów AVR, który to posiada między innymi możliwość zmiany zawartości pamięci Flash (programu).

## Idea

Obecnie popularne programatory posiadają następujące wady:
  * Są stosunkowo drogie - Najtańszy oficialny programator AVR Dragon to wydatek rzędu ∼250 PLN (2010)
  * Są skomplikowane - wiele programatorów posiada np. bufory konieczne do programowania układów pracujących przy napięciach zasilania innych niż 5V
  * <del>Wymagają niepodpisanych sterowników (problemy w 64 Windowsie)</del> (Edit: Najnowsze wydania USBLib nie posiadają tego problemu)
Oraz co najgorsze:
  * Wymagają innego programatora do uruchomienia!

Kod programatora opiera się na projekcie wchodzącym w skład pakietu LUFA((Lightweight USB Framework for AVRs by Dean Camera)): <https://web.archive.org/web/20241108081242/http://www.fourwalledcubicle.com/AVRISP.php> Natomiast płytka została zaprojektowana przeze mnie.

## Zalety tego programatora

  * Dzięki wbudowanemu [[bootloaderowi]] USB nie jest konieczne posiadanie innego programatora w celu jego uruchomienia.
  * Umożliwia zasilenie układu docelowego
  * Zastosowanie elementów [[SMD]] eliminuje konieczność wiercenia (chyba najbardziej uciążliwy proces podczas wytwarzania płytek).
  * Tylko 4 elementy wymagają odpowiedniej polaryzacji + mikrokontroler (trudniej o pomyłkę).
  * Pracuje z avrdude lub z AVR Studio (w zależności od wybranego firmware)
  * Niski koszt (20÷25 PLN październik 2011)
  * Małe wymiary
  * Posiada generator 4MHz (do ratowania zablokowanych układów przez złe ustawienie fusebitów źródła taktowania)
  * Programuje układy korzystające z interfejsów [[ISP]], PDI, TPI (Układy AVR32 i xMega)
  * Prawdziwe USB (nie przekombinowane jak w przypadku np. USBASP)

## Schematy

![alt](/projects/avrc/media/avrisp_schematic.png)
![alt](/projects/avrc/media/board_kolory.png)

## Lista elementów

| Element | Wartość | Opis |  
| --- | --- | --- |
| IC1 | AT90USB162 | Mikrokontroler | 
| USB | - | Pola lutownicze do podłączenia przewodu USB | 
| F1  | 500 [mA] | Bezpiecznik polimerowy |  
| R1 R2 | 22 [Ω] | Rezystory linii USB |  
| C1 | 1 [uF] | Kondensator stabilizatora napięcia 3V3 ((Dla modułu USB układu)) | 
| C3 C4 | 33 [pF] | Kondensatory oscylatora | 
| Y1 | 16 [MHz] | Oscylator kwarcowy | 
| C2 | 100 [nF] | Kondensator szyny zasilania | 
| C5 | 10 [uF] | Kondensator szyny zasilania | 
| R3 | 1 [kΩ] | Rezystor ustalający stan nieaktywny (wysoki) na sygnale reset uC | 
| R4 | 1 [kΩ] | Rezystor ustalający stan nieaktywny (wysoki) na sygnale hardware bootloader uC | 
| R5 R6 | x [kΩ] | Rezystory ograniczające prądy w diodach sygnalizacyjnych | 
| LED1 LED2 | Diody sygnalizacyjne | 
| | | Złącza szpilkowe typu goldpin | 

## Wykonanie

- Laminat należy przyciąć do odpowiednich wymiarów
- Krawędzie laminatu należy zaokrąglić za pomocą pilnika do metalu lub papieru ściernego
- Laminat należy dokładnie oczyścić z zabrudzeń
- Na laminat należy przenieść obraz ścieżek układu dowolną metodą
- Laminat należy wytrawić
- Obraz ścieżek należy zmyć
- Wszystkie ścieżki należy sprawdzić pod kątem przerw i zwarć z pobliskimi ścieżkami 
- Płytkę należy zabezpieczyć roztworem kalafonii
- Pobielamy pady układu scalonego
- Jako pierwszy montujemy układ scalony, po dokładnym spozycjonowaniu i sprawdzeniu poprawności pozycji. Przylutowywujemy dwa naprzeciw położone wyprowadzenia cały czas przytrzymując układ. Po unieruchomieniu układu przylutowywujemy pozostałe wyprowadzenia.
- Sprawdzamy każde wyprowadzenie układu pod kątem zwarć i przerw
- Przylutowywujemy kolejne elementy zaczynając od najmniejszych.
- Diody oraz kondensatory tantalowe muszą być odpowiednio spolaryzowane.
- Przylutowywujemy przewody USB
- Przewody przylutowywujemy do pól lutowniczych (:!: w złączu linie MOSI i MISO muszą być zkrosowane!)

## Uruchomienie

### Sprawdzenie poprawności działania i troubleshooting

- Sprawdzamy polaryzację kondensatorów
- Sprawdzamy poprawność połączeń
- Sprawdzamy czy nie ma zwarcia pomiędzy masą a szyną zasilania
- Sprawdzamy czy kryształ jest połączony z uC i czy nie ma zwarć
- Sprawdzamy czy nie ma zimnych lutów (matowe połączenie zamiast błyszczącego)
- Podłączamy urządzenie do komputera
- Sprawdzamy napięcie na kondensatorach tantalowych: na większym powinno wynosić  5±0.5 [V] na mniejszym (regulator 3V3 dla szyny danych USB) 3.3±5 [V]
- Sprawdzamy czy linie MOSI i MISO są skrosowane

### Oprogramowanie

1. Ściągamy potrzebne narzędzia:

* [Najnowsze libUSB-win](http://sourceforge.net/apps/trac/libusb-win32/wiki)
* [Najnowszy pakiet LUFA](https://web.archive.org/web/20241108081242/http://www.fourwalledcubicle.com/LUFA.php) (wymaga modyfikacji)
* [Narzędzie Atmel FLIP](http://www.atmel.com/dyn/products/tools_card.asp?tool_id=3886) lub [[http://dfu-programmer.sourceforge.net/|DFU-programmer]] pod Linuksem
* (Dodatkowo) [USBView](http://www.ftdichip.com/Support/Utilities.htm)

Osoby korzystające z Linuksa powinny pobrać odpowiednie dla siebie narzędzia i odpowiednio dostosować następujące kroki.

> Kod z pakietu LUFA wymaga modyfikacji: pin PB4 musi być w czasie pracy nieaktywny. Najnowszy kod posiada błąd uniemożliwiający poprawną prace (reset aktywny stanem wysokim)

2. Sprawdzony układ podłączamy do komputera, za pomocą menedżera urządzeń lub programu USBView powinniśmy zaobserwować pojawienie się nowego urządzenia. (Pod Linuksem można użyć narzędzia lsusb)

3. Instalujemy sterowniki które znajdują się w katalogu instalacyjnym narzędzia Atmel FLIP.

4. Jeżeli skompilowaliśmy program samodzielnie, do zaprogramowania układu możemy wykorzystać makro znajdujące się w pliku makefile. Jeżeli wgrywamy prekompilowany program należy: 
  - uruchomić narzędzie Atmel FLIP
  - wybrać opcje z menu głównego: __Device__->__Select__...->__AT90USB162__->OK
  - wybrać opcje z menu głównego: __Settings__->__Communication__->__USB__
  - w momencie pojawienia się okna __USB Port Connection__ wybieramy opcje __Open__
  - wybrać opcje z menu głównego: __File__->__Load HEX File...__ i otworzyć odpowiedni plik
  - w zakładce __Operations Flow__ klikamy przycisk __Run__
  - zamykamy narzędzie Atmel FLIP

5. Resetujemy urządzenie poprzez ponowne podłączenie do portu USB. W śród urządzeń USB powinno się pojawić nowe urządzenie, sterowniki instalujemy z katalogu instalacji libUSB-win.

6. Jeżeli nasz system nie chce uruchomić niepodpisanego sterownika musimy jeszcze wygenerować odpowiednie pliki INF za pomocą narzędzia inf-wizard należącego do pakietu libUSB-win.

### Możliwe problemy

  * Jeżeli na komputerze zainstalowano AVRStudio to w systemie będą zainstalowane sterowniki [Jungo WinDriver](http://www.jungo.com/st/windriver_usb_pci_driver_development_software.html), urządzenie nie będzie działało poprawnie dopóki nie zostanie zainstalowany sterownik libUSB. [Pomoc](http://www.societyofrobots.com/robotforum/index.php?topic=6664.0)

## Korzystanie z programatora

Jeżeli programujemy za pomocą avrdude należy korzystać z następującego schematu:
`avrdude -pXX -cavrispmkii -P usb` gdzie pod XXX wstawiamy nazwę układu do programowania (np. -pm8 dla ATmega8). Użytecznym argumentem linii poleceń jest `-B 4` który ustala okres trwania sygnału taktującego (w tym przypadku 4 [us]: 250 [kHz] )


## Aktualizacja oprogramowania

Kiedy kupujemy MCU ma on wgrany jedynie bootloader znajdujący się na końcu pamięci programu. Po resecie PC((program counter)) "przelatuje" przez całą pamięć (wypełnioną rozkazem NOP((NO Opearation)) ) aż trafia na program bootloadera.
Po wgraniu oprogramowania MCU, bootloader nie jest automatycznie aktywowany. Można jednak wymusić uruchomienie bootloadera już po wgraniu programu. Należy:
  * Podciągnąć linię HWB((HardWare Boot)) do minusa [1]
  * Zresetować układ poprzez linię reset [2] (tutaj wystarczy ułamek sekundy zwarcia z masą, ale linia HWB musi być w tym czasie również zwarta)
Aby to zrobić należy zewrzeć następujące punkty do masy (układ ma być podłączony do komputera).

![alt](/projects/avrc/media/avrisp_boot.jpg)

TICK Do zwarcia linii z masą konieczne jest metalowe narzędzie. Jedna z ścieżek może zostać zwarta za pomocą czarnego przewodu wyprowadzonego z płytki.

> Należy zwrócić szczególną ostrożność podczas procedury, można spowodować zwarcie linii zasilania komputera. Kolorem czerwonym oznaczyłem ścieżki szyny zasilania,
> niebieskim masę a fioletowym ścieżki do zwarcia z masą. 

## Pliki

* [Schematy](/media/programmer_v3.zip) - Eagle, now owned by Autodesk
* [Aktualny wsad do procesora Maj 2012](/media/avrisp-mkii2.zip)
