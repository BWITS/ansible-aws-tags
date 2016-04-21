#!/usr/bin/python
# Ansible module to get aws ec2 instances tags
#
# The output from this module is a bunch of Ansible facts

DOCUMENTATION = '''
---
module: aws_tags
short_description: Return ec2 instance tags
description:
   - Given an instance id and its region, return its tags, such as Name, etc.
version_added: "1.0"
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
action: aws_tags instance_id=i-ac13f01d region=us-west-2
'''

from boto import ec2

def main():

  module = AnsibleModule(
      argument_spec = dict(
          instance_id = dict(required=True),
          region = dict(required=True),
      )
  )

  conn = ec2.connect_to_region(module.params['region'])
  instance = conn.get_only_instances(module.params['instance_id'])[0]

  facts = {}

  for key in instance.tags:
    facts['ansible_ec2_tag_' + key] = instance.tags[key]

  module.exit_json(changed=False, ansible_facts=facts)

from ansible.module_utils.basic import *
if __name__ == '__main__':
    main()
