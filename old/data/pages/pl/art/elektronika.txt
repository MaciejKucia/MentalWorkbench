====== Czym jest elektronika? ======
Elektronika, jest interdyscyplinarną dziedziną nauki i techniki zajmującą się przetwarzaniem sygnałów. Historycznie wywodzi się z techniki radiowej, pierwszymi urządzeniami //elektronicznymi// były odbiorniki i nadajniki radiowe. Rozwój elektroniki umożliwił gwałtowny rozwój telekomunikacji i informatyki prowadząc do [[wp>Digital_Revolution|rewolucji informatycznej]]. Dzisiaj elektronika jest elementem prawie każdej dziedziny życia i rozwija się coraz szybciej.

====== Czym zajmuje się elektronika? ======
Ogólnie elektronika zajmuje się generowaniem i przetwarzaniem sygnałów, najczęściej skojarzonych z przepływem ładunku, czyli elektrycznych, magnetycznych, elektromagnetycznych  ale również np. sygnałów świetlnych (laser, światłowody). Elektronika zajmuje się również problemami przetwarzania energii (np. w zasilaczach: elektrycznej w elektryczną, w silnikach: elektrycznej w mechaniczną, elektrycznej w świetlną itd.) Jeżeli przetwarzane są duże moce, mówimy nie o elektronice a o [[wppl>elektrotechnika|elektrotechnice]]. Obecnie możemy kontrolować pojedyncze atomy (elektronika mezoskopowa, elektronika spinowa: [[wppl>spintronika]]).

====== Podział elektroniki ======
Elektronikę można podzielić na dwie dziedziny:
<WRAP column 45% left justify>
**Elektronikę analogową**

W elektronice analogowej przetwarzane są sygnały analogowe. Elektronika analogowa jest wykorzystywana np. w wzmacniaczach akustycznych, radiu, telewizji analogowej. Każde urządzenie elektroniczne wymaga zasilania, nawet jeżeli układ przemiany energii jest sterowany cyfrowo procesy zachodzące w takim zasilaczu są analogowe. Zjawiska zachodzące w przyrodzie mają charakter analogowy a elektronika cyfrowa jest "podzbiorem" elektroniki analogowej.
</WRAP>
<WRAP column 45% right justify>
**Elektronikę cyfrową**

W elektronice cyfrowej przetwarzane są sygnały dyskretne. Sygnał dyskretny w przeciwieństwie do analogowego można podzielić na skończoną ilość stanów (mówiąc matematycznie zbiór wartości sygnału analogowego jest zbiorem nieskończonym natomiast sygnału dyskretnego skończonym). Przykładem sygnału dyskretnego jest sygnał binarny (dwójkowy) który posiada 2 stany: niski (0, LO, false) oraz wysoki (1, HI, true). Istnieją inne sygnały dyskretne np. ternarny (trójkowy).
</WRAP>
<WRAP clear></WRAP>

Najczęściej sygnał analogowy jest analizowany w dziedzinie czasu ciągłego a dyskretny w dziedzinie czasu dyskretnego. 

Należy pamiętać że elektronika cyfrowa opiera się na analogowej. Nieznajomość zagadnień "analogowych" może doprowadzić do problemów w realizacji układów cyfrowych.
====== Elektronika cyfrowa ======
Coraz więcej urządzeń przetwarza głównie sygnały cyfrowe. Dlaczego? Zamiana sygnału analogowego na cyfrowy wiąże się z utratą części informacji. W zamian sygnał cyfrowy oferuje możliwość bezstratnego przetwarzania i kopiowania informacji (nieosiągalną przy sygnale analogowym). Kopiując muzykę nagraną na kasetę magnetofonową każda kopia kopii posiada coraz gorszą jakość, natomiast kopiując muzykę cyfrową (np. mp3) nawet nieskończona liczba kopii nie będzie się różnić od oryginału. Sygnały cyfrowe dzięki coraz lepszym rozwiązaniom technicznym coraz częściej zastępują czysty "analog" (telewizja, telefonia komórkowa, fotografia, radio). Rozwiązania cyfrowe są bardziej energooszczędne i dużo mniejsze (chodzi o fizyczny wymiar urządzenia/układu co nie tylko przekłada się na ergonomie ale i koszty wytworzenia, transportu) od rozwiązań analogowych. Kolejnym wielkim plusem "cyfrówki" jest duża "plastyczność" (ang. [[wp>Flexibility_(engineering)|flexibility]]). Komputer cyfrowy można programować, analogowy posiada program wpisany w swoją budowę więc najczęściej zmiana zadania jakie wykonuje jest niemożliwa (patrz np. komputery analogowe do obliczania torów pocisków balistycznych).

