### Ansible module to get aws ec2 instances tags

The output from this module is a bunch of Ansible facts

Tested in Ansible 2.0.1+

```
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
```

###Examples
```
   # save aws_tags.py to library folder

   # usage
   $ cat roles/common/tasks/main.yml
   
   - action: aws_tags instance_id=i-ac13f01d region=us-west-2
```

###Best practice

Suppose when you created the instances, assign IAM role with `AmazonEC2ReadOnlyAccess` policy. 

`aws_tags` module works perfect with ansible `ec2_facts` module

```
- name: get ec2 facts
  action: ec2_facts

- name: get instance tags
  action: aws_tags instance_id={{ ansible_ec2_instance_id }} region={{ ansible_ec2_placement_region }}
  
- name: export aws_tags
  command: echo {{ Name }}
```
