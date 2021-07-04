# FinalCutProController-RPico
<h2>Macro pad for FCPX using a Raspberry Pi Pico and running KMK</h2>

This project uses KMK (https://github.com/KMKfw/kmk_firmware)...specifically the modular variety available on 7.4.21.

To load the firmware, copy boot.py, kb.py, main.py and kmk (the whole folder) to you Rasberry Pi Pico (which should already be running Circuitpython).

<h2>KMK (folder)</h2>
the kmk folder contains the files needed to run kmk.  the version bundled with this project is known to work.  kmk changes from time to time, updates may break this project.

<h2>BOOT.PY</h2>
Boot information, no need to make edits.

<h2>KB.PY</h2>
kb.py contains the colum/row pin definitions and diode orientation information.  If you are using the provided gerbers, you won't need to change this file (read: changes will break the device).

If you are drafting new schematics, you'll need to edit kb.py with your specific column and row pin info (and double check diode oritentation)

<h2>MAIN.PY</h2>
main.py contains the "juice" of the controller.  edit the custom key, encoder and layers definitions as needed.

<u>custom key definitions:</u> define your own custom keys using the same method as declaring a variable.
<p><i> custom key = key code (or key code chain) </i></p>


