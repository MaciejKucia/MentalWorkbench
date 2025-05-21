---
title: Printed circuit boards
layout: "base.njk"
---

## Printed circuit boards

## PCB Design

General tips:

* Ordered List Item Up to 1 GHz you can still use normal FR4 PCB. (I used this with good results up to around 1.6Ghz for GPS amplifiers) Don't use the 64mil thickness, go for 32mil or so.
* Short tracks. Use the correct width to match 50Ohm, mitered corners etc.
* Good groundplane's
* Plenty of vias, especially the ones next to microstrip lines.
* Don't use groundplane under osc tank circuits. (Variation in temp can cause capacitance to vary)
* Follow application layout guidelines where possible.
* Keep coils/inductors at right angles to each other when they are closely spaced.
* When crossing tracks, on layers, cross at right angles for minimum interference between them
* Thin long tracks radiate, short thick ones less so.
* Keep tracks away from each other by at least 1.5 times the thickness of your pcb for minimal coupling.

Despite these conclusions, there are a few simple reasons to continue to avoid 90° angles:

* There is a higher possibility of an acid-trap forming during etching on the inside of the angle (especially in acute angles). An acid trap causes over-etching which can be a yield issue in PCBs with small trace widths.
* Routing at 45° typically reduces overall trace length. This practice frees board area, reduces current loops, and improves both EMC emissions and immunity.
* It looks better. This consideration is an important factor for anyone who appreciates the art of PCB layout.

## PCB fabs

| Name | Country |
| --- | --- |
| <http://www.faldruk.pl/> | Poland |
| <http://www.prototypy.com.pl/> | Poland |
| <http://www.pragoboard.cz/>| Czech Republic |
| <http://www.eurocircuits.com/> | Belgium |
| <https://www.pcbway.com/> | China |
| PCBPOOL | Germany |
| PCBCART | China |

## Laminates

|  IPC Number | Thickness [inch] | Thickness [mm] |
| --- | --- | --- |
| L1 | 0.002 | 0.05 |
| L2 | 0.004 | 0.10 |
| L3 | 0.006 | 0.15 |
| L4 | 0.008 | 0.20 |
| L5 | 0.010 | 0.25 |
| L6 | 0.012 | 0.30 |
| L7 | 0.016 | 0.40 |
| L8 | 0.020 | 0.50 |
| L9 | 0.028 | 0.70 |
| L10 | 0.035 | 0.90 |
| L11 | 0.043 | 1.10 |
| L12 | 0.055 | 1.40 |
| L13 | 0.059 | 1.50 |
| L14 | 0.075 | 1.90 |
| L15 | 0.090 | 2.30 |
| L16 | 0.122 | 3.10 |

<table class="inline">
	<thead>
	<tr class="row0">
		<th class="col0">Material </th><th class="col1"> Symbol </th>
	</tr>
	</thead>
	<tbody><tr class="row1">
		<td class="col0 centeralign" rowspan="2">  Teflon  </td><td class="col1 centeralign">  FR-1  </td>
	</tr>
	<tr class="row2">
		<td class="col0 centeralign">  FR-4  </td>
	</tr>
	<tr class="row3">
		<td class="col0 centeralign">  phenolic cotton paper  </td><td class="col1 centeralign">  FR-2  </td>
	</tr>
	<tr class="row4">
		<td class="col0 centeralign">  cotton paper and epoxy  </td><td class="col1 centeralign">  FR-3  </td>
	</tr>
	<tr class="row5">
		<td class="col0 centeralign" rowspan="2">  <strong>glass and epoxy</strong>  </td><td class="col1 centeralign">  <a href="https://en.wikipedia.org/wiki/FR-4">FR-4</a>  </td>
	</tr>
	<tr class="row6">
		<td class="col0 centeralign">  FR-5  </td>
	</tr>
	<tr class="row7">
		<td class="col0 centeralign">  glass and polyester  </td><td class="col1 centeralign">  FR-6  </td>
	</tr>
</tbody></table>

_Note: FR → flame retardant_

Parameters:

* Fire retardance
* Dielectric constant
* Loss factor
* Tensile strength
* Shear strength
* Glass tensition temperature
* Expansion coefficient

## Cordwood

![http://en.wikipedia.org/wiki/File:Cordwoodcircuit.agr.jpg](/lib/800px-cordwoodcircuit.agr.jpg)

## Voronoi PCB

## References

* [SZZA009 - PCB Design Guidelines For Reduced EMI, Texas Instruments November 1999](http://www.ti.com/lit/an/szza009/szza009.pdf)
* [PCB design and layout guidelines - Radio-Electronics.com](http://www.radio-electronics.com/info/electronics-design/pcb/pcb-design-layout-guidelines.php)
* [Analog.com - PRINTED CIRCUIT BOARD (PCB) DESIGN ISSUES](http://www.analog.com/library/analogdialogue/archives/43-09/EDch%2012%20pc%20issues.pdf)
