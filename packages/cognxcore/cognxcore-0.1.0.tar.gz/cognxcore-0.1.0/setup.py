from setuptools import setup, find_packages


VERSION = '0.1.0'
DESCRIPTION = 'Gemini python bridge'

#setting up
setup(
    name = "cognxcore",
    version=VERSION,
    author= "Conradium",
    author_email= "<leiconrad5@gmail.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['google.generativeai'],
    keywords=['python', 'ai', 'gemini'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows"
    ]
)