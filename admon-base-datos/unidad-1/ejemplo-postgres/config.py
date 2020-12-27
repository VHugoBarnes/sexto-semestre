#coding: utf-8

from configparser import ConfigParser


def config(filename='database.ini', section='postgresql'):
    # crear un parser.
    parser = ConfigParser()
    # leer el archivo de configuración
    parser.read(filename)

    # obtener la section, por defecto es postgresql.
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file.'.format(section,filename))

    return db