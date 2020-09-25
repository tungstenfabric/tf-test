from jinja2 import Environment, FileSystemLoader
import json

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
print(policies)

env = Environment(loader=FileSystemLoader("./template"))
template = env.get_template("policy.yaml.j2")
print(template.render(policies=policies))
with open('policy.yaml', 'w') as f:
  f.write(template.render(policies=policies))

# cd /root/nuthanc-tf-test/tcutils/kubernetes/auth/play
# python jinjaTemplate.py
# Apply policy with 
# juju config kubernetes-master keystone-policy="$(cat /root/nuthanc-tf-test/tcutils/kubernetes/auth/play/policy.yaml)"

