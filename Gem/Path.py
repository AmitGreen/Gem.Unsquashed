#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Gem.Path')
def gem():
    require_gem('Gem.CatchException')
    require_gem('Gem.Import')


    PythonOperatingSystem = import_module('os')
    PythonPath            = import_module('os.path')
    remove_path           = PythonOperatingSystem.remove
    rename_path           = PythonOperatingSystem.rename
    open_path             = PythonBuiltIn.open


    @export
    @privileged_2
    def read_text_from_path(path):
        with open_path(path, 'r') as f:
            return f.read()


    @export
    def remove_path__ignore_file_not_found(path):
        with catch_FileNotFoundError():
            remove_path(path)


    @export
    def rename_path__ignore_file_not_found(from_path, to_path):
        with catch_FileNotFoundError():
            rename_path(from_path, to_path)


    export(
        'path_basename',            PythonPath.basename,
        'path_join',                PythonPath.join,
        'path_split_extension',     PythonPath.splitext,
        'remove_path',              PythonOperatingSystem.remove,
        'rename_path',              PythonOperatingSystem.rename,
    )

    restricted(
        'open_path',    PythonBuiltIn.open,
    )
