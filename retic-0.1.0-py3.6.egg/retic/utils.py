from __future__ import print_function

import ast, traceback, os, sys
from . import typing, flags, exc
from .exc import UnknownTypeError

def copy_assignee(n, ctx):
    if isinstance(n, ast.Name):
        ret = ast.Name(id=n.id, ctx=ctx)
    elif isinstance(n, ast.Attribute):
        ret = ast.Attribute(value=n.value, attr=n.attr, ctx=ctx)
    elif isinstance(n, ast.Subscript):
        ret = ast.Subscript(value=n.value, slice=n.slice, ctx=ctx)
    elif isinstance(n, ast.List):
        elts = [copy_assignee(e, ctx) for e in n.elts]
        ret = ast.List(elts=elts, ctx=ctx)
    elif isinstance(n, ast.Tuple):
        elts = [copy_assignee(e, ctx) for e in n.elts]
        ret = ast.Tuple(elts=elts, ctx=ctx)
    elif isinstance(n, ast.Starred):
        ret = ast.Starred(value=copy_assignee(n.value, ctx), ctx=ctx)
    elif isinstance(n, ast.Call):
        args = [copy_assignee(e, ctx) for e in n.args]
        ret = ast.Call(func=n.func, args=args, keywords=n.keywords, starargs=n.starargs, kwargs=n.kwargs)
    else: return n
    ast.copy_location(ret, n)
    return ret

def iter_type(ty):
    if isinstance(ty, typing.List):
        return ty.type
    else: return typing.Dyn

def handle_static_type_error(error, exit=True):
    print('\n====STATIC TYPE ERROR=====', file=sys.stderr)
    print(*error.args, file=sys.stderr)
    print(file=sys.stderr)
    if exit:
        quit()

def handle_runtime_error(exit=False):
    retic_install_dir = os.path.dirname(flags.__file__)

    ty, error, tb = sys.exc_info()

    extract = traceback.extract_tb(tb)
    if not flags.MINIMIZE_ERRORS or (not isinstance(error, exc.RuntimeTypeError) and\
        extract[-1][0].startswith(retic_install_dir)):
        raise
    

    print('\nTraceback (most recent call last):', file=sys.stderr)

    lines = []
    for line in extract:
        if line[0].startswith(retic_install_dir):
            continue
        else: 
            lines.append(line)

    print(*traceback.format_list(lines), sep='', end='', file=sys.stderr)
    print(*traceback.format_exception_only(ty, error), end='', file=sys.stderr)
    if exit:
        quit(1)
