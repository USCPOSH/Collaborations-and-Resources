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

# USC Netlist Sanitizer and Desanitizer

USC Netlist Sanitizer is an open-source tool for sanitizing the netlists of analog mixed-signal (AMS) circuits by removing all foundry-proprietary information. This allows AMS designers to accelerate innovation by open-sourcing their new designs to share with the wider community. Other designers can carry out further innovations by using the sanitized netlists in conjunction with a predictive or a foundry-proprietary PDK. To facilitate this, our team has also developed the USC Netlist Desanitizer, an open-source tool for adding to the netlist the foundry-proprietary information necessary for accurate simulation.

These versions of the sanitizer and desanitizer work with the SCS netlist format. These versions are still under development and not ready for production use.

If you have any questions, please contact us at:  [uscposh@ee.usc.edu](mailto:uscposh@ee.usc.edu)

# Installation

## 0. Install JAVA and Python 2.7

## 1. Netlist Parser Dependency

```bash

git clone https://github.com/USCPOSH/Sanitizer.git

cd Sanitizer/netlist-parser

make

```

*Rerun `make` command when the grammar `.g4` files are changed.

## 2. POSH Code

```bash

cd Sanitizer/posh

sudo pip install -r requirements-dev.txt

```

# User Guide

## Sanitizer

```bash

cd Sanitizer/posh/bin

python sanitizer [netlist.scs] [sanitizer.config]

```

### Sanitizer Configuration file

The sanitizer configuration file is created by the user to instruct the sanitizer which parameters are foundry-proprietary and hence must be removed from the circuit netlist. 

This configuration file must be created the first time a team uses the sanitizer for a particular technology. The file must include a complete list of device types in the technology and, for each device type, the list of parameters whose names (along with their values) are allowed to be included in the sanitized netlist file output by the sanitizer.

[Instructions for creating sanitizer configuration file](https://github.com/USCPOSH/Sanitizer/blob/master/posh/bin/v1_sanitizer_TSMC65nm.config)

## Desanitizer

```bash

cd Sanitizer/posh/bin

python desanitizer [netlist.scs] [desanitizer.config]

```

### Desanitizer Configuration file

The desanitizer configuration file is created by the user to instruct the desanitizer which foundry-protected parameters must be added to a sanitized circuit netlist to enable accurate simulations.

This configuration file must be created the first time a team uses the desanitizer for a particular technology. The file must include a complete list of device types in the technology and, for each device type, the list of parameters that must be added to the sanitized netlist. For each parameter to be added, the configuration file must also include a value or an algebraic expression  to compute its value. The algebraic expression must use only constants or names of parameters available in the sanitized netlist. 

[Instructions for creating desanitizer configuration file](https://github.com/USCPOSH/Sanitizer/blob/master/posh/bin/desanitizer_TSMC65NM.config)

# Developer Guide

## Steps to develop new feature in sanitizer:

1. Add grammar into parser/lexer:

```bash

netlist-parser/SpectreParser.g4

netlist-parser/SpectreLexer.g4

```

grammar examples for parser:

```bash

icstatement

: 'ic' paramList

;

```

2. Copy and Overwrite the function from

```bash

netlist-parser/build/netlist_parser/SpectreParserVisitor.py

```

into the class in

```bash

posh/src/posh/NetlistVisitor.py

```

Example:

```python

def visitIcStatement(self, ctx):

print('Overwritting here')

return self.visitChildren(ctx)

```

3. Recompile the project:

```bash

cd Sanitizer/netlist_parser

make

cd Sanitizer/posh

make

```

4. Test new feature in sanitizer

```bash

cd Sanitizer/posh/bin

python sanitizer input.scs user.config

```

# TODO

1. The `vector` statement

2. The `ic` statement with `vdd!`

# ANTLR Reference

Here are some helpful links for ANTLR(a powerful parser generator).

[ANTLR Home](https://www.antlr.org/)

[ANTLR Documentation](https://github.com/antlr/antlr4/blob/master/doc/index.md)

[ANTLR Examples](https://github.com/antlr/grammars-v4)

[ANTLR Python](https://github.com/antlr/antlr4/blob/master/doc/python-target.md)

[ANTLR Tutorial](https://tomassetti.me/antlr-mega-tutorial/)

