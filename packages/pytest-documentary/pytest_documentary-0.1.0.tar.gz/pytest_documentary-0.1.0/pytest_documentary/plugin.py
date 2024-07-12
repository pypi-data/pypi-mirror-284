import os

import pytest
import pandas as pd


def pytest_addoption(parser):
    parser.addoption(
        "--pytest-documentary",
        action="store_true",
        default=False,
        help="Generate test documentation"
    )
    parser.addini(
        "documentary-enabled",
        type="bool",
        default=None,
        help="Generate test documentation"
    )
    parser.addoption(
        "--documentary-output-file",
        action="store",
        default=None,
        help="Output file for test documentation"
    )
    parser.addini(
        "documentary-output-file",
        type="string",
        default="documentary_output.xlsx",
        help="Output file for test documentation"
    )
    parser.addoption(
        "--documentary-output-path",
        action="store",
        default=None,
        help="Output path for test documentation"
    )
    parser.addini(
        "documentary-output-path",
        type="string",
        default='./',
        help="Output path for test documentation"
    )


def pytest_configure(config):
    enabled = config.getini("documentary-enabled")
    if enabled is None:
        enabled = config.getoption("--pytest-documentary")
    config._generate_documentation = enabled

    output_file = config.getoption("--documentary-output-file")
    if output_file is None:
        output_file = config.getini("documentary-output-file")
    config._documentary_output_file = output_file

    output_path = config.getoption("--documentary-output-path")
    if output_path is None:
        output_path = config.getini("documentary-output-path")
    config._documentary_output_path = output_path


def pytest_collection_modifyitems(config, items):
    print(not config._generate_documentation)
    if not config._generate_documentation:
        return
    config._pytest_documentary_collected_data = []
    for item in items:
        function_data = {
            "Test name": item.name,
            "Test location": item.location,
            "Function nodeId": item.nodeid,
            "Own markers": [marker.name for marker in item.own_markers]
        }
        config._pytest_documentary_collected_data.append(function_data)


def pytest_terminal_summary(terminalreporter, exitstatus, config):
    if not config._generate_documentation:
        return
    collected_data = getattr(config, "_pytest_documentary_collected_data", [])
    if collected_data:
        output_file = config._documentary_output_file
        output_path = config._documentary_output_path
        output = output_path.rstrip("/") + "/" + output_file

        df = pd.DataFrame(collected_data)
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        df.to_excel(output, index=False)

        terminalreporter.write_sep("=", f"Test documentation generated at {output}")
