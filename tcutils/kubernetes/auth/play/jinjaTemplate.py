from jinja2 import Environment, FileSystemLoader
import json
import os

policies = None
if policies is None:
    policies = [
        {
            "resource": {
                "verbs": ["*"],
                "resources": ["*"],
                "version": "*",
                "namespace": "*"
            },
            "match": [
                {
                    "type": "role",
                    "values": ["*"]
                },
                {
                    "type": "project",
                    "values": ["admin"]
                }
            ]
        }
    ]

policies = json.dumps(policies)
# print(policies)
THIS_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(THIS_DIR, 'template')
print(THIS_DIR)
env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
filename = os.path.join(THIS_DIR, 'policy.yaml')
template = env.get_template("policy.yaml.j2")
# print(template.render(policies=policies))
with open(filename, 'w') as f:
    f.write(template.render(policies=policies))

# cd /root/nuthanc-tf-test/tcutils/kubernetes/auth/play
# python jinjaTemplate.py
# Apply policy with
# juju config kubernetes-master keystone-policy="$(cat /root/nuthanc-tf-test/tcutils/kubernetes/auth/play/policy.yaml)"
