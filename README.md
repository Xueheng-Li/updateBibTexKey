# Update BibTeX Citations in LaTeX Files

This script updates the citation keys in a LaTeX `.tex` file based on new BibTeX entries. It matches old citation keys to new ones using fuzzy string matching on the titles of the papers.

## Requirements

- Python 3.x
- `fuzzywuzzy` library
- `bibtexparser` library

You can install the required libraries using pip:

```sh
pip install fuzzywuzzy bibtexparser
```

## Usage

1. **Clone the repository:**

   Clone the repository from GitHub:

   ```sh
   git clone https://github.com/Xueheng-Li/updatebib.git
   cd updatebib
   ```

2. **Set the old BibTeX files, new BibTeX file, and the LaTeX file to update:**

   Edit the `main` function call in the script to specify the paths to your old BibTeX files, new BibTeX file, and the LaTeX file you want to update.

   ```python
   if __name__ == '__main__':
       # old_bibs are the old bib files, new_bib is the new bib file, and tex_file_to_update is the tex file to update
       old_bibs = [
           'path/to/old_bib1.bib',
           'path/to/old_bib2.bib',
       ]
       new_bib = 'path/to/new_bib.bib'
       tex_file_to_update = 'path/to/tex_file.tex'

       # Run the main function
       main(old_bibs, new_bib, tex_file_to_update)
   ```

3. **Run the script:**

   Execute the script using Python:

   ```sh
   python update_bib.py
   ```

4. **Check the output:**

   The script will create a backup of your original `.tex` file with a `.bak` extension and update the citations in the original `.tex` file. It will also print a report of the changes made.

## Functions

- `load_bib_entries(bib_file)`: Loads BibTeX entries from a file and returns a dictionary of titles to keys.
- `create_key_mapping(old_bib, new_bib, bar=90)`: Creates a mapping between old and new citation keys based on paper titles.
- `create_key_mapping_multi(old_bibs, new_bib, bar=90)`: Creates a mapping from multiple old BibTeX files to new citation keys.
- `update_tex_file(tex_file, key_mapping)`: Updates citations in a LaTeX file with a backup.
- `print_change_report(mapping, changes, show_detail=False)`: Prints a detailed report of citation key changes.
- `main(old_bibs, new_bib, tex_file_to_update)`: Main function to run the update process.

## Notes

- The script uses fuzzy string matching to find the best match for titles between old and new BibTeX entries.
- The `bar` parameter in the `create_key_mapping` and `create_key_mapping_multi` functions sets the threshold for the fuzzy matching ratio (default is 90%).

Feel free to modify the script as needed for your specific use case.
