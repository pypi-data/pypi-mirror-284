# #!/usr/bin/python3
# -*- coding: utf-8 -*-


import itertools as itt


import numpy as np
import scipy.constants as scpct
import datastock as ds


#############################################
#############################################
#       DEFAULTS
#############################################


_DMODEL = {

    # ----------
    # background

    'linear': {'var': ['a0', 'a1']},
    'exp_lamb': {'var': ['amp', 'rate']},

    # --------------
    # spectral lines

    'gauss': {
        'var': ['amp', 'vccos', 'sigma'],
        'param': [('lamb0', float), ('mz', float, np.nan)],
    },
    'lorentz': {
        'var': ['amp', 'vccos', 'gam'],
        'param': [('lamb0', float), ('mz', float, np.nan)],
    },
    'pvoigt': {
        'var': ['amp', 'vccos', 'sigma', 'gam'],
        'param': [('lamb0', float), ('mz', float, np.nan)],
    },
    'voigt': {
        'var': ['amp', 'vccos', 'sigma', 'gam'],
        'param': [('lamb0', float), ('mz', float, np.nan)],
    },

    # -----------
    # pulse shape

    'pulse1': {
        'var': ['amp', 't0', 't_up', 't_down'],
    },
    'pulse2': {
        'var': ['amp', 't0', 't_up', 't_down'],
    },
    'lognorm': {
        'var': ['amp', 't0', 'mu', 'sigma'],
    },
}


_LMODEL_ORDER = [
    # background
    'linear', 'exp_lamb', 'exp_E',
    # spectral lines
    'gauss', 'lorentz', 'pvoigt', 'voigt',
    # pulse shape
    'pulse1', 'pulse2', 'lognorm',
]


#############################################
#############################################
#       MODEL CHECK
#############################################


def _dmodel(
    coll=None,
    key=None,
    dmodel=None,
):

    # ----------
    # key
    # ----------

    wsm = coll._which_model
    key = ds._generic_check._obj_key(
        d0=coll.dobj.get(wsm, {}),
        short='sm',
        key=key,
        ndigits=2,
    )

    # --------------
    # check dmodel
    # --------------

    dmodel = _check_dmodel(
        coll=coll,
        key=key,
        dmodel=dmodel,
    )

    # --------------
    # store
    # --------------

    # add ref_nfun
    knfunc = f"nf_{key}"
    coll.add_ref(knfunc, size=len(dmodel))

    # dmodel
    dobj = {
        wsm: {
            key: {
                'keys': sorted(dmodel.keys()),
                'ref_nx': None,
                'ref_nf': knfunc,
                'dmodel': dmodel,
                'dconstraints': None,
            },
        },
    }

    coll.update(dobj=dobj)

    return


#############################################
#############################################
#       check dmodel
#############################################


def _dmodel_err(key, dmodel):

    # prepare list of str
    lstr = []
    for ii, (k0, v0) in enumerate(_DMODEL.items()):
        if v0.get('param') is None:
            stri = f"\t- 'f{ii}': '{k0}'"
        else:
            lpar = v0['param']
            pstr = ", ".join([f"'{tpar[0]}': {tpar[1]}" for tpar in lpar])
            stri = f"\t- 'f{ii}': " + "{" + f"'type': '{k0}', {pstr}" + "}"

        if k0 == 'linear':
            lstr.append("\t# background-oriented")
        elif k0 == 'gauss':
            lstr.append("\t# spectral lines-oriented")
        elif k0 == 'pulse1':
            lstr.append("\t# pulse-oriented")
        lstr.append(stri)

    # Provided
    if isinstance(dmodel, dict):
        prov = "\n".join([f"\t'{k0}': {v0}," for k0, v0 in dmodel.items()])
        prov = "{\n" + prov + "\n}"
    else:
        prov = str(dmodel)

    # concatenate msg
    return (
        f"For model '{key}' dmodel must be a dict of the form:\n"
         + "\n".join(lstr)
         + f"\n\nProvided:\n{prov}"
    )


