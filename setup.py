from setuptools import setup


setup(
    name='cldfbench_defilippo_et_al2012',
    py_modules=['cldfbench_defilippo_et_al2012'],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'cldfbench.dataset': [
            'defilippo_et_al2012=cldfbench_defilippo_et_al2012:Dataset',
        ]
    },
    install_requires=[
        'phlorest',
        'tqdm',
    ],
    extras_require={
        'test': [
            'pytest-cldf',
        ],
    },
)
