import setuptools

setuptools.setup(
    name="streamlit-imp-sidebar",
    version="0.0.6",
    author="",
    author_email="",
    description="",
    long_description="",
    long_description_content_type="text/plain",
    url="",
    packages=setuptools.find_packages(),
    include_package_data=True,
    python_requires=">=3.8",
    install_requires=[
        "streamlit",
        # Add other dependencies
    ],
    package_data={
        "streamlit-imp-sidebar": ["frontend/build/*"],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
