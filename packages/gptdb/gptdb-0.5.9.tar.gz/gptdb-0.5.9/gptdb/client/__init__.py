"""This module is the client of the gptdb package."""

from .client import Client, ClientException  # noqa: F401

__ALL__ = ["Client", "ClientException"]
