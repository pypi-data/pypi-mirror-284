import importlib
import inspect
import logging
import os
import re
import typing

from remotemanager.storage.sendablemixin import SendableMixin
from remotemanager.utils.uuid import generate_uuid

logger = logging.getLogger(__name__)


_SCRIPT_TEMPLATE = """
{function}

if __name__ == '__main__':
\tkwargs = {args}

\tresult = {name}(**kwargs)
"""


class Function(SendableMixin):
    """
    Serialise function to an executable python file for transfer

    Args:
        func:
            python function for serialisation
    """

    def __init__(self, func: [typing.Callable, str], force_self: bool = False):
        logger.debug("creating new serialisable function for %s", func)

        self._uuid = ""
        # collect the source, name and signature
        if isinstance(func, str):
            source = func
            # need to extract the name
            name = "f"
            signature = ")"
            for line in func.split("\n"):
                if line.startswith("def"):
                    name, signature = line.lstrip("def ").split("(", maxsplit=1)

            signature = "(" + signature.strip(":")
        else:
            source = inspect.getsource(func)
            name = func.__name__
            signature = inspect.signature(func)

        if name in ["remote_load", "remote_dump"]:
            raise ValueError(f'function name "{name}" is protected')

        tmp = []
        indent = -1
        is_self = force_self  # default to False, allow forcing
        append = False  # don't begin the append until we hit the `def ...` line
        for line in source.split("\n"):
            if indent == -1 and line.strip().startswith("def"):
                if "(self" in line:
                    is_self = True
                append = True
                indent = line.index("def")

            if append:
                tmp.append(line[indent:])

        source = "\n".join(tmp).strip()

        signature = Function.prepare_signature(signature, is_self=is_self)

        self._signature = signature

        logger.debug("updated signature to %s", self._signature)
        rawsig = Function.get_raw_signature(source)
        logger.debug("raw typed signature detected as %s", self._signature)
        source = source.replace(rawsig, self._signature, 1)

        self._source = source
        self._fname = name

        # use 1:-1 to escape ()
        self._arglist = [a.strip() for a in self._signature[1:-1].split(",")]

        self._uuid = generate_uuid(self._source)

    def __call__(self, *args, **kwargs):
        return self.object(*args, **kwargs)

    @staticmethod
    def get_raw_signature(source):
        """
        Strips the signature as it is typed.
        inspect.signature does some formatting which can cause replacement to
        break in some conditions

        Args:
            source (str):
                raw source

        Returns:
            (str): raw signature as typed
        """
        definition = []
        for line in source.split("\n"):
            # we need to split from the function name for the raw signature
            if "(" in line:
                # split from first ( and up,
                # then join for any tuples defined as default
                line = "(" + "(".join(line.split("(")[1:])

            # appending the final ":" causes issues, strip that in a safe
            # manner then append
            definition.append(line.rstrip(" ").rstrip(":"))

            # we've reached the end of the definition
            if line.endswith(":"):
                break

        return "\n".join(definition)

    @staticmethod
    def prepare_signature(sig, is_self: bool = False) -> str:
        """
        Inserts *args and **kwargs into any signature that does not already
        have it

        Args:
            sig:
                inspect.signature(func)
            is_self:
                inspect.signature ignores `self`, yet we want to preserve it.
                Adds the argument if True

        Returns:
            (str): formatted sig
        """
        if isinstance(sig, str):
            sig = sig[: sig.rindex(")")]
            sig = sig.strip("(")
            args = [a.strip() for a in sig.split(",") if a.strip() != ""]
        else:
            args = [str(a) for a in sig.parameters.values()]

        if is_self and "self" not in args:
            args = ["self"] + args

        args_pattern = r"(\s|\()(\*{1}[\w]+)"
        kwargs_pattern = r"(\s|\()(\*{2}[\w]+)"

        has_args = re.search(args_pattern, str(sig)) is not None
        has_kwargs = re.search(kwargs_pattern, str(sig)) is not None

        if not has_args:
            if has_kwargs:
                args.insert(-1, "*args")
            else:
                args.append("*args")

        if not has_kwargs:
            args.append("**kwargs")

        return f'({", ".join(args)})'

    @property
    def name(self):
        """
        Function name
        """
        return self._fname

    @property
    def raw_source(self):
        """
        Function source
        """
        return self._source

    @property
    def source(self):
        """
        Function source

        Returns:
            (str): source code
        """
        return self._source

    @property
    def signature(self):
        return self._signature

    @property
    def args(self):
        return self._arglist

    @property
    def uuid(self):
        """
        Function uuid (64 characters)
        """
        return self._uuid

    @property
    def object(self):
        """
        Recreates the function object by writing out the source, and importing.

        Returns:
            typing.Callable:
                the originally passed function
        """

        tmp_file = ""
        try:
            tmp_file = os.path.abspath(f"{self.uuid}.py")

            with open(tmp_file, "w+") as o:
                o.write(self.source)

            spec = importlib.util.spec_from_file_location(self.uuid, tmp_file)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            func_object = getattr(module, f"{self.name}")

        finally:
            os.remove(tmp_file)

        return func_object

    def dump_to_string(self, args):
        """
        Dump this function to a serialised string, ready to be written to a
        python file

        Args:
            args (dict):
                arguments to be used for this dumped run

        Returns:
            (str):
                serialised file
        """

        if args is None:
            args = {}

        return _SCRIPT_TEMPLATE.format(
            **{"function": self.source, "name": self.name, "args": args}
        )
