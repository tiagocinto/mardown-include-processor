# Mardown Include Processor
Simple app that takes a base markdown file as input and includes content from secondary files

## Install
Run `make install`.

# Usage
Suppose you have a `base_file.md` with the following content:
```
# Intro

Lorem ipsum dolor sit amet, consectetur adipiscing elit. 

[include]secondary_file.md

Nullam mollis tellus in libero euismod, eget ultrices enim mollis. 
```

Use the include snippets (`[include]`) to include content from secondary files (e.g., `secondary_file.md`).

Finally, run `python app.py --base_md_file base_file.md`. 

The processed md file will be saved as `processed_base_file.md`.
