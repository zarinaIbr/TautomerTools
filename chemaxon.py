import os
from subprocess import call
import argparse
from tempfile import mkdtemp
from shutil import rmtree
from pathlib import Path

os.environ['JAVA_HOME'] = '/usr/lib/jvm/java-11-openjdk-amd64'
os.environ['JVM_PATH'] = '/usr/lib/jvm/java-11-openjdk-amd64/lib/server/libjvm.so'


def main(i_sdf, o_sdf):
    work_dir = Path(mkdtemp(prefix='tau_'))
    file = work_dir / 'sdf_mol.mol'

    # convert sdf to mol format
    params1 = ["molconvert", "mol", i_sdf, "-o", file]
    exit = call(params1)
    if exit != 0:
        raise ValueError('Conversion SDF to MOL format didnt work')
    params2 = ["cxcalc", "tautomers", "-f", "sdf", file]
    with open(o_sdf, 'w') as f:
        call(params2, stdout=f)
    rmtree(work_dir)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Tautomer_chemaxon")
    parser.add_argument("-i", "--input_file", type=str, required=True, help="Input SDF file")
    parser.add_argument("-o", "--output_file", type=str, required=True, help="Output SDF file")
    args = parser.parse_args()
    main(i_sdf=args.input_file, o_sdf=args.output_file)

