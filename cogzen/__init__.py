#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Top-level package for CogZen."""

# fmt: off
from . import _version
__version__ = _version.get_versions()['version']
__version_dict__ = _version.get_versions()
# fmt: on

__author__ = """cogsys.io"""
__email__ = "cogsys@cogsys.io"


from . import aux_sys
from .aux_sys import chdir
from .aux_sys import pushdir
from .aux_sys import pushdir as pdir

from . import aux_log  # noqa: F401
from .aux_log import Log0

from . import aux_str
from .aux_str import clean_str
from .aux_str.now import now

from . import aux_pandas
from .aux_pandas import disp_df
from .aux_pandas import repr_df
from .aux_pandas import disp_df as ddf
from .aux_pandas import repr_df as rdf

from . import aux_srsly
from .aux_srsly import jsonable
from .aux_srsly import yamlstr

from . import aux_bids


def get_module_version():
    return __version__


# end
