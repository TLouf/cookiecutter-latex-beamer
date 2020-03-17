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

def process_bibtex(tex_root):
    """Act on ``bibtex`` option.

    Parameters
    ----------
    bibtex : bool
        If True, nothing is done.
        Else, delete dabib.bib
    tex_root : str
        Path to root of LaTeX project.
    """
    bibtex_path = os.path.join(tex_root, 'biblio.bib')
    os.remove(bibtex_path)


def delete_temp(tex_root):
    """Delete figs/README.txt"""
    readme_path = os.path.join(tex_root, 'figs/used/','README.txt')
    os.remove(readme_path)

{% if cookiecutter.bibtex!="yes" %}
if __name__ == '__main__':
    tex_root = os.getcwd()
    process_bibtex(tex_root)
    delete_temp(tex_root)
{% endif %}

