# -*- coding: UTF-8 -*-
from FileAnalysis import list_dir

path = "pro/ThemeTemplateV3"
listModule = list_dir(path)
totalLines = 0
totalFiles = 0
for module in listModule:
    for file in module.java_files:
        totalLines += file.lines
        totalFiles += 1
        if file.lines > 300:
            print(file.lines, file.fName)
print("totalLines:", totalLines, "totalFiles:", totalFiles)
