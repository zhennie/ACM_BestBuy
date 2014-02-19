__author__ = 'ash'

def abs_path(pwd_orig, path_orig):
    pwd_list = pwd_orig.split('/')
    pwd_list.pop(0)

    if str(path_orig).startswith('/'):
        path_abs = path_orig
        return path_abs

    path_list = path_orig.split('/')

    for node in path_list:
        if '.' == node or '' == node:
            continue
        if '..' == node:
            if len(pwd_list) == 0:
                continue
            else:
                pwd_list.pop(len(pwd_list)-1)

        else:
            pwd_list.append(node)

    path_abs = ''

    # for item in pwd_list:
        # assert isinstance(item, object)
    path_abs = '/'.join(pwd_list)

    return '/' + path_abs


if __name__ == '__main__':
    print abs_path('/home/ash/documents', '../.././/..')