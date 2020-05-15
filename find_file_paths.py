from pathlib import Path
def list_files(pwd, pttrn='*.json'):
    ret = []
    for filename in Path(pwd).rglob(pttrn):
        ret.append(filename)
    return ret
