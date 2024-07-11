from setuptools import find_packages, setup

PACKAGE_NAME = "place_intelligence_prompt_flow"

setup(
    name=PACKAGE_NAME,
    version="0.0.3",
    description="This is Place Intelligence prompt flow",
    long_description="This is Place Intelligence prompt flow",
    packages=find_packages(),
    entry_points={
        "package_tools": ["place_api_tool = place.tools.utils:list_package_tools"],
    },
    include_package_data=True,  # This line tells setuptools to include files from MANIFEST.in
)
