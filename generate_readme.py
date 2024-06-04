import os
import traceback
import re

re_title = re.compile('#+ (.+)')
docs_title = 'Python Snippets'
document_dirname = 'docs'
image_dirname = 'img'
markdown_ext = '.md'
readme_filename = 'README' + markdown_ext
previous_url = f'[Previous](..)'


class Content:
    def __init__(self, dirpath, content, is_file):
        self._dirpath = dirpath
        self._content = content
        self._is_file = is_file
        self._content_name = os.path.splitext(content)[0] if is_file else content
        self._content_path = os.path.join(dirpath, content)
        self._children = []

        # validate document
        if is_file:
            with open(self._content_path, 'r') as f:
                contents = f.read().split('\n')
                modified = False

                # check previous
                if len(contents) < 1 or not contents[0].startswith(previous_url):
                    contents.insert(0, previous_url)
                    modified = True

                # check title
                if 1 < len(contents) and contents[1].startswith('#'):
                    m = re_title.match(contents[1])
                    if m:
                        self._content_name = m.groups()[0]
                    else:
                        self._content_name = contents[1]
                else:
                    # insert document title
                    contents.insert(1, f'## {self._content_name}')
                    modified = True

                if modified:
                    try:
                        with open(self._content_path, 'w') as f:
                            f.write('\n'.join(contents))
                    except:
                        print(traceback.format_exc())

        # validate filename
        for x in ':;"?/\\[]<>':
            if x in content:
                print(f'Error: invalidate filename: {self._content_path}')
                break

    def __lt__(self, other):
        return self._content < other._content

    def __str__(self):
        return f'dirpath: {self._dirpath}, content: {self._content}'

    def get_content_url(self, root_path):
        relative_content_path = os.path.relpath(self._content_path, root_path)
        tab = '\t' * (relative_content_path.count('/'))
        content_path = relative_content_path.replace(' ', '%20')
        return f'{tab}- [{self._content_name}]({content_path})'

def generate_contents_tree(content_map, dirpath, dirnames, filenames):
    parent_content = content_map[dirpath]

    for filename in filenames:
        if filename != readme_filename and os.path.splitext(filename)[1] == markdown_ext:
            content_name = os.path.splitext(filename)[0]
            if content_name not in dirnames:
                content = Content(dirpath=dirpath, content=filename, is_file=True)
                parent_content._children.append(content)
                content_path = os.path.join(dirpath, filename)
                content_map[content_path] = content

    for dirname in dirnames:
        if dirname != image_dirname:
            content = Content(dirpath=dirpath, content=dirname, is_file=False)
            parent_content._children.append(content)
            content_path = os.path.join(dirpath, dirname)
            content_map[content_path] = content

    parent_content._children.sort()

def gather_contents(root, content, contents_list):
    if root != content:
        contents_list.append(content.get_content_url(root._content_path))
    for child in content._children:
        gather_contents(root, child, contents_list)

def write_to_read(content):
    if content._is_file or len(content._children) < 1:
        return

    # recursive gather contents
    contents_list = []
    gather_contents(content, content, contents_list)

    content_dirpath = os.path.join(content._dirpath, content._content)
    readme_filepath = os.path.join(content_dirpath, readme_filename)
    with open(readme_filepath, 'w') as f:
        title = content_dirpath.replace(document_dirname, docs_title, 1)
        tokens = title.split('/')
        num_tonkens = len(tokens)
        parent_pages = []
        for (i, token) in enumerate(tokens):
            if (num_tonkens - 1) == i:
                parent_pages.append(token)
            else:
                parent_page_filename = ('../' * (num_tonkens - 1 - i)) + readme_filename
                parent_pages.append(f'[{token}]({parent_page_filename})')
        f.write(f"### {' / '.join(parent_pages)}\n")
        f.write('\n'.join(contents_list))
    print(f'write: {readme_filepath}')

    # recursive write to readme
    for child in content._children:
        write_to_read(child)

def clean_up_empty_directory(path):
    for x in os.listdir(path):
        content = os.path.join(path, x)
        if os.path.isdir(content):
            clean_up_empty_directory(content)

    contents = [x for x in os.listdir(path)]
    if len(contents) == 1 and contents[0] == readme_filename:
        try:
            readme_filepath = os.path.join(path, readme_filename)
            os.remove(readme_filepath)
            contents = []
            print(f'clean_up_directory: {readme_filepath}')
        except:
            pass

    if not contents:
        try:
            os.removedirs(path)
            print(f'clean_up_directory: {path}')
        except:
            pass

if __name__ == '__main__':
    # make root content
    root_path = ''
    root = Content(dirpath=root_path, content=document_dirname, is_file=False)
    root_content_path = os.path.join(root_path, document_dirname)
    content_map = {root_content_path: root}

    # clean-up directories
    clean_up_empty_directory(root_content_path)

    # build content tree
    for (dirpath, dirnames, filenames) in os.walk(document_dirname):
        if os.path.split(dirpath)[1] != image_dirname:
            generate_contents_tree(content_map, dirpath, dirnames, filenames)

    # recursive write readme
    write_to_read(root)