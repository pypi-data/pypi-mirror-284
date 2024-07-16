from setuptools import setup, find_packages

setup(
    name='owo_pjt',
    version='0.0.1',
    description='owo pjt(the elice Original widget based on Orange3)',
    author='yongjin Kim',
    author_email='yongjinkim@elicer.com',
    install_requires=['Orange3', 'openai', ],
    packages=find_packages(exclude=[]),
    keywords=['orange3', 'genAI', 'openai', 'orange3 tutorial'],
    python_requires='>=3.6',
    package_data={},
    zip_safe=False,
)
