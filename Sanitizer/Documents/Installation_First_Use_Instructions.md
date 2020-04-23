# SANITIZER TOOLS README - Installation and First Use Instructions

This is a simple README instructing how to set up *sanitizer* and *desanitizer* configuration files and use **USC's Lossless Sanitizer and Desanitizer**, which enable sharing of netlists of analog mixed-signal (AMS) circuits without multi-way NDAs with foundries.  

### REQUISITES

1. YAML (for both python 2.7 and python 3.x)
```bash
pip install pyYAML

pip3 install pyYAML
```
## Find all devices in a PDK - NOTE: only needs to be done once per PDK

1. Move `sanitizer_tools.il` file into your cadence workarea

2. Load up Virtuoso Cadence `virtuoso &`

3. In the Cadence .cds console, use command `load("sanitizer_tools.il")` and hit return

4. Then, run command `printCDF("<pdk_name_here>")` e.g (`printCDF("tsmcN65")`) in the Cadence .cds console, and hit return

This will produce file `devices.txt`, which will be cleaned up and used in the following script, please move this file to `Sanitizer/posh/bin`



## Sanitizer/Desanitizer BASH scripts

Run the bash script 
```bash
bash sanitizer.sh <netlist_name>.scs 
```
or 
```bash
bash desanitizer.sh <netlist_name>.scs
```
The bash script will do the following three things:

1. Run the [netlist_scraper.py]() which will produce the netlist.yaml file for further use

2. Run the backend.py, which will save all device information and configuration in `master.yaml`

please read the **Backend** section for further instructions and clarification

3. Run sanitizer/desanitizer, and produce your desired sanitized or desanitized netlist called `netlist_sanitized.scs` or `netlist_desanitized.scs`

## Backend

New devices will be recognized in netlist: follow GUI steps and configure devices correctly, and produce the config files by following the steps below.

Sanitizer configuration files update:

1. Move the files `config.txt` and `netlist_skill.il` to your cadence workarea environment

2. Return to Virtuoso Cadence

3. Open a new/blank schematic

4. Open the device adder, default hotkey "i"

5. In console, use command `load("netlist_skill.il")`

6. Then, run command `find_EQ()`. This will update the sanitizer.config and desanitizer.config with the new devices

8. Copy these files (both sanitizer.config and desanitizer.config) back to `Sanitizer/posh/bin`.

9. Return to the bash console, and hit Enter to continue.

Sanitizer/desanitizer will then run and create your desired sanitized or desanitized netlist called `netlist_sanitized.scs` or `netlist_desanitized.scs`

##
If you have any questions, please contact us at:  [uscposh@ee.usc.edu](mailto:uscposh@ee.usc.edu)
