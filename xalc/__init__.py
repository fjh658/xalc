# -*- coding: utf-8 -*-

from .transformer import XalcInputTransformer
from .formatter import XalcFormatter


def load_ipython_extension(ip):
    transformer = XalcInputTransformer()
    ip.input_transformer_manager.logical_line_transforms.append(transformer)

    formatter = ip.display_formatter.formatters['text/plain']
    formatter.for_type(int, XalcFormatter().format_int)
