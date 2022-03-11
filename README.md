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
A programmable macropad with at least 5 buttons, or a knob. (other input methods can be programmed in later)
a SBC. My recommendation is one under $50, using ARM, without a power on button, 1GB of ram, and a 2 core CPU.

# SBC's

orange pi zero 2 (Amazon US): https://www.amazon.com/Orange-Pi-Open-Source-Android10-OPI/dp/B08M8VZ1B6/ref=sr_1_6?crid=29IH1OSGA0EW0&keywords=orange+pi+board&qid=1646913243&sprefix=orange+pi+board%2Caps%2C195&sr=8-6

# macro pads

Seems viable for both functions (knob and scroll wheel), useful for testing. (Amazon US): https://www.amazon.com/Mechanical-Keyboard-Multifunctional-Shortcut-Programmable/dp/B09V8H9SKV/ref=sr_1_81?crid=321D7MSCWX9A8&keywords=macro+pad+for+linux&qid=1647030267&sprefix=macro+pad+for+linux%2Caps%2C86&sr=8-81

just buttons, useable for a beta for testers (Amazon US): https://www.amazon.com/Koolertron-Mechanical-Keyboard-One-Handed-Programmable/dp/B0998QXB8F/ref=sr_1_101_sspa?crid=321D7MSCWX9A8&keywords=macro%2Bpad%2Bfor%2Blinux&qid=1647030655&sprefix=macro%2Bpad%2Bfor%2Blinux%2Caps%2C86&sr=8-101-spons&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFNQTFHSzNDQ0k4RUomZW5jcnlwdGVkSWQ9QTAzOTI2OTNPWFRHQVNWUTlTOTEmZW5jcnlwdGVkQWRJZD1BMDAwMzI0N0dHTDZHNk44MVJGWCZ3aWRnZXROYW1lPXNwX2J0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU&th=1
