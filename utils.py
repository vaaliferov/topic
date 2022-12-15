import json
import scipy
import pickle

def load_lines(path):
    with open(path) as fd:
        return fd.read().splitlines()

def dump_lines(lines, path):
    with open(path, 'w') as fd:
        fd.write('\n'.join(lines)+'\n')

def load_json(path):
    with open(path) as fd:
        return json.load(fd)

def dump_json(obj, path):
    with open(path, 'w') as fd:
        json.dump(obj, fd, ensure_ascii=False)

def load_pickle(path):
    with open(path, 'rb') as fd:
        return pickle.load(fd)

def dump_pickle(obj, path):
    with open(path, 'wb') as fd:
        pickle.dump(obj, fd, protocol=pickle.HIGHEST_PROTOCOL)

def load_sparse(path):
    return scipy.sparse.load_npz(path)

def save_sparse(mat, path):
    scipy.sparse.save_npz(path, mat)

def encode_labels(s):
    labels = sorted(s.unique().tolist())
    return {v:k for k,v in enumerate(labels)}