import os
import shutil
import json

def check_true(option):
    """Check if option is true.

    Account for user inputting "yes", "Yes", "True", "Y" ...
    """
    option = option.lower()
    if 'y' in option or 't' in option:
        return True
    else:
        return False

def process_bibtex(bibtex, tex_root):
    """Act on ``bibtex`` option.

    Parameters
    ----------
    bibtex : bool
        If True, nothing is done.
        Else, delete dabib.bib
    tex_root : str
        Path to root of LaTeX project.
    """
    if bibtex:
        return
    bibtex_path = os.path.join(tex_root, 'biblio.bib')
    os.remove(bibtex_path)


def delete_temp(tex_root):
    """Delete figs/README.txt"""
    readme_path = os.path.join(tex_root, 'figs/used/','README.txt')
    os.remove(readme_path)

if __name__ == '__main__':
    # TODO: Include conditional for tex root.
    tex_root = os.getcwd()
    # tex_root = os.path.join(os.getcwd(),'tex')
    # with open('options.json','r') as f:
    #     options = json.load(f)
        # process_bibtex(check_true(options['bibtex']), tex_root)
        # process_nomencl(check_true(options['nomenclature']), tex_root)
    delete_temp(tex_root)
