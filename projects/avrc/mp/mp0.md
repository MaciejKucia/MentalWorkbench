---
title: Zamek szyfrowy z tarczą telefoniczną
layout: "base.njk"
---

## Zamek szyfrowy z tarczą telefoniczną

Projekt ten ma na celu pokazanie jak powinno się realizować mały projekt.

## Założenia

Bardzo ważna jeżeli nie najważniejsza część, zauważyłem że bardzo często wręcz pomijana przez kolegów. Jak można pracować nie wiedząc o się chce zrobić? W założeniach powinny się znaleźć:

  * Cel
  * Wymagania
  * Dostępne środki (koszty i czas)

Wypisując założenia warto zaczynać od najważniejszych zagadnień. Planując projekt trzeba pamiętać o własnych umiejętnościach, dostępnych narzędziach i zasobach. Urządzenie które chcemy zrealizować musi mieć wstępną specyfikację, im dokładniejsza tym lepiej. Budując urządzenie należy przestrzegać technicznej zasady: jak najlepiej jak najmniejszym kosztem (optymalnie).

W moim przypadku założenia wyglądają tak:

 Projekt zamka szyfrowego
  * Chcę zrealizować zamek szyfrowy
  * Wprowadzanie kombinacji jest realizowane za pomocą tarczy telefonicznej
  * Urządzenie powinno posiadać wyświetlacz
  * Koszty: żadne: wykorzystanie dostępnych części, budowa na płytce prototypowej
  * Czas wykonania: 2 dni
  * Funkcja edukacyjna

## Projektowanie

Kiedy już wiadomo co się chce zrobić trzeba zastanowić się jak to zrobić. 

### Wyświetlacz

