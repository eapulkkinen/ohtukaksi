import toml
from urllib import request
from project import Project


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        print(content)

        parsed = toml.loads(content)
        print(parsed)
        tool = parsed["tool"]
        print(tool)
        poetry = tool["poetry"]
        print(poetry)
        group = poetry["group"]
        print(group)
        dev = group["dev"]
        print(dev)

        name = poetry["name"]
        print(name)

        description = poetry["description"]
        print(description)

        license_str = poetry["license"]
        print(license_str)

        authors = poetry["authors"]
        print(authors)

        dependencies = poetry["dependencies"]
        print(dependencies)

        development_dependencies = dev["dependencies"]
        print(development_dependencies)
        #development_dependencies = poetry["group"]
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, description, license_str, authors, dependencies, development_dependencies)