---
title: STM32F4 - using SWV (serial wire viewer)
layout: "base.njk"
---

## STM32F4 - using SWV (serial wire viewer)
I am using Atollic TrueSTUDIO for ARM Lite and STMicroelectronics STM32F4Discovery board.
  * [Atollic® TrueSTUDIO®](https://www.st.com/en/development-tools/truestudio.html)
  * [STM32F4DISCOVERY](http://www.st.com/internet/evalboard/product/252419.jsp)

## Using Serial Wire Viewer (SWV)
To use this debugging interface it must be first enabled under active debug configutarion.

![alt](/lib/stm32/screenshotenableswv.png)

Now characters can be transmitted through ST-LINK2 without external serial adapter!

```
  ITM_SendChar('t');
  ITM_SendChar('e');
  ITM_SendChar('s');
  ITM_SendChar('t');
```

To receive data:

* Show SWV Console (Under Debug perspective use __View__->__SWV Console__)
* Under __Serial Wire Viewer settings__ dialog enable __ITM Stimulus Port__ number 0
* Enable __Start/Stop Trace__ button

![alt](/lib/stm32/screenshotswvconsole.png)

User can implement it's own `printf` function using `ITM_SendChar`.