Informacja o stanie w jakim znajduje się urządzenie będzie przekazywana za pomocą prostego wyświetlacza [[integra:elem#Wyświetlacze_7_segmentowe|7 segmentowego]]. Ponieważ będzie to zamek zastosuje również dwukolorową diodę (czerwony/zielony). Pierwszym krokiem jest wysterowanie wyświetlaczem. Ponieważ sterowanie takim wyświetlaczem jest bardzo proste, wyprowadzenia odpowiednich segmentów podłączyłem w sposób zupełnie losowy do portu C. Następnie na mikrokontrolerze uruchomiłem prosty program ustawiający po kolei wszystkie piny portu C co 1 sekundę. Na papierze narysowałem schemat wyświetlacza i obliczyłem kombinacje liczb dla wszystkich potrzebnych znaków ( 0,1,2,3,4,5,6,7,8,9, ,-,=, <animacja obrotu>).

```
// Tablica znaków 7 seg
const char chartab[] = {252,144,234,186,150,
			62,126,152,254,190,
			0,
			2,114,
			8,128+8,16+8+128,32+8+16+128,64+32+8+16+128,4+64+32+8+16+128};
```
			
W ostatniej linijce tablicy widać jak zostały utworzone kolejne znaki: poprzez dodawanie liczb odpowiadających konkretnym segmentom. Powyższy kod jest poprawny tylko dla pewnej **nieokreślonej** konfiguracji połączeń, każdy musi stożyć tablicę odpowiadającą jego połączeniom. Uprościłem również sposób ograniczania prądu diod w wyświetlaczu, rezystory ograniczające prąd są wpięte pomiędzy katody a masę. Rozwiązanie takie powoduje zmianę jasności segmentów w zależności od tego ile ich jest używanych równocześnie.

## Tarcza

Tarcze telefoniczną dostałem od kolegi. Posiada ona 3 wyprowadzenia. Po odkręceniu tylnej obudowy ukazał się skomplikowany układ mechaniczny. Jeden z przewodów był przewodem wspólnym dla 2 styków. Tarcza generuje 2 sygnały:
  * Impulsy wybieranego numeru
  * Ciągły sygnał aktywny w momencie obracania się tarczy

Początkowo planowałem wykorzystanie obu sygnałów, jednak zrezygnowałem z drogiego ponieważ same impulsy wystarczą do poprawnego odczytu stanu tarczy. Elektrycznie przewód wspólny jest podłączony do dodatniej szyny zasilania natomiast przewód sygnału impulsów jest podciągnięty pod masę przez rezystor 10k. Zastosowałem również kondensator 100nF podłączony pomiędzy linią sygnału a masą w celu debouncingu styków tarczy.

## Stany

Następnym krokiem jest zaprojektowanie zachowania programu, rozrysowałem stany w jakich może się znajdować program.\\

:pl:avrc:art:tarcza_stany.png?400|\\

Urządzenie po resecie i inicjalizacji peryferiów wchodzi do punktu Reset gdzie są zerowane wszystkie znaczące zmienne, wyświetlacz i dioda. Następnie urządzenie może znajdować się w stanach:
  * Idle: stan bezczynności - na wyświetlaczu miga znak zachęty.
  * Rotating - występuje w momencie obracania się tarczy, na wyświetlaczu pojawia się zliczana liczba
  * Locked - po zliczeniu implulsów liczba zostaje wczytana
  * Ridle - bezczynność ale z oczekiwaniem na kolejne cyfry kombinacji
  * Locked pattern - wszystkie cyfry kombinacji zostały wprowadzone
  * Fail - cyfry kombinacji nie zgadzają się z zaszytym wzorem
  * Success - cyfry kombinacji zgadzają się z wzorem

Schemat pozwala zaplanować logiczne przejścia i możliwe stany urządzenia. 

## Schemat ideowy

:pl:avrc:art:tarcza_zamek.png?nolink&800|\\

Na schemacie nie zaznaczyłem kondensatorów na szynie zasilania.

## Program

```
#include "avr/interrupt.h"
#include "util/delay.h"
#include "avr/io.h"

//PORTY
#define DISPP 	PORTC
#define DISPD 	DDRC
#define LED_DIR DDRD
#define LED 	PORTD

#define forever for(;;)

// Tablica znaków 7 seg
const char chartab[] = { 252, 144, 234, 186, 150, 62, 126, 152, 254, 190, 0, 2,
		114, 8, 128 + 8, 16 + 8 + 128, 32 + 8 + 16 + 128, 64 + 32 + 8 + 16
				+ 128, 4 + 64 + 32 + 8 + 16 + 128 };

//STAN
enum STATUS {
	st_reset,
	st_idle,
	st_ridle,
	st_rotating,
	st_locked,
	st_lockpattern,
	st_fail,
	st_success
};
volatile enum STATUS status = st_reset;

//GLOBALS
const uint8_t codetab[6] = { 1, 2, 3, 4, 5, 6 };
volatile uint8_t counter = 0;
uint8_t numpos = 0;
uint8_t numtab[6];

//TIMER
volatile uint8_t divider = 0;
volatile uint8_t blinker = 0;
volatile uint8_t timeout = 0;
//Przerwanie timera
ISR(TIMER1_COMPA_vect)
{
	if (divider++ == 10) 
	{
		blinker ^= 1;
		divider = 0;
	}

	if (timeout < 0xFF)
		timeout++;
}

//INT
//Przerwanie zewnętrzne INT1
ISR (SIG_INTERRUPT1)
{
	//Tylko w tych 3 stanach sygnał z tarczy jest oczekiwany
	if ((status == st_rotating) || (status == st_idle) || (status == st_ridle)) 
	{
		status = st_rotating;
		timeout = 0; // resetujemy
		counter++; // zliczamy impulsy
	}
}

int main() 
{
	int i;

	//IO Settings
	LED_DIR = (1 << 5) | (1 << 6);
	LED = 0;
	DISPD = 0xFF;

	//Ustawiamy timer
	TCCR1B |= (1 << WGM12); // Timer1 w trybie CTC
	TIMSK |= (1 << OCIE1A); // Włączam przerwanie CTC
	OCR1A = 868;            // Ustawiam wartość do porównania
	TCCR1B |= ((1 << CS10) | (1 << CS12)); // Ustawiam preskaler Fcpu/1024

	//Tylko zbocze rosnące aktywuje INT1
	MCUCR |= (1 << ISC11) | (1 << ISC10);

	//Aktywacja przerwań
	sei();

	//Main loop
	forever 
	{
		switch (status) 
		{
		case st_reset:
			//kasujemy
			timeout = 0;
			counter = 0;
			numpos = 0;
			LED &= ~((1 << 5) | (1 << 6));
			//aktywuje przerwanie INT1
			GICR |= (1 << INT1);
			status = st_idle;
			break;

		case st_idle:
			//nic sie nie dzieje

			//prompt
			DISPP = chartab[11 - ((blinker ? 1 : 0))];

			//tutaj można dopisać jakis kod do uspienia MCU dla oszczednosci energii
			//
			break;

		case st_rotating:
			// impulsy sa teraz zliczane przez przerwanie

			//wyswietlam liczbe  (modulo bo zawijam do 0)
			DISPP = chartab[counter % 10];

			//nowych impulsow dawno nie bylo wiec numer jest wczytywany
			if (timeout > 10)
				status = st_locked;
			break;

		case st_locked:
			//numer wpisany
			numtab[numpos++] = counter;
			counter = 0;
			timeout = 0;

			//keeping number for a while
			_delay_ms(150);

			//Czy to juz wszystkie cyfry?
			if (numpos >= 6)
				status = st_lockpattern;
			else
				status = st_ridle;

			break;

		case st_ridle:
			//oczekiwanie na kolejna liczbe

			//Po pewnym czasie wyswietlacz zaczyna migać sygnalizujac uplywajacy czas
			if ((timeout > 50) && (divider % 5))
				LED |= (1 << 5);
			else
				LED &= ~(1 << 5);

			//Wyswietlam ile cyfr wpisano
			DISPP = chartab[12 + numpos];

			//jezeli za dlugo nie wpisujemy kodu to resetujemy wszystko
			if (timeout > 100)
				status = st_reset;
			break;

		case st_lockpattern:
			//kod wpisany

			//czyszcze wyswietlacz blokuje INT
			GICR &= ~(1 << INT1);

			_delay_ms(150);

			status = st_success;
			//sprawdzam
			for (i = 0; i < 6; i++)
				if (numtab[i] != codetab[i]) 
				{
					status = st_fail;
					break;
				}
			break;
			DISPP = 0;

		case st_fail:
			//porazka

			//migam szybko czerwona dioda
			if (divider % 5)
				LED |= (1 << 5);
			else
				LED &= ~(1 << 5);

			if (timeout > 50)
				status = st_reset;

			break;

		case st_success:
			//sukces

			//migam zielona dioda
			if (blinker == 0)
				LED |= (1 << 6);
			else
				LED &= ~(1 << 6);

			//tutaj mozna zalaczyc jakis przekaznik otwierajacy np drzwi
			//

			//otwarcie zamka trwa tylko chwile
			if (timeout > 100)
				status = st_reset;
			break;

		}
	}
}
```

## Upgrade

W projekcie można by zmienić kilka rzeczy. Po pierwsze zamek nie otwiera niczego, w kodzie jest komentarz w którym momencie można włączyć np. przekaźnik. Ponieważ zawieszenie się programu (które może zostać spowodowane np. zakłóceniami) spowodowałoby odcięcie możliwości otwarcia zatrzasku sterowanego przez ten zamek szyfrowy dobrym pomysłem byłoby zaimplementowanie [[integra:warsztaty:w0b#Watchdog|watchdoga]]. Porogram nie jest optymalny, niektóre zmienne można zupełnie wyeliminować (czy zauważysz które?). 
