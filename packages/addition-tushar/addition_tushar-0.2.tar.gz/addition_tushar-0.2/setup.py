from setuptools import setup, find_packages

# setup(
#     name='addition', 
#     version='0.1',
#     packages=find_packages(),
#     install_requires=[
#         'numpy',
#         'pandas'
#     ],
# )

setup(
    name='addition_tushar', 
    version='0.2',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas'
    ],
    entry_points = {
        "console_scripts": [
            "add = addition_tushar: add_main",
        ],
    },
)

