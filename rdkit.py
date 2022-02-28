import argparse
from CGRtools import SDFWrite
from rdkit.Chem.MolStandardize.rdMolStandardize import CanonicalTautomer
from rdkit.Chem import SDMolSupplier, SDWriter


def main(i_sdf, o_sdf):
    i_mols = SDMolSupplier(i_sdf)
    with SDWriter(o_sdf) as w:
        for m in i_mols:
            mm = CanonicalTautomer(m)
            w.write(mm)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Tautomer_rdkit")
    parser.add_argument("-i", "--input_file", type=str, required=True, help="Input SDF file")
    parser.add_argument("-o", "--output_file", type=str, required=True, help="Output SDF file")
    args = parser.parse_args()
    main(i_sdf=args.input_file, o_sdf=args.output_file)

