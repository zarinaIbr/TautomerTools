import os
from subprocess import call
import argparse
from tempfile import mkdtemp
from shutil import rmtree
from pathlib import Path

os.environ['JAVA_HOME'] = '/usr/lib/jvm/java-11-openjdk-amd64'
os.environ['JVM_PATH'] = '/usr/lib/jvm/java-11-openjdk-amd64/lib/server/libjvm.so'


def main(i_sdf, o_sdf, c, n, g, M, d, D, m, l, H, a, C, e, P, T, L, E, s, r):
    work_dir = Path(mkdtemp(prefix='tau_'))
    file = work_dir / 'sdf_mol.mol'

    # convert sdf to mol format
    params1 = ["molconvert", "mol", i_sdf, "-o", file]
    exit = call(params1)
    if exit != 0:
        raise ValueError('Conversion SDF to MOL format didnt work')
    params2 = ['cxcalc', 'tautomers', '-f', 'sdf', file, '-c', c, '-n', n, '-g', g, '-M', M, 'd', d, 'D', D,
               'm', m, 'l', l, 'H', H, 'a', a, 'C', C, 'e', e, 'P', P, 'T', T, 'L', L, 'E', E, 's', s, 'r', r]
    with open(o_sdf, 'w') as f:
        call(params2, stdout=f)
    rmtree(work_dir)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Tautomer_chemaxon")
    parser.add_argument("-i", "--input_file", type=str, required=True, help="Input SDF file")
    parser.add_argument("-o", "--output_file", type=str, required=True, help="Output SDF file")
    parser.add_argument("-с", "--canonical", type=str, default=False)
    parser.add_argument("-n", "--normal", type=str, default=False)
    parser.add_argument("-g", "--generic", type=str, default=False)
    parser.add_argument("-M", "--major", type=str, default=False)
    parser.add_argument("-d", "--dominants", type=str, default=True)
    parser.add_argument("-D", "--distribution", type=str, default=False)
    parser.add_argument("-m", "--max", type=str, default=200)
    parser.add_argument("-l", "--pathlength", type=str, default=4)
    parser.add_argument("-H", "--pH", type=str)
    parser.add_argument("-a", "--protectaromaticity", type=str, default=True)
    parser.add_argument("-C", "--protectcharge", type=str, default=True)
    parser.add_argument("-e", "--excludeantiaroma", type=str, default=True)
    parser.add_argument("-P", "--protectdoublebondstereo", type=str, default=False)
    parser.add_argument("-T", "--protectalltetrahedralcenters", type=str, default=False)
    parser.add_argument("-L", "--protectlabeledtetrahedralcenters", type=str, default=False)
    parser.add_argument("-E", "--protectestergroups", type=str, default=True)
    parser.add_argument("-s", "--symfilter", type=str, default=True)
    parser.add_argument("-r", "--ring", type=str, default=False)
    args = parser.parse_args()
    main(i_sdf=args.input_file, o_sdf=args.output_file,
         c=args.canonical, n=args.normal, g=args.generic, M=args.major, d=args.dominants, D=args.distribution,
         m=args.max, l=args.pathlength, H=args.pH, a=args.protectaromaticity, C=args.protectcharge,
         e=args.excludeantiaroma, P=args.protectdoublebondstereo, T=args.protectalltetrahedralcenters,
         L=args.protectlabeledtetrahedralcenters, E=args.protectestergroups, s=args.symfilter, r=args.ring)

