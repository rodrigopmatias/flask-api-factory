from unittest import mock

from flask_api_factory.auth import allow_any, factory_authorize_config


def test_allow_any():
    allow_any(None)


def test_factory_authorize_config_with_defaults():
    conf = factory_authorize_config()

    for method in conf.values():
        assert method == allow_any


def test_factory_authorize_config_without_defaults():
    mocked_method = mock.Mock()
    conf = factory_authorize_config(mocked_method, mocked_method, mocked_method, mocked_method)

    for method in conf.values():
        assert method == mocked_method
        assert method != allow_any
