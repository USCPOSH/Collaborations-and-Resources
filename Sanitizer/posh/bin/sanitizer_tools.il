procedure( fprintParams(filewrite pdk component)

   mstr=dbOpenCellViewByType(pdk component "symbol"  "schematicSymbol" "r")
   fprintf(write "Cell: %s\n" cell~>name)
    schCreateInst(geGetEditCellView() mstr "I0" 0:0 "R0" 1)

    _treeNavActivateOpc(dwindow('treeAssistant2) "Objects/Instances")

    _treeNavSelect(dwindow('treeAssistant2) "/I0(symbol) Inst")

   let( (inst cdf)
      inst=car(geGetSelSet())
      cdf=cdfGetBaseCellCDF(ddGetObj(inst~>libName inst~>cellName))
      foreach( param cdf->parameters
	 ;printf(filewrite "\tData: %s %s\n" param->prompt param~>editable)
         fprintf(filewrite "\tData: %s %s %L %s \n" param->prompt param~>name get(inst param~>name) param~>editable)
      ) ;foreach
      printf("Job done\n")
   ) ;let
   
   schHiDelete()
) ;procedure


procedure( printDevices(pdk)
	write = outfile("devices.txt")
	foreach(cell ddGetObj(pdk)~>cells
      
	errset(fprintParams(write pdk cell~>name))
   )
) ;procedure


procedure( params(write)
	opForm->tabField->value=2
	opForm->tabField->topTab2->simulatorField->value="spectre"
	fprintf(write opForm->tabField->topTab2->instParametersspectre->value)
	fprintf(write "\n")
	fprintf(write opForm->tabField->topTab2->termOrderspectre->value)
	fprintf(write "\n")
	fprintf(write opForm->tabField->topTab2->propMappingspectre->value)
	fprintf(write "\n")

) ;procedure


procedure( printCDF(pdk)
	filename = "devices.txt"
	write = outfile(filename)
	fprintf(write "%s\n" pdk)
	fprintf(write "l w m nf\n")
	aedEditCDF()
	_cdfFormFocusCBLibName()
	
	count = 0 
	opForm->addLibName->value=pdk
	foreach(cell ddGetObj(pdk)~>cells
		opForm->addCellName->value=cell~>name
		fprintf(write cell~>name)
		printf(cell~>name)
		printf("\n")
		fprintf(write "\n")
		errset(params(write))
		count = count + 1
	)
	printf("%d", count)
	close(write)
);procedure