def _check_dmodel(
    coll=None,
    key=None,
    dmodel=None,
):

    # -------------
    # model
    # -------------

    if isinstance(dmodel, str):
        dmodel = [dmodel]

    if isinstance(dmodel, (tuple, list)):
        dmodel = {ii: mm for ii, mm in enumerate(dmodel)}

    if not isinstance(dmodel, dict):
        raise Exception(_dmodel_err(key, dmodel))

    # prepare for extracting lamb0
    wsl = coll._which_lines

    # ------------
    # check dict
    # ------------

    dmod2 = {}
    dout = {}
    ibck, il = 0, 0
    for k0, v0 in dmodel.items():

        # -----------------
        # check str vs dict

        if isinstance(v0, dict):
            if isinstance(v0.get('type'), str):
                typ = v0['type']
            else:
                dout[k0] = v0
                continue

        elif isinstance(v0, str):
            typ = v0

        else:
            dout[k0] = v0
            continue

        # ----------
        # check type

        if typ not in _DMODEL.keys():
            dout[k0] = v0
            continue

        # ----------
        # check key

        if isinstance(k0, int):
            if typ in ['linear', 'exp']:
                k1 = f'bck{ibck}'
                ibck += 1
            else:
                k1 = f"l{il}"
                il += 1
        else:
            k1 = k0

        # ---------------------------
        # check parameter (if needed)

        haspar = _DMODEL[typ].get('param') is not None
        if haspar is True:

            lpar = _DMODEL[typ]['param']

            # loop on parameters
            dpar = {}
            for tpar in lpar:

                # provided
                c0 = (
                    isinstance(v0, dict)
                    and isinstance(v0.get(tpar[0]), tpar[1])
                )
                if c0:
                    dpar[tpar[0]] = v0[tpar[0]]

                elif tpar[0] in ('lamb0', 'mz'):

                    # check if lamb0 can be extracted from existing lines
                    c1 = (
                        typ in ['gauss', 'lorentz', 'pvoigt', 'voigt']
                        and k1 in coll.dobj.get(wsl, {}).keys()
                    )
                    if c1 and tpar[0] == 'lamb0':
                        dpar[tpar[0]] = coll.dobj[wsl][k1]['lamb0']

                    elif c1 and tpar[0] == 'mz':
                        kion = coll.dobj[wsl][k1]['ion']
                        dpar[tpar[0]] = coll.dobj['ion'][kion]['A'] * scpct.m_u

                    elif len(tpar) == 3:
                        dpar[tpar[0]] = tpar[2]
                    else:
                        dout[k0] = v0
                        continue

                elif len(tpar) == 3:
                    dpar[tpar[0]] = tpar[2]

                else:
                    dout[k0] = v0
                    continue

        # ----------------
        # assemble

        dmod2[k1] = {'type': typ, 'var': _DMODEL[typ]['var']}

        # add parameter
        if haspar is True:
            dmod2[k1]['param'] = dpar

    # ---------------
    # raise error
    # ---------------

    if len(dout) > 0:
        raise Exception(_dmodel_err(key, dout))

    return dmod2


#############################################
#############################################
#       Get variables
#############################################


