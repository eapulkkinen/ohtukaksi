class Project:
    def __init__(self, name, description, license_str, authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.license_str = license_str
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_dependencies(self, dependencies):
        return "\n- ".join(dependencies) if len(dependencies) > 0 else "-"

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license_str or '-'}\n"
            f"\nAuthors: \n- {self._stringify_dependencies(self.authors)}"
            f"\nDependencies: \n- {self._stringify_dependencies(self.dependencies)}"
            f"\nDevelopment dependencies: \n- {self._stringify_dependencies(self.dev_dependencies)}"
        )
