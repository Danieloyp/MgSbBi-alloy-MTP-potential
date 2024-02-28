from pymatgen.core import Structure
from maml.apps.pes import MTPotential
from pymacy.icsd.db import ICSD
import pickle
import timeit
import json

start = timeit.default_timer()

mtp = MTPotential()

with open('./alloy_relaxed.json', 'r') as a:
  with open('./alloy_unrelaxed.json','r') as b:
    with open('./Mg3Sb2_deform_a_soc.json', 'r') as c:     
      with open('./Mg3Sb2_deform_c_soc.json', 'r') as d:
        with open('./Mg3Bi2_AIMD.json', 'r') as e:
          with open('./Mg3Bi2_strain.json', 'r') as h:
            with open('./Mg3Sb2_AIMD.json', 'r') as i:
              with open('./Mg3Sb2_strain.json', 'r') as j:
                        datapool = 1*json.load(a)+1*json.load(b)+10*json.load(c)+1*json.load(d)+1*json.load(e)+1*json.load(h)+1*json.load(i)+1*json.load(j)


print(len(datapool))
structures = [Structure.from_dict(d['structure']) for d in datapool]
energies = [d['outputs']['energy'] for d in datapool]
forces = [d['outputs']['forces'] for d in datapool]
stresses = [d['outputs']['stress'] for d in datapool]

mtp.train(train_structures=structures,
          train_energies=energies,
          train_forces=forces,
          train_stresses=stresses,
          unfitted_mtp='20g.mtp',
          energy_weight=1,
          force_weight=0.01,
          stress_weight=0.00,
          max_dist=4.8,
          max_iter=1000)

stop = timeit.default_timer()
print('basis = 20g.mtp, max_dist = 4.8, time used: ', stop - start)

with open('deforma010_20_4.8_mtp.pkl', 'wb') as f:
    pickle.dump(mtp, f)

