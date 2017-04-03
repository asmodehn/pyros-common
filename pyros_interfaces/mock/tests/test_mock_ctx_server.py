from __future__ import absolute_import

from pyros.client.client import PyrosClient
from pyros_interfaces.common.ctx_server import pyros_ctx
from pyros_interfaces.mock import PyrosMock


def testPyrosMockCtx():
    with pyros_ctx(node_impl=PyrosMock) as ctx:
        assert isinstance(ctx.client, PyrosClient)

    # TODO : assert the context manager does his job ( HOW ? )


if __name__ == '__main__':

    import nose
    nose.runmodule()
