import argparse
from CGRtools.algorithms.tautomers import Tautomers
from CGRtools import SDFRead, SDFWrite


def main(i_sdf, o_sdf, prepare_molecules, zwitter, ring_chain, keto_enol, limit):
    with SDFWrite(o_sdf) as tau_f, SDFRead(i_sdf) as f:
        for mol in f:
            Tautomers.tautomerize(mol, prepare_molecules, zwitter, ring_chain, keto_enol, limit)
            tau_f.write(mol)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Tautomer_cgrtools")
    parser.add_argument("-i", "--input_file", type=str, required=True, help="Input SDF file")
    parser.add_argument("-o", "--output_file", type=str, required=True, help="Output SDF file")
    parser.add_argument("-p", "--prepare_molecules", type=str, default=True)
    parser.add_argument("-z", "--zwitter", type=str, default=True)
    parser.add_argument("-rc", "--ring_chain", type=str, default=True)
    parser.add_argument("-ke", "--keto_enol", type=str, default=True)
    parser.add_argument("-l", "--limit", type=str, default=1000)
    args = parser.parse_args()
    main(i_sdf=args.input_file, o_sdf=args.output_file, prepare_molecules=args.prepare_molecules,
         zwitter=args.zwitter, ring_chain=args.ring_chain, keto_enol=args.keto_enol, limit=args.limit)


