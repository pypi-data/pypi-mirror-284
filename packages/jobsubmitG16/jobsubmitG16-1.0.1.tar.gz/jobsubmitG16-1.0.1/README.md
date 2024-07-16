# jobsubmitG16
This Python program can edit Gaussian input files, generate PBS scripts, and submit jobs to NDSU CCAST Prime HPC.
It can be used for other HPCs by change default PBS environmental variables

### Installation  
`pip install jobsubmitG16`

## Running jobsubmitG16 
```
python -m jobsubmitG16 [-options] [values] 
some options are mutually exclusive
```

* `-com` raw input files are in in g16 format with com extension 
* `-gjf` raw input files are in in g16 format with gjf extension
* `-xyz` raw input files are in in xyz format with xyz extension
* `-keyincom` Read Gaussian option keys from com/gjf files. Not applicable for xyz files 
* `-formatcom` Format com/gjf files if True, else False 
* `-nopbs` No pbs file if True 
* `-nojobsub` Jobs will be prepared but won't be submitted if True 

###Resource setup 
* `--queue` Queue name, type: `str`, default `default`  
* `--group` Research group ID in Prime, type: `str`, default `kilina`  
* `--core` Number of Core to request, type: `int`, default `1`  
* `--mem` Memory in GB to use, type: `int`, default `10gb`
* `--ncpus` Number of CPUs to request, type: `int`, default `16`
* `--hours` Time request, Hours. type: `int`, default: `23`
* `--mints` Time request, Minutes, type: `int`, default `00`
* `--seconds` Time request, seconds, type: `int`, default `00` 

###Gaussian options
* `--functional` Functional name, default `pbe1pbe`
* `--solvent` Solvent name, default `no solvent`
* `--basis` Basis name for ligher elements, default `6-31g*`
* `--basis_tran` Basis name for transition metals, default `Lanl2dz`
* `--nscf` Number of max SCF cycles, default `129`

### About the model 
* `--charge` Charge of the model, if not read from com file. No default
* `--multiplicity` multiplicity of the model if not read from com file. No default
* `--other` All other keys not listed, input as full string. No default

---
##### Pipeline features:
* adding options to check errors after optimization calculation 
* Continue job for TDDFT calculation if optimization terminate normal
---

#### License: 
jobsubmitG16 is freely available under an [MIT](https://opensource.org/licenses/MIT) License
