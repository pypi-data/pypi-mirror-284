# Copyright (c) 2023 - 2024 Benjamin Mummery

"""Process android phone footage default names into plex-friendly filename."""

import os
from datetime import datetime
from pathlib import Path
from typing import Optional


def _discover_files(directory: str, recursive: bool = False) -> dict:
    """Find files that match the format we want to convert.

    Args:
        directory (str): The path to the directory to be searched.
        recursive (bool, optional): If True, subdirectories will be searched. If false,
            only the specified directory will be searched. Defaults to False.

    Returns:
        dict: A mapping of datetime date objects to file paths, where the date is
            derived from the file name.
    """
    formats = [
        "%Y%m%d_%H%M%S",
        "%Y%m%d_%H%M%-S",
        "%Y%m%d_%H%M",
        "%Y%m%d_%H%M%f",
        "%Y%m%d-%H%M%S",
        "%Y%m%d-%H%M%-S",
        "%Y%m%d-%H%M",
        "%Y%m%d-%H%M%f",
        "%Y-%m-%d_%H-%M-%S",
        "%Y-%m-%d_%H-%M-%-S",
        "%Y-%m-%d_%H-%M",
        "%Y-%m-%d_%H-%M-%f",
        "%Y-%m-%d-%H-%M-%S",
        "%Y-%m-%d-%H-%M-%-S",
        "%Y-%m-%d-%H-%M",
        "%Y-%m-%d-%H-%M-%f",
    ]

    print(f"Discovering files in {directory}", end="")
    if recursive:
        print(" and subdirectories", end="")

    days: dict = {}
    if recursive:
        files = [os.path.join(dp, f) for dp, _, fn in os.walk(directory) for f in fn]
    else:
        files = os.listdir(directory)

    for file in files:
        _, filename = os.path.split(file)
        oldname = os.path.splitext(filename)[0]

        # some systems append _1 for duplicated filenames. We should strip these out
        while oldname.endswith(("_1", "_2")):
            oldname = oldname[:-2]
            print("\n", oldname)

        for format in formats:
            try:
                if (
                    date := datetime.strptime(
                        os.path.splitext(oldname)[0], format
                    ).date()
                ) not in days:
                    days[date] = [file]
                else:
                    days[date].append(file)
                break
            except ValueError:
                continue
    return days


def _rename(
    filepath: Path, series_title: str, day: datetime, part: Optional[int] = None
):
    """Generate a new name and rename the specified file.

    Args:
        filepath (Path): The file to be renamed.
        series_title (str): The series that this file should be part of.
        day (datetime): The date on which the file was created.
        part (Optional[int], optional): If specified, renames the files as part of a
            multi-file episode for this day. Defaults to None.

    Returns:
        str: _description_
    """
    dir, _ = os.path.split(filepath)

    new_name = f"{series_title} - " f"{day.year}-{day.month:02d}-{day.day:02d}"
    if part is not None:
        new_name += f" - Part{part}"
    new_name += os.path.splitext(filepath)[1]

    os.rename(
        filepath,
        os.path.join(dir, new_name),
    )
    print(f"  {filepath} --> {new_name}")


def main(directory: str, series_title: str, recursive: bool = False):
    """Find and rename matching files.

    Args:
        directory (str): The directory in which to look for renamable files.
        series_title (str): The series to which the files should belong.
        recursive (bool, optional): If True, search subdirectories of the specified
            directory. Defaults to False.
    """

    if len(days := _discover_files(directory, recursive)) == 0:
        print("No files to rename, exiting.")
        return

    print("\nRenaming files:")
    for day in days:
        if len(files := days[day]) == 1:
            _rename(os.path.join(directory, files[0]), series_title, day)
        else:
            for i, file in enumerate(sorted(files)):
                _rename(os.path.join(directory, file), series_title, day, part=i + 1)
    return
