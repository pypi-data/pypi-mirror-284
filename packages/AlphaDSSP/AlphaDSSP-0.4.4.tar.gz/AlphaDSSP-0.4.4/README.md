# AlphaDSSP
 DSSP Analysis for Alphafold Secondary Structure Parsing

This tool generates DSSP secondary structure information and allows masks to be generated that identify specific regions of a protein by secondary structure and confidence. It can be useful when searching for sequence motifs; for example, if you're searching sequences for a short linear motif that must exist in disordered strands (rather than, say, a helix or a beta-strand), you can use AlphaDSSP to make a boolean mask that shows you everywhere in the sequence that cannot contain your motif due to incompatible secondary structure. 

Alphafold provides data as tar shards for organisms by TaxID, which you can download by following the instructions at https://github.com/google-deepmind/alphafold/blob/main/afdb/README.md
To use this tool, you must have a directory containing the tar shards for your organism of interest. 

# Usage

1. Install this tool from PyPI by running the command `pip install alphadssp`
2. Import the main function into your script as `from alphadssp import generate_dssp`
3. Use the main function either with default arguments or your own: `excluded_results = generate_dssp(tar_dir = None, dssp_executable="/usr/bin/dssp", forbidden_codes = ("H","B","E","G","I","T"), plddt_thres=70)`

`dssp_executable` is the path to your local installation of the DSSP program, which generally comes with BioPython
`forbidden_codes` refers to a tuple of DSSP single-letter codes for secondary structures that you want to mask out. For example, if you want to find everything that isn't a disordered strand, this is a tuple of all other non-disordered secondary structure codes. 
`plddt_thres` is the pLDDT confidence threshold required for a predicted forbidden DSSP secondary structure to contribute to the mask of forbidden residues

The output is a dictionary, `excluded_results`, where each key is a base file name (e.g. AF-A0A023HHL0-F1-model_v4). The dict value is a tuple of (mask, dssp_str), where `mask` is a boolean mask of forbidden areas of the sequence containing confidently disallowed secondary structures, and `dssp_str` is a string of DSSP letter codes corresponding to the protein sequence. 
