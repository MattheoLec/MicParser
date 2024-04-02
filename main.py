import os
import re
import sys
import pandas as pd


def extract_method_names(directory):
    method_names = []
    for root, _, files in os.walk(directory):
        for filename in files:
            if filename.endswith(".java"):
                filepath = os.path.join(root, filename)
                with open(filepath, "r") as java_file:
                    content = java_file.read()
                    methods = re.findall(r"([A-Z][\w<>.,\[\]?]+|void|int|float)\s+(\w+)\s*\([^)]*\).*[={;]", content)
                    for method in methods:
                        method_names.append(method[1])
    return method_names


if __name__ == "__main__":
    target_directory = sys.argv[-1]
    method_names = []
    methods_count = 0
    for dir_name in os.listdir(target_directory):
        dir_path = os.path.join(target_directory, dir_name, 'src/main/java')
        if os.path.isdir(dir_path):
            print(dir_name)
            method_names.append(extract_method_names(dir_path))
            methods_count += len(method_names[len(method_names)-1])
            method_names[len(method_names)-1].insert(0, dir_name)

    method_names_df = pd.DataFrame(method_names).T
    method_names_df.to_csv('methods.csv', index=False, header=False)

    print(f"Extracted {methods_count} method names.")
