# Manson HCS3202 controller

This script enables control of the Manson HCS3202 power supply for optogenetic applications.

## Dependencies

* python3

## Description

During my PhD I used an optogenetic transcription factor to induce light-dependent transcription. To do so, I used a self-built LED stand with in an incubator, to illuminate cells growing in well plates. To enable dynamic illumination patterns, I used a Raspberry Pi to control a Manson HCS3602 power supply driving the LEDs.  

Within my setup, the 6 blue LEDs supplied with 15.5V and 0.20A provided sufficient light to induce light-dependent transcription, while preventing phototoxicity. To further limit phototoxicity, I applied blue light for 5 seconds, every 30 seconds. 

## Usage

