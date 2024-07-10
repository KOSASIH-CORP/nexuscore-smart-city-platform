import kubernetes

class NFVManagementOrchestrationKubernetes:
    def __init__(selfself, kube_config_path):
        self.kube_config_path = kube_config_path
        self.api_client = kubernetes.client.ApiClient()
        self.api_client.load_kube_config(config_file=self.kube_config_path)
        self.v1 = kubernetes.client.CoreV1Api(self.api_client)

    def create_vnf(self, vnf_name, vnf_image):
        deployment = kubernetes.client.V1Deployment(
            api, kube_config_path):
        self.kube_config_path = kube_config_path
        self.api_client = kubernetes.client.ApiClient()
        self.api_client.load_kube_config(config_file=self.kube_config_path)
        self.v1 = kubernetes.client.CoreV1Api(self.api_client)

    def create_vnf(self, vnf_name, vnf_image):
        deployment = kubernetes.client.V1Deployment(
            api_version='_version='apps/v1',
            kind='Deployment',
            metadata=kubernetes.client.V1ObjectMeta(name=vnf_name),
            spec=kubernetes.client.V1DeploymentSpec(
                replicas=1,
                selector=kubernetes.client.V1LabelSelector(
                    match_labels={'app': vnf_name}
                ),
                template=kubernetes.client.V1PodTemplateSpec(
                    metadata=kubernetes.client.V1ObjectMeta(labels={'app': vnf_name}),
                    spec=kubernetes.client.V1PodSpec(containers=[
                        kubernetes.client.V1Container(
                            name=vnf_name,
                            image=vnf_image,
                            ports=[
                                kubernetes.client.V1ContainerPort(container_port=8080)
                            ]
                        )
                    ])
                )apps/v1',
            kind='Deployment',
            metadata=kubernetes.client.V1ObjectMeta(name=vnf_name),
            spec=kubernetes.client.V1DeploymentSpec(
                replicas=1,
                selector=kubernetes.client.V1LabelSelector(
                    match_labels={'app': vnf_name}
                ),
                template=kubernetes.client.V1PodTemplateSpec(
                    metadata=kubernetes.client.V1ObjectMeta(labels={'app': vnf_name}),
                    spec=kubernetes.client.V1PodSpec(containers=[
                        kubernetes.client.V1Container(
                            name=vnf_name,
                            image=vnf_image,
                            ports=[
                                kubernetes.client.V1ContainerPort(container_port=8080)
                            ]
                        )
                    ])
                )
            )
        )
        response = self.v1.create_namesp
            )
        )
        response = self.v1.create_namespaced_deployment(namespace='default', body=deployment)
        return response

    def delete_vnf(self, vnf_name):
        response = self.v1.delete_namespaced_deployment(name=vnf_name, namespace='default', body=kubernetes.client.V1DeleteOptions())
        return response

    def scale_vnf(self, vnf_name, scale_out):
        deployment = self.v1.read_namespaced_deployment(name=vnf_name, namespace='default')
        deployment.spec.replicas = scale_out
        response = self.v1.replace_namespaced_deployment(name=vnf_name, namespace='default', body=deployment)
        return response
