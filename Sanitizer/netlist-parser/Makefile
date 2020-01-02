
all: clean compile
	echo "Done"


compile:
	mkdir -p build
	cp setup.py build/
	java -jar "lib/antlr-4.7.2-complete.jar" -Dlanguage=Python2 -o build/netlist_parser -visitor SpectreLexer.g4 SpectreParser.g4
	cp __init__.py build/netlist_parser/
	cd build ; tar zcvf netlist-parser-0.0.0.tar.gz netlist_parser/


java:
	mkdir -p build/java
	java -jar "lib/antlr-4.7.2-complete.jar" -o build/java/ -visitor SpectreLexer.g4 SpectreParser.g4
	jar cvf build/netlist-parser.jar build/java/*


clean:
	rm -rf build/
