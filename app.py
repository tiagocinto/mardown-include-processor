import click

MD_DIR='md'

def read_include(include_file):
    with open(f'{MD_DIR}/{include_file}') as f:
        include_content = f.read()
    return include_content

def save_processed_md_file(processed_content, base_md_file):
    processed_md_file_name = f'{MD_DIR}/processed_{base_md_file}'
    with open(processed_md_file_name, 'w') as f:
        f.write(processed_content)
    print(f'processed content saved to {MD_DIR}/{processed_md_file_name}')

@click.command()
@click.option(
    "--base_md_file",
    type=str,
    help="The base md file having the include snippets ([include]).",
)
def process_base_md_file(base_md_file):
    processed_content = ''
    with open(f'{MD_DIR}/{base_md_file}') as f:
        for line in f:
            if "[include]" in line.strip():
                processed_content += read_include(line.strip().split("[include]")[1]) 
            else:
                processed_content += f'{line.strip()}\n' 
    save_processed_md_file(processed_content, base_md_file)

if __name__ == "__main__":
    process_base_md_file()
