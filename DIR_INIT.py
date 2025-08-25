import sys
import os

if len(sys.argv)>1:
    root_dir = str(sys.argv[1])
else:
    root_dir = str(input("The root dir to init:"))
os.chdir(root_dir)

bases_dir = ["ui", "ui_core", "qrc", "res", "api", r"\configures\groups", r"\configures\active", r"runtimes\web_socket"]
data_dir = []
plugins_dir = []

for __base_dir__ in bases_dir:
    if __base_dir__:
        try:
            os.makedirs(rf".\bases\{__base_dir__}")
        except FileExistsError:
            continue

# for _data_dir__ in bases_dir:
#     if __base_dir__:
#         try:
#             os.makedirs(rf".\bases\{__base_dir__}")
#         except FileExistsError:
#             continue
os.mkdir(r".\data")
os.mkdir(r".\plugins")
