# -*- coding: utf-8 -*-
"""RDFlib Graph Factory for SmartContainers.

This module provides a common interface to all RDFlib graphs created by all
vocabularies. New vocabularies should subclass graphFactory.
"""


class GraphFactory:
    """Base GraphFactory."""

    factories = {}
    def addFactory(id, graphFactory):
        """TODO: addFactory registers a new graph.

        Args:
            id (TODO): TODO
            graphFactory (TODO): TODO

        Returns: None
        """
        GraphFactory.factories.put[id] = graphFactory
    addFactory = staticmethod(addFactory)
    # A Template Method:
    def createGraph(id):
        """TODO: createGraph registers a new graph.

        Args:
            id (TODO): TODO
            graphFactory (TODO): TODO

        Returns: None
        """
        if not (id in GraphFactory.factories):
            GraphFactory.factories[id] = \
              eval(id + '.Factory()')
        return GraphFactory.factories[id].create()
    createGraph = staticmethod(createGraph)


class Graph(object):
    """Base Graphfactory Graph."""

    def __init__(self):
        """TODO: to be defined1."""
