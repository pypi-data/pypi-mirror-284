import argparse
import sys
import time

from xdevs.sim import Coordinator

from xdevs.examples.devstone.devstone import LI, HO, HI, HOmod
from xdevs.examples.devstone.generator import Generator
from xdevs.models import Coupled


sys.setrecursionlimit(10000)

MODEL_TYPES = ("LI", "HI", "HO", "HOmod")


class DEVStoneEnvironment(Coupled):
    def __init__(self, name, devstone_model, num_gen_outputs=1):
        super(DEVStoneEnvironment, self).__init__(name=name)
        generator = Generator("generator", num_gen_outputs)
        self.add_component(generator)
        self.add_component(devstone_model)

        self.add_coupling(generator.o_out[0], devstone_model.i_in)
        if isinstance(devstone_model, HO) or isinstance(devstone_model, HOmod):
            self.add_coupling(generator.o_out[0], devstone_model.i_in2)


def parse_args():
    parser = argparse.ArgumentParser(description='Script to compare DEVStone implementations with different engines')

    parser.add_argument('-m', '--model-type', required=True, help='DEVStone model type (LI, HI, HO, HOmod)')
    parser.add_argument('-d', '--depth', type=int, required=True, help='Number of recursive levels of the model.')
    parser.add_argument('-w', '--width', type=int, required=True, help='Width of each coupled model.')
    parser.add_argument('-i', '--int-cycles', type=int, default=0, help='Dhrystone cycles executed in internal transitions')
    parser.add_argument('-e', '--ext-cycles', type=int, default=0, help='Dhrystone cycles executed in external transitions')
    parser.add_argument('-f', '--flatten', action="store_true", help='Activate flattening on model')

    args = parser.parse_args()

    if args.model_type not in MODEL_TYPES:
        raise RuntimeError("Unrecognized model type.")

    return args


if __name__ == '__main__':
    args = parse_args()

    if args.model_type == "LI":
        devstone_model = LI("LI_root", args.depth, args.width, args.int_cycles, args.ext_cycles)
    elif args.model_type == "HI":
        devstone_model = HI("HI_root", args.depth, args.width, args.int_cycles, args.ext_cycles)
    elif args.model_type == "HO":
        devstone_model = HO("HO_root", args.depth, args.width, args.int_cycles, args.ext_cycles)
    elif args.model_type == "HOmod":
        devstone_model = HOmod("HOmod_root", args.depth, args.width, args.int_cycles, args.ext_cycles)
    else:
        raise RuntimeError("Unrecognized model type.")

    start_time = time.time()
    env = DEVStoneEnvironment("DEVStoneEnvironment", devstone_model)
    model_created_time = time.time()

    coord = Coordinator(env, flatten=args.flatten)
    coord.initialize()
    engine_setup_time = time.time()

    coord.simulate_iters()
    sim_time = time.time()

    print(f"Model creation time: {model_created_time - start_time}")
    print(f"Engine setup time: {engine_setup_time - model_created_time}")
    print(f"Simulation time: {sim_time - engine_setup_time}")
