from contextlib import suppress
from json import dumps
from os.path import splitext

from ruamel.yaml import YAML


def write_package_config(cmd, basename, filename):
    yaml = YAML()

    with suppress(FileNotFoundError):
        with open('package_config.yaml') as file:
            value = yaml.load(file)

        argname = splitext(basename)[0]

        str_value = dumps(value, separators=(',', ':'), ensure_ascii=False)

        cmd.write_or_delete_file(argname, filename, str_value)


def write_external_requires(cmd, basename, filename):
    externals = getattr(cmd.distribution, 'requires_external', None) or []

    externals = '\n'.join(externals)

    argname = splitext(basename)[0]

    cmd.write_or_delete_file(argname, filename, externals)
