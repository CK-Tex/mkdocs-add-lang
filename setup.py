from setuptools import setup

setup(
    name="mkdocs-add-lang",
    version="0.0.3",
    author="CK_Tex",
    packages=["mkdocs_add_lang"],
    entry_points={
        "mkdocs.plugins": [
            "addlang = mkdocs_add_lang.plugin:LangPlugin",
        ],
    },
)
