# octo-klipper-screen
a display plugin for octoprint and klipper. This is a work in progress, that's no where near finished. That and my knowledge is limited.

# why this? Isn't there display plugins already?
yes, but they only work with touch screens to my knowledge, and with ARM boards at least, the Pi. Those boards are in high demand and are currently overpriced in the US. $100+ for a 4b, or even a 3b. This is meant for boards other than the Pi.

# how can I help?
Fix and add issues as needed, and have some examples for me if you're giving me pointers. I work best off of those.

What I need done rn:

startup screen switching to the main screen
add #standwithukraine to the startup screen
the menu for doing things with the printer via octoprint

# what sets this apart?

My plan is to make the menu accessable to those who are sight impaired and/or colorblind. So finding a text to speech API that works on the Pi and windows, as I test and develop on windows, without a cloud server being needed.

the customization is rather immese here, each icon is meant to be redrawn via vector graphics.

# what hardware is needed?
A screen with a 480x800 res minimum
A programmable macropad with at least 5 buttons, preffably in a cross.
a SBC. My recommendation is one under $50, using ARM, without a power on button, 1GB of ram, and a 2 core CPU.

# SBC's

orange pi zero 2 (US amazon): https://www.amazon.com/Orange-Pi-Open-Source-Android10-OPI/dp/B08M8VZ1B6/ref=sr_1_6?crid=29IH1OSGA0EW0&keywords=orange+pi+board&qid=1646913243&sprefix=orange+pi+board%2Caps%2C195&sr=8-6
