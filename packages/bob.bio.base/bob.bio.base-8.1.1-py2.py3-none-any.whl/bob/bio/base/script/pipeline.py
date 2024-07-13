import importlib.metadata

import click

from clapper.click import AliasedGroup
from click_plugins import with_plugins


@with_plugins(importlib.metadata.entry_points(group="bob.bio.pipeline.cli"))
@click.group(cls=AliasedGroup)
def pipeline():
    """Available pipelines"""
    pass
