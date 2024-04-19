# -*- coding: utf-8 -*-
# Copyright (c) Facebook, Inc. and its affiliates.

# flake8: noqa

# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
import mock
from sphinx.domains import Domain
from typing import Dict, List, Tuple

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
import sphinx_rtd_theme


class GithubURLDomain(Domain):
    """
    Resolve certain links in markdown files to github source.
    """

    name = "githuburl"
    ROOT = "https://github.com/facebookresearch/detectron2/blob/master/"
    LINKED_DOC = ["tutorials/install", "tutorials/getting_started"]

    def resolve_any_xref(self, env, fromdocname, builder, target, node, contnode):
        github_url = None
        if not target.endswith("html") and target.startswith("../../"):
            url = target.replace("../", "")
            github_url = url
        if fromdocname in self.LINKED_DOC:
            # unresolved links in these docs are all github links
            github_url = target

        if github_url is not None:
            if github_url.endswith("MODEL_ZOO") or github_url.endswith("README"):
                # bug of recommonmark.
                # https://github.com/readthedocs/recommonmark/blob/ddd56e7717e9745f11300059e4268e204138a6b1/recommonmark/parser.py#L152-L155
                github_url += ".md"
            print("Ref {} resolved to github:{}".format(target, github_url))
            contnode["refuri"] = self.ROOT + github_url
            return [("githuburl:any", contnode)]
        else:
            return []


# to support markdown
from recommonmark.parser import CommonMarkParser

sys.path.insert(0, os.path.abspath("../"))
os.environ["DOC_BUILDING"] = "True"
DEPLOY = os.environ.get("READTHEDOCS") == "True"


# -- Project information -----------------------------------------------------

# fmt: off
try:
    import torch  # noqa
except ImportError:
    for m in [
        "torch", "torchvision", "torch.nn", "torch.nn.parallel", "torch.distributed", "torch.multiprocessing", "torch.autograd",
        "torch.autograd.function", "torch.nn.modules", "torch.nn.modules.utils", "torch.utils", "torch.utils.data", "torch.onnx",
        "torchvision", "torchvision.ops",
    ]:
        sys.modules[m] = mock.Mock(name=m)
    sys.modules['torch'].__version__ = "1.5"  # fake version

for m in [
    "cv2", "scipy", "portalocker", "detectron2._C",
    "pycocotools", "pycocotools.mask", "pycocotools.coco", "pycocotools.cocoeval",
    "google", "google.protobuf", "google.protobuf.internal", "onnx",
    "caffe2", "caffe2.proto", "caffe2.python", "caffe2.python.utils", "caffe2.python.onnx", "caffe2.python.onnx.backend",
]:
    sys.modules[m] = mock.Mock(name=m)
# fmt: on
sys.modules["cv2"].__version__ = "3.4"

import detectron2  # isort: skip


project = "detectron2"
copyright = "2019-2020, detectron2 contributors"
author = "detectron2 contributors"

# The short X.Y version
version = detectron2.__version__
# The full version, including alpha/beta/rc tags
release = version


# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
needs_sphinx = "3.0"

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "recommonmark",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx.ext.coverage",
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
    "sphinx.ext.githubpages",
]

# -- Configurations for plugins ------------
napoleon_google_docstring = True
napoleon_include_init_with_doc = True
napoleon_include_special_with_doc = True
napoleon_numpy_docstring = False
napoleon_use_rtype = False
autodoc_inherit_docstrings = False
autodoc_member_order = "bysource"

if DEPLOY:
    intersphinx_timeout = 10
else:
    # skip this when building locally
    intersphinx_timeout = 0.1
intersphinx_mapping = {
    "python": ("https://docs.python.org/3.6", None),
    "numpy": ("https://docs.scipy.org/doc/numpy/", None),
    "torch": ("https://pytorch.org/docs/master/", None),
}
# -------------------------


# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

source_suffix = [".rst", ".md"]

# The master toctree document.
master_doc = "index"

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "build", "README.md", "tutorials/README.md"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"


# -- Options for HTML output -------------------------------------------------

