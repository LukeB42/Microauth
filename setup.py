# _*_ coding: utf-8 _*_
from setuptools import setup, find_packages
banner= """
██████╗ ███████╗██╗   ██╗██████╗ ███████╗██████╗ ███╗   ██╗███████╗████████╗██╗ ██████╗███████╗   
██╔══██╗██╔════╝╚██╗ ██╔╝██╔══██╗██╔════╝██╔══██╗████╗  ██║██╔════╝╚══██╔══╝██║██╔════╝██╔════╝   
██████╔╝███████╗ ╚████╔╝ ██████╔╝█████╗  ██████╔╝██╔██╗ ██║█████╗     ██║   ██║██║     ███████╗   
██╔═══╝ ╚════██║  ╚██╔╝  ██╔══██╗██╔══╝  ██╔══██╗██║╚██╗██║██╔══╝     ██║   ██║██║     ╚════██║   
██║     ███████║   ██║   ██████╔╝███████╗██║  ██║██║ ╚████║███████╗   ██║   ██║╚██████╗███████║██╗
╚═╝     ╚══════╝   ╚═╝   ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝ ╚═════╝╚══════╝╚═╝
"""
print banner

setup(
    name="microauth",
    version='0.1.3',
    packages=["microauth", "microauth.resources"],
    zip_safe=False,
    install_requires=[
        "Flask-RESTful",
        "Flask-SQLAlchemy",
        "bcrypt",
        "gevent",
        "requests",
        "pyopenssl",
    ]
)