====== Mikroprocesor, mikrokontroler, FPGA, DSP ======
Pojawienie się tranzystora zrewolucjonizowało elektronikę. Prekursorka tranzystora: lampa elektronowa była zawodna, ciężka, energochłonna i posiadała ograniczony czas pracy. Oczywiście budowano komputery na bazie lamp (np. [[wp>ENIAC|ENIAC]]) ale dopiero tranzystor pozwolił na budowę miniaturowych układów zintegrowanych. Układy intela serii Nehalem (core i7) posiadają około 0.7 miliarda tranzystorów na pojedynczej płytce krzemu!

Komputer jest urządzeniem służącym jak sama nazwa wskazuje do liczenia (ang. compute) a jego jednostką centralną (CPU central processing unit) jest właśnie mikroprocesor.
===== Mikroprocesor =====

Pierwszymi cyfrowymi układami scalonymi były bramki logiczne (nor, xor, and itp.) są to podstawowe elementy z których można zbudować komputer, i właśnie z wielu takich układów budowano pierwsze krzemowe, elektroniczne komputery i kalkulatory. W latach '70 w firmie Intel (INTegrated ELectronics) zintegrowano wiele układów w jednej obudowie, w wyniku czego powstał układ [[wp>Intel_4004|Intel 4004]]. Wiele firm pracowało nad takim zintegrowanym układem i co ciekawe właścicielem patentu na mikroprocesor została firma Texas Instruments która również pracowała nad analogicznym rozwiązaniem. Technika uP (od micro processor) rozwijała się i dodawano coraz szersze rejestry (poczatkowo 4 bitowe, następnie 8, 16, 32 a dziś w domowych komputerach mamy 64 bitowe). Popularnymi układami stały się np. Zilog Z80, Intel 8080, Motorola 6800. Na rynku rozpętała się prawdziwa batalia. 32 bitowy układ Intel 80386 stał się bazą dla obecnie najpopularniejszych komputerów domowych: rodziny IBM PC. 

===== Mikrokontroller =====
O ile mikroprocesory były dużym krokiem na drodze do miniaturyzacji to sam mikroprocesor potrzebuje pewnych układów pomocniczych aby pracować. Początkowo na płycie głównej obok procesora była cała masa układów, dzisiaj większość z nich została zintegrowana w formie chipsetu (ang. chip set - zestaw chipów) ale i tak dzisiejszy komputer domowy to zestaw układów połączonych ze sobą płytą główną.
Mikrokontroller jest układem który łączy w jednej obudowie układy konieczne do przetwarzania informacji oraz komunikacji ze "światem zewnętrznym" czyli:
  * Rdzeń - mikroprocesor 
  * Pamięć programu, pamięć operacyjną (RAM)
  * Układy wejścia/wyjścia
Mikrokontroller może zawierać również całą masę innych peryferiów:
  * Źródło sygnału zegarowego
  * Zegar / licznik
  * Kontroler poziomu napięcia (Brown-out detector)
  * Pamięć ustawień (np. EEPROM)
  * Przetworniki cyfra/analog analog/cyfra (C/A -> DAC, A/C -> ADC)
  * Termometr
  * Interfejsy (fizyczne/softwareowe rozwiązania komunikacyjne) (USB I2C SPI UART CAM OneWire itd...)
  * itd...
Podczas pracy na warsztatach będziemy pracować właśnie z mikrokontrolerami.

===== PSOC, FPGA, DSP =====
Warto wspomnieć też o kilku innych popularnych typach układów cyfrowych. 

**PSOC** (Programmable System-on-Chip) to zaawansowany układ integrujący w sobie zarówno elementy cyfrowe (mikrokontroler) jak i analgowe.

**FPGA** (Field programmable gate array) to układ cyfrowy składający się z matrycy wielu mikrokomórek logicznych które można zaprogramować tak aby pełniły określone funkcje logiczne. Za pomocą FPGA można zrealizować dowolny układ cyfrowy (np. mikroprocesor) i zmieniać jego strukturę wewnętrzną w czasie pracy. Układy FPGA cechują się bardzo dużą prędkością pracy i plastycznością ale również dużym poborem energii oraz skomplikowanym procesem tworzenia "programu".

**DSP** (digital signal processor) to wyspecializowany mikroprocessor przeznaczony do przetwarzania sygnałów cyfrowych w czasie rzeczywistym. Układy DSP są tak zaprojektowane aby być w stanie przetworzyć sygnał cyfrowy utworzony z analogowego (np. przetwarzanie obrazu w czasie rzeczywistym, kontrola lotu i wiele innych).