To have py's be compiled every time you save the notebook, in ~/.ipython/profile_default/ipython_notebook_config.py, add:

import os
from subprocess import check_call

def post_save(model, os_path, contents_manager):
    """post-save hook for converting notebooks to .py scripts"""
    if model['type'] != 'notebook':
        return # only do this for notebooks
    d, fname = os.path.split(os_path)
    check_call(['ipython', 'nbconvert', '--to', 'script', fname], cwd=d)

def post_save_test(model, os_path, contents_manager):
    print "test"

import ipdb; ipdb.set_trace()
FileContentsManager.post_save_hook = post_save_test

#ContentsManager.pre_save_hook
