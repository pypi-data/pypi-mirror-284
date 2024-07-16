# Qualia-Plugin-Template
Copyright 2023 © Pierre-Emmanuel Novac <penovac@unice.fr> Université Côte d'Azur, LEAT. All rights reserved.

Template plugin for Qualia.

## How to create a plugin from the template

### Install Qualia

Install Qualia with the developer setup using PDM by following the [Installation guide](https://naixtech.unice.fr/~gitlab/docs/qualia/Installation.html).

### Install Qualia-Plugin-Template

Move into the base Qualia folder, then clone the Qualia-Plugin-Template repository:
```
git clone ssh://git@naixtech.unice.fr:2204/qualia/qualia-plugin-template.git
```

If you do not have an SSH key registered in Gitlab, use the HTTPS URL instead:
```
git clone https://naixtech.unice.fr/gitlab/qualia/qualia-plugin-template.git
```

Then install it:
```
pdm add -e ./qualia-plugin-template --dev
```

### Create a new Git repository for your plugin

In the Gitlab web interface of the [Qualia group](https://naixtech.unice.fr/gitlab/qualia),
create a new repository by clicking the `New project` button. Select `Create blank project`.

Set `Qualia-Plugin-<name>` as the project name, with `<name>` replaced by the name of your plugin.

Select the appropriate visibility level

Uncheck `Initialize repository with a README`.

Finally, click `Create project`.

### Generate a plugin project from the template

Move into the base Qualia folder, then generate the plugin project:
```
pdm run qualia-create-plugin <name>
```
`<name>` should be replaced by the name of your plugin (without the `qualia-plugin-` prefix).

Then, follow the questions asked to provide the author's name and email address, the homepage and git repository of the plugin.

For more information about the structure of the created plugin project,
see [Repository structure](https://naixtech.unice.fr/~gitlab/docs/qualia/Developer/RepositoryStructure.html).

### Push the new plugin to the git repository

Move into the newly created plugin's folder:
```
cd qualia-plugin-<name>
```

Then push the new content to the repository:
```
git push -u origin master
```

### Edit the plugin dependencies 

Edit the `pyproject.toml` file to fill the dependencies required by your plugin,
in particular any other required Qualia plugin.
You can choose between mandatory or optional dependencies.
Any item inside angle brackets `<>` must be replaced by a value of your choice.

#### Mandatory dependencies

```
[project]
dependencies = [
  '<dependency1>',
  '<…>',
  '<dependencyN>',
]
```

#### Optional dependency groups

```
[project.optional-dependencies]
<group1> = ['<dependency1>', '<…>', '<dependencyN>']
<…>
<groupN> = ['<dependency1>', '<…>', '<dependencyN>']
```

### Edit `README.md`

Edit the `README.md` file to provide the description of your plugin, a short user guide and any information that the user must know about to use your plugin.

### Install the plugin and its dependencies

Move into the base Qualia folder, then install your plugin:

Then install it:
```
pdm add -e ./qualia-plugin-<name>[<group1>,<group2>] --dev
```
with `<name>` the name of your plugin and `<group1>`, `<group2>` optional dependency groups.

### Edit documentation builder configuration

If the documentation of the plugin needs to cross-reference external Python modules, add the link to the documentation in the InterSphinx mapping of the `docs/conf.py` file.
Any item inside angle brackets `<>` must be replaced by a value of your choice.

```
intersphinx_mapping = {
    '<external_module_name>': ('<documentation_url>', None),
}
```

### Provide the Python source files of your module

Add any source file for your module under one of Qualia's package in the `src/qualia_plugin_<name>/` folder.

Dummy modules for the dataset, learningmodel.pytorch, postprocessing and preprocessing are supplied in the template to illustrate adding new modules for these packages.
A learningframework override for PyTorch is provided to illustrate overriding an existing module, and, in this case, import the supplied Dummy learningmodel for use with PyTorch.
These Dummy modules must be removed before publishing you plugin, unnecessary packages should also be removed.

For more information about the various Qualia packages, see [Python package structure](https://naixtech.unice.fr/~gitlab/docs/qualia/Developer/PackageStructure.html).
For more information about how the plugin's packages are loaded, see [Plugin architecture](https://naixtech.unice.fr/~gitlab/docs/qualia/Developer/PluginArchitecture.html).

### Provide example configuration files

Add example configuration files in the `conf/` directory to demonstrate the usage of your plugin.

All configuration files must load the plugin:
```
[bench]
plugins = ['qualia_plugin_<name>']
```

A Dummy configuration is provided in the template to load the provided Dummy modules. The Dummy configuration must be removed before publishing your plugin.

For more information about configuration files, see: [Configuration file](https://naixtech.unice.fr/~gitlab/docs/qualia/User/ConfigurationFile.html)

### Provide documentation

Add any API documentation as docstrings in your source files.

Add any high-level documentation pages in the `docs/` directory and reference them in the documentation homepage file `docs/index.rst`.

For more information about writing documentation, see: [Writing documentation](https://naixtech.unice.fr/~gitlab/docs/qualia/Developer/Documentation.html).

### Provide tests for your plugin modules

Add any automatic testing modules that use the PyTest framework in the `tests/` directory.

For more information about tests, see: [Tests](https://naixtech.unice.fr/~gitlab/docs/qualia/Developer/Tests.html)
