# Frostshake/TrinityCoreClassic

This project is a fork of [TrinityCore](https://github.com/TrinityCore/TrinityCore), with the aim of adding support for the modern classic clients.

Development branch: **vanilla_classic**
Supported client: **classic 1.14.0.40618**

**TCC Discord:**
https://discord.gg/berq85VDGF

Notable references:

Link | Note
:------------: | :------------:
|[TrinityCore/TrinityCore [wotlk_classic]](https://github.com/Frostshake/TrinityCoreClassic/commit/2d50c3da52f356ba88ff5cdb38d537f1f02ccb00)|Project starting point.|
|[TDB 927.22082](https://github.com/TrinityCore/TrinityCore/releases/tag/TDB927.22082)| Database starting point.|
|[TrinityCore/TrinityCore [~legion]](https://github.com/TrinityCore/TrinityCore/commit/8725eec9c1c15f3e76bd9d524d4a5d8d0b3f0a44)|Reference for update fields.|
|[TrinityCore/TrinityCore [3.3.5]](https://github.com/TrinityCore/TrinityCore/tree/3.3.5)| Reference for classic behaviour. |
|[VMangos/Core](https://github.com/vmangos/core)|Reference data and classic behaviour.|
|[WowLegacyCore/HermesProxy](https://github.com/WowLegacyCore/HermesProxy)| 1.12/1.14 conversions. |


### Further Info
This project is an effort to build a version of trinitycore that is compatible with modern classic wow clients. Currently only `1.14.0` is supported, but I beleive more could be supported via conditional compilation, e.g a single code base for `1.14.x` and `2.5.x`.

As reference data already exists for the expansions covered, data will be imported in from other projects rather than maintaining seperate dataset here. Currently only a vmangos data importer exists (in-progress).

See `contrib/vmangos_db_import` & `python db_import.py`

--------------

# ![logo](https://community.trinitycore.org/public/style_images/1_trinitycore.png) TrinityCore (master)

[![Average time to resolve an issue](https://isitmaintained.com/badge/resolution/TrinityCore/TrinityCore.svg)](https://isitmaintained.com/project/TrinityCore/TrinityCore "Average time to resolve an issue") [![Percentage of issues still open](https://isitmaintained.com/badge/open/TrinityCore/TrinityCore.svg)](https://isitmaintained.com/project/TrinityCore/TrinityCore "Percentage of issues still open")

--------------


* [Build Status](#build-status)
* [Introduction](#introduction)
* [Requirements](#requirements)
* [Install](#install)
* [Reporting issues](#reporting-issues)
* [Submitting fixes](#submitting-fixes)
* [Copyright](#copyright)
* [Authors &amp; Contributors](#authors--contributors)
* [Links](#links)



## Build Status

master | 3.3.5
:------------: | :------------:
[![master Build Status](https://travis-ci.org/TrinityCore/TrinityCore.svg?branch=master)](https://travis-ci.org/TrinityCore/TrinityCore) | [![3.3.5 Build Status](https://travis-ci.org/TrinityCore/TrinityCore.svg?branch=3.3.5)](https://travis-ci.org/TrinityCore/TrinityCore)
[![master Build status](https://ci.appveyor.com/api/projects/status/54d0u1fxe50ad80o/branch/master?svg=true)](https://ci.appveyor.com/project/DDuarte/trinitycore/branch/master) | [![Build status](https://ci.appveyor.com/api/projects/status/54d0u1fxe50ad80o/branch/3.3.5?svg=true)](https://ci.appveyor.com/project/DDuarte/trinitycore/branch/3.3.5)
[![Coverity Scan Build Status](https://scan.coverity.com/projects/435/badge.svg)](https://scan.coverity.com/projects/435) | [![Coverity Scan Build Status](https://scan.coverity.com/projects/4656/badge.svg)](https://scan.coverity.com/projects/4656)

## Introduction

TrinityCore is a *MMORPG* Framework based mostly in C++.

It is derived from *MaNGOS*, the *Massive Network Game Object Server*, and is
based on the code of that project with extensive changes over time to optimize,
improve and cleanup the codebase at the same time as improving the in-game
mechanics and functionality.

It is completely open source; community involvement is highly encouraged.

If you wish to contribute ideas or code, please visit our site linked below or
make pull requests to our [Github repository](https://github.com/TrinityCore/TrinityCore/pulls).

For further information on the TrinityCore project, please visit our project
website at [TrinityCore.org](https://www.trinitycore.org).

## Requirements


Software requirements are available in the [wiki](https://trinitycore.info/en/install/requirements) for
Windows, Linux and macOS.


## Install

Detailed installation guides are available in the [wiki](https://trinitycore.info/en/home) for
Windows, Linux and macOS.


## Reporting issues

Issues can be reported via the [Github issue tracker](https://github.com/TrinityCore/TrinityCore/labels/Branch-master).

Please take the time to review existing issues before submitting your own to
prevent duplicates.

In addition, thoroughly read through the [issue tracker guide](https://community.trinitycore.org/topic/37-the-trinitycore-issuetracker-and-you/) to ensure
your report contains the required information. Incorrect or poorly formed
reports are wasteful and are subject to deletion.


## Submitting fixes

C++ fixes are submitted as pull requests via Github. For more information on how to
properly submit a pull request, read the [how-to: maintain a remote fork](https://community.trinitycore.org/topic/9002-howto-maintain-a-remote-fork-for-pull-requests-tortoisegit/).
For SQL only fixes, open a ticket; if a bug report exists for the bug, post on an existing ticket.


## Copyright

License: GPL 2.0

Read file [COPYING](COPYING).


## Authors &amp; Contributors

Read file [AUTHORS](AUTHORS).


## Links

* [Website](https://www.trinitycore.org)
* [Wiki](https://www.trinitycore.info)
* [Forums](https://community.trinitycore.org)
* [Discord](https://discord.trinitycore.org/)
