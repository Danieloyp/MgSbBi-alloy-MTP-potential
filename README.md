# MgSbBi-alloy-MTP-potential
data set for fitting MgSbBi alloy MTP potential

# Moment Tensor Potential


This repository contains Moment Tensor Potential (MTP) models for 
Mg$_{3}$(Sb$_{1-x}$Bi$_{x}$)$_{2}$ thermoelectric material, including the corresponding parameters and training data used to develop the models. For MTP model training and potential generations, please use the mlip package [https://mlip.skoltech.ru/download/](https://mlip.skoltech.ru/download/).

The structure of the folder organization is as follows

```
- Element/
    - training/
    - usage/
```
where the `training` folder contains the original datasets used for developing the model and `usage` contains examples for running the simulations with developed potentials. 

Below are the units of training metrics:

* Energy: `meV/atom`
* Forces: `eV/Angstrom`

## LAMMPS interface installation 
The interface with LAMMPS is distributed separately, at the public repository [https://gitlab.com/ashapeev/interface-lammps-mlip-2/](https://gitlab.com/ashapeev/interface-lammps-mlip-2/)under the GNU public license.




## Running examples

The examples are under the `usage` folder.
Noting that the current MTP parameters are compatible with Lammps-2018 version.
For newer version of Lammps, minor changes may need to be adjusted. 

For example, one can run the `usage` by simply the following command
> lmp_intel_cpu_intelmpi -i in.elastic

The final results should look like the following:

```
print """
${C11all} ${C12all} ${C13all} ${C14all} ${C15all} ${C16all}
${C12all} ${C22all} ${C23all} ${C24all} ${C25all} ${C26all}
${C13all} ${C23all} ${C33all} ${C34all} ${C35all} ${C36all}
${C14all} ${C24all} ${C34all} ${C44all} ${C45all} ${C46all}
${C15all} ${C25all} ${C35all} ${C45all} ${C55all} ${C56all}
${C16all} ${C26all} ${C36all} ${C46all} ${C56all} ${C66all}
"""

43.0330997305078 35.4105576114989 30.2855426757447 2.03007161923381 0.0851635063865696 -0.111383771768735
35.4105576114989 43.9320077025058 30.2036277190041 -2.16439895069289 -0.0344303524800076 -0.18565337576906
30.2855426757447 30.2036277190041 63.7214067830086 0.00407278548699752 0.0014498290552563 0.025563385752745
2.03007161923381 -2.16439895069289 0.00407278548699752 11.0447188400048 -0.0571402869609554 -0.0447268194876375
0.0851635063865696 -0.0344303524800076 0.0014498290552563 -0.0571402869609554 11.2888432626826 2.26889107991401
-0.111383771768735 -0.18565337576906 0.025563385752745 -0.0447268194876375 2.26889107991401 4.41796511491503

Total wall time: 0:15:28
```
