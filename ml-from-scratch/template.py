import os 
from pathlib import Path

project_name = "ml-from-scratch"

list_of_files = [
    f"{project_name}/__init__.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/split.py",
    f"{project_name}/utils/metrics.py",
    f"{project_name}/models/__init__.py",
    f"{project_name}/models/linear_regression.py",
    f"{project_name}/datasets/__init__.py",
    f"{project_name}/datasets/synthetic.py",
    "run_test.py"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir,filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok = True)
        print(f"Creating directory: {filedir} for the file: {filename}")
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath )== 0):
        with open(filepath, "w") as f:
            pass
            print(f"Creating empty file:{filename}")
    else:
        print(f"{filename} already exists")