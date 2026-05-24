import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))


@pytest.fixture
def client(tmp_path):
    db_path = str(tmp_path / "test.db")

    import src.app as app_module

    original_db_path = app_module.DB_PATH
    app_module.DB_PATH = db_path
    app_module.init_db()

    app_module.app.config["TESTING"] = True
    with app_module.app.test_client() as test_client:
        yield test_client

    app_module.DB_PATH = original_db_path
