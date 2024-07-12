import re
import os
from pathlib import Path
import shutil
from pypinyin import lazy_pinyin
from omoospace.types import PathLike
from omoospace.validators import is_autosave, is_number, is_version, is_recovered, is_buckup
from omoospace import pyperclip


def format_name(string: str):
    def is_semantic(string: str):
        return (not is_number(string)) \
            and (not is_version(string)) \
            and (not is_autosave(string)) \
            and (not is_recovered(string)) \
            and (not is_buckup(string))

    # get rid of no semantic string parts.
    string = " ".join([s for s in string.split(' ')
                       if is_semantic(s)])
    string = "_".join([s for s in string.split('_')
                       if is_semantic(s)])
    string = ".".join([s for s in string.split('.')
                       if is_semantic(s)])

    # [A-Za-z0-9_-] only
    string = re.sub(r'[^\w-]', ' ', string)

    # Chinese character to pinyin
    string = ' '.join([
        string
        for string in string.split()
        for string in lazy_pinyin(string)
    ])

    # to PascalCase
    string = ' '.join([
        string.title() if string.islower() else string
        for string in string.split()
    ])
    string = '_'.join([
        string.title() if string.islower() else string
        for string in string.split("_") if string != ''
    ])

    string = string.replace(" ", "")
    return string


def remove_duplicates(list, key):
    seen = set()
    new_list = []
    for d in list:
        if d[key] not in seen:
            seen.add(d[key])
            new_list.append(d)
    return new_list


def reveal_in_explorer(dst: PathLike):
    """Open the directory in file exploarer

    Args:
        dst (PathLike): The directory want to open
    """
    try:
        os.startfile(Path(dst))
    except Exception as err:
        print("Fail to reveal", err)


def is_subpath(child: PathLike, parent: PathLike, or_equal=False) -> bool:
    """Return True if child is a subpath of parent .

    Args:
        child (PathLike): Child path
        parent (PathLike): Parent path
        or_equal (bool, optional): [description]. Defaults to False.

    Returns:
        bool: Result.
    """
    parent = Path(parent).resolve()
    child = Path(child).resolve()
    is_subpath = parent in child.parents
    is_equal = parent == child
    if or_equal:
        return is_subpath or is_equal
    else:
        return is_subpath


def copy_to(src: PathLike, dst: PathLike):
    """Copies the contents form src to dst .

    Args:
        src (Path): [description]
        dst (Path): [description]
    """
    src = Path(src).resolve()
    dst = Path(dst).resolve()
    dst.parent.mkdir(parents=True, exist_ok=True)
    if src.is_dir():
        shutil.copytree(src, dst)
    else:
        shutil.copy(src, dst)


def copy_to_clipboard(string: str):
    """Copy to clipboard

    Args:
        string (str): The string want to be copyed.
    """

    pyperclip.copy(string)


def rm_children(dir: PathLike):
    dirpath = Path(dir).resolve()
    for child in dirpath.iterdir():
        if child.is_file():
            child.unlink()
        else:
            shutil.rmtree(child, ignore_errors=True)
