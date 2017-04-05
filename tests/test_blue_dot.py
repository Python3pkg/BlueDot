import pytest

from bluedot.mock import MockBlueDot

def test_client_connected():
    bd = MockBlueDot()
    bd._server.mock_client_connected()
    assert bd.is_connected
