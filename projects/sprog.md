# sprog - simple serial AVR bootloader

_20.6.2010, Krakow Poland_

> This project is very old and no longer developed.

[Source code](/media/sprog.zip)

![alt](/media/sprog1.jpg)

Zniechęcony rozwiązaniami dostępnymi w internecie postanowiłem napisać własny bootloader dla mikrokontrolerów z rodziny AVR. Gotowe rozwiązania jakie znalazłem były zbyt rozbudowane lub po prostu nie działały. Projekt powstał w około 6-7 dni ale tylko dla tego że było to zagadnienie zupełnie mi obce i wszystkiego musiałem się nauczyć. Rozwiązanie jest proste i znacząco upraszcza proces programowania. Mam nadzieję że mój projekt będzie dobrą bazą dla własnych rozwiązań! 

## Czym jest bootloader
 
Nazwa pochodzi od angielskiego bootstrap load. Słówko bootstrap pochodzi z kolei od powiedzenia "pull oneself up by one`s bootstraps" czyli dawać sobie samemu radę. Bootloader jest więc programem który "sam siebie wczytuje". 
Bootloader jest uruchamiany jako pierwszy w chwili zresetowania procesora (dzięki ustawieniu odpowiednich fusebitów). Bootloader znajduje się na końcu pamięci flash. Jedynie kod umieszczony w sekcji bootloadera może wykonywać pewne operacje, np zapisywać pamięć Flash, kod położony poza tą sekcją nie ma dostępu do tego typu operacji. Dzięki temu za pomocą bootloadera możemy zmieniać zawartość pamięci a dane do wpisania uC odbiera przez zaprogramowany przez nas interfejs (uart, i2c, ręcznie, ultradźwiękami, mikrofalami, kartą sd ... co tylko programista wymyśli). Pozwala to zrezygnować z programatora. 

Założenia: 
* Komunikacja przez interfejs szeregowy uart( ja korzystam z przejściówki usb->com ) 
* Mały rozmiar, do 512 bajtów (początkowo urządzeniem docelowym była ATMega8 ale niestety zabił ją ładunek elektrostatyczny, obecnie wersja jest przygotowana pod ATMega32, rozwiązanie oczywiście bardzo łatwo przeportować na inne µC AVR). 
* Programowanie flash szybciej od avrdude. 
* Kontrola danych "w locie" (dzięki czemu można pominąć odczyt tak jak to dzieje się w avrdude, metoda xor ale sprawdza się bardzo dobrze) 
* Zdalny reset (poprzez linie DTR, RTS) 
* Integracja z WinAVR 

Co udało się dodatkowo "upchnąć": 
* Odczyt Flash 
* Zapis i odczyt EEPROM (w trybie terminalu) 
* Odczyt fusebitów i lockbitów 

Dodatkowe plusy rozwiązania: 
* Dzięki wgranemu wcześniej bootloaderowi można programować nawet jeżeli za pomocą fusebitów zablokujemy ISP,reset itp. 
* Kod całkowicie darmowy, licencja MIT (X11) 

Pytania i odpowiedzi: 
1. Mam zablokowany układ, czy bootloader pomoże mi go odblokować/zaprogramować/cokolwiek? 
   
   Nie, bootloader musi zostać jakoś wgrany więc zablokowany układ należy wcześniej odblokować. 
1. Dlaczego w ogóle zawracać sobie głowę bootloaderem?

    Za pomocą bootloadera nie można popsuć fusebitów (bo się nie da ich zmienić ); bootloader w większości przypadków zaprogramuje układ szybciej niż usbasp, lpt i tym podobne rozwiązania; bootloader korzysta z rs232 więc można wykorzystać np. moduł bluetooth i programować zdalnie!; Jeżeli już nasz projekt wykorzystuje komunikację szeregową to redukujemy znacząco ilość przewodów na płytce, stopień skomplikowania układu.; Podczas projektowania płytki łatwiej wyprowadzić 3 przewody do transferu szeregowego niż gniazdo w standardzie Kanda. 
1. Mam atmegę8 czy mogę użyć do niej tego kodu?

    Bootloader znajduje się na końcu pamięci flash, więc konieczna jest zmiana (niewielka). Mogę na życzenie skompilować kod pod atmegę8 ale niestety nie posiadam układu więc nie mogę sprawdzić działania (tak nawiasem: jeżeli układy te nie wrócą po 3zł /sztukę to wróżę im marną przyszłość  ) 
1. Czy trzeba grzebać w fusebitach aby bootloader działał?

    Niestety tak, procesor musi wiedzieć że startuje od adresu np. 0x3F00 a nie od 0x0000 
1. Dlaczego nie można wykorzystać Avrdude?

    Avrdude nie wspiera mojego rozwiązania, co więcej nie wspiera żadnego prostego bootloadera (tylko takie >= 1kB). 
1. Dlaczego Atmel nie wgrywa fabrycznie bootloadera

    Może zarabiają na zablokowanych ATMegach8  NXP i Microchip (ICSP) wgrywają fabryczny bootloader. 
1. Czy można programować EEPROM? Tak ale tylko po bajcie w trybie terminalu. Teoretycznie mógłbym dodać zapis z pliku ale kasowanie strony dla każdego bajtu w stronie nie wyszłoby na zdrowie układowi. W pełni funkcjonalny zapis EEPROM wymaga rozszerzenia programu bootloadera. 

Tutaj screen z Programmer's Notepad, czyli jak to działa w praktyce: 

![alt](/media/sprog2.jpg)

Po wgraniu bootloadera wystarczy prosty interfejs, ja zastosowałem przejściówkę com/usb oraz układ max232 jak w zdjęciu poniżej, można użyć ftdi czy adaptera bluetooth (np BTM-222). W porównaniu z usbasp znacząco zredukowałem ilość przewodów na płytce szczególnie że w projektach często wykorzystuje rs. 
 
Przydatne linki: 
*
 [Bootloader kolegi mirekk36](http://www.elektroda.pl/rtvforum/topic1343484.html#6695669), niestety rozwiązanie komercyjne 
* [Opis bootloaderów w środowisku arduino](http://arduino.cc/en/Hacking/Bootloader?from=Main.Bootloader)
* [Bootloader kolegi master_pablo](http://www.elektroda.pl/rtvforum/topic1368320.html)
* [Kolejny ciekawy bootloader.](http://avr-news.freehostia.com/projekty/avrub-uniwersalny-bootloader/)
