from setuptools import find_packages, setup

PACKAGE_NAME = "context_info_flow"

setup(
    name=PACKAGE_NAME,
    version="0.0.1",
    description="This is including context information for LLM response",
    packages=find_packages(),
    entry_points={
        "package_tools": [
            "context_info_tool = context_info.tools.utils:list_package_tools"
        ],
    },
    include_package_data=True,  # This line tells setuptools to include files from MANIFEST.in
)
