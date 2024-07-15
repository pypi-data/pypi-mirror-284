"""
This module contains tests for tofu.geom in its structured version
"""


# Built-in
import itertools as itt


# local
from ._setup_teardown import setup_module0, teardown_module0
from .. import nist


#######################################################
#
#     Setup and Teardown
#
#######################################################


def setup_module(module):
    setup_module0(module)


def teardown_module(module):
    teardown_module0(module)


#######################################################
#
#     Creating Ves objects and testing methods
#
#######################################################


class Test_nist(object):

    # ------------------------
    #   setup and teardown
    # ------------------------

    @classmethod
    def setup_class(cls):
        pass

    @classmethod
    def setup_method(self):
        pass

    def teardown_method(self):
        pass

    @classmethod
    def teardown_class(cls):
        pass

    # ------------------------
    #  search online
    # ------------------------

    def test01_search_online_by_wavelengthA(self):

        llambmin = [None, 3.94]
        llambmax = [None, 4.]
        lion = [None, 'H', ['ar', 'W44+']]

        lcache_from = [False, True]
        ldatacol = [False, True]

        # Search by searchstr
        llcomb = [
            llambmin, llambmax, lion,
            lcache_from,
            ldatacol,
        ]
        ii, itot = -1, 2*2*3*2*2
        for comb in itt.product(*llcomb):
            ii += 1
            if all([vv is None for vv in comb[:2]]):
                continue
            if comb[2] == 'H' and comb[1] is None:
                continue
            if comb[2] == 'H' and all([vv is not None for vv in comb[:2]]):
                continue
            if any([vv is None for vv in comb[:2]]) and comb[2] != 'H':
                continue
            print(f'{ii} / {itot}  -  {comb}')

            # out = nist.step01_search_online_by_wavelengthA(
                # lambmin=comb[0],
                # lambmax=comb[1],
                # ion=comb[2],
                # verb=True,
                # return_dout=True,
                # return_dsources=True,
                # cache_from=comb[3],
                # cache_info=True,
                # format_for_DataStock=comb[4],
                # create_custom=True,
            # )
            # del out

    # ------------------------
    #  clear cache
    # ------------------------

    def test02_clear_cache(self):
        nist.clear_cache()
