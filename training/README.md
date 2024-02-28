# These are the data sets used to fit Mg3(Sb1-xBix)2 alloy MTP potential.

## training data sets:
* alloy_relaxed.json
* alloy_unrelaxed.json
* Mg3Sb2_deform_a_soc.json    
* Mg3Sb2_deform_c_soc.json
* Mg3Bi2_AIMD.json
* Mg3Bi2_strain.json
* Mg3Sb2_AIMD.json
* Mg3Sb2_strain.json

## test data set:
* test_data_Mg3Sb2_468aimd.json (Mg3Sb2 AIMD in 400K, 600K and 800K)

`pot_fit.py` is the python file used to fit this potential and get
deforma010_20_4.8_mtp.pkl file.

`write_para.py` is the python core to transform the .pkl file 
into .mtp file.

`evaluate.py` is the python core to evalute the force and energy error compared with DFT calculation.
