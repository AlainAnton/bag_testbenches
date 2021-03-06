# -*- coding: utf-8 -*-

from bag.core import BagProject

from bag.simulation.core import DesignManager

if __name__ == '__main__':

    config_file = 'specs_test/nch_w0d5.yaml'

    local_dict = locals()
    if 'bprj' not in local_dict:
        print('creating BAG project')
        bprj = BagProject()

    else:
        print('loading BAG project')
        bprj = local_dict['bprj']

    sim = DesignManager(bprj, config_file)
    sim.test_layout(gen_sch=True)
