#!/usr/bin/python
#
# This is a free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This Ansible library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this library.  If not, see <http://www.gnu.org/licenses/>.
#
# Ansible module to get aws ec2 instances tags
#
# The output from this module is a bunch of Ansible facts, README at:
# https://github.com/BWITS/ansible-aws-tags/blob/master/README.md

DOCUMENTATION = '''
---
module: aws_tags3
short_description: Return ec2 instance tags
description:
   - Given an instance id and its region, return its tags, such as Name, etc.
version_added: "2.1"
author: Bill Wang
requirements:
  - none
options:
  instance_id:
    required: true
    description:
      - ec2 instance id
  region:
    required: true
    description:
      - aws region
'''

EXAMPLES = '''
action: aws_tags3 instance_id=i-ac13f01d region=us-west-2
'''

RETURN = '''
  ansible_ec2_tag_KEYS:
     description: ec2 instance tags key and value.
''' 

import boto3

def main():

  module = AnsibleModule(
      argument_spec = dict(
          instance_id = dict(required=True),
          region = dict(required=True),
      )
  )

  ec2 = boto3.resource('ec2', module.params['region'])

  facts = {}

  for instance in ec2.instances.all():
    if instance.id == module.params['instance_id']:
      for tag in instance.tags:
        facts['ansible_ec2_tag_' + tag['Key']] = tag['Value']

  module.exit_json(changed=False, ansible_facts=facts)

from ansible.module_utils.basic import *
if __name__ == '__main__':
    main()
