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

# NOTE

USC Netlist Sanitizer is an open-source tool for sanitizing the netlists of analog mixed-signal (AMS) circuits by removing all foundry-proprietary information. This allows AMS designers to accelerate innovation by open-sourcing their new designs to share with the wider community. Other designers can use the sanitized netlists in conjunction with a predictive or a foundry-proprietary PDK. USC team is developing a de-sanitizer to facilitate this.

This version of the sanitizer works with SCS netlist format. It is still under development and not ready for production use.

If you have any questions, please contact us at:  [uscposh@ee.usc.edu](mailto:uscposh@ee.usc.edu)

# Development

```bash
git clone

cd sanitizer/netlist-parser

make
```

# Contributing

## Report Issues

## Submit Pull Requests


# TODOS

1. Add steps to deploy to PyPi when this repo is made public.

1. Currently, Netlist Parser does not support all netlist specification.
    * Spice simluation language is not supported.
    * The `check` control statement is not *fully* supported.
    * The `ic` control statement is not *fully* supported.
    * The `info` control statement is not *fully* supported.
    * The `options` control statement is not *fully* supported.
    * The `paramset` control statement is not *fully* supported.
    * The `statistics` block is not *fully* supported.
    * The `nodeset` control statement is *not* supported.
