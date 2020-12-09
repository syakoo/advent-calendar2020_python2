import setuptools


setuptools.setup(
    name="hello-world",
    version="0.1",
    author="syakoo",
    author_email="hogehoge@hoge.hoge",
    description="Say Hello.",
    url="https://github.com/syakoo/advent-calender2020_python2",
    packages=["hello_world"],
    package_dir={"hello_world": "src/hello_world"},
    python_requires=">=3.8"
)
