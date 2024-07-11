import setuptools

PACKAGE_NAME = "organization-profile-local"
package_dir = PACKAGE_NAME.replace("-", "_")

setuptools.setup(
    name=PACKAGE_NAME,
    version='0.0.17',  # https://pypi.org/project/organization-profile-local
    author="Circles",
    author_email="info@circlez.ai",
    description="PyPI Package for Circles organization-profile-local Python",
    long_description="PyPI Package for Circles organization-profile-local Python",
    long_description_content_type='text/markdown',
    url=f"https://github.com/circles-zone/{PACKAGE_NAME}-python-package",
    packages=[package_dir],
    package_dir={package_dir: f'{package_dir}/src'},
    package_data={package_dir: ['*.py']},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'logger-local',
        'database-mysql-local',
    ],
)
