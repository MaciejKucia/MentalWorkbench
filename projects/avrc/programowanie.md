---
title: Programowanie AVR
layout: "base.njk"
---

## Na czym polega programowanie?

Programowanie polega na zapisywaniu zawartości pamięci FLASH (programu) lub EEPROM (danych nieulotnych).

## Jak najprościej zaprogramować uC AVR?

Istnieje kilka sposobów programowania układów AVR, najprostszy to programowanie za pomocą ISP(In System Programming - Programowanie w systemie).

## Jak programować za pomocą ISP?

Aby programować za pomocą ISP potrzebujemy interfejsu pomiędzy komputerem a układem docelowym - programatora. Obecnie najpopularniejszym programatorem dla hobbistów jest [USBasp](http://www.fischl.de/usbasp/).

## Mam już działający programator co teraz?

Programator trzeba połączyć z układem docelowym. Standardowym złączem programatora jest złącze Kanda i takie znajduje się na programatorze.

![alt](/projects/avrc/media/isp_conn.png)

Czyli VCC z VCC, GND z GND, RST z RST, itd. Proste.

Załóżmy że pracujemy z uniwersalną płytką stykową. Potrzebujemy sposobu na elektryczne połączenie programatora z układem. Istnieje wiele rozwiązań, praktycznie każdy ma swoje (wystarczy popatrzeć np na Google Images Search). Przykładowe rozwiązania to:

  * Bezpośrednie połączenie pomiędzy wtyczką a układem za pomocą kabelków powtykanych w tyczkę. (Najprostrze)
  * Wykonanie przejściówki tak jak to zaproponowałem (Wymaga pewnych umiejętności manualnych)
  * Chyba najlepsze rozwiązanie, wykonanie takiego przewodu:

![alt](/projects/avrc/media/kabel_adv.jpg)

## Co z zasilaniem?
Czasami zasilanie układu docelowego (jeszcze nie wiem dlaczego) nie działa poprawnie (jest ale układu nie da się zaprogramować). W takim przypadku podczas programowania konieczne jest zasilanie zewnętrzne (koniecznie stabilizowane 5V). Zasilanie z USB można włączyć aktywując zworkę nr1 w "programatorze Integry". W moim przypadku zasilanie z USB działa z netbookiem marki HP i nie działa z laptopem marki Compal.

## Uwagi
Podłączenie programatora nie zakłóci pracy urządzenia (wysoka impedancja na złączu programatora) ale obecność czegokolwiek na pinach MOSI MISO SCK może zakłócić proces programowania, na czas programowania należy odłączyć wszystko co jest podpięte pod te złącza.
