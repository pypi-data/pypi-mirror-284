from setuptools import find_packages, setup

PACKAGE_NAME = "recommendation_intelligence_flow"

setup(
    name=PACKAGE_NAME,
    version="0.0.2",
    description="This is Recommendation Intelligence prompt flow",
    long_description="This is Recommendation Intelligence prompt flow",
    packages=find_packages(),
    entry_points={
        "package_tools": [
            "recommendation_api_tool = recommendation.tools.utils:list_package_tools"
        ],
    },
    include_package_data=True,  # This line tells setuptools to include files from MANIFEST.in
)
