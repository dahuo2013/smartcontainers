# SmartContainers (sc) for docker enabled software and data preservation

SmartContainers is python wrapper for docker that facilitates the recording
and tracking of provenance information using the W3C recommendation [prov-o](http://www.w3.org/TR/prov-o/).
SmartConainers is being developed as part of the Data and Software Preservation  for Open Science [(DASPOS)](http://daspos.org) project.

Current build status  build status: [![Build Status](https://travis-ci.org/crcresearch/smartcontainers.svg?branch=master)](https://travis-ci.org/crcresearch/smartcontainers)

SmartContainers provides a command line tool, sc, that provides a surrogate for the docker command line tool.

```bash
sc --docker <docker command line>
```

Will create a docker label with provenance metadata using the W3C Prov-o vocabulary with respect to the
computational environment created or provided by a particular docker container.

A python setup file is provided for installation of the command line utility. It is recommended to install the tool in a Python virtual environment.

```bash
pip install .
```

Will install the tool and it's dependencies in a virtual environment. 

### Usage
To search [Orcid.org](http://www.orcid.org) for an Orcid ID and write the RDF graph information to the configuration file from the command line or shell:

`python cli.py config orcid`

This option gives you the ability to search for an Orcid user by name, email, and keywords, such as department, institution, or state.

-----------------------------------------------------------------
If you already know the Orcid ID or Orcid email of the user that you want to write a configuration file for, then you can use the following arguments:

`python cli.py config orcid -i 0000-0000-0000-0000`

`python cli.py config orcid -e your_email@gmail.com`

The configuration file will be written to a .sc directory created in your home directory.  In the future, the configuration file location will be a user option.
