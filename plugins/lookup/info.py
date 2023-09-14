
# flake8: noqa: E402

# python 3 headers, required if submitting to Ansible
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = """
  name: info
  author: Markus Falb (@mafalb) <markus.falb@mafalb.at>
  version_added: "0.1"  # for collections, use the collection version, not the Ansible version
  short_description: return a list of OSes, images or other information.
  description:
      - This lookup get a list of information about containerimages from imagetree.yml.
  options:
    action:
      description: kind of information to fetch
      required: True
    os:
      description: the Operating System
    image:
      description: the image
    file:
      description: the yaml file to look for information
      required: False
"""
from ansible.errors import AnsibleError, AnsibleParserError
from ansible.plugins.lookup import LookupBase
from ansible.utils.display import Display

from ..module_utils.containerimages.schema import Containerimages
from os.path import dirname

display = Display()


class LookupModule(LookupBase):

    def run(self, terms=None, variables=None, **kwargs):

        valid_actions = [
            "get_baseimage",
            "get_parent",
            "get_parentimage",
            "list_children",
            "list_images",
            "list_oses",
        ]

        # First of all populate options,
        # this will already take into account env vars and ini config
        self.set_options(var_options=variables, direct=kwargs)

        # lookups in general are expected to both take a list as input and output a list
        # this is done so they work with the looping construct 'with_'.
        ret = []

        if self.get_option('action') not in valid_actions:
            raise AnsibleError("invalid action '%s'." % self.get_option('action'))
        try:
            images = Containerimages(dirname(__file__) + '/../../imagetree.yml')
            # images = Containerimages(dirname(__file__) + '/../../imagetree.yml')

            if self.get_option('action') == 'list_oses':
                ret.append(images.list_os())
            elif self.get_option('action') == 'list_images':
                ret.append(images.list_images(self.get_option('os')))
            elif self.get_option('action') == 'list_children':
                ret.append(images.get_children(self.get_option('os'), self.get_option('image')))
            elif self.get_option('action') == 'get_parent':
                parent = images.get_parent(self.get_option('os'), self.get_option('image'))
                if parent:
                    ret.append(parent)
            elif self.get_option('action') == 'get_parentimage':
                parentimage = images.get_parentimage(self.get_option('os'), self.get_option('image'))
                if parentimage:
                    ret.append(parentimage)
            elif self.get_option('action') == 'get_baseimage':
                baseimage = images.get_attribute(self.get_option('os'), self.get_option('image'), 'base_image')
                if baseimage:
                    ret.append(baseimage)
                else:
                    ret.append(None)

        except AnsibleParserError:
            raise AnsibleError("error with retrieving data")

        return ret
