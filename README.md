Experitest - Java8 ansible role
=========

[![Build Status](https://travis-ci.org/ExperitestOfficial/ansible-role-java8.svg?branch=master)](https://travis-ci.org/ExperitestOfficial/ansible-role-java8)

This role will install \ uninstall Java8 (or alternatives) in all platforms

Requirements
------------

Supports on Windows, Mac and Linux os hosts only.

Role Variables
--------------

| Name | Description | Type | Default | Required |
|------|-------------|:----:|:-----:|:-----:|
| state | should the application be present or absent | present, absent | present | no |
| java_version | java jre version to install | string | 1.8.0_181 | no |
| java_installation_folder | the folder in which the applcation will be installed | string | for mac: /Applications/Experitest/jre <br> for windows: C:\\Experitest\\jre <br> for linux: /opt/Experitest/jre | no |

Example Playbook
----------------

#### [see working example](/example)
