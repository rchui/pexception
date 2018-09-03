from typing import List, Tuple, Type
from types import TracebackType
import sys
import traceback

from colorama import Fore, Style

__all__ = ['hook']
ALIGN = True
VERBOSE = True


def _trace(exctype: Type[BaseException], value: BaseException, tb: TracebackType) -> None:
    """Function that overrides sys.excepthook. Parses, formats the traceback and pretty prints the stack trace.

    Args:
        exctype (Type[BaseException]): Type of the exception.
        value (BaseException): Value passed to the exception when raised.
        tb (TracebackType): Traceback object.
    """

    stack = traceback.extract_tb(tb).format()
    _eprint(_format(*_parse(stack)))
    print(f'{exctype.__name__}: {value}', file=sys.stderr)


def _parse(stack: List[str]) -> Tuple[int, int, int, List[Tuple[str, str, str, str]]]:
    """Parses the stack frames from the traceback object.

    Args:
        stack (List[str]): Preformatted strings of the stack trace.

    Returns:
        int: Longest file name.
        int: Longest function name.
        int: Highest number of line digits.
        List[Tuple[str, str, str, str]]: File name, function name, line number, stack entry point.
    """

    max_file = max_func = max_line = 0
    frames = []
    for summary in stack:
        # Parse frame from stack
        frame = [value.strip() for value in summary.split('\n')[:-1]]

        # Parse entry point
        entrypoint = frame[-1]

        # Parse location information
        locations = [value.strip() for value in frame[0].split(',')]
        _file = locations[0].split(' ')[-1]
        line = locations[1].split(' ')[-1]
        func = locations[2].split(' ')[-1]

        # Store frame and find max element lengths
        frames.append((_file, func, line, entrypoint))
        max_file = max(max_file, len(_file))
        max_func = max(max_func, len(func))
        max_line = max(max_line, len(line))
    return max_file, max_func, max_line, frames


def _format(max_file: int, max_func: int, max_line: int, frames: List[Tuple[str, str, str, str]]) -> List[str]:
    """Formats the parsed stack frames.

    Args:
        max_file (int): Longest file name.
        max_func (int): Longest function name.
        max_line (int): Highest number of line digits.
        frames (List[Tuple[str, str, str, str]]): File name, function name, line number, stack entry point.

    Returns:
        List[str]: Formatted summaries of each stack frame.
    """

    summaries = []
    if not ALIGN:
        max_file = max_func = max_line = 0
    for frame in frames:
        if VERBOSE:
            summaries.append(
                f'From {Fore.RED}{frame[0]:<{max_file}}{Style.RESET_ALL} '
                f'in {Fore.BLUE}{frame[1]:<{max_func}}{Style.RESET_ALL} '
                f'line {Fore.GREEN}{frame[2]:>{max_line}}{Style.RESET_ALL} '
                f'at {Fore.YELLOW}{frame[3]}{Style.RESET_ALL}'
            )
        else:
            location = (
                f'{Fore.RED}{frame[0]}{Style.RESET_ALL}.'
                f'{Fore.BLUE}{frame[1]}{Style.RESET_ALL}.'
                f'{Fore.GREEN}{frame[2]}{Style.RESET_ALL}'
            )
            location_size = max_file + max_func + max_line + 29
            summaries.append(f'{location:>{location_size}} > {Fore.YELLOW}{frame[3]}{Style.RESET_ALL}')

    return summaries


def _eprint(summaries: List[str]) -> None:
    """Print stack frame summaries to sys.stderr.

    Args:
        List[str]: Formatted summaries of each stack frame.
    """

    for summary in summaries:
        print(summary, file=sys.stderr)


def hook(verbose: bool = True, align: bool = True) -> None:
    """Hook to pretty print exceptions.
        verbose (bool, optional): Defaults to True. Print verbose output.
        align (bool, optional): Defaults to True. Print aligned output.
    """

    global ALIGN, VERBOSE
    ALIGN = align
    VERBOSE = verbose
    sys.excepthook = _trace  # type: ignore
