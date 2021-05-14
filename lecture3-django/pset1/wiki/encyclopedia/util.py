import re

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

def list_entries(s = ''):
    """
    Returns a list of all names of encyclopedia entries
    """
    _, filenames = default_storage.listdir("entries")
    
    if s == '':
        return list(sorted(get_entryName(filename) 
                    for filename in filenames if filename.endswith(".md"))) 
    else:
        return list(sorted(get_entryName(filename) 
                    for filename in filenames if filename.endswith(".md") and s in get_entryName(filename))) 

def save_entry(title, content):
    """
    Saves an encyclopedia entry, given its title and Markdown
    content. If an existing entry with the same title already exists,
    it is replaced.
    """
    filename = f"entries/{title}.md"
    
    if default_storage.exists(filename):
        return False
        """default_storage.delete(filename)"""
    if default_storage.save(filename, ContentFile(content)):
        return True
    else:
        return False


def get_entry(title):
    """
    Retrieves an encyclopedia entry by its title. If no such
    entry exists, the function returns None.
    """
    try:
        f = default_storage.open(f"entries/{title}.md")
        return f.read().decode("utf-8")
    except FileNotFoundError:
        return None

def get_SearchEntry(title):
    """
    Search function.
    """

    filename = f"entries/{title}.md"
    if default_storage.exists(filename):
        get_entry(title)

def get_entryName(filename):
    return re.sub(r"\.md$", "", filename) 