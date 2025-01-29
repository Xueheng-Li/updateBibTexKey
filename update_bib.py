from fuzzywuzzy import fuzz
import bibtexparser
import re
import fileinput
from pathlib import Path

# old_bibs are the old bib files, new_bib is the new bib file, and tex_file_to_update is the tex file to update
old_bibs = [
    'path/to/old_bib1.bib',
    'path/to/old_bib2.bib',
]
new_bib = 'path/to/new_bib.bib'
tex_file_to_update = 'path/to/tex_file.tex'


def load_bib_entries(bib_file):
    """Load bib file and return dict of {title: key}"""
    with open(bib_file) as f:
        bib_db = bibtexparser.load(f)
    
    entries = {}
    for entry in bib_db.entries:
        if 'title' in entry:
            # Normalize title by removing spaces and converting to lowercase
            title = entry['title'].lower().replace(' ', '')
            entries[title] = entry['ID']
    return entries

def create_key_mapping(old_bib, new_bib, bar=90):
    """Create mapping between old and new citation keys based on paper titles"""
    old_entries = load_bib_entries(old_bib)
    new_entries = load_bib_entries(new_bib)
    
    mapping = {}
    for old_title, old_key in old_entries.items():
        # Find best matching title in new entries
        best_match = None
        best_ratio = 0
        
        for new_title in new_entries.keys():
            ratio = fuzz.ratio(old_title, new_title)
            if ratio > best_ratio and ratio > bar:  # threshold of bar%
                best_ratio = ratio
                best_match = new_title
        
        if best_match:
            mapping[old_key] = new_entries[best_match]
    
    return mapping

def create_key_mapping_multi(old_bibs, new_bib, bar=90):
    """Create mapping from multiple old bib files to new citation keys"""
    mapping = {}
    new_entries = load_bib_entries(new_bib)
    # Get all keys from new bib
    new_keys = set(new_entries.values())
    
    # Process each old bib file in sequence
    for old_bib in old_bibs:
        old_entries = load_bib_entries(old_bib)
        
        for old_title, old_key in old_entries.items():
            # Skip if we already found a mapping or key exists in new bib
            if old_key in mapping or old_key in new_keys:
                continue
                
            # Find best matching title in new entries
            best_match = None
            best_ratio = 0
            
            for new_title in new_entries.keys():
                ratio = fuzz.ratio(old_title, new_title)
                if ratio > best_ratio and ratio > bar:
                    best_ratio = ratio
                    best_match = new_title
            
            if best_match:
                mapping[old_key] = new_entries[best_match]
    
    return mapping

def update_tex_file(tex_file, key_mapping):
    """Update citations in tex file with backup"""
    backup_file = tex_file + '.bak'
    Path(tex_file).rename(backup_file)
    
    citation_patterns = [
        r'\\cite{([^}]*)}', 
        r'\\citep{([^}]*)}', 
        r'\\citet{([^}]*)}', 
        r'\\citeauthor{([^}]*)}', 
        r'\\citeyear{([^}]*)}',
        r'\\citep\[[^\]]*\]{([^}]*)}',  # Pattern for \citep with optional text
        r'\\citep\[[^\]]*\]\[[^\]]*\]{([^}]*)}'  # Pattern for \citep with multiple optional texts
    ]
    changes = []  # Track changes
    
    with open(backup_file) as infile, open(tex_file, 'w') as outfile:
        for line_num, line in enumerate(infile, 1):
            updated_line = line
            
            for pattern in citation_patterns:
                citations = re.finditer(pattern, line)
                for match in citations:
                    old_keys = match.group(1).split(',')
                    new_keys = [key_mapping.get(k.strip(), k.strip()) for k in old_keys]
                    
                    # Log changes if any key was updated
                    if any(ok != nk for ok, nk in zip(old_keys, new_keys)):
                        changes.append({
                            'line': line_num,
                            'old': old_keys,
                            'new': new_keys
                        })
                    
                    old_citation = match.group(0)
                    new_citation = old_citation.replace(match.group(1), ','.join(new_keys))
                    updated_line = updated_line.replace(old_citation, new_citation)
            
            outfile.write(updated_line)
    
    return changes

def print_change_report(mapping, changes, show_detail=False):

    if show_detail:
        """Print detailed report of citation key changes"""
        print("\nKey Mapping Summary:")
        print("-" * 50)
        for old_key, new_key in mapping.items():
            if old_key != new_key:
                print(f"{old_key} -> {new_key}")
    
    print("\nChanges in TEX file:")
    print("-" * 50)
    for change in changes:
        print(f"Line {change['line']}:")
        old_keys = ', '.join(change['old'])
        new_keys = ', '.join(change['new'])
        print(f"  Old: {old_keys}")
        print(f"  New: {new_keys}\n")

def main(old_bibs, new_bib, tex_file_to_update):
    changes_all = []
    for bar in range(100, 85, -2):
        mapping = create_key_mapping_multi(old_bibs, new_bib, bar=bar)
        changes = update_tex_file(tex_file_to_update, mapping)
        changes_all.extend(changes)
        if len(changes) > 0:
            print_change_report(mapping, changes)
            print(f"Changed {len(changes)} lines with bar={bar}")
        else:
            print(f"No changes made with bar={bar}")
    

if __name__ == '__main__':
    # Run the main function
    main(old_bibs, new_bib, tex_file_to_update)
