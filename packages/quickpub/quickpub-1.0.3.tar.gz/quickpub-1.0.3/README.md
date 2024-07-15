# quickpub V1.0.3
**Tested python versions**: `3.8.0`, `3.9.0`, `3.10.13`,

Example usage of how this package was published
```python
from quickpub import publish, MypyRunner, PylintRunner, UnittestRunner, CondaPythonProvider, \
    PypircUploadTarget, SetuptoolsBuildSchema, GithubUploadTarget


def main() -> None:
    publish(
        name="quickpub",
        version="1.0.3",
        author="danielnachumdev",
        author_email="danielnachumdev@gmail.com",
        description="A python package to quickly configure and publish a new package",
        homepage="https://github.com/danielnachumdev/quickpub",
        build_schemas=[SetuptoolsBuildSchema()],
        upload_targets=[PypircUploadTarget(), GithubUploadTarget()],
        python_interpreter_provider=CondaPythonProvider(["base", "390", "380"]),
        quality_assurance_runners=[
            MypyRunner(bound="<=15", configuration_path="./mypy.ini"),
            PylintRunner(bound=">=0.8", configuration_path="./.pylintrc"),
            UnittestRunner(bound=">=0.8"),
        ],
        dependencies=["danielutils>=0.9.90"],
        min_python="3.8.0",
    )


if __name__ == '__main__':
    main()


```