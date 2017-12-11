from setuptools import setup

# Get the long description by reading the README
try:
    readme_content = open("README.rst").read()
except Exception as e:
    readme_content = ""

# Create the actual setup method
setup(
    name="s3cookiejar",
    version="1.0.0",
    description="HTTP Cookie Jar that reads from/writes to an S3 bucket (optional KMS encryption)",
    long_description=readme_content,
    install_requires=["boto3", "six"],
    author="Steve McMaster",
    author_email="mcmaster@hurricanelabs.com",
    maintainer="Steve McMaster",
    maintainer_email="mcmaster@hurricanelabs.com",
    url="https://github.com/hurricanelabs/python-s3cookiejar",
    license="MIT License",
    keywords=["aws", "s3", "cookiejar", "requests"],
    py_modules=["s3cookiejar"],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Development Status :: 4 - Beta",
    ]
)
