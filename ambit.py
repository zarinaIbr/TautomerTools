import os
from subprocess import call
import argparse


os.environ['JAVA_HOME'] = '/usr/lib/jvm/java-11-openjdk-amd64'
os.environ['JVM_PATH'] = '/usr/lib/jvm/java-11-openjdk-amd64/lib/server/libjvm.so'


def main(i_sdf, o_sdf, a, b, c, l, m, n, r, t, z):
    am_jar = 'ambit_tautomers.jar'
    params = ["java", "-", "jar", am_jar, "-f", i_sdf, "-o", o_sdf, "-a", a, "-b", b, "-c", c, "-l", l,
              "-m", m, "-n", n, "-r", r, "-t", t, "-z", z]
    exit = call(params)
    if exit != 0:
        raise ValueError('Error')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Tautomer_ambit")
    parser.add_argument("-i", "--input_file", type=str, required=True, help="Input SDF file")
    parser.add_argument("-o", "--output_file", type=str, required=True, help="Output SDF file")
    parser.add_argument("-a", "--algorithm", type=str, default='comb')
    parser.add_argument("-b", "--benchmark", type=str, default='benchmark.txt')
    parser.add_argument("-c", "--maxsubcombinations", type=str, default=10000)
    parser.add_argument("-l", "--rulenumberlimit", type=str, default=10)
    parser.add_argument("-m", "--maxbacktracks", type=str, default=5000)
    parser.add_argument("-n", "--inchicheck", type=str, default='off')
    parser.add_argument("-r", "--maxregistrations", type=str, default=1000)
    parser.add_argument("-t", "--tautomers", type=str, default='best')
    parser.add_argument("-z", "--isomorphismcheck", type=str, default='on')
    # parser.add_argument("-3", "--rule1_3", type=str, default='on')
    # parser.add_argument("-5", "--rule1_5", type=str, default='on')
    # parser.add_argument("-7", "--rule1_5", type=str, default='off')
    args = parser.parse_args()
    main(i_sdf=args.input_file, o_sdf=args.output_file, a=args.algorithm, b=args.benchmark, c=args.maxsubcombinations,
         l=args.rulenumberlimit, m=args.maxbacktracks, n=args.inchicheck, r=args.maxregistrations,
         t=args.tautomers, z=args.isomorphismcheck)

