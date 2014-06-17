from genericpath import isfile, exists
from os import listdir, makedirs
from os.path import join

REPORT_DIR = "sql"


def file2str(file, directory="./"):
    with open(join(directory, file), 'r') as f:
        return f.read()


def str2file(string, file, directory="./"):
    if not exists(directory):
        makedirs(directory)
    with open(join(directory, file), 'w') as f:
        f.write(string)


def report_name(report, tpl, ext=".sql"):
    return report.replace(":", "").replace(" ", "_") + "_" + tpl[0:tpl.rindex(".")] + ext


def process_dir(directory, mapping):
    files = [f for f in listdir(directory) if isfile(join(directory, f))]
    for tpl_file in files:
        for m in mapping:
            file = report_name(m["report_name"], tpl_file)
            res = file2str(tpl_file, directory).format_map(m)
            # print(file2str(tpl_file, directory).format_map(m), "\n\n\n")
            str2file(res, file, join(directory, REPORT_DIR))
            # open(join)


# print("select {col} from {table}".format(col="id", table="login"))
# print("select {col} from {table}".format_map({"col": 1, "table": "login", "name": 123, "row": "1adsa"}))
# print(tpl2str("reports_apps/device_dau.tpl").format_map({"game_id":21}))

process_dir("reports_apps", ({"report_name": "Snark Busters: Welcome to the Club (Alawar) (41)", "game_id": 21},
                             {"report_name": "ZR iOS App (3)", "game_id": 777}))


# str2file("text", "1.txt", "reports_apps/sql")

