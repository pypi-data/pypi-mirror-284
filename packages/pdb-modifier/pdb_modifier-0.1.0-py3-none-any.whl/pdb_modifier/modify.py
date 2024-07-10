# pdb_modifier/pdb_modifier/modify.py
def modify_pdb(input_file, output_file):
    """
    Reads a PDB file, adds " F F F" to the end of each coordinate line
    after the "Direct" keyword, and saves the changes to a new file.

    Args:
        input_file (str): The path to the input PDB file.
        output_file (str): The path to save the modified PDB file.
    """

    with open(input_file, 'r') as f_in:
        lines = f_in.readlines()

    with open(output_file, 'w') as f_out:
        direct_section = False
        for line in lines:
            if line.startswith("Direct"):
                direct_section = True
                f_out.write(line)  
            elif direct_section:
                f_out.write(line.rstrip('\n') + " F F F\n") 
            else:
                f_out.write(line) 