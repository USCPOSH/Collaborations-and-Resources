simulator lang=spice
** Generated for: hspiceD
** Generated on: Jul 18 13:04:27 2019
** Design library name: CAD_modules
** Design cell name: test_VCO_Dtype1_ASAP7
** Design view name: schematic
.PARAM lastt=40n rres=20k vbias=0.7 vdd=0.8


.IC
+    V(on2<1>)=0
+    V(on<1>)=0
.TRAN 1e-12 40e-9 START=0.0

.TEMP 25.0
.OPTION
+    ARTIST=2
+    INGOLD=2
+    PARHIER=LOCAL
+    PSF=2
** .INCLUDE "/home/mohsen/workarea_ASAP07/cdslib/asap7_TechLib_06/tech.db"
.INCLUDE "/home/mohsen/workarea_ASAP07/models/hspice/7nm_TT.pm"

**.PRINT V(vdd)
V1 vdd vss dc=vdd
V0 vss gnd! dc=0
V2 vbias vss pwl(0 0 40n vbias)

** Library name: CAD_modules
** Cell name: diff2sing_v1_ASAP7
** View name: schematic
.subckt diff2sing_v1_ASAP7 b vdd vss in1 in2 o
m2 o in2 net3 vdd pmos_lvt w=216e-9 l=20e-9 nfin=8
m1 net8 in1 net3 vdd pmos_lvt w=216e-9 l=20e-9 nfin=8
m0 net3 b vdd vdd pmos_lvt w=216e-9 l=20e-9 nfin=8
m4 net8 net8 vss vss nmos_lvt w=108e-9 l=20e-9 nfin=4
m3 o net8 vss vss nmos_lvt w=108e-9 l=20e-9 nfin=4
.ends diff2sing_v1_ASAP7
** End of subcircuit definition.

** Library name: CAD_modules
** Cell name: VCO_type1_ASAP7
** View name: schematic
.subckt VCO_type1_ASAP7 vdd vss o<1> o<2> o<3> o<4> o<5> vbias
m0 o<2> o<1> vss vss nmos_lvt w=27e-9 l=20e-9 nfin=12
m1 o<3> o<2> vss vss nmos_lvt w=27e-9 l=20e-9 nfin=12
m2 o<4> o<3> vss vss nmos_lvt w=27e-9 l=20e-9 nfin=12
m3 o<5> o<4> vss vss nmos_lvt w=27e-9 l=20e-9 nfin=12
m4 o<1> o<5> vss vss nmos_lvt w=27e-9 l=20e-9 nfin=12
m5 o<2> vbias vdd vdd pmos_lvt w=27e-9 l=20e-9 nfin=6
m8 o<5> vbias vdd vdd pmos_lvt w=27e-9 l=20e-9 nfin=6
m9 o<1> vbias vdd vdd pmos_lvt w=27e-9 l=20e-9 nfin=6
m6 o<3> vbias vdd vdd pmos_lvt w=27e-9 l=20e-9 nfin=6
m7 o<4> vbias vdd vdd pmos_lvt w=27e-9 l=20e-9 nfin=6
.ends VCO_type1_ASAP7
** End of subcircuit definition.

** Library name: CAD_modules
** Cell name: VCO_Dtype1_ASAP7
** View name: schematic
.subckt VCO_Dtype1_ASAP7 vdd vss on<1> on<2> on<3> on<4> on<5> op<1> op<2> op<3> op<4> op<5> vbias
xi1 vdd vss op<1> op<2> op<3> op<4> op<5> vbias VCO_type1_ASAP7
xi0 vdd vss on<1> on<2> on<3> on<4> on<5> vbias VCO_type1_ASAP7
.ends VCO_Dtype1_ASAP7
** End of subcircuit definition.

** Library name: CAD_modules
** Cell name: test_VCO_Dtype1_ASAP7
** View name: schematic
xi10 oo2<1> vss sampler_writer Vth=0 dir=1 ttol=1e-12
xi11 oo<1> vbias sampler_writer2 Vth=0 dir=1 ttol=1e-12 ofile=ref_edge2.txt
xi6<1> vss vdd vss on<1> op<1> oo<1> diff2sing_v1_ASAP7
xi6<2> vss vdd vss on<2> op<2> oo<2> diff2sing_v1_ASAP7
xi6<3> vss vdd vss on<3> op<3> oo<3> diff2sing_v1_ASAP7
xi6<4> vss vdd vss on<4> op<4> oo<4> diff2sing_v1_ASAP7
xi6<5> vss vdd vss on<5> op<5> oo<5> diff2sing_v1_ASAP7
xi12<1> vss vdd vss on2<1> op2<1> oo2<1> diff2sing_v1_ASAP7
xi12<2> vss vdd vss on2<2> op2<2> oo2<2> diff2sing_v1_ASAP7
xi12<3> vss vdd vss on2<3> op2<3> oo2<3> diff2sing_v1_ASAP7
xi12<4> vss vdd vss on2<4> op2<4> oo2<4> diff2sing_v1_ASAP7
xi12<5> vss vdd vss on2<5> op2<5> oo2<5> diff2sing_v1_ASAP7
xi9 vdd vss on2<1> on2<2> on2<3> on2<4> on2<5> op2<1> op2<2> op2<3> op2<4> op2<5> vss VCO_Dtype1_ASAP7
xi0 vdd vss on<1> on<2> on<3> on<4> on<5> op<1> op<2> op<3> op<4> op<5> vbias VCO_Dtype1_ASAP7
.hdl "/home/mohsen/EE536a/CAD_modules/sampler_writer/veriloga/veriloga.va"
.hdl "/home/mohsen/EE536a/CAD_modules/sampler_writer2/veriloga/veriloga.va"



.MEAS TRAN t1  TRIG V(oo<1>) VAL=0  RISE=2 TARG V(oo<1>) VAL=0  RISE=3
.MEAS TRAN td1 WHEN V(oo<1>) VAL=0.5  FALL=LAST
.MEAS TRAN t2  TRIG V(oo<1>) VAL=0  RISE=1 TD=td1 TARG V(oo<1>) VAL=0  RISE=2 TD=td1
.MEAS TRAN lv FIND V(vbias) AT = td1
.MEAS TRAN pwr  avg I(V1) from .001ns to td1



.END
