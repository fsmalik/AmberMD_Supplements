import numpy as np
import pandas as pd
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", required=True, help='input PDB file // FORMAT --> .pdb')
parser.add_argument("-e", "--error", required=True, help='input errors file // FORMAT --> .txt')
parser.add_argument("-o", "--output", required=True, help='output PDB file // FORMAT --> .pdb')
args = parser.parse_args()

initial_read  = open(str(args.input), 'r')
listed_initial_read = list(initial_read)

remark_count = 0

for i in np.arange(0, len(listed_initial_read)):
    if listed_initial_read[i].startswith('REMARK'):
        remark_count = i+1

column_names = ["record_name", "serial_number", "atom_name", "residue", "chain", "res_seq", "orth_x", "orth_y", "orth_z", "occupancy", "temp_factor", "element_plus_charge"]

pdb = pd.read_csv(str(args.input), sep='\t', skiprows=remark_count, header=None, names = column_names)

pdb['serial_number']=pdb['record_name'].str.slice(start=6,stop=11).str.strip()
pdb['atom_name']=pdb['record_name'].str.slice(start=11,stop=16).str.strip()
pdb['residue']=pdb['record_name'].str.slice(start=16,stop=20).str.strip()
pdb['chain']=pdb['record_name'].str.slice(start=20,stop=22).str.strip()
pdb['res_seq']=pdb['record_name'].str.slice(start=22,stop=26).str.strip()
pdb['orth_x']=pdb['record_name'].str.slice(start=30,stop=38).str.strip()
pdb['orth_y']=pdb['record_name'].str.slice(start=38,stop=46).str.strip()
pdb['orth_z']=pdb['record_name'].str.slice(start=46,stop=54).str.strip()
pdb['occupancy']=pdb['record_name'].str.slice(start=54,stop=60).str.strip()
pdb['temp_factor']=pdb['record_name'].str.slice(start=60,stop=66).str.strip()
pdb['element_plus_charge']=pdb['record_name'].str.slice(start=66,stop=79).str.strip()
pdb['record_name']=pdb['record_name'].str.slice(stop=6).str.strip()

# TO DROP
# pdb = pdb[(pdb.residue != 'ACE') | (pdb.atom_name != 'CH3')]

# TO QUERY
# pdb.query("residue=='ACE' and atom_name=='H1'")
# pdb.query("residue=='HIE'")

error_report  = open(str(args.error), 'r')
listed_errors = list(error_report)

uss_enterprise = [];

for i in np.arange(0, len(listed_errors)):
    if listed_errors[i].startswith('Created'):
        uss_enterprise.append([listed_errors[i].split()[5], listed_errors[i].split()[8][3:]])
        
uss_enterprise_errors = []
NMA_errors = []
ACE_errors = []
for error in uss_enterprise:
    if 'ACE' not in error:
        if 'NMA' not in error:
            if error not in uss_enterprise_errors:
                uss_enterprise_errors.append(error)
        
print(uss_enterprise_errors)

#Making Fixes for the Terminals

pdb = pdb[(pdb.residue != 'ACE') | (pdb.atom_name != '1H')]
pdb = pdb[(pdb.residue != 'ACE') | (pdb.atom_name != '2H')]
pdb = pdb[(pdb.residue != 'ACE') | (pdb.atom_name != '3H')]

pdb = pdb[(pdb.residue != 'NMA') | (pdb.atom_name != 'H')]
pdb = pdb[(pdb.residue != 'NMA') | (pdb.atom_name != '1HA')]
pdb = pdb[(pdb.residue != 'NMA') | (pdb.atom_name != '2HA')]
pdb = pdb[(pdb.residue != 'NMA') | (pdb.atom_name != '3HA')]
pdb = pdb[(pdb.residue != 'NMA') | (pdb.atom_name != 'CA')]

pdb.loc[(pdb.residue == 'NMA') & (pdb.atom_name == 'N'), 'residue'] = 'NHE'

