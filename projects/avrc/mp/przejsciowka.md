---
title: Przejsciówka
layout: "base.njk"
---

======= Wstęp ======
Doświadczenie pokazuje że podstawą są porządne narzędzia na których można polegać. Programator USBasp jest zakończony złączem Kanda, które jest bardzo wygodne w przypadku płytek ewaluacyjnych. Ponieważ będziemy korzystać z płytki stykowej musimy znaleźć sposób na połączenie programatora i układu. Najprostszym rozwiązaniem jest kombinowanie z przewodami pomiędzy złączem Kanda a płytką, jednak nie jest to rozwiązanie trwałe ani stabilne. Dlatego proponuje zbudowanie następującej przejściówki:\\
![alt](:warsztaty:przej_e.jpg|}}

Do jej zbudowania będziemy potrzebować:
  - Gniazda wanienkowego IDC10
  - 6 przewodów (z kolorowej taśmy, nie z skrętki)
  - 6 goldpinów oraz 6 gniazd goldpin zaciskanych na kabel (goldpin to popularna nazwa złącza szpilkowego raster((raster to po prostu rozstaw)) 2.54 [mm]((2.54 [mm] to 0.1 cala)))
  - Po jednej sztuce plastikowych obudów na gniazda goldpin: pojedyncze, podwójne i potrójne
  - Taśmy izolacyjnej
Narzędzia:
  - Nóż
  - Lutownica
  - Szczypce boczne
  - Szczypce płaskie
![alt](:warsztaty:przej_a.jpg|}}\\
\\
//Na każdym etapie prac warto sprawdzać jakość połączenia elektrycznego (np. miernikiem uniwersalnym z akustycznym testerem ciągłości obwodu) :!://

====== Krok 1 ======
Najtrudniejszy, musimy przymocować przewody do gniazda IDC. Po pierwsze trzeba zwrócić uwagę jak wyglądają wyprowadzenia w odbiciu lustrzanym. Przymocowanie przewodu do złego wyprowadzenia to spory problem.\\

![alt](:art001_kanda.png|}}\\

Przewody należy odsłonić na długości około 4 [mm], owinąć nóżki i przylutować ostrożnie (plastik się topi) do gniazda, połączenie musi być dobre elektrycznie i mechanicznie (oczywiście w rozsądnym zakresie). Zbyt długie grzanie (powyżej 2 sekund) może spowodować stopienie elementu i przemieszczenie pinów złącza. Przewody jakich używamy nie są przystosowane do lutowania, ich izolacja się przytopi (to nic, byle nie doprowadzić do sytuacji w której może dojść do zwarcia!). Podczas usuwania izolacji należy używać bardzo małej siły, żyły bardzo łatwo się przecinają. Jeżeli ktoś ma dostęp do ściągacza izolacji to polecam jego użycie do tego celu.\\
Proszę zwrócić uwagę na kolejność przewodów, ja niestety połączyłem źle i musiałem zamienić w obudowie parę przewodów! (konkretnie sck z mosi)! Przez co przewody nie układają się równo. Fajnie byłoby gdyby kolory przewodów były takie same jak zastosowałem ja. Szczególnie **masa powinna być czarna**, zaoszczędzi to problemów przy podłączaniu zasilania.\\

![alt](:warsztaty:isp_conn.png|}}\\

![alt](:warsztaty:przej_b.jpg|}}\\

Szary przewód to linia RST.\\

![alt](:warsztaty:przej_c.jpg|}}\\

//**Uwaga! Na zdjęciu powyżej jest błąd, przewody niebieski i fioletowy powinny być zamocowane odwrotnie.**//
Początkowo miałem zamiar połączenie wykonać za pomocą laminatu, tj. pomiędzy rzędy gniazda włożyć małą płytkę laminatu dwustronnego o grubości 1,5 mm, przewody i złącze przylutować właśnie do niego. Nie zrobiłem tego ze względu na to że nie wszyscy mają w domu zapasy laminatu dwustronnego.

====== Krok 2 ======
Teraz należy zabezpieczyć przymocowane przewody za pomocą taśmy izolacyjnej. Na początku proponuje owinąć wiązkę przewodów przy samym gnieździe a następnie owijać cały obszar pod złączem w aż "obudowa" będzie zakrywać całą powierzchnię i będzie (stosunkowo) wytrzymała mechanicznie. Od tego kroku zależy wytrzymałość całej przejściówki!\\

![alt](:warsztaty:przej_d.jpg|}}\\

Początkowo planowałem zalanie obszaru mocowania przewodów za pomocą jakiejś żywicy lub silikonu jednak jest z tym sporo roboty.

====== Krok 3 ======

![alt](:warsztaty:img_20110213_214849.jpg}}

  * Przewody należy wyrównać oraz przygotować do mocowania tj. odsłonić na długość około 4 [mm] oraz zagiąć do izolacji (w taki sposób będzie najlepszy docisk). 
  * Zaciskane złącza (BLS, te blaszki na 2 zdjęciu) mają "dół" w miejscu gdzie łączą się z goldpinami (część zamknięta) a "górę" tam gdzie łączy się kabel (wystające blaszki, trójkątne na samej górze). 
  * Aby połączyć solidnie złącze z goldpinem należy: włożyć goldpin na długość jak na zdjęciu poniżej (najlepiej jeszcze z plastikiem żeby było równo), następnie podgrzać całość lutownicą (mały element, szybko nagrzeje się zarówno złącze jak i goldpin) i wprowadzić spoiwo od "góry" w miejscu gdzie kończy się otwarta część złącza. Należy użyć takiej ilości cyny aby goldpin był solidnie zamocowany w złączu (nie trzeba jej dużo), za duża ilość cyny spowoduje problemy z włożeniem złącza do obudowy.
  * Na koniec usuwamy plastikową część z goldpina, nie jest już do niczego potrzebna.

![alt](:warsztaty:przej_x.jpg}}

====== Krok 4 ======
Tak przygotowane złącza zaciskamy z przewodami. Złącze od "góry" posiada 2 pary blaszek: "trójkątną" oraz "mniejszą". Część przewodu z wystającymi żyłami wkładamy tak aby przewody dotykały blaszki "mniejszej" i zaciskamy dosyć mocno (ale bez przesady żeby nie powyginać złącza). Blaszki trójkątne zaciskamy na izolacji przewodu. Na koniec umieszczamy obudowy na wyprowadzeniach. Gotowe.

