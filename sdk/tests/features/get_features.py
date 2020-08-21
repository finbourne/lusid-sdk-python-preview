import inspect
import os
import re

##1 First iterate through all packages in a directory
##2 then  iterate through all package modules

print(os.path.dirname(os.path.realpath(__file__)))

path = "..\\tutorials"
module_paths = []
for root, directories, files in os.walk(path, topdown=False):
    for name in files:
        # print(os.path.join(root, name))
        module_paths.append(str(os.path.join(root, name)))

module_list_disconnected = []
for path in module_paths:
    # print(path.partition('.'))
    splitted_formatted = path.replace('..', '')
    splitted_formatted = re.split('[.\\\]', splitted_formatted)
    module_list_disconnected.append(splitted_formatted[1:-1])

module_list = []
for module in module_list_disconnected:
    module_list.append(".".join(module))

# This returns all the nested filepaths to modules in our 'tutorials folder. Resolves #1 and #2

## 2.1 import all the files above. (make sure that it doesn't import itself)
import importlib.util

imported_modules = []
for module in module_list:
    try:
        imported_modules.append(importlib.import_module(module))
    except Exception as e:
        pass
        # print(e) # cant import __pychache__...

# print(imported_modules)

##3 then iterate through all classes in each module
all_methods_for_all_classes = []
for module in imported_modules:
    classes = inspect.getmembers(module, predicate=inspect.isclass)
    for cls in classes:
        methods = inspect.getmembers(cls[1])
        all_methods_for_all_classes.append(methods)


##4 Then check each method in each class

for cls in all_methods_for_all_classes:
    for method in cls:
        try:
            print(method[1].decorator_value[0])
        except:
            pass


##5 then try/catch for decorator_value for each method...

