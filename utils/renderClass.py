# coding: utf8
import os
import json
import codecs
import jinja2


def dirFormat(dirname):
    if not dirname.endswith('/'):
        return dirname + '/'
    return dirname


def renderFile(s_templatePath, d_filePath, keys):
    s_templatePath = dirFormat(s_templatePath)
    d_filePath = dirFormat(d_filePath)
    files = os.listdir(s_templatePath)
    print(files)
    for file in files:
        if not os.path.isdir(file) and file.startswith("index"):
            fileObj = codecs.open(s_templatePath + file, 'r', 'utf-8').read()
            result = jinja2.Template(fileObj).render(keys)
            with codecs.open(d_filePath + file, 'w', 'utf-8') as fp:
                fp.write(result)


if __name__ == "__main__":
    s_t = "h:/xxx/commonIndex/nz/wx/"
    d_file = "./"
    keys = {"version": "1.2.3.33"}
    renderFile(s_t, d_file, keys)
