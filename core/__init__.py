from core.orchestrator import Orchestrator
from ipywidgets import widgets
from IPython.display import display, Image
from core.category_component import CategoryComponent
from core.db_client import DBClient
import pandas as pd
from core.ed_component import EDComponent
from core.blockchain_client import BlockchainClient
from core.dml_client import DMLClient
import numpy as np
import configparser


class Explora(Orchestrator):
    """
    Directly called by user to set up Orchestrator and components it uses.
    """
    def __init__(self, config_filepath='configuration.ini'):
        """
        Wrapper around Orchestrator so that:

        1. User simply has to call "explora.<command>" to execute functions
           in Orchestrator
        2. We maintain use of dependency injection, which simplifies testing.
        """
        config = configparser.ConfigParser()
        config.read(config_filepath)
        db_client = DBClient(config)
        blockchain_client = BlockchainClient(config)
        dml_client = DMLClient(config)
        category_component = CategoryComponent(db_client, blockchain_client)
        ed_component = EDComponent()
        Orchestrator.__init__(self, category_component, ed_component, dml_client)

