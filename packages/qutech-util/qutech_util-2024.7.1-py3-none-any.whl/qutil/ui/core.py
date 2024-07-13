"""This module contains UI utility functions."""
from __future__ import annotations

import logging
import os
import socketserver
import sys
import webbrowser
from http.server import SimpleHTTPRequestHandler
from threading import Thread
from typing import Iterable, Optional, TextIO

from ..functools import wraps

__all__ = ['progressbar', 'progressbar_range']

_NOTEBOOK_NAME = None  # flags if _import_tqdm was run
tqdm = None
trange = None


def _in_spyder_kernel():
    """Determine if we are currently running inside spyder on a best effort basis."""
    if 'spyder_kernels' not in sys.modules:
        return False
    return type(sys.stdout).__module__.startswith('spyder_kernels.')


class TCPServerThread(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


class ThreadedWebserver:
    """Serves a simple HTTP server in a background thread.

    If *qcodes_monitor_mode* is true, the port will be grabbed from
    :mod:`qcodes:qcodes.monitor.monitor`.

    Examples
    --------
    Run as server for the qcodes monitor:

    >>> from qcodes.monitor import Monitor
    >>> from qcodes.parameters import ManualParameter
    >>> server = ThreadedWebserver(qcodes_monitor_mode=True)
    >>> server.show()
    >>> monitor = Monitor(ManualParameter('foobar'))

    Join the threads again:

    >>> monitor.stop()
    >>> server.stop()

    """

    def __init__(self, qcodes_monitor_mode: bool = False, url: str = 'localhost',
                 port: int = 3000):
        if qcodes_monitor_mode:
            # Copy stuff from qcodes.monitor.monitor. Purely convenience
            from qcodes.monitor import monitor
            self.port = monitor.SERVER_PORT
            self.log = monitor.log
            self.static_dir = STATIC_DIR = os.path.join(os.path.dirname(monitor.__file__), "dist")

            class HTTPRequestHandler(SimpleHTTPRequestHandler):
                def __init__(self, *args, directory: str | None = ..., **kwargs):
                    super().__init__(*args, directory=STATIC_DIR, **kwargs)

        else:
            self.port = port
            self.log = logging.getLogger(__name__)

            class HTTPRequestHandler(SimpleHTTPRequestHandler):
                ...
        self.url = url

        self.log.info(f"Starting HTTP Server at http://{self.url}:{self.port}")
        self.server = TCPServerThread(("", self.port), HTTPRequestHandler)
        self.thread = self.server.server_thread = Thread(target=self.server.serve_forever)
        self.thread.start()

    def __del__(self):
        self.stop()

    def stop(self):
        self.log.info("Shutting Down HTTP Server")
        self.server.shutdown()
        self.server.server_close()
        self.thread.join()

    def show(self, new=0, autoraise=True):
        """Show the server in a browser.

        See :func:`webbrowser:webrowser.open` for parameters.
        """
        webbrowser.open(f"http://{self.url}:{self.port}", new=new, autoraise=autoraise)

    open = show


def _import_tqdm():
    # In principle there is tqdm.autonotebook, but it doesn't work in a Spyder kernel.
    global tqdm, trange, _NOTEBOOK_NAME

    import importlib
    try:
        import ipynbname
        _NOTEBOOK_NAME = ipynbname.name()
    except (ImportError, IndexError, FileNotFoundError):
        _NOTEBOOK_NAME = ''

    try:
        if _NOTEBOOK_NAME:
            tqdm = importlib.import_module('tqdm.notebook').tqdm
            trange = importlib.import_module('tqdm.notebook').trange
        elif _NOTEBOOK_NAME is not None:
            # Either not running notebook or not able to determine
            tqdm = importlib.import_module('tqdm').tqdm
            trange = importlib.import_module('tqdm').trange
    except (ImportError, AttributeError):
        pass


def _simple_progressbar(iterable: Iterable, desc: str = "Computing", disable: bool = False,
                        total: Optional[int] = None, size: int = 25, file: TextIO = sys.stdout,
                        *_, **__):
    """https://stackoverflow.com/a/34482761"""
    if disable:
        yield from iterable
        return

    if total is None:
        try:
            total = len(iterable)
        except TypeError:
            raise ValueError(f'{iterable} has no len, please supply the total argument.')

    def show(j):
        x = int(size*j/total)
        file.write("\r{}:\t[{}{}] {} %".format(desc, "#"*x, "."*(size - x),
                   int(100*j/total)))
        file.flush()

    show(0)
    for i, item in enumerate(iterable):
        yield item
        show(i + 1)

    file.write("\n")
    file.flush()


class ProgressbarLock:
    """A global lock for progressbars used as a decorator.

    The intended use case is to keep nested progressbars from interfering in
    non-interactive (notebook) mode.

    Examples
    --------
    >>> import time
    >>> for i in progressbar_range(10, desc='outer', file=sys.stdout):
    ...     for j in progressbar_range(10, desc='inner', file=sys.stdout, leave=False):
    ...         time.sleep(0.05) # doctest: +NORMALIZE_WHITESPACE
    outer: ...
    >>> for i in progressbar_range(10, desc='outer', file=sys.stdout, disable=True):
    ...     for j in progressbar_range(10, desc='inner', file=sys.stdout):
    ...         time.sleep(0.05)  # doctest: +NORMALIZE_WHITESPACE
    inner: ...

    """
    _stack: list[bool] = []
    disable: bool | None = None

    def __call__(self, func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            disable = kwargs.get('disable', self.disable if self.disable is not None else False)
            self.lock(disable if all(self._stack) else not self.notebook_session)
            kwargs['disable'] = self.locked
            try:
                yield from func(*args, **kwargs)
            finally:
                self.release()

        return wrapper

    @property
    def notebook_session(self) -> bool:
        # Needs to be dynamic because it is lazily evaluated.
        return _NOTEBOOK_NAME != ''

    @property
    def locked(self) -> bool:
        try:
            return self._stack[-1]
        except IndexError:
            return False

    def lock(self, val):
        self._stack.append(val)

    def release(self):
        self._stack.pop()


def auto_progress_bar_lock(pbar_function: callable) -> callable:
    """Enable progress bar lock for the given progress bar if a spyder kernel is detected."""
    if _in_spyder_kernel():
        return ProgressbarLock()(pbar_function)
    else:
        return pbar_function


@auto_progress_bar_lock
def progressbar(iterable: Iterable, *args, **kwargs):
    """
    Progress bar for loops. Uses tqdm if available or a quick-and-dirty
    implementation from stackoverflow.

    Usage::

        for i in progressbar(range(10)):
            do_something()

    See :class:`~tqdm.tqdm` or :func:`_simple_progressbar` for possible
    args and kwargs.
    """
    if _NOTEBOOK_NAME is None:
        _import_tqdm()
    if tqdm is not None:
        return tqdm(iterable, *args, **kwargs)
    else:
        return _simple_progressbar(iterable, *args, **kwargs)


@auto_progress_bar_lock
def progressbar_range(*args, **kwargs):
    if _NOTEBOOK_NAME is None:
        _import_tqdm()
    if tqdm is not None:
        return trange(*args, **kwargs)
    else:
        return _simple_progressbar(range(*args), **kwargs)
