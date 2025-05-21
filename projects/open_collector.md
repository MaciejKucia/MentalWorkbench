---
title: Otwarty kolektor
layout: "base.njk"
---

## Otwarty kolektor
Otwarty kolektor (open collector) jest rodzajem wyjścia układu elektronicznego. 
Jeżeli układ jest zbudowany nie w technologi bipolarnej a polowej (MOSFET) to wyjście takie nazywamy otwartym drenem (open drain), pełni taką samą role i działa tak samo jak otwarty kolektor.
Emiter tranzystora wyjściowego jest połączony z masą. Kolektor tranzystora jest bezpośrednio wyprowadzony na zewnątrz obudowy (stąd nazwa).
Wersje układów z otwartym emiterem są dużo rzadsze. 

![alt](/projects/open_collector_1.svg)

Układy trójstanowe różnią się od układów z otwartym kolektorem. W układzie trójstanowym mamy 3 tranzystory: dwa podciągające linie do masy bądź zasilania
oraz trzeci włączający lub rozłączający układ od linii. 

Układ otwartego kolektora umożliwia ustawienie 2 stanów wyjściowych:
  * Logicznego 0 (potencjał masy, prąd wpływa do układu)
  * Wysokiej impedancji (high impedance; hiZ; 3rd state; floating ) (prąd ani nie wpływa ani nie wypływa z układu)

Często linie sterowane przez układ otwartego kolektora posiadają logikę odwrotną: stan aktywny jest sygnalizowany przez niskie napięcie. 
Aby linia pracowała poprawnie konieczne jest zastosowanie rezystorów podciągających (pull-up) tak aby stan linii był ustalony na napięcie wysokie, 
kiedy każde wyjście z podłączonych urządzeń jest w stanie wysokiej impedancji.

![alt](/projects/open_collector_2.svg)


Układ umożliwia:

* Sterowanie układami o innym napięciu niż napięcie układu

  ![alt](/projects/open_collector_3.svg)
* Podłączenie więcej niż jednego wyjścia (ale muszą one wszystkie być typu otwarty kolektor) do jednej linii. 

  ![alt](/projects/open_collector_4.svg)

Interfejsy pracujące z wyjściami typu open collector:
   * I2C
   * 1-Wire
   * SMBus 

Dodatkowo:

  * <http://www.interfacebus.com/IC_Open_Collector_Output_pins.html> (lista IC z OC + wzory na rezystory podciągające)

## Iloczyn galwaniczny

Inna nazwa to iloczyn montażowy lub w odniesieniu do logiki ujemnej sumą galwaniczną (wired AND; wired OR).
Jeżeli którykolwiek z wyjściowych tranzystorów jest aktywny, napięcie na wszystkich tranzystorach podpiętych pod tą samą linię jest niskie.

![alt](/projects/open_collector_5.svg)

* Sygnał przechodzi przez dwa bufory z wyjściami OC, połączenie przewodów (kropka) zastępuje bramkę AND \(Y=A \cdot B\)
* Sygnał przechodzi przez dwa inwertery z wyjściami OC, połączenie przewodów zastępuje brankę OR \(Z= \bar C \vee \bar D\)

## Źródła

* "Elektronika" Augustyn Chwaleba,Bogdan Moeschke,Grzegorz Płoszajski WSiP Warszawa 2008
