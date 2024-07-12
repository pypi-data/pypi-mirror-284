import setuptools

setuptools.setup(
    name="RenderKit",
    version="1.0.0",
    description="Simplifying app development with Python and HTML rendering.",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/cj-praveen/RenderKit/",
    keywords="RenderKit",
    package_dir={"": "src"},
    python_requires=">=3.9"
)
