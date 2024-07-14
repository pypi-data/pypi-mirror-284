import os
import scipy as sp
from hashlib import sha256
import shutil
import numpy as np
from scipy.sparse import csc_matrix
import pandas as pd
from .shaplh import *

__doc__ = shaplh.__doc__
if hasattr(shaplh, "__all__"):
    __all__ = shaplh.__all__

def shparse(obj, pthin, opt='uset'):  
    if isinstance(obj, pd.core.frame.DataFrame):
        csc_m = csc_matrix(obj.to_numpy()) 
    elif isinstance(obj, np.ndarray):
        csc_m = csc_matrix(obj) 
    elif isinstance(obj, sp.sparse.csc.csc_matrix):
        csc_m = obj
    else: 
        return 'invalid parameter'
    if not os.path.exists(pthin+'/.sh'):
        os.makedirs(pthin+'/.sh/')
    df = pd.DataFrame({'row':csc_m.tocoo().col if csc_m.ndim==1 else csc_m.indices, 'col':0 if csc_m.ndim==1 else csc_m.tocoo().col, 'val':csc_m.data})
    df.to_csv(pthin+'/.dat', index=False)
    output = shaplh.libshparse(pthin, opt)
    if os.path.isfile(pthin+'/.dat'):
        os.remove(pthin+'/.dat')
    if output[0]=="i":
        f = pthin+'/.sh/'+output
        if os.path.isfile(f):
            df = pd.read_csv(f)
            df = df.sort_values(by=['id']).reset_index(drop=True)
            return df
        else:
            return "Error: missing results" 
    else:
        return False 


def shcluster(sourcevec, pthin):
    return shaplh.libshcluster(','.join(sourcevec), pthin)


def shclustert(sourcevec, pthin):
    return shaplh.libshclustert(','.join(sourcevec), pthin)


def shstage(_df, pthin):
    dat = ','.join([str(v) for v in _df.row.values]+[str(v) for v in _df.val.values])
    return shaplh.libshstage(dat, pthin)


def shmerget(referencea, referenceavec, pthin):
    value = shaplh.libshmerget(referencea, ','.join(referenceavec), pthin)
    return value.split(',')


def shmerge(referencea, refb, pthin):
    return shaplh.libshmerge(referencea, refb, pthin)


def shapply(referencea, refb, pthin):
    k = referencea+'_'+refb
    sha_val = sha256(k.encode('utf-8')).hexdigest()[0:15]
    f = pthin+'/.sh/'+sha_val
    if not os.path.isfile(f):
        output = shaplh.libshapply(referencea, refb, pthin, sha_val)
    return pd.read_csv(f)


def shapley(referencea, referencebvec, pthin, ofs='none', limit='none', size=100, force=True, opt='uset', summarize='none'):
    refbvs = [ refb+'|a'+sha256((referencea+'_'+refb).encode('utf-8')).hexdigest()[0:15] for refb in referencebvec]
    subrefbs = refbvs if force else [b for b in refbvs if not os.path.isfile(pthin+'/.sh/'+b.split('|')[1] )]
    if len(subrefbs) > 0:
        sourcevec = [ ','.join(list(o)) for o in np.split(subrefbs, np.arange(size,len(subrefbs),size)) ]
        resultvec =  [ shaplh.libshapley(referencea, mx, pthin, opt, ofs, limit, summarize) for mx in sourcevec]
    result = {referencea+'|'+b:pd.read_csv(pthin+'/.sh/'+b.split('|')[1]) for b in refbvs if os.path.isfile(pthin+'/.sh/'+b.split('|')[1]) }
    return result

