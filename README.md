The ```pdb_box.py``` file determines the dimensions of the system for parameters and topology files.

The ```tleap_error_fix.py``` will fix errors in residues that tleap produces. The ```error_report.txt``` file is a sample file of the tleap errors that can be used for the ```-e``` flag. I looked into as many residue errors that tleap may face when using a PDB file produced by schrodinger, but you can easily manipulate the script to add other potential errors that you come across.
