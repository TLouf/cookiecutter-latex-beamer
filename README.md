# cookiecutter-latex-beamer
A template for preparing LaTeX presentations. 

* Pretty Title Page: fields are automatically populated at project creation. 
* BibTeX: Set up to use BibTeX (IEEE style).
* Standard directory structure. 


## Usage

Install *cookiecutter*:

    pip install cookiecutter

Generate a LaTeX project:

    cookiecutter https://github.com/TLouf/cookiecutter-latex-beamer.git


## Features

### BibTeX

An empty ``biblio.bib`` file is included with the template if you answer positively to ``bibtex``. Bibliography style and insertion at the bottom of ``main.tex``.



### Directory Structure

I like to keep my figures in a separate folder (in this case "figs") and my ``.tex`` files in the same directory as the main. I also like to have my LaTeX files in a subdirectory (in this case "tex") and keep related documents, e.g. an Excel workbook, IPython Notebook or project instructions, in the project's root directory.
