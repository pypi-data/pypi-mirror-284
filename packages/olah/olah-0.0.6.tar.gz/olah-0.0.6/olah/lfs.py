import datetime
import json
import os
from typing import Literal
from fastapi import FastAPI, Header, Request

from olah.files import _file_realtime_stream
from olah.utils.file_utils import make_dirs
from olah.utils.url_utils import check_cache_rules_hf, get_org_repo


async def lfs_head_generator(
    app,
    dir1: str, dir2: str, hash_repo: str, hash_file: str, request: Request
):
    # save
    repos_path = app.app_settings.repos_path
    head_path = os.path.join(
        repos_path, f"lfs/heads/{dir1}/{dir2}/{hash_repo}/{hash_file}"
    )
    save_path = os.path.join(
        repos_path, f"lfs/files/{dir1}/{dir2}/{hash_repo}/{hash_file}"
    )
    make_dirs(head_path)
    make_dirs(save_path)

    # use_cache = os.path.exists(head_path) and os.path.exists(save_path)
    allow_cache = True

    # proxy
    return _file_realtime_stream(
        app=app,
        save_path=save_path,
        head_path=head_path,
        url=str(request.url),
        request=request,
        method="HEAD",
        allow_cache=allow_cache,
        commit=None,
    )

async def lfs_get_generator(
    app,
    dir1: str, dir2: str, hash_repo: str, hash_file: str, request: Request
):
    # save
    repos_path = app.app_settings.repos_path
    head_path = os.path.join(
        repos_path, f"lfs/heads/{dir1}/{dir2}/{hash_repo}/{hash_file}"
    )
    save_path = os.path.join(
        repos_path, f"lfs/files/{dir1}/{dir2}/{hash_repo}/{hash_file}"
    )
    make_dirs(head_path)
    make_dirs(save_path)

    # use_cache = os.path.exists(head_path) and os.path.exists(save_path)
    allow_cache = True

    # proxy
    return _file_realtime_stream(
        app=app,
        save_path=save_path,
        head_path=head_path,
        url=str(request.url),
        request=request,
        method="GET",
        allow_cache=allow_cache,
        commit=None,
    )