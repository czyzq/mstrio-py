![MicroStrategy Logo][logo]

[![image](https://img.shields.io/pypi/v/mstrio-py.svg)](https://pypi.org/project/mstrio-py)
[![image](https://img.shields.io/pypi/l/mstrio-py.svg)](https://pypi.org/project/mstrio-py)
[![image](https://img.shields.io/pypi/dm/mstrio-py.svg)](https://pypi.org/project/mstrio-py)

# mstrio: Simple and Secure Access to MicroStrategy Data <!-- omit in toc -->

**mstrio** provides a high-level interface for [Python][py_github] and [R][r_github] and is designed to give **data scientists**, **developers**, and **administrators** simple and secure access to their MicroStrategy environment. It wraps [MicroStrategy REST APIs][mstr_rest_docs] into simple workflows, allowing users to fetch data from cubes and reports, create new datasets, add new data to existing datasets, and manage Users/User Groups, Servers, Projects, and more. Since it enforces MicroStrategy’s user and object security model, you don’t need to worry about setting up separate security rules.

With mstrio-py for **data science**, it’s easy to integrate cross-departmental, trustworthy business data in machine learning workflows and enable decision-makers to take action on predictive insights in MicroStrategy Reports, Dossiers, HyperIntelligence Cards, and customized, embedded analytical applications.

With mstrio-py for **system administration**, it’s easy to minimize costs by automating critical, time-consuming administrative tasks, even enabling administrators to leverage the power of Python to address complex administrative workflows for maintaining a MicroStrategy environment.

**MicroStrategy for Jupyter** is an extension for Jupyter Notebook which provides a graphical user interface for mstrio-py methods with the help of which user can perform all of the import and export actions without writing a single line of code manually. MicroStrategy for Jupyter is contained within mstrio-py package and is available after installation and enabling as Jupyter extension

# Table of Contents <!-- omit in toc -->

<!--ts-->

- [Main Features](#main-features)
- [Documentation](#documentation)
- [Usage Remarks](#usage-remarks)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
    - [mstrio-py](#mstrio-py)
    - [MicroStrategy for Jupyter](#microstrategy-for-jupyter)
  - [Install the `mstrio-py` Package](#install-the-mstrio-py-package)
  - [Enable the Jupyter Notebook extension](#enable-the-jupyter-notebook-extension)
- [Versioning & Changelog](#versioning--changelog)
- [Deprecating Features](#deprecating-features)
- [More Resources](#more-resources)
- [Other](#other)
<!--te-->

# Main Features<a id="main-features"></a>

Main features of **mstrio-py** allows to access MicroStrategy data:

- Connect to your MicroStrategy environment using **Connection** class (see [examples][example_conn])

  **Note**: to log into Library and use mstrio-py user needs to have _UseLibrary_ privilege.

- Import and filter data from a **OlapCube**, **SuperCube** or **Report** into a Pandas DataFrame (see [examples][example_import])
- Export data into MicroStrategy by creating or updating **SuperCube** (see [examples][example_export])

Since version **11.3.0.1**, **mstrio-py** includes also administration modules:

- **Project** management module (see [examples][example_project])
- **Server** management module (see [examples][example_server])
- **User** and **Usergroup** management modules (see [examples][example_user])
- **Schedules** management module (see [examples][example_schedules])
- **Subscription** management modules including **Email Subscription** and **Cache Update Subscription** (see [examples][example_subs])
- **Document** and **Dossiers** in **User Library** modules (see [examples][example_library])
- **User Connections** management module
- **Privilege** and **Security Role** management modules
- **Cube Cache** management modules (see [examples][example_cache])
- **Intelligent Cube** management modules (see [examples][example_olap])
- **Security filter** module (see [examples][example_security_filter])
- **Datasources** subpackage for database management (see [examples][example_datasource])
- **Job Monitor** module for job monitoring (see [examples][example_job_monitor])
- **Object management** module (see [examples][example_object_mgmt])
- **Contact** module (see [examples][example_contact])
- **Contact Group** module (see [examples][example_contact_group])
- **Device** module (see [examples][example_device])
- **Transmitter** module (see [examples][example_transmitter])
- **Event** module (see [examples][example_events])

Known limitations in v11.3.4.101:

- `mstrio.server.migration` module is work in progress and not all functionalities are available yet.
We plan to release them on 03.2022.

# Documentation<a id="documentation"></a>

Detailed information about **mstrio-py** package can be found in [**official documentation**][mstrio_py_doc].

# Usage Remarks<a id="usage-remarks"></a>

## General

- **Chrome** is the only supported web browser. `mstrio-py` should work properly in **Safari**, **Opera** or **Edge** but we cannot guarantee a seamless experience.
- It is recommended NOT to use Anaconda environment. Please see **Installation** section below for details.

## GUI

- GUI `Import -> Prepare Data` filters out all "**_Row Count - ..._**" columns even if they are an integral part of a Dataset. Starting column's name with "_Row Count_" is not advised.

## Backend

- Currently it is not possible to use `mstrio-py` package to update cubes created via Web. Unfortunately it is not possible to use any REST API endpoint to check whether cube was created
via Web or via REST API to provide some warning. In case of seeing one of the following error
messages it is most probable that cube was created via Web and REST API can't handle its update,
so if you want to update this particular cube you have to use Web.

```
When we tried to map the new dataset, we detected that some columns are missing or the data type changed, etc.
```

```
We could not obtain the data because the DB connection changed and the table does not exist anymore.
```

- When trying to download a big IMDB Cube (or a Report based on such Cube) on multi-node environment, sometimes the process may fail. This is due to the characteristic of data retrieval of IMDB Cubes with connection to more than one node on iServer. For now, known workaround is to log out and just simply try again. This type of issue can be identified when seeing any of the following error messages during work with IMDB Cube on multi-node environment:

```
Cube cannot be found.
```
(even if previously it was found without issue)

```
Error getting cube metadata information. I-Server Error ERR001, (ServiceManager: XML syntax error.)
```

# Installation<a id="installation"></a>

## Prerequisites<a id="prerequisites"></a>

### mstrio-py<a id="mstrio-py"></a>

- Python 3.6+
- MicroStrategy 2019 Update 4 (11.1.4)+

### MicroStrategy for Jupyter<a id="microstrategy-for-jupyter"></a>

- [CORS enabled on MicroStrategy Library server][cors_manual]
- [Cookies sent by MicroStrategy Library server have 'SameSite' parameter set to 'None'][same_site_manual]

## Install the `mstrio-py` Package<a id="install-the-mstrio-py-package"></a>

**Note**: it is NOT recommended to install mstrio-py in an Anaconda environment.
For a seamless experience, install and run it in Python's [virtual environment][python_venv] instead.

Installation is easy when using [pip](https://pypi.org/project/mstrio-py). Read more about installation on MicroStrategy's [product documentation][mstr_help_docs].

```bash
pip install mstrio-py
```

## Enable the Jupyter Notebook extension<a id="enable-the-jupyter-notebook-extension"></a>

Once mstrio-py is installed you can install and enable the Jupyter Notebook extension by using the commands below:

```
jupyter nbextension install connector-jupyter --py --sys-prefix
jupyter nbextension enable connector-jupyter --py --sys-prefix
```

# Versioning & Changelog<a id="versioning--changelog"></a>

Current version: **11.3.4.101** (28 January 2022). Check out [**Changelog**][release_notes] to see what's new.

mstrio-py is constantly developed to support newest MicroStrategy REST APIs. Functionalities may be added to mstrio on monthly basis. It is **recommended** to always install the newest version of mstrio-py, as it will be most stable and still maintain backwards compatibility with various MicroStrategy installations, dating back to 11.1.4.

Features that will be added to the package but require APIs not supported by your environment (I-Server), will raise `VersionException`.

mstrio-py can be used for both, **data-science** related activities and for **administrative tasks**. Former requires at least MicroStrategy 2019 Update 4 (11.1.4), latter works with 11.2.1 and higher.

If you intend to use mstrio with MicroStrategy version older than 11.1.4, refer to the PyPI package archive to download mstrio 10.11.1, which is supported on:

- MicroStrategy 2019 (11.1)
- MicroStrategy 2019 Update 1 (11.1.1)
- MicroStrategy 2019 Update 2 (11.1.2)
- MicroStrategy 2019 Update 3 (11.1.3)

Refer to the [PyPI package archive][pypi_archive] for a list of available versions.

To install a specific, archived version of mstrio, choose the desired version available on [PyPI package archive][pypi_archive] and install with `pip`, as follows:

```python
pip install mstrio-py==10.11.1
```

# Deprecating Features<a id="deprecating-features"></a>

When features (modules, parameters, attributes, methods etc.) are marked for deprecation but still accessed, the following `DeprecationWarning` will be shown (example below). The functionality will continue to work until the version specified in the warning is released.

![Deprecation warning ][deprecation]

# More Resources<a id="more-resources"></a>

- [Tutorials for mstrio][mstr_datasci_comm]
- [Check out mstrio for R][r_github]
- [Learn more about the MicroStrategy REST API][mstr_rest_docs]
- [MicroStrategy REST API demo documentation][mstr_rest_demo]

# Other<a id="other"></a>

"Jupyter" and the Jupyter logos are trademarks or registered trademarks of NumFOCUS.

[pypi_archive]: https://pypi.org/project/mstrio-py/#history
[py_github]: https://github.com/MicroStrategy/mstrio-py
[r_github]: https://github.com/MicroStrategy/mstrio
[mstr_datasci_comm]: https://community.microstrategy.com/s/topic/0TO44000000AJ2dGAG/python-r-u108
[mstrio_py_doc]: http://www2.microstrategy.com/producthelp/Current/mstrio-py/
[mstr_rest_demo]: https://demo.microstrategy.com/MicroStrategyLibrary/api-docs/index.html
[mstr_rest_docs]: https://lw.microstrategy.com/msdz/MSDL/GARelease_Current/docs/projects/RESTSDK/Content/topics/REST_API/REST_API.htm
[mstr_help_docs]: https://www2.microstrategy.com/producthelp/current/MSTR-for-Jupyter/Content/mstr_for_jupyter.htm
[cors_manual]: https://lw.microstrategy.com/msdz/MSDL/GARelease_Current/docs/projects/EmbeddingSDK/Content/topics/EnableCORS.htm
[same_site_manual]: https://community.microstrategy.com/s/article/Chrome-v80-Cookie-Behavior-and-the-impact-on-MicroStrategy-Deployments?language=undefined&t=1581355581289
[python_venv]: https://docs.python.org/3/tutorial/venv.html
[release_notes]: https://github.com/MicroStrategy/mstrio-py/blob/master/NEWS.md
[logo]: https://github.com/MicroStrategy/mstrio-py/blob/master/mstr-logo.png?raw=true
[deprecation]: https://github.com/MicroStrategy/mstrio-py/blob/master/deprecation.png?raw=true
[example_conn]: https://github.com/MicroStrategy/mstrio-py/blob/master/examples/connect.py
[example_contact]: https://github.com/MicroStrategy/mstrio-py/blob/master/examples/contacts.py
[example_contact_group]: https://github.com/MicroStrategy/mstrio-py/blob/master/examples/contact_group_mgmt.py
[example_device]: https://github.com/MicroStrategy/mstrio-py/blob/master/examples/device_mgmt.py
[example_import]: https://github.com/MicroStrategy/mstrio-py/blob/master/examples/cube_report.py
[example_export]: https://github.com/MicroStrategy/mstrio-py/blob/master/examples/create_super_cube.py
[example_project]: https://github.com/MicroStrategy/mstrio-py/blob/master/examples/project_mgmt.py
[example_server]: https://github.com/MicroStrategy/mstrio-py/blob/master/examples/server_mgmt.py
[example_user]: https://github.com/MicroStrategy/mstrio-py/blob/master/examples/user_mgmt.py
[example_schedules]: https://github.com/MicroStrategy/mstrio-py/blob/master/examples/schedules.py
[example_subs]: https://github.com/MicroStrategy/mstrio-py/blob/master/examples/subscription_mgmt.py
[example_library]: https://github.com/MicroStrategy/mstrio-py/blob/master/examples/user_library.py
[example_cache]: https://github.com/MicroStrategy/mstrio-py/blob/master/examples/cube_cache.py
[example_olap]: https://github.com/MicroStrategy/mstrio-py/blob/master/examples/intelligent_cube.py
[example_job_monitor]: https://github.com/MicroStrategy/mstrio-py/blob/master/examples/job_monitor.py
[example_object_mgmt]: https://github.com/MicroStrategy/mstrio-py/blob/master/examples/object_mgmt.py
[example_security_filter]: https://github.com/MicroStrategy/mstrio-py/blob/master/examples/security_filters.py
[example_datasource]: https://github.com/MicroStrategy/mstrio-py/blob/master/examples/datasource_mgmt.py
[example_transmitter]: https://github.com/MicroStrategy/mstrio-py/blob/master/examples/transmitter_mgmt.py
[example_events]: https://github.com/MicroStrategy/mstrio-py/blob/master/examples/events.py