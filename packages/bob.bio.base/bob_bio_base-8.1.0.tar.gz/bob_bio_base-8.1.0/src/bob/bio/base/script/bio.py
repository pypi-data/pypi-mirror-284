"""The main entry for bob.bio (click-based) scripts.
"""
import importlib.metadata

import click

from clapper.click import AliasedGroup
from click_plugins import with_plugins


@with_plugins(importlib.metadata.entry_points(group="bob.bio.cli"))
@click.group(cls=AliasedGroup)
def bio():
    """Biometric recognition commands."""
    pass
