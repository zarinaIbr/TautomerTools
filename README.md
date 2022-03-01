# TautomerTools
## ChemAxon
export JAVA_HOME='/usr/lib/jvm/java-11-openjdk-amd64'
export JVM_PATH='/usr/lib/jvm/java-11-openjdk-amd64/lib/server/libjvm.so'
export CHEMAXON_LICENSE_SERVER_KEY='our_key'
python chemaxon.py -i inp_sdf -o out_sdf -M True
## Ambit
python ambit.py -i inp_sdf -o out_sdf
## Rdkit
python rdkit.py -i inp_sdf -o out_sdf
## Cgrtools
python cgrtools.py -i inp_sdf -o out_sdf
#### Доп.параметры Chemaxon: https://docs.chemaxon.com/display/docs/cxcalc-calculator-functions.md#src-1806682-cxcalccalculatorfunctions-tautomers
#### Доп.параметры Ambit: https://github.com/ideaconsult/apps-ambit/tree/master/tautomers-example
