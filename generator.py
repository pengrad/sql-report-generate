import ast
from genericpath import isfile, exists
from os import listdir, makedirs
from os.path import join

REPORT_DIR = "sql"
TPL_EXTENSION = ".tpl"


def file2str(file, directory="./"):
    with open(join(directory, file), 'r') as f:
        return f.read()


def str2file(string, file, directory="./"):
    if not exists(directory):
        makedirs(directory)
    with open(join(directory, file), 'w') as f:
        f.write(string)


def report_name(report, tpl, ext=".sql"):
    return report.replace(":", "").replace("-", "").replace(" ", "_") + "_" + tpl[0:tpl.rindex(".")] + ext


def is_tpl(file):
    return isfile(file) & file.endswith(TPL_EXTENSION)


def process_dir(directory, mapping):
    files = [f for f in listdir(directory) if is_tpl(join(directory, f))]
    for tpl_file in files:
        for m in mapping:
            file = report_name(m["report_name"], tpl_file)
            res = file2str(tpl_file, directory).format_map(m)
            str2file(res, file, join(directory, REPORT_DIR))


s = '({"report_name": "ZR iOS App (3)", "game_id": 3},{"report_name": "ZR Android App (4)", "game_id": 4})'
e = ast.literal_eval(s)

process_dir("reports_apps", e)