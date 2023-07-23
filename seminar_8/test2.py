def dct_formatter(total_dct: dict[str, dict[str]],
                  path: str,
                  item_name: str,
                  item_type: str) -> None:
    if item_type == 'F':
        total_dct[path] = dict(unit_type='File',
                               unit_name=item_name,
                               unit_size=os.path.getsize(os.path.join(path, item_name)),
                               parent_dir=os.path.split(path)[-1])
    elif item_type == 'D':
        total_dct[path] = dict(unit_type='Directory',
                               unit_name=item_name,
                               unit_size=count_size(os.path.join(path, item_name)),
                               parent_dir=os.path.split(os.path.abspath(path))[-1])