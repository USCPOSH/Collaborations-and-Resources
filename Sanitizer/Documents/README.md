Copyright [2019]

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.


# Development

## Netlist Parser Dependency

```bash
git clone https://github.com/USCPOSH/Sanitizer.git

cd Sanitizer/netlist-parser

make
```

Rerun `make` command when the grammar `.g4` files are changed.


## USC Netlist Sanitizer Code

```bash
cd Sanitizer/posh

sudo pip install -r requirements-dev.txt
```

# USC Netlist Sanitizer
USC Netlist Sanitizer is an open-source tool for sanitizing the netlists of analog mixed-signal (AMS) circuits by removing all foundry-proprietary information. This allows AMS designers to accelerate innovation by open-sourcing their new designs to share with the wider community. Other designers can use the sanitized netlists in conjunction with a predictive or a foundry-proprietary PDK. USC team is developing a de-sanitizer to facilitate this.

This version of the sanitizer works with SCS netlist format. Since our team could not find an open-source parser for SCS format, we have built this sanitizer using an open-source parser generator ANTLR (ANother Tool for Language Recognition) and writing the grammar for SCS. This allows us the flexibility for updating the grammar for SCS. More importantly, this also allows the sanitizer to be adapted for other netlist formats (e.g., SPICE). 

The key steps for using the USC Netlist Sanitizer:

1. The sanitizer is available in the following GitHub repository. If you wish to modify the grammar (for SCS or to support another netlist format), or modify the sanitizer code in any other way, a makefile is provided for recompilation.
[https://github.com/USCPOSH/Sanitizer](https://github.com/USCPOSH/Sanitizer)


2. Before you run the USC Netlist Sanitizer the first time, please review and **update** the configuration file. This configuration file is used by the sanitizer to decide what information in the original netlist it keeps, what it removes, and what it modifies. The instructions on how to update, as well as several precautions that you should take, are provided at the top of the default configuration file.

```bash
   USCPOSH/Sanitizer/posh/bin/v1_sanitizer_TSMC65nm.config
   USCPOSH/Sanitizer/posh/bin/v2_sanitizer_TSMC65nm.config	
```

 
3. To run the sanitizer simply type the following command. 
```bash
./sanitizer <netlist file> <config file>
```
4. ***Important***: Please carefully review the netlist file output by the sanitizer to double-check that it does not include any proprietary information. (If it does, further update the configuration file and repeat until the output netlist file is free of proprietary information.)

5. If you have any questions, please contact us at: uscposh@ee.usc.edu

