#!/usr/bin/python


class FilterModule(object):
    def filters(self):
        return {
            'os_family_to_os_type': self.os_family_to_os_type,
            'ansible_arch_to_java_arch': self.ansible_arch_to_java_arch
        }

    def os_family_to_os_type(self, os_family):

        os_family_to_os_type_dict = dict({
            "redhat": "linux",
            "debian": "linux",
            "suse": "linux",
            "darwin": "darwin",
            "windows": "windows"
        })                   

        return os_family_to_os_type_dict[os_family.lower()]

    def ansible_arch_to_java_arch(self, ansible_arch):
        """
        Convert Ansible architecture names to Java download architecture names
        """
        arch_mapping = {
            # Intel/AMD 64-bit
            "x86_64": "x64",
            "amd64": "x64",
            # ARM 64-bit (Apple Silicon, etc.)
            "arm64": "aarch64", 
            "aarch64": "aarch64",
            # Intel 32-bit (legacy)
            "i386": "x32",
            "i686": "x32"
        }
        
        return arch_mapping.get(ansible_arch.lower(), ansible_arch)
