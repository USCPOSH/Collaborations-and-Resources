#!/bin/bash
echo "Making netlist.yaml"
/usr/bin/python netlist_scraper.py $1
echo "Running Backend"
/usr/bin/python3 backend.py $1
echo "Running Desanitizer"
/usr/bin/python sanitizer $1 sanitizer.config $1
