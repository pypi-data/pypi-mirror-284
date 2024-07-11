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
        spx = csc_matrix(obj.to_numpy()) 
    elif isinstance(obj, np.ndarray):
        spx = csc_matrix(obj) 
    elif isinstance(obj, sp.sparse.csc.csc_matrix):
        spx = obj
    else: 
        return 'invalid parameter'
    df = pd.DataFrame({'row':spx.tocoo().col if spx.ndim==1 else spx.indices, 'col':0 if spx.ndim==1 else spx.tocoo().col, 'val':spx.data})
    df.to_csv(pthin+'/.dat', index=False)
    out = shaplh.libshparse(pthin, opt)
    if os.path.isfile(pthin+'/.dat'):
        os.remove(pthin+'/.dat')
    if out[0]=="i":
        f = pthin+'/.sh/'+out
        if os.path.isfile(f):
            df = pd.read_csv(f)
            df = df.sort_values(by=['id']).reset_index(drop=True)
            return df
        else:
            return "Error: missing results" 
    else:
        return False 


def shcluster(svec, pthin):
    vs = ','.join(svec)
    return shaplh.libshcluster(vs, pthin)

def shclustert(svec, pthin):
    vs = ','.join(svec)
    return shaplh.libshclustert(vs, pthin)


def shstage(_df, pthin):
    dat = ','.join([str(v) for v in _df.row.values]+[str(v) for v in _df.val.values])
    return shaplh.libshstage(dat, pthin)


def shmerget(refa, refbv, pthin):
    refbvs = ','.join(refbv)
    v = shaplh.libshmerget(refa, refbvs, pthin)
    return v.split(',')


def shmerge(refa, refb, pthin):
    return shaplh.libshmerge(refa, refb, pthin)


def shapply(refa, refb, pthin):
    k = refa+'_'+refb
    sha_val = sha256(k.encode('utf-8')).hexdigest()[0:15]
    f = pthin+'/.sh/'+sha_val
    if not os.path.isfile(f):
        out = shaplh.libshapply(refa, refb, pthin, sha_val)
    return pd.read_csv(f)


def shapley(refa, refbv, pthin, ofs='none', limit='none', size=300, force=True, opt='uset', summarize='none'):
    refbvs = [ refb+'|a'+sha256((refa+'_'+refb).encode('utf-8')).hexdigest()[0:15] for refb in refbv]
    subrefbs = refbvs if force else [b for b in refbvs if not os.path.isfile(pthin+'/.sh/'+b.split('|')[1] )]
    if len(subrefbs) > 0:
        mmm = [ ','.join(list(o)) for o in np.split(subrefbs, np.arange(size,len(subrefbs),size)) ]
        rr =  [ shaplh.libshapley(refa, mx, pthin, opt, ofs, limit, summarize) for mx in mmm]
    resD = {refa+'|'+b:pd.read_csv(pthin+'/.sh/'+b.split('|')[1]) for b in refbvs if os.path.isfile(pthin+'/.sh/'+b.split('|')[1]) }
    return resD

