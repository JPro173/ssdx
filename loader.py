import json
import os
import os.path
import copy

apps_dir = './apps'
info_file = 'info.json'

def get_config(app_dir, i):
    fd = open(os.path.join(apps_dir,app_dir, info_file))
    data = json.load(fd)
    data['id'] = i
    return data

def get_apps():
    apps = os.listdir(apps_dir)
    apps = {app_dir: get_config(app_dir, i) for i, app_dir in enumerate(apps)}
    return apps#return OrderedDict(sorted(apps.items(), key=))

def get_list(path):
    app = [app for app in get_apps().items() if app[1]['id'] == path.app][0]
    lst = app[1]['list']
    i = 0
    while len(path) > i:
        lst = list(lst.items())[path[i]][1]
        i += 1
    return lst

def get_current(path):
    app = [app for app in get_apps().items() if app[1]['id'] == path.app][0]
    lst = app[1]['list']
    i = 0
    while len(path) > i:
        lst = list(lst.items())[path[i]][1]
        i += 1
    return list(lst.keys())[path[-1]]

def is_command(path, i):
    path = copy.deepcopy(path)
    if len(path):
        path.pop()
    lst = get_list(path)
    return isinstance(list(lst.values())[i], str)

