from pymatgen.core import Structure
from maml.apps.pes import MTPotential
from pymacy.icsd.db import ICSD
import pickle
import timeit
import json
import numpy as np
start = timeit.default_timer()

mtp = MTPotential()

with open('./test_data_Mg3Sb2_468aimd.json', 'r') as c: #You can change different data sets to evaluate the potential.
     datapool = 1*json.load(c)

print(len(datapool))
structures = [Structure.from_dict(d['structure']) for d in datapool]
energies = [d['outputs']['energy'] for d in datapool]
forces = [d['outputs']['forces'] for d in datapool]
stresses = [d['outputs']['stress'] for d in datapool]



import pickle
with open('./deforma010_20_4.8_mtp.pkl','rb') as f:
    MTP = pickle.load(f)
origin_train, predict_train = MTP.evaluate(test_structures=structures, test_energies=energies,test_forces=forces)


def output_xy(df_orig, df_predict, tag):
    orig = df_orig[df_orig['dtype'] == tag]
    predict = df_predict[df_predict['dtype'] == tag]
    x = orig['y_orig'] / orig['n']
    y = predict['y_orig'] / predict['n']
    return x, y

from sklearn.metrics import mean_absolute_error
x1, y1 = output_xy(origin_train, predict_train, 'energy')
np.savetxt('test_data_deforma010_energy.out',np.column_stack((x1,y1)))
print('test_data_deforma010_20_4.8 train energy: ', mean_absolute_error(x1, y1) * 1000)
x2, y2 = output_xy(origin_train, predict_train, 'force')
np.savetxt('test_data_deforma010_20_4.8_force.out',np.column_stack((x2,y2)))
print('test_data_deforma010_20_4.8 train force: ', mean_absolute_error(x2, y2))

