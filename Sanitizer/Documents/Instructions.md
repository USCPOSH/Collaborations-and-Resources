
# SANITIZER TOOLS README - Continued/Subsequent Use Instructions

This is a simple README instructing how to set up *sanitizer* and *desanitizer* configuration files and use **USC's Lossless Sanitizer and Desanitizer**, which enable sharing of netlists of analog mixed-signal (AMS) circuits without multi-way NDAs with foundries.  

### REQUISITES

1. YAML (for both python 2.7 and python 3.x)
```bash
pip install pyYAML

pip3 install pyYAML
```

## Sanitizer/Desanitizer BASH scripts

Run the bash script 
```bash
bash sanitizer.sh <nelist_name>.scs
```
 or
  ```bash
  bash desanitizer.sh <netlist_name>.scs
  ```

The bash script will do the following three things:

1. Run the [netlist_scraper.py]() which will produce the netlist.yaml file for further use.

2. Run the backend.py, which will save the list of all devices in the PDK in 'master.yaml'. Also, for each device, it will save the names of all its parameters classified into two categories, namely user-defined parameters (UDP) or PDK-defined parameterr (PDP), in 'master.yaml'.

Please read the **Backend** section for further instructions and clarification.

3. Run sanitizer/desanitizer, and produce your desired sanitized or desanitized netlist called '<netlist_name>_sanitized.scs' or '<netlist_name>_desanitized.scs'

## Backend

### 1. If no new devices are found in netlist:

Sanitizer.config and desanitizer.config will both cleared for use, and sanitizer/desanitizer will run.

This which will produce your desired sanitized or desanitized netlist called '<netlist_name>_sanitized.scs' or '<netlist_name>_desanitized.scs', if your input netlist file was called '<netlist_name>.scs'

### 2. If new devices are found in netlist

Follow the steps listed by the user-interface and make sure that the parameters of devices are in the correct category, namely either user-defined parameter (UDP) or PDK-defined parameter (PDP). Then continue with following the steps below.

Update Sanitizer/desanitizer configuration files:

1. Move the files 'config.txt' and 'netlist_skill.il' to your cadence workarea 
2. Return to Virtuoso Cadence

3. Open a new/blank schematic

4. Open the device adder, default hotkey "i"

5. In console, use command 'load("netlist_skill.il")'

6. Then, run command 'find_EQ()'. This will update the files sanitizer.config and desanitizer.config with the new devices

8. Copy both these files, namely sanitizer.config and desanitizer.config, to Sanitizer/posh/bin

9. Return to the bash console, and hit enter to continue

Sanitizer/desanitizer will then run and create your desired sanitized or desanitized netlist called '<netlist_name>_sanitized.scs' or '<netlist_name>_desanitized.scs'

##
If you have any questions, please contact us at:  [uscposh@ee.usc.edu](mailto:uscposh@ee.usc.edu)