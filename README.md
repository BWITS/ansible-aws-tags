### Ansible module to get aws ec2 instances tags

The output from this module is a bunch of Ansible facts

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

###EXAMPLES
```
   # save aws_tags.py to library folder

   # usage
   $ cat roles/common/tasks/main.yml
   
   - action: aws_tags instance_id=i-ac13f01d region=us-west-2
```
