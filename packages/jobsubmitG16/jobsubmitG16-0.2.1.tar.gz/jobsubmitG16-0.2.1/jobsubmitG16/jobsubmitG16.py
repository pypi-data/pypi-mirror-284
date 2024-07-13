# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 21:58:16 2024

@author: Mohammed A. Jabed 
This script is written for bulk Gaussing job submission in NDSU CCAST Prime 
It can be used in different environments by modifying the default Gaussian module and other related job scheduler variables.

"""

import os,  sys
from glob import glob 
from argparse import ArgumentParser 


top_dir=os.getcwd()
heavy_atom = ECP_list = [ 'Pt', 'Ir', 'Ru', 'Cd', 'Se', 'Pb', 'Ag', 'Cu', 'Ni', 'Fe','Co','Cr','Os' ]  #List of the element for which lanl2dz basis function will be used 


ccast_pbs_gaussian='''#!/bin/bash
#PBS -q default
#PBS -N _NAME
#PBS -j oe
#PBS -l select=_CORE:ncpus=_CPUS:mem=_MEMgb
#PBS -l walltime=_HOURS:_MINS:_SECOND
#PBS -m abe
#PBS -W group_list=x-ccast-prj-_GROUP 

## load Gaussian16 
module load gaussian/16-c02-avx2
name=_NAME
export G16_INPUT=_NAME.com
export G16_OUTPUT=_NAME.out
export GAUSS_SCRDIR=/mmfs1/scratch/$USER/gaussian_jobs/g16.$PBS_JOBID
mkdir -p $GAUSS_SCRDIR

# Gaussian internal variable, Helpful in very large cubegen calculations 
#export GAUSS_MEMDEF=20GB
#export GAUSS_MDEF=20GB

cd $PBS_O_WORKDIR

## sleep time to help avoid authentication errors when running on multiple nodes
sleep 5

# Replacing with correct %LindaWorkers entry in your Gaussian input file
if [ -f nodefile.dat ]; then
 rm -rf nodefile.dat
fi

for i in `uniq $PBS_NODEFILE`;do ssh $i "hostname" >> nodefile.dat;done
sed -i 's/$/-ib/g' nodefile.dat
export LINDA=`cat nodefile.dat | tr -s "\n" "," | sed "s/,$//"`
sed -i "/%LindaWorkers/c %LindaWorkers=$LINDA" $G16_INPUT

g16 < $G16_INPUT > $G16_OUTPUT

rm -rf nodefile.dat $GAUSS_SCRDIR 


'''

def get_inputfiles(ftype = ".com", **kwargs) : 
    f_files = glob("*{}".format(ftype)) 
    return f_files 

def get_coord(name, **kwargs): 
    
    if kwargs['ftype'] == "xyz": 
        with open(name) as myfile: 
            natoms = int(myfile.readline() )
            myfile.readline() 
            coord = [] 
            for i in range(natoms): 
                coord.append(myfile.readline()) 
            return coord 

    if kwargs['ftype'] == "com": 
        f = open(name) 
        line =  f.readline() 
        while line: 
            if line.lstrip()[:1] =="#":
                keys=""
                while line: 
                    keys = keys+ ' ' + line.strip()
                    line=f.readline()
                    if len(line.strip()) == 0:
                        break 
                commentline = f.readline() 
                line = f.readline() 
                charge, multi= [int(j) for j in f.readline().split()]  
                coord = [] 
                while line: 
                    line = f.readline() 
                    if len(line.strip()) ==0 : 
                        f.seek(0,2) 
                    else: coord.append(line)
            else: line=f.readline() 
        print(keys) 
        return keys, charge, multi, coord 

def write_com(name,coord, keys=None, _charge=None, _multiplicity=None, **kwargs):
    global top_dir, heavy_atom 

    elements = set([i.split()[0] for i in coord if len(i.strip())!=0]) 
    light_elem = [i for i in elements if i not in heavy_atom] 
    ecp_elem = [i for i in elements if i in heavy_atom] 
    
    if len(ecp_elem) ==0: 
        func_basis = "{}/{}".format(kwargs['functional'],kwargs['basis']) 
    else: 
        func_basis = "{}/gen".format(kwargs['functional']) 

    Header = " %mem={}GB \n %nprocshared={} \n %chk={}.chk \n\n".format(kwargs['mem'],kwargs['ncpus'],name) 

    f = open("{}.com".format(name),'w') 
    f.write(Header) 
    if kwargs['keyincom'] == True: 
        f.write("{} \n\n".format(keys)) 
    else: 
        f.write("#p opt s{} nosymm {}".format(func_basis, kwargs['other']))
        if kwargs['solvent'] != None:
            f.write(" scrf=(solvent={}) ".format(kwargs["solvent"])) 
        if kwargs['nscf'] != None:  
            f.write(" scf=maxcycles={} ".format(kwargs["nscf"])) 

    f.write("\n\n{}\n\n{} {} \n".format(name,_charge, _multiplicity)) 
    for line in coord: 
        f.write(line)
    f.write('\n')

    if len(ecp_elem) ==0:
        ecp_block = "\n\n\n\n\n"
    else: 
        ecp_block = '''%s 0
%s 
****
%s 0
%s
****

%s  0
%s 
\n\n\n''' %(" ".join(ecp_elem),kwargs['basis_tran'], " ".join(light_elem),kwargs['basis'], " ".join(ecp_elem),kwargs['basis_tran'] ) 
    f.write(ecp_block) 
    f.close() 

def write_pbs(name, pbs = ccast_pbs_gaussian, **kwargs): 
    f = open("{}.pbs".format(name),'w')
    f.write(ccast_pbs_gaussian) 
    f.close() 
    
    os.system("sed -i 's/_NAME/{}/g' {}.pbs ".format(name,name))
    os.system("sed -i 's/_CORE/{}/g' {}.pbs ".format(kwargs['core'],name))
    os.system("sed -i 's/_CPUS/{}/g' {}.pbs ".format(kwargs['ncpus'],name))
    os.system("sed -i 's/_MEM/{}/g' {}.pbs ".format(kwargs['mem'],name))
    os.system("sed -i 's/_HOURS/{}/g' {}.pbs ".format(kwargs['hours'],name))
    os.system("sed -i 's/_MINS/{}/g' {}.pbs ".format(kwargs['mints'],name))
    os.system("sed -i 's/_SECOND/{}/g' {}.pbs ".format(kwargs['seconds'],name))
    os.system("sed -i 's/_GROUP/{}/g' {}.pbs ".format(kwargs['group'],name))
    
    
def main(): 
    global top_dir, heavy_atom 
    
    parser = ArgumentParser()
    parser.add_argument("-com", dest="com", action='store_true', 
                        help="if input files are com format")
    parser.add_argument("-xyz", dest="xyz", action='store_true', 
                        help="if input files are xyz format") 
    parser.add_argument("-gjf", dest="gjf", action='store_true',
                        help="if input files are gjf format") 
    parser.add_argument("-keyincom", dest="keyincom",action='store_true',
                        help="Should options read from input files?")
    parser.add_argument("-formatcom", dest="formatcom",action='store_true',
                        help="To generate com from xyz or format com file.")
    parser.add_argument("-nopbs", dest="nopbs",action='store_true',
                        help="Only format xyz, nor pbs writing or submission") 
    parser.add_argument("-nojobsub", dest="nojobsub",action='store_true',
                        help="job submit or not, default will be submitted")

    parser.add_argument("--core", dest="core", action='store', type=int, default=1,
                            help="number of core, LINDA is not included yet") 
    parser.add_argument("--mem", dest="mem", action='store', type=int, default=10,
                            help="Memory to use, default 10GB") 
    parser.add_argument("--ncpus", dest="ncpus", action='store', type=int, default=16,
                        help="Number of processors to use, default 16") 
    parser.add_argument("--functional", dest="functional", action='store', default='pbe1pbe',
                        help="Functional") 
    parser.add_argument("--solvent", dest="solvent", action='store',  default=None,
                        help="Solvent name")
    parser.add_argument("--basis", dest="basis", action='store', default='6-31g*', 
                        help="Basis set for lighter molecules")
    parser.add_argument("--basis_tran", dest="basis_tran", action='store', default="Lanl2dz",
                        help="Basis name for heaver atoms, same ECP will be use")
    parser.add_argument("--nscf", dest="nscf", action='store', type=int, default=None,
                        help="max scf cycles, Gaussian default is 129")

    parser.add_argument("--nstate", dest="nstate", action='store', type=int,  default=70,
                        help="number of scf cycles on the TDDFT caculation")
    parser.add_argument("--charge", dest="charge", action='store', type=int, default=None,
                        help="for xyz file only. Charge of the model.")
    parser.add_argument("--multiplicity", dest="multiplicity", action='store', type=int, default=None,
                        help="Multiplicity of the system, otherwise read from .com file")
    parser.add_argument("--other", dest="other", action='store', type=str, default=' ',
                        help="All other keys that not listed avobe, as a complete string")

    parser.add_argument("--hours", dest="hours", action='store', type=int, default=23,
                        help="Hours to request")
    parser.add_argument("--mints", dest="mints", action='store', type=int, default=00,
                        help="Time in minutes ")
    parser.add_argument("--seconds", dest="seconds", action='store', type=int, default=00,
                        help="Time in second") 
    parser.add_argument("--queue", dest="queue", action='store', type=str, default='default',
                        help="queue name")
    parser.add_argument("--group", dest="group", action='store', type=str, default='kilina',
                        help="user's research group name in ccast")

    (options, args) = parser.parse_known_args() 

    if any([options.xyz,options.com, options.gjf]): 
        if options.com : 
            ftype = "com"
            f_files = get_inputfiles(ftype = ".com", top_dir = top_dir) 
        elif options.xyz:
            ftype="xyz" 
            f_files = get_inputfiles(ftype=".xyz", top_dir=top_dir) 
        elif options.gjf:
            ftype="gjf"
            f_files = get_inputfiles(ftype=".gjf", top_dir=top_dir)
    else: 
        f_files = glob("*.com") + glob("*.gjf") 
        _files = [i[:-4] for i in f_files] 
        if len(_files) != len(set(_files)): 
            print("\n----------\nSame name are exist with both com and gjf extension.\n Remove duplicate or run with a given file type. \n----------") 
            sys.exit() 

    print("---------------\nfollowing input files are found, total {}".format(len(f_files)))
    print(f_files)
    print("\n---------------\n")

    for f in f_files: 
        print("Working on the model {}".format(f)) 
        name   = os.path.splitext(os.path.basename(f))[0] 
        job_dir = os.path.join(top_dir,name)
        os.mkdir(job_dir)

        if options.xyz:  
            coord = get_coord(f,ftype = "xyz") 
            if any([options.charge == None, options.multiplicity==None]): 
                print("\n----------\nCharge and Multiplicity are required if given files are in xyz format.\n Run again. \n----------") 
            sys.exit() 
        else: 
            keys, charge,  multiplicity, coord = get_coord(f,ftype = "com")
            if not options.charge == None: 
                charge = options.charge 
            if not options.multiplicity == None: 
                multiplicity = options.multiplicity
        os.chdir(job_dir) 
        if options.formatcom:  
            write_com(name,coord,keys=keys,_charge=charge,_multiplicity=multiplicity, **vars(options))
        else: os.system('cp ../{} .'.format(f)) 
        
        if not options.nopbs: 
            write_pbs(name,**vars(options))
        if not options.nojobsub: 
            os.system('qsub {}.pbs'.format(name)) 
 
        os.chdir(top_dir) 


if __name__ == "__main__":
    main()  
