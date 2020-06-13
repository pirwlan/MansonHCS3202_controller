# Manson HCS3202 controller

This script enables control of the Manson HCS3202 power supply for dynamic activation/deactivation.

## Dependencies

* python3
* pyserial (pip install pyserial, not serial)

## Description

During my PhD I used an optogenetic transcription factor to induce light-dependent transcription. To do so, I used a self-built LED stand within an incubator, to illuminate cells growing in well plates. To enable dynamic illumination patterns, I used a Raspberry Pi to control a Manson HCS3602 power supply driving the LEDs. However, the script can be used for any purpose requiring dynamic control of a power supply. 

Within my setup, the 6 blue LEDs supplied with 15.5V and 0.20A provided sufficient light to induce light-dependent transcription, while preventing phototoxicity. To further limit phototoxicity, I applied blue light for 5 seconds, every 30 seconds. For the majority of photoreceptors, a short illumination period is sufficient for transition to the lit state, while limiting light exposure. 



## Usage

This script establishes an USB connection between the Raspberry Pi and the power supply. Thus, the power supply has to be switch on and connected to the Raspberry Pi before the script is started. Voltage and current settings should be fine-tuned to the given photoreceptor and the experimental set up.

The script will start an illumination scheme with blue light illumination for 5 seconds every 30 seconds for 1 hour, followed by an 1 hour dark phase. The timings and settings can easily be adjusted. 

A simple, adaptable logging function keeps track of the experiment.

#### Be careful to not use too much Voltage/Amp, this might break your equipment. 
