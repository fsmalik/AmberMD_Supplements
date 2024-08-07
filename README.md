The ```pdb_box.py``` file determines the dimensions {x,y,z} of any system (PDB format) which can then be used when generating parameters and topology files.

The ```tleap_error_fix.py``` will fix errors in residues that tleap produces for a PDB file generated by Schrodinger. The ```error_report.txt``` file is a sample file of the tleap errors that can be used for the ```-e``` flag. I looked into as many residue errors that tleap may face when using a PDB file produced by schrodinger, but you can easily manipulate the script to add other potential errors that you come across.

To run either script -> ```python3 [pdb_box.py|tleap_error_fix.py] --help```


The ```ter_addition_for_lipids.sh``` script will add termination records for lipids. When saving PDB files from Chimera, it will remove these records. Using this script will re-insert those records.

```./ter_addition_for_lipids.sh [input-file] [output-file]```