def _get_var(
    coll=None,
    key=None,
    concatenate=None,
    returnas=None,
):

    # --------------
    # check key
    # -------------

    # key
    wsm = coll._which_model
    lok = list(coll.dobj.get(wsm, {}).keys())
    key = ds._generic_check._check_var(
        key, 'key',
        types=str,
        allowed=lok,
    )

    # keys and dmodel
    keys = coll.dobj[wsm][key]['keys']
    dmodel = coll.dobj[wsm][key]['dmodel']

    # returnas
    if isinstance(returnas, str):
        returnas = [returnas]
    returnas = ds._generic_check._check_var_iter(
        returnas, 'returnas',
        types=(list, tuple),
        types_iter=str,
        default=['all', 'param'],
        allowed=['all', 'free', 'tied', 'param_key', 'param_value'],
    )

    # concatenate
    concatenate = ds._generic_check._check_var(
        concatenate, 'concatenate',
        types=bool,
        default=True,
    )

    # -------------
    # get lvar
    # -------------

    dout = {}

    # ---------------
    # all variables

    if 'all' in returnas:
        dout['all'] = [
            [f"{k0}_{k1}" for k1 in dmodel[k0]['var']]
            for k0 in keys
        ]

    # -----------------------
    # free or tied variables

    if 'free' in returnas or 'tied' in returnas:
        dconstraints = coll.dobj[wsm][key]['dconstraints']
        lref = [v0['ref'] for v0 in dconstraints['dconst'].values()]

        # lvar
        if 'free' in returnas:
            dout['free'] = [
                [
                    f"{k0}_{k1}" for k1 in dmodel[k0]['var']
                    if f"{k0}_{k1}" in lref
                ]
                for k0 in keys
            ]

        if 'tied' in returnas:
            dout['tied'] = [
                [
                    f"{k0}_{k1}" for k1 in dmodel[k0]['var']
                    if f"{k0}_{k1}" not in lref
                ]
                for k0 in keys
            ]

    # ---------------
    # parameters

    if 'param_key' in returnas:
        dout['param_key'] = [
            [f"{k0}_{tpar[0]}" for tpar in _DMODEL[dmodel[k0]['type']]['param']]
            for k0 in keys if dmodel[k0].get('param') is not None
        ]

    if 'param_value' in returnas:
        dout['param_value'] = [
            [dmodel[k0]['param'][tpar[0]] for tpar in _DMODEL[dmodel[k0]['type']]['param']]
            for k0 in keys if dmodel[k0].get('param') is not None
        ]

    # ----------------
    # concatenate
    # ----------------

    if concatenate is True:
        for k0, v0 in dout.items():
            dout[k0] = list(itt.chain.from_iterable(v0))

            if k0 == 'param_value':
                dout[k0] = np.array(dout[k0])

    # ----------------
    # return
    # ----------------

    return dout


#############################################
#############################################
#       Get variables dind
#############################################