html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
html_css_files = ["css/custom.css"]

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "detectron2doc"


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',
    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, "detectron2.tex", "detectron2 Documentation", "detectron2 contributors", "manual")
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(master_doc, "detectron2", "detectron2 Documentation", [author], 1)]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        "detectron2",
        "detectron2 Documentation",
        author,
        "detectron2",
        "One line description of project.",
        "Miscellaneous",
    )
]


# -- Options for todo extension ----------------------------------------------

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True


def autodoc_skip_member(app, what, name, obj, skip, options):
    # we hide something deliberately
    if getattr(obj, "__HIDE_SPHINX_DOC__", False):
        return True

    # Hide some that are deprecated or not intended to be used
    HIDDEN = {
        "ResNetBlockBase",
        "GroupedBatchSampler",
        "build_transform_gen",
        "export_caffe2_model",
        "export_onnx_model",
        "apply_transform_gens",
        "TransformGen",
        "apply_augmentations",
        "StandardAugInput",
        "build_batch_data_loader",
    }
    try:
        if obj.__doc__.lower().strip().startswith("deprecated") or name in HIDDEN:
            print("Skipping deprecated object: {}".format(name))
            return True
    except:
        pass
    return skip


_PAPER_DATA = {
    "resnet": ("1512.03385", "Deep Residual Learning for Image Recognition"),
    "fpn": ("1612.03144", "Feature Pyramid Networks for Object Detection"),
    "mask r-cnn": ("1703.06870", "Mask R-CNN"),
    "faster r-cnn": (
        "1506.01497",
        "Faster R-CNN: Towards Real-Time Object Detection with Region Proposal Networks",
    ),
    "deformconv": ("1703.06211", "Deformable Convolutional Networks"),
    "deformconv2": ("1811.11168", "Deformable ConvNets v2: More Deformable, Better Results"),
    "panopticfpn": ("1901.02446", "Panoptic Feature Pyramid Networks"),
    "retinanet": ("1708.02002", "Focal Loss for Dense Object Detection"),
    "cascade r-cnn": ("1712.00726", "Cascade R-CNN: Delving into High Quality Object Detection"),
    "lvis": ("1908.03195", "LVIS: A Dataset for Large Vocabulary Instance Segmentation"),
    "rrpn": ("1703.01086", "Arbitrary-Oriented Scene Text Detection via Rotation Proposals"),
    "imagenet in 1h": ("1706.02677", "Accurate, Large Minibatch SGD: Training ImageNet in 1 Hour"),
    "xception": ("1610.02357", "Xception: Deep Learning with Depthwise Separable Convolutions"),
    "mobilenet": (
        "1704.04861",
        "MobileNets: Efficient Convolutional Neural Networks for Mobile Vision Applications",
    ),
}


def paper_ref_role(
    typ: str,
    rawtext: str,
    text: str,
    lineno: int,
    inliner,
    options: Dict = {},
    content: List[str] = [],
):
    """
    Parse :paper:`xxx`. Similar to the "extlinks" sphinx extension.
    """
    from docutils import nodes, utils
    from sphinx.util.nodes import split_explicit_title

    text = utils.unescape(text)
    has_explicit_title, title, link = split_explicit_title(text)
    link = link.lower()
    if link not in _PAPER_DATA:
        inliner.reporter.warning("Cannot find paper " + link)
        paper_url, paper_title = "#", link
    else:
        paper_url, paper_title = _PAPER_DATA[link]
        if "/" not in paper_url:
            paper_url = "https://arxiv.org/abs/" + paper_url
    if not has_explicit_title:
        title = paper_title
    pnode = nodes.reference(title, title, internal=False, refuri=paper_url)
    return [pnode], []


def setup(app):
    from recommonmark.transform import AutoStructify

    app.add_domain(GithubURLDomain)
    app.connect("autodoc-skip-member", autodoc_skip_member)
    app.add_role("paper", paper_ref_role)
    app.add_config_value(
        "recommonmark_config",
        {"enable_math": True, "enable_inline_math": True, "enable_eval_rst": True},
        True,
    )
    app.add_transform(AutoStructify)