# executing this portion of code will change the pdb Data Frame
# you can add other errors to this loop as well
for i in np.arange(0,len(uss_enterprise_errors)):
    qres = uss_enterprise_errors[i][1]
    qatom = uss_enterprise_errors[i][0]
    query_00 = pdb.query("residue==@qres and atom_name==@qatom").to_numpy()

    if qres == 'LEU' and qatom == 'HB':
        for j in np.arange(0,len(query_00)):
            qres_seq = query_00[j][5] # this gives the residue number in sequence of the error
            pdb.loc[(pdb.residue == qres) & (pdb.atom_name == 'HB2') & (pdb.res_seq == qres_seq), 'atom_name'] = 'HB3'
            pdb.loc[(pdb.residue == qres) & (pdb.atom_name == qatom) & (pdb.res_seq == qres_seq), 'atom_name'] = 'HB2'

    if qres == 'GLN' and qatom == 'HB':
        for j in np.arange(0,len(query_00)):
            qres_seq = query_00[j][5] # this gives the residue number in sequence of the error
            pdb.loc[(pdb.residue == qres) & (pdb.atom_name == 'HB2') & (pdb.res_seq == qres_seq), 'atom_name'] = 'HB3'
            pdb.loc[(pdb.residue == qres) & (pdb.atom_name == qatom) & (pdb.res_seq == qres_seq), 'atom_name'] = 'HB2'

    if qres == 'GLU' and qatom == 'HE2':
        for j in np.arange(0,len(query_00)):
            qres_seq = query_00[j][5] # this gives the residue number in sequence of the error
            pdb = pdb[(pdb.residue != qres) | (pdb.atom_name != qatom) | (pdb.res_seq != qres_seq)]

    if qres == 'ASP' and qatom == 'HD2':
        for j in np.arange(0,len(query_00)):
            qres_seq = query_00[j][5] # this gives the residue number in sequence of the error
            pdb = pdb[(pdb.residue != qres) | (pdb.atom_name != qatom) | (pdb.res_seq != qres_seq)]

    if qres == 'ASP' and qatom == 'HB':
        for j in np.arange(0,len(query_00)):
            qres_seq = query_00[j][5] # this gives the residue number in sequence of the error
            pdb.loc[(pdb.residue == qres) & (pdb.atom_name == 'HB2') & (pdb.res_seq == qres_seq), 'atom_name'] = 'HB3'
            pdb.loc[(pdb.residue == qres) & (pdb.atom_name == qatom) & (pdb.res_seq == qres_seq), 'atom_name'] = 'HB2'

    if qres == 'LYS' and qatom == 'HB':
        for j in np.arange(0,len(query_00)):
            qres_seq = query_00[j][5] # this gives the residue number in sequence of the error
            pdb.loc[(pdb.residue == qres) & (pdb.atom_name == 'HB2') & (pdb.res_seq == qres_seq), 'atom_name'] = 'HB3'
            pdb.loc[(pdb.residue == qres) & (pdb.atom_name == qatom) & (pdb.res_seq == qres_seq), 'atom_name'] = 'HB2'

    if qres == 'TYR' and qatom == 'HB':
        for j in np.arange(0,len(query_00)):
            qres_seq = query_00[j][5] # this gives the residue number in sequence of the error
            pdb.loc[(pdb.residue == qres) & (pdb.atom_name == 'HB2') & (pdb.res_seq == qres_seq), 'atom_name'] = 'HB3'
            pdb.loc[(pdb.residue == qres) & (pdb.atom_name == qatom) & (pdb.res_seq == qres_seq), 'atom_name'] = 'HB2'

    if qres == 'THR' and qatom == 'HB2':
        for j in np.arange(0,len(query_00)):
            qres_seq = query_00[j][5] # this gives the residue number in sequence of the error
            pdb.loc[(pdb.residue == qres) & (pdb.atom_name == qatom) & (pdb.res_seq == qres_seq), 'atom_name'] = 'HB'

    if qres == 'THR' and qatom == 'H2':
        for j in np.arange(0,len(query_00)):
            qres_seq = query_00[j][5] # this gives the residue number in sequence of the error
            pdb.loc[(pdb.residue == qres) & (pdb.atom_name == qatom) & (pdb.res_seq == qres_seq), 'atom_name'] = 'H'

    if qres == 'THR' and qatom == 'H1':
        for j in np.arange(0,len(query_00)):
            qres_seq = query_00[j][5] # this gives the residue number in sequence of the error
            pdb.loc[(pdb.residue == qres) & (pdb.atom_name == qatom) & (pdb.res_seq == qres_seq), 'atom_name'] = 'H'

    if qres == 'HIE' and qatom == 'HB':
        for j in np.arange(0,len(query_00)):
            qres_seq = query_00[j][5] # this gives the residue number in sequence of the error
            pdb.loc[(pdb.residue == qres) & (pdb.atom_name == 'HB3') & (pdb.res_seq == qres_seq), 'atom_name'] = 'HB2'
            pdb.loc[(pdb.residue == qres) & (pdb.atom_name == qatom) & (pdb.res_seq == qres_seq), 'atom_name'] = 'HB3'

    if qres == 'TRP' and qatom == 'HB':
        for j in np.arange(0,len(query_00)):
            qres_seq = query_00[j][5] # this gives the residue number in sequence of the error
            pdb.loc[(pdb.residue == qres) & (pdb.atom_name == qatom) & (pdb.res_seq == qres_seq), 'atom_name'] = 'HB2'

    if qres == 'TRP' and qatom == 'H1':
        for j in np.arange(0,len(query_00)):
            qres_seq = query_00[j][5] # this gives the residue number in sequence of the error
            pdb.loc[(pdb.residue == qres) & (pdb.atom_name == qatom) & (pdb.res_seq == qres_seq), 'atom_name'] = 'H'
    
    if qres == 'MET' and qatom == 'H2':
        for j in np.arange(0,len(query_00)):
            qres_seq = query_00[j][5] # this gives the residue number in sequence of the error
            pdb.loc[(pdb.residue == qres) & (pdb.atom_name == qatom) & (pdb.res_seq == qres_seq), 'atom_name'] = 'H'

    if qres == 'ARG' and qatom == 'H1':
        for j in np.arange(0,len(query_00)):
            qres_seq = query_00[j][5] # this gives the residue number in sequence of the error
            pdb.loc[(pdb.residue == qres) & (pdb.atom_name == qatom) & (pdb.res_seq == qres_seq), 'atom_name'] = 'H'

    if qres == 'ALA' and qatom == 'H1':
        for j in np.arange(0,len(query_00)):
            qres_seq = query_00[j][5] # this gives the residue number in sequence of the error
            pdb.loc[(pdb.residue == qres) & (pdb.atom_name == qatom) & (pdb.res_seq == qres_seq), 'atom_name'] = 'H'

    if qres == 'GLU' and qatom == 'H1':
        for j in np.arange(0,len(query_00)):
            qres_seq = query_00[j][5] # this gives the residue number in sequence of the error
            pdb.loc[(pdb.residue == qres) & (pdb.atom_name == qatom) & (pdb.res_seq == qres_seq), 'atom_name'] = 'H'
  
    if qres == 'SER' and qatom == 'H1':
        for j in np.arange(0,len(query_00)):
            qres_seq = query_00[j][5] # this gives the residue number in sequence of the error
            pdb.loc[(pdb.residue == qres) & (pdb.atom_name == qatom) & (pdb.res_seq == qres_seq), 'atom_name'] = 'H'
    
    if qres == 'LEU' and qatom == 'H1':
        for j in np.arange(0,len(query_00)):
            qres_seq = query_00[j][5] # this gives the residue number in sequence of the error
            pdb.loc[(pdb.residue == qres) & (pdb.atom_name == qatom) & (pdb.res_seq == qres_seq), 'atom_name'] = 'H'

    if qres == 'PHE' and qatom == 'H1':
        for j in np.arange(0,len(query_00)):
            qres_seq = query_00[j][5] # this gives the residue number in sequence of the error
            pdb.loc[(pdb.residue == qres) & (pdb.atom_name == qatom) & (pdb.res_seq == qres_seq), 'atom_name'] = 'H'

    if qres == 'GLY' and qatom == 'H1':
        for j in np.arange(0,len(query_00)):
            qres_seq = query_00[j][5] # this gives the residue number in sequence of the error
            pdb.loc[(pdb.residue == qres) & (pdb.atom_name == qatom) & (pdb.res_seq == qres_seq), 'atom_name'] = 'H'

with open(str(args.output), 'w') as f:
    for i, row in pdb.iterrows():
        atom_line = f'{row["record_name"]:<6}{row["serial_number"]:>5}{row["atom_name"]:>5}{row["residue"]:>4}{row["chain"]:>2}{row["res_seq"]:>4}{row["orth_x"]:>12}{row["orth_y"]:>8}{row["orth_z"]:>8}{row["occupancy"]:>6}{row["temp_factor"]:>6}{row["element_plus_charge"]:>12}'+'\n'
        f.write(atom_line)
