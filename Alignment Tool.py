"""Alignment Tool"""

import Bio

SEQUENCE = '1'
ALIGNMENT = '2'
PHYLOGENY = '3'


def prompt_filetype() -> str:
    filetype = input("""Choose the type of file you are dealing with:
    [1] - DNA or Protein Sequence
    [2] - Pairwise or Multiple Sequence Alignment
    [3] - Phylogenetic Tree \n """).strip()
    
    while not (prompt_filtype == SEQUENCE \
          or prompt_filetype == ALIGNMENT \
          or prompt_filetype == PHYLOGENY):
        prompt_filetype = input('''Invalid choice. Please 
        enter [1], [2] or [3]:''').strip()
    return prompt_filetype    

prompt_filetype()