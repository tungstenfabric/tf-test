### Canonical JuJu Contrail CNI (K8S) Deployment Using Existing Keystone (CEM-13066)

* https://contrail-jws.atlassian.net/browse/CEM-13066
* Using keystone-auth to create k8s objects for Openstack Users

### To run tests
* Install kubectl and client-keystone-auth in juju server
* Configure keystone context to kubectl
* Clone tf-test to juju server
* Run test container with the below volumes
```sh
docker run --name nuthan_test --entrypoint /bin/bash --env-file ./env_file -v /root/contrail_test_input.yaml:/nuthanc-tf-test/contrail_test_input.yaml -v /root/nuthanc-tf-test:/root/nuthanc-tf-test -v /root/.ssh:/root/.ssh --network=host -it bng-artifactory.juniper.net/contrail-nightly/contrail-test-test:2011.102
```