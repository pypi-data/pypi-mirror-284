"""
The ``mlflow.models`` module provides an API for saving machine learning models in
"flavors" that can be understood by different downstream tools.

The built-in flavors are:

For details, see `MLflow Models <../models.html>`_.
"""

from ..utils.environment import infer_pip_requirements
from .model import Model

__all__ = [
    "Model",
    "infer_pip_requirements",
]


# Under skinny-mlflow requirements, the following packages cannot be imported
# because of lack of numpy/pandas library, so wrap them with try...except block
try:
    from .signature import (  # pylint: disable=unused-import
        ModelSignature,
        infer_signature,
    )
    from .utils import ModelInputExample  # pylint: disable=unused-import

    __all__ += [
        "ModelSignature",
        "ModelInputExample",
        "infer_signature",
    ]
except ImportError:
    pass