def _get_var_dind(
    coll=None,
    key=None,
):

    # --------------
    # check key
    # -------------

    # key
    wsm = coll._which_model
    lok = list(coll.dobj.get(wsm, {}).keys())
    key = ds._generic_check._check_var(
        key, 'key',
        types=str,
        allowed=lok,
    )

    # keys and dmodel
    keys = coll.dobj[wsm][key]['keys']
    dmodel = coll.dobj[wsm][key]['dmodel']

    # -------------
    # get lvar and param
    # -------------

    dout = coll.get_spectral_model_variables(
        key,
        returnas=['all', 'free', 'param_key', 'param_value'],
        concatenate=True,
    )
    x_all = dout['all']
    x_free = dout['free']
    param_key = dout['param_key']

    # ---------------
    # derive dind
    # ---------------

    types = sorted(set([v0['type'] for v0 in dmodel.values()]))

    dind = {}
    for ktype in types:

        # list functions with corresponding model type
        lf = [k0 for k0 in keys if dmodel[k0]['type'] == ktype]

        # populate
        dind[ktype] = {
            k1: {
                'ind': np.array([x_all.index(f"{kf}_{k1}") for kf in lf]),
                'keys': [f"{kf}_{k1}" for kf in lf],
            }
            for k1 in dmodel[lf[0]]['var']
        }

        # add param
        if dmodel[lf[0]].get('param') is not None:
            for kpar in dmodel[lf[0]]['param'].keys():
                dind[ktype][kpar] = [
                    param_key.index(f"{kf}_{kpar}")
                    for kf in lf
                ]

    # ---------------
    # safety checks
    # ---------------

    # aggregate all variables
    lvar = tuple(itt.chain.from_iterable([
        list(itt.chain.from_iterable([
            v1['keys']
            for k1, v1 in vtype.items()
            if not isinstance(v1, list)
        ]))
        for ktype, vtype in dind.items()
    ]))

    # check all indices are unique
    lind = tuple(itt.chain.from_iterable([
        list(itt.chain.from_iterable([
            v1['ind']
            for k1, v1 in vtype.items()
            if not isinstance(v1, list)
        ]))
        for ktype, vtype in dind.items()
    ]))

    # check all variable are represented
    nn = len(x_all)
    c0 = (
        (tuple(sorted(lvar)) == tuple(sorted(x_all)))
        and np.allclose(sorted(lind), np.arange(nn))
        and (tuple([lvar[ii] for ii in np.argsort(lind)]) == tuple(x_all))
    )
    if not c0:
        msg = (
            "dind corrupted!\n"
            f"\t- x_all: {x_all}\n"
            f"\t- lvar: {lvar}\n"
            f"\t- lind: {lind}\n"
            f"\ndind:\n{dind}\n"
        )
        raise Exception(msg)

    # ----------------
    # add func
    # ----------------

    dind['func'] = {}
    for ktype in types:

        # list functions with corresponding model type
        lf = [k0 for k0 in keys if dmodel[k0]['type'] == ktype]

        # get indices
        ind = [keys.index(ff) for ff in lf]

        # store
        dind['func'][ktype] = {
            'keys': lf,
            'ind': np.array(ind, dtype=int),
        }

    #-------------------------
    # add total number of func

    dind['nfunc'] = len(keys)

    # ----------------
    # add jac
    # ----------------

    dind['jac'] = {ktype: {} for ktype in types}
    for ktype in types:
        lf = [k0 for k0 in keys if dmodel[k0]['type'] == ktype]
        for kvar in _DMODEL[ktype]['var']:
            dind['jac'][ktype][kvar] = np.array(
                [
                    x_free.index(f"{kf}_{kvar}")
                    for kf in lf
                    if f"{kf}_{kvar}" in x_free
                ],
                dtype=int,
            )

    # ---------------
    # safety checks
    # ---------------

    lind = sorted(itt.chain.from_iterable([
        list(itt.chain.from_iterable([v1.tolist() for v1 in v0.values()]))
        for v0 in dind['jac'].values()
    ]))
    if not np.allclose(lind, np.arange(len(x_free))):
        msg = (
            "Something wrong with dind['jac'] !\n"
            f"\t- lind = {lind}\n"
            f"\t- dind['jac']:\n{dind['jac']}\n"
        )
        raise Exception(msg)

    return dind


#############################################
#############################################
#       Show
#############################################


def _show(coll=None, which=None, lcol=None, lar=None, show=None):

    # ---------------------------
    # list of functions
    # ---------------------------

    # list of models
    lkey = [
        k1 for k1 in coll._dobj.get(which, {}).keys()
        if show is None or k1 in show
    ]

    # list of relevant functions
    lfunc = []
    for k0 in lkey:
        dmod = coll.dobj[which][k0]['dmodel']
        for k1 in _LMODEL_ORDER:
            lk2 = [k2 for k2, v2 in dmod.items() if v2['type'] == k1]
            if len(lk2) > 0 and k1 not in lfunc:
                lfunc.append(k1)

    # reorder
    lfunc = [k1 for k1 in _LMODEL_ORDER if k1 in lfunc]

    # ---------------------------
    # column names
    # ---------------------------

    lcol.append([which] + lfunc + ['constraints', 'free var'])

    # ---------------------------
    # data array
    # ---------------------------

    lar0 = []
    for k0 in lkey:

        # initialize with key
        arr = [k0]

        # add nb of func of each type
        dmod = coll.dobj[which][k0]['dmodel']
        for k1 in lfunc:
            nn = str(len([k2 for k2, v2 in dmod.items() if v2['type'] == k1]))
            arr.append(nn)

        # add nb of constraints
        dconst = coll.dobj[which][k0]['dconstraints']['dconst']
        nn = str(len([k1 for k1, v1 in dconst.items() if len(v1) > 1]))
        arr.append(nn)

        # add number of free variables
        lfree = coll.get_spectral_model_variables(k0, returnas='free')['free']
        lall = coll.get_spectral_model_variables(k0, returnas='all')['all']
        arr.append(f"{len(lfree)} / {len(lall)}")

        lar0.append(arr)

    lar.append(lar0)

    return lcol, lar


