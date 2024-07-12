import inspect
import os


def dot_slash(relative_path: str) -> str:
    """Converts the `relative_path` into an absolute path using
    this file's directory as the root directory.

    Parameters
    ----------
    relative_path : str
        The path to convert to an absolute path.

    Returns
    -------
    str
        The absolute path.

    Examples
    --------
    # If this file is located at "/path/to/this/file.py"
    >>> dot_slash("sibling.py") => "/path/to/this/sibling.py"
    >>> dot_slash("../foo/cousin.py") => "/path/to/foo/cousin.py"
    """
    called_from_file = inspect.stack()[1].filename
    here = os.path.dirname(called_from_file)
    joined = os.path.join(here, relative_path)
    normed = os.path.normpath(joined)
    return normed
