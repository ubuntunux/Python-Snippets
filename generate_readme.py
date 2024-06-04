import os

docs_title = 'Python Snippets'
document_dirname = 'docs'
image_dirname = 'img'
markdown_ext = '.md'
contents_filename = 'README' + markdown_ext

def generate_contents(dirpath, dirnames, filenames):
    if os.path.split(dirpath)[1] == image_dirname:
        return

    contents_list = []

    for filename in filenames:
        if filename != contents_filename and os.path.splitext(filename)[1] == markdown_ext:
            content_name = os.path.splitext(filename)[0]
            if content_name not in dirnames:
                content_path = filename.replace(' ', '%20')
                contents_list.append(f'- [{content_name}]({content_path})')

    for dirname in dirnames:
        if dirname != image_dirname:
            content_name = dirname
            #content_path = os.path.join(dirname, contents_filename).replace(' ', '%20')
            content_path = dirname.replace(' ', '%20')
            contents_list.append(f'- [> {content_name}]({content_path})')

    contents_list.sort()
    contents_filepath = os.path.join(dirpath, contents_filename)

    with open(contents_filepath, 'w') as f:
        title = dirpath.replace(document_dirname, docs_title, 1)
        tokens = title.split('/')
        num_tonkens = len(tokens)
        parent_pages = []
        for (i, token) in enumerate(tokens):
            if (num_tonkens - 1) == i:
                parent_pages.append(token)
            else:
                parent_page_filename = ('../' * (num_tonkens - 1 - i)) + contents_filename
                parent_pages.append(f'[{token}]({parent_page_filename})')
        f.write(f"### {' / '.join(parent_pages)}\n")
        f.write('\n'.join(contents_list))
    print(f'write: {contents_filepath}')

if __name__ == '__main__':
    for (dirpath, dirnames, filenames) in os.walk(document_dirname):
        generate_contents(dirpath, dirnames, filenames)