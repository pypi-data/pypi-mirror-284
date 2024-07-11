from setuptools import find_packages, setup

PACKAGE_NAME = "perplexity_api_tool"

setup(
    name=PACKAGE_NAME,
    version="0.0.1",
    description="This is perplexity response tool",
    packages=find_packages(),
    entry_points={
        "package_tools": [
            "perplexity_api_tool = perplexity.tools.utils:list_package_tools"
        ],
    },
    include_package_data=True,  # This line tells setuptools to include files from MANIFEST.in
)
