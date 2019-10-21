Experitest - Java8 ansible role
=========

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
| update_java_path | add java bin path to system path variable | boolean | False | no |

Example Playbook
----------------

#### [see working example](/example)
