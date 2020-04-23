
Copyright 2020

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
git clone https://github.com/USCPOSH/Collaborations-and-Resources.git

cd Collaborations-and-Resources/Sanitizer/netlist-parser

make
```

*Rerun `make` command once the grammar `.g4` files are modified.

## 2. POSH Code

Within the `Sanitizer` folder, run:
```bash
cd posh

sudo pip install -r requirements-dev.txt
```

# User Guide

## First Time Use and Installation
If you are installing Sanitizer, or if you are using Sanitizer on a new PDK, please [click here](https://github.com/USCPOSH/Sanitizer/blob/master/posh/bin/Installation_First_Use_Instructions.md) for installation or first use instructions

## Subsequent/Continued Use Instructions
 If you are using Sanitizer for an already established PDK, then please [click here](https://github.com/USCPOSH/Sanitizer/blob/master/posh/bin/Instructions.md) for User Instructions.
 
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