#############################################
#############################################
#       Show single model
#############################################


def _show_details(coll=None, key=None, lcol=None, lar=None, show=None):

    # ---------------------------
    # get dmodel
    # ---------------------------

    wsm = coll._which_model
    dmodel = coll.dobj[wsm][key]['dmodel']
    dconst = coll.dobj[wsm][key]['dconstraints']['dconst']

    lkeys = coll.dobj[wsm][key]['keys']
    llvar = [dmodel[kf]['var'] for kf in lkeys]

    nvarmax = np.max([len(lvar) for lvar in llvar])
    lfree = coll.get_spectral_model_variables(key, returnas='free')['free']

    lpar = sorted(set(itt.chain.from_iterable([
        v0.get('param', {}).keys() for v0 in dmodel.values()
    ])))

    # ---------------------------
    # column names
    # ---------------------------

    lvar = [f"var{ii}" for ii in range(nvarmax)]
    lcol.append(['func', 'type', ' '] + lvar + [' '] + lpar)

    # ---------------------------
    # data
    # ---------------------------

    lar0 = []
    for kf in lkeys:

        # initialize with key, type
        arr = [kf, dmodel[kf]['type'], '|']

        # add variables of each func
        for ii, k1 in enumerate(dmodel[kf]['var']):
            key = f"{kf}_{k1}"
            if key in lfree:
                nn = key
            else:
                gg = [kg for kg, vg in dconst.items() if key in vg.keys()][0]
                nn = f"{key}({dconst[gg]['ref']})"

            arr.append(nn)

        # complement
        arr += ['' for ii in range(nvarmax - ii - 1)] + ['|']

        # add parameters of each func
        for k1 in lpar:
            nn = dmodel[kf].get('param', {}).get(k1, '')
            if not isinstance(nn, str):
                nn = f"{nn:.6e}"
            arr.append(nn)

        lar0.append(arr)

    lar.append(lar0)

    return lcol, lar


# =============================================================================
# def _initial_from_from_model(
#     coll=None,
#     key=None,
#     dmodel=None,
# ):
#
#     # -----------
#     # initialize
#     # ----------
#
#     wsl = coll._which_lines
#
#     dinit = {}
#     for k0, v0 in dmodel.items():
#
#         # -----
#         # bck
#
#         if v0['type'] == 'linear':
#             dinit[k0] = {'c0': 0, 'c1': 0}
#
#         elif v0['type'] == 'exp':
#             dinit[k0] = {'c0': 0, 'c1': 0}
#
#         else:
#
#             # if from spectral lines
#             if k0 in coll.dobj.get(wsl, {}).keys():
#                 lamb0 = coll.dobj[wsl][k0]['lamb0']
#             else:
#                 lamb0 = 0
#
#             if v0['type'] == 'gauss':
#                 dinit[k0] = {
#                     'amp': 1,
#                     'shift': lamb0,
#                     'width': 1,
#                 }
#
#             elif v0['type'] == 'lorentz':
#                 dinit[k0] = np.r_[0, lamb0, 0]
#
#             elif v0['type'] == 'pvoigt':
#                 dinit[k0] = np.r_[0, lamb0, 0]
#
#
#     # -------------
#     # lines
#     # -------------
#
#
#
#
#
#     coll.add_spectral_model(key=key, dmodel=dmodel)
#     coll.set_spectral_model_initial(key=key, initial=initial)
#
#     return
# =============================================================================