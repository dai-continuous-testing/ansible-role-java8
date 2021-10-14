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
| java_version | java jre version to install | string | 8u292-b10 | no |
| installation_root_folder | the root folder in which the java application will be installed under jre folder | string | for mac: /Applications/Experitest <br> for windows: C:\\Experitest <br> for linux: /opt/Experitest | no |
| update_java_path | add java bin path to system path variable | boolean | False | no |
| custom_download_url | custom url to download the installation from (zip format) | string |  | no |
| custom_download_username | username to download from custom url on windows | string |  | no |
| custom_download_password | password to download from custom url on windows | string |  | no |

Example Playbook
----------------

#### [see working example](/example)
