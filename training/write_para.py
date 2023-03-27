import pickle
import sys

file = sys.argv[1] #pickle file
with open(file,'rb') as f:
    mtp = pickle.load(f)
mtp.write_param()
