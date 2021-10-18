import os
import logging
import validators
from bs4 import BeautifulSoup
from tqdm import tqdm
import requests


def path_exist(dest):
    return os.path.exists(dest)


def create_dir_if_not_exist(dest):
    if not path_exist(dest):
        os.makedirs(dest)


def validate_url(url):
    return validators.url(url)


def fetch_url_content(url):
    return requests.get(url, stream=True, allow_redirects=True)


def fetch_url_header(url):
    return requests.head(url, stream=True, allow_redirects=True)


def download_file(dest, url, file_size_limit=None):
    file_name = url.split("/")[-1]
    create_dir_if_not_exist(dest)
    dest = dest + '/' + file_name
    # FiveMegaBytes = 5 * 1024 * 1024;
    if os.path.exists(dest) and os.path.getsize(dest):
        logging.warning("File Already Downloaded: " + dest)
    else:
        if validate_url(url):
            r = fetch_url_header(url)
            total_size = None
            if r.headers.get('content-length'):
                total_size = int(r.headers.get('content-length'))
                initial_pos = 0
            if not file_size_limit or total_size < file_size_limit:
                r = fetch_url_content(url)
                with open(dest, 'wb') as f:
                    with tqdm(total=total_size, unit='B', unit_scale=True, desc=dest, initial=initial_pos, ascii=True) as pbar:
                        for ch in r.iter_content(chunk_size=1024):
                            if ch:
                                f.write(ch)
                                pbar.update(len(ch))
                                if file_size_limit and os.path.getsize(dest) > file_size_limit:
                                    remove_file(dest, pbar)
                                    break


def remove_file(file_path, pbar):
    try:
        os.remove(file_path)
    except OSError as e:
        pass
    if not os.path.exists(file_path):
        pbar.set_description("[FILE DELETED: File exceeds download limit size]")
    else:
        raise


def delete_all_empty_dirs(destFolder):
    # delete empty folders
    for root, dirs, files in os.walk(destFolder):
        if not len(dirs) and not len(files):
            os.rmdir(root)
