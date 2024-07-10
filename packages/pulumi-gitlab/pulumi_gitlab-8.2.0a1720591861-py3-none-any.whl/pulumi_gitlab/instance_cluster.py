# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['InstanceClusterArgs', 'InstanceCluster']

@pulumi.input_type
class InstanceClusterArgs:
    def __init__(__self__, *,
                 kubernetes_api_url: pulumi.Input[str],
                 kubernetes_token: pulumi.Input[str],
                 domain: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 environment_scope: Optional[pulumi.Input[str]] = None,
                 kubernetes_authorization_type: Optional[pulumi.Input[str]] = None,
                 kubernetes_ca_cert: Optional[pulumi.Input[str]] = None,
                 kubernetes_namespace: Optional[pulumi.Input[str]] = None,
                 managed: Optional[pulumi.Input[bool]] = None,
                 management_project_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a InstanceCluster resource.
        :param pulumi.Input[str] kubernetes_api_url: The URL to access the Kubernetes API.
        :param pulumi.Input[str] kubernetes_token: The token to authenticate against Kubernetes. This attribute cannot be read.
        :param pulumi.Input[str] domain: The base domain of the cluster.
        :param pulumi.Input[bool] enabled: Determines if cluster is active or not. Defaults to `true`. This attribute cannot be read.
        :param pulumi.Input[str] environment_scope: The associated environment to the cluster. Defaults to `*`.
        :param pulumi.Input[str] kubernetes_authorization_type: The cluster authorization type. Valid values are `rbac`, `abac`, `unknown_authorization`. Defaults to `rbac`.
        :param pulumi.Input[str] kubernetes_ca_cert: TLS certificate (needed if API is using a self-signed TLS certificate).
        :param pulumi.Input[str] kubernetes_namespace: The unique namespace related to the instance.
        :param pulumi.Input[bool] managed: Determines if cluster is managed by gitlab or not. Defaults to `true`. This attribute cannot be read.
        :param pulumi.Input[str] management_project_id: The ID of the management project for the cluster.
        :param pulumi.Input[str] name: The name of cluster.
        """
        pulumi.set(__self__, "kubernetes_api_url", kubernetes_api_url)
        pulumi.set(__self__, "kubernetes_token", kubernetes_token)
        if domain is not None:
            pulumi.set(__self__, "domain", domain)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if environment_scope is not None:
            pulumi.set(__self__, "environment_scope", environment_scope)
        if kubernetes_authorization_type is not None:
            pulumi.set(__self__, "kubernetes_authorization_type", kubernetes_authorization_type)
        if kubernetes_ca_cert is not None:
            pulumi.set(__self__, "kubernetes_ca_cert", kubernetes_ca_cert)
        if kubernetes_namespace is not None:
            pulumi.set(__self__, "kubernetes_namespace", kubernetes_namespace)
        if managed is not None:
            pulumi.set(__self__, "managed", managed)
        if management_project_id is not None:
            pulumi.set(__self__, "management_project_id", management_project_id)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="kubernetesApiUrl")
    def kubernetes_api_url(self) -> pulumi.Input[str]:
        """
        The URL to access the Kubernetes API.
        """
        return pulumi.get(self, "kubernetes_api_url")

    @kubernetes_api_url.setter
    def kubernetes_api_url(self, value: pulumi.Input[str]):
        pulumi.set(self, "kubernetes_api_url", value)

    @property
    @pulumi.getter(name="kubernetesToken")
    def kubernetes_token(self) -> pulumi.Input[str]:
        """
        The token to authenticate against Kubernetes. This attribute cannot be read.
        """
        return pulumi.get(self, "kubernetes_token")

    @kubernetes_token.setter
    def kubernetes_token(self, value: pulumi.Input[str]):
        pulumi.set(self, "kubernetes_token", value)

    @property
    @pulumi.getter
    def domain(self) -> Optional[pulumi.Input[str]]:
        """
        The base domain of the cluster.
        """
        return pulumi.get(self, "domain")

    @domain.setter
    def domain(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "domain", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Determines if cluster is active or not. Defaults to `true`. This attribute cannot be read.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter(name="environmentScope")
    def environment_scope(self) -> Optional[pulumi.Input[str]]:
        """
        The associated environment to the cluster. Defaults to `*`.
        """
        return pulumi.get(self, "environment_scope")

    @environment_scope.setter
    def environment_scope(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "environment_scope", value)

    @property
    @pulumi.getter(name="kubernetesAuthorizationType")
    def kubernetes_authorization_type(self) -> Optional[pulumi.Input[str]]:
        """
        The cluster authorization type. Valid values are `rbac`, `abac`, `unknown_authorization`. Defaults to `rbac`.
        """
        return pulumi.get(self, "kubernetes_authorization_type")

    @kubernetes_authorization_type.setter
    def kubernetes_authorization_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kubernetes_authorization_type", value)

    @property
    @pulumi.getter(name="kubernetesCaCert")
    def kubernetes_ca_cert(self) -> Optional[pulumi.Input[str]]:
        """
        TLS certificate (needed if API is using a self-signed TLS certificate).
        """
        return pulumi.get(self, "kubernetes_ca_cert")

    @kubernetes_ca_cert.setter
    def kubernetes_ca_cert(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kubernetes_ca_cert", value)

    @property
    @pulumi.getter(name="kubernetesNamespace")
    def kubernetes_namespace(self) -> Optional[pulumi.Input[str]]:
        """
        The unique namespace related to the instance.
        """
        return pulumi.get(self, "kubernetes_namespace")

    @kubernetes_namespace.setter
    def kubernetes_namespace(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kubernetes_namespace", value)

    @property
    @pulumi.getter
    def managed(self) -> Optional[pulumi.Input[bool]]:
        """
        Determines if cluster is managed by gitlab or not. Defaults to `true`. This attribute cannot be read.
        """
        return pulumi.get(self, "managed")

    @managed.setter
    def managed(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "managed", value)

    @property
    @pulumi.getter(name="managementProjectId")
    def management_project_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the management project for the cluster.
        """
        return pulumi.get(self, "management_project_id")

    @management_project_id.setter
    def management_project_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "management_project_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of cluster.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _InstanceClusterState:
    def __init__(__self__, *,
                 cluster_type: Optional[pulumi.Input[str]] = None,
                 created_at: Optional[pulumi.Input[str]] = None,
                 domain: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 environment_scope: Optional[pulumi.Input[str]] = None,
                 kubernetes_api_url: Optional[pulumi.Input[str]] = None,
                 kubernetes_authorization_type: Optional[pulumi.Input[str]] = None,
                 kubernetes_ca_cert: Optional[pulumi.Input[str]] = None,
                 kubernetes_namespace: Optional[pulumi.Input[str]] = None,
                 kubernetes_token: Optional[pulumi.Input[str]] = None,
                 managed: Optional[pulumi.Input[bool]] = None,
                 management_project_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 platform_type: Optional[pulumi.Input[str]] = None,
                 provider_type: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering InstanceCluster resources.
        :param pulumi.Input[str] cluster_type: Cluster type.
        :param pulumi.Input[str] created_at: Create time.
        :param pulumi.Input[str] domain: The base domain of the cluster.
        :param pulumi.Input[bool] enabled: Determines if cluster is active or not. Defaults to `true`. This attribute cannot be read.
        :param pulumi.Input[str] environment_scope: The associated environment to the cluster. Defaults to `*`.
        :param pulumi.Input[str] kubernetes_api_url: The URL to access the Kubernetes API.
        :param pulumi.Input[str] kubernetes_authorization_type: The cluster authorization type. Valid values are `rbac`, `abac`, `unknown_authorization`. Defaults to `rbac`.
        :param pulumi.Input[str] kubernetes_ca_cert: TLS certificate (needed if API is using a self-signed TLS certificate).
        :param pulumi.Input[str] kubernetes_namespace: The unique namespace related to the instance.
        :param pulumi.Input[str] kubernetes_token: The token to authenticate against Kubernetes. This attribute cannot be read.
        :param pulumi.Input[bool] managed: Determines if cluster is managed by gitlab or not. Defaults to `true`. This attribute cannot be read.
        :param pulumi.Input[str] management_project_id: The ID of the management project for the cluster.
        :param pulumi.Input[str] name: The name of cluster.
        :param pulumi.Input[str] platform_type: Platform type.
        :param pulumi.Input[str] provider_type: Provider type.
        """
        if cluster_type is not None:
            pulumi.set(__self__, "cluster_type", cluster_type)
        if created_at is not None:
            pulumi.set(__self__, "created_at", created_at)
        if domain is not None:
            pulumi.set(__self__, "domain", domain)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if environment_scope is not None:
            pulumi.set(__self__, "environment_scope", environment_scope)
        if kubernetes_api_url is not None:
            pulumi.set(__self__, "kubernetes_api_url", kubernetes_api_url)
        if kubernetes_authorization_type is not None:
            pulumi.set(__self__, "kubernetes_authorization_type", kubernetes_authorization_type)
        if kubernetes_ca_cert is not None:
            pulumi.set(__self__, "kubernetes_ca_cert", kubernetes_ca_cert)
        if kubernetes_namespace is not None:
            pulumi.set(__self__, "kubernetes_namespace", kubernetes_namespace)
        if kubernetes_token is not None:
            pulumi.set(__self__, "kubernetes_token", kubernetes_token)
        if managed is not None:
            pulumi.set(__self__, "managed", managed)
        if management_project_id is not None:
            pulumi.set(__self__, "management_project_id", management_project_id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if platform_type is not None:
            pulumi.set(__self__, "platform_type", platform_type)
        if provider_type is not None:
            pulumi.set(__self__, "provider_type", provider_type)

    @property
    @pulumi.getter(name="clusterType")
    def cluster_type(self) -> Optional[pulumi.Input[str]]:
        """
        Cluster type.
        """
        return pulumi.get(self, "cluster_type")

    @cluster_type.setter
    def cluster_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cluster_type", value)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[pulumi.Input[str]]:
        """
        Create time.
        """
        return pulumi.get(self, "created_at")

    @created_at.setter
    def created_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created_at", value)

    @property
    @pulumi.getter
    def domain(self) -> Optional[pulumi.Input[str]]:
        """
        The base domain of the cluster.
        """
        return pulumi.get(self, "domain")

    @domain.setter
    def domain(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "domain", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Determines if cluster is active or not. Defaults to `true`. This attribute cannot be read.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter(name="environmentScope")
    def environment_scope(self) -> Optional[pulumi.Input[str]]:
        """
        The associated environment to the cluster. Defaults to `*`.
        """
        return pulumi.get(self, "environment_scope")

    @environment_scope.setter
    def environment_scope(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "environment_scope", value)

    @property
    @pulumi.getter(name="kubernetesApiUrl")
    def kubernetes_api_url(self) -> Optional[pulumi.Input[str]]:
        """
        The URL to access the Kubernetes API.
        """
        return pulumi.get(self, "kubernetes_api_url")

    @kubernetes_api_url.setter
    def kubernetes_api_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kubernetes_api_url", value)

    @property
    @pulumi.getter(name="kubernetesAuthorizationType")
    def kubernetes_authorization_type(self) -> Optional[pulumi.Input[str]]:
        """
        The cluster authorization type. Valid values are `rbac`, `abac`, `unknown_authorization`. Defaults to `rbac`.
        """
        return pulumi.get(self, "kubernetes_authorization_type")

    @kubernetes_authorization_type.setter
    def kubernetes_authorization_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kubernetes_authorization_type", value)

    @property
    @pulumi.getter(name="kubernetesCaCert")
    def kubernetes_ca_cert(self) -> Optional[pulumi.Input[str]]:
        """
        TLS certificate (needed if API is using a self-signed TLS certificate).
        """
        return pulumi.get(self, "kubernetes_ca_cert")

    @kubernetes_ca_cert.setter
    def kubernetes_ca_cert(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kubernetes_ca_cert", value)

    @property
    @pulumi.getter(name="kubernetesNamespace")
    def kubernetes_namespace(self) -> Optional[pulumi.Input[str]]:
        """
        The unique namespace related to the instance.
        """
        return pulumi.get(self, "kubernetes_namespace")

    @kubernetes_namespace.setter
    def kubernetes_namespace(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kubernetes_namespace", value)

    @property
    @pulumi.getter(name="kubernetesToken")
    def kubernetes_token(self) -> Optional[pulumi.Input[str]]:
        """
        The token to authenticate against Kubernetes. This attribute cannot be read.
        """
        return pulumi.get(self, "kubernetes_token")

    @kubernetes_token.setter
    def kubernetes_token(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kubernetes_token", value)

    @property
    @pulumi.getter
    def managed(self) -> Optional[pulumi.Input[bool]]:
        """
        Determines if cluster is managed by gitlab or not. Defaults to `true`. This attribute cannot be read.
        """
        return pulumi.get(self, "managed")

    @managed.setter
    def managed(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "managed", value)

    @property
    @pulumi.getter(name="managementProjectId")
    def management_project_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the management project for the cluster.
        """
        return pulumi.get(self, "management_project_id")

    @management_project_id.setter
    def management_project_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "management_project_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of cluster.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="platformType")
    def platform_type(self) -> Optional[pulumi.Input[str]]:
        """
        Platform type.
        """
        return pulumi.get(self, "platform_type")

    @platform_type.setter
    def platform_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "platform_type", value)

    @property
    @pulumi.getter(name="providerType")
    def provider_type(self) -> Optional[pulumi.Input[str]]:
        """
        Provider type.
        """
        return pulumi.get(self, "provider_type")

    @provider_type.setter
    def provider_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "provider_type", value)


class InstanceCluster(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 domain: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 environment_scope: Optional[pulumi.Input[str]] = None,
                 kubernetes_api_url: Optional[pulumi.Input[str]] = None,
                 kubernetes_authorization_type: Optional[pulumi.Input[str]] = None,
                 kubernetes_ca_cert: Optional[pulumi.Input[str]] = None,
                 kubernetes_namespace: Optional[pulumi.Input[str]] = None,
                 kubernetes_token: Optional[pulumi.Input[str]] = None,
                 managed: Optional[pulumi.Input[bool]] = None,
                 management_project_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The `InstanceCluster` resource allows to manage the lifecycle of an instance cluster.

        > This is deprecated GitLab feature since 14.5

        **Upstream API**: [GitLab REST API docs](https://docs.gitlab.com/ee/api/instance_clusters.html)

        ## Example Usage

        ```python
        import pulumi
        import pulumi_gitlab as gitlab

        bar = gitlab.InstanceCluster("bar",
            name="bar-cluster",
            domain="example.com",
            enabled=True,
            kubernetes_api_url="https://124.124.124",
            kubernetes_token="some-token",
            kubernetes_ca_cert="some-cert",
            kubernetes_namespace="namespace",
            kubernetes_authorization_type="rbac",
            environment_scope="*",
            management_project_id="123456")
        ```

        ## Import

        GitLab instance clusters can be imported using a `clusterid`, e.g.

        ```sh
        $ pulumi import gitlab:index/instanceCluster:InstanceCluster bar 123
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] domain: The base domain of the cluster.
        :param pulumi.Input[bool] enabled: Determines if cluster is active or not. Defaults to `true`. This attribute cannot be read.
        :param pulumi.Input[str] environment_scope: The associated environment to the cluster. Defaults to `*`.
        :param pulumi.Input[str] kubernetes_api_url: The URL to access the Kubernetes API.
        :param pulumi.Input[str] kubernetes_authorization_type: The cluster authorization type. Valid values are `rbac`, `abac`, `unknown_authorization`. Defaults to `rbac`.
        :param pulumi.Input[str] kubernetes_ca_cert: TLS certificate (needed if API is using a self-signed TLS certificate).
        :param pulumi.Input[str] kubernetes_namespace: The unique namespace related to the instance.
        :param pulumi.Input[str] kubernetes_token: The token to authenticate against Kubernetes. This attribute cannot be read.
        :param pulumi.Input[bool] managed: Determines if cluster is managed by gitlab or not. Defaults to `true`. This attribute cannot be read.
        :param pulumi.Input[str] management_project_id: The ID of the management project for the cluster.
        :param pulumi.Input[str] name: The name of cluster.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: InstanceClusterArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The `InstanceCluster` resource allows to manage the lifecycle of an instance cluster.

        > This is deprecated GitLab feature since 14.5

        **Upstream API**: [GitLab REST API docs](https://docs.gitlab.com/ee/api/instance_clusters.html)

        ## Example Usage

        ```python
        import pulumi
        import pulumi_gitlab as gitlab

        bar = gitlab.InstanceCluster("bar",
            name="bar-cluster",
            domain="example.com",
            enabled=True,
            kubernetes_api_url="https://124.124.124",
            kubernetes_token="some-token",
            kubernetes_ca_cert="some-cert",
            kubernetes_namespace="namespace",
            kubernetes_authorization_type="rbac",
            environment_scope="*",
            management_project_id="123456")
        ```

        ## Import

        GitLab instance clusters can be imported using a `clusterid`, e.g.

        ```sh
        $ pulumi import gitlab:index/instanceCluster:InstanceCluster bar 123
        ```

        :param str resource_name: The name of the resource.
        :param InstanceClusterArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(InstanceClusterArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 domain: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 environment_scope: Optional[pulumi.Input[str]] = None,
                 kubernetes_api_url: Optional[pulumi.Input[str]] = None,
                 kubernetes_authorization_type: Optional[pulumi.Input[str]] = None,
                 kubernetes_ca_cert: Optional[pulumi.Input[str]] = None,
                 kubernetes_namespace: Optional[pulumi.Input[str]] = None,
                 kubernetes_token: Optional[pulumi.Input[str]] = None,
                 managed: Optional[pulumi.Input[bool]] = None,
                 management_project_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = InstanceClusterArgs.__new__(InstanceClusterArgs)

            __props__.__dict__["domain"] = domain
            __props__.__dict__["enabled"] = enabled
            __props__.__dict__["environment_scope"] = environment_scope
            if kubernetes_api_url is None and not opts.urn:
                raise TypeError("Missing required property 'kubernetes_api_url'")
            __props__.__dict__["kubernetes_api_url"] = kubernetes_api_url
            __props__.__dict__["kubernetes_authorization_type"] = kubernetes_authorization_type
            __props__.__dict__["kubernetes_ca_cert"] = kubernetes_ca_cert
            __props__.__dict__["kubernetes_namespace"] = kubernetes_namespace
            if kubernetes_token is None and not opts.urn:
                raise TypeError("Missing required property 'kubernetes_token'")
            __props__.__dict__["kubernetes_token"] = None if kubernetes_token is None else pulumi.Output.secret(kubernetes_token)
            __props__.__dict__["managed"] = managed
            __props__.__dict__["management_project_id"] = management_project_id
            __props__.__dict__["name"] = name
            __props__.__dict__["cluster_type"] = None
            __props__.__dict__["created_at"] = None
            __props__.__dict__["platform_type"] = None
            __props__.__dict__["provider_type"] = None
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["kubernetesToken"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(InstanceCluster, __self__).__init__(
            'gitlab:index/instanceCluster:InstanceCluster',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            cluster_type: Optional[pulumi.Input[str]] = None,
            created_at: Optional[pulumi.Input[str]] = None,
            domain: Optional[pulumi.Input[str]] = None,
            enabled: Optional[pulumi.Input[bool]] = None,
            environment_scope: Optional[pulumi.Input[str]] = None,
            kubernetes_api_url: Optional[pulumi.Input[str]] = None,
            kubernetes_authorization_type: Optional[pulumi.Input[str]] = None,
            kubernetes_ca_cert: Optional[pulumi.Input[str]] = None,
            kubernetes_namespace: Optional[pulumi.Input[str]] = None,
            kubernetes_token: Optional[pulumi.Input[str]] = None,
            managed: Optional[pulumi.Input[bool]] = None,
            management_project_id: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            platform_type: Optional[pulumi.Input[str]] = None,
            provider_type: Optional[pulumi.Input[str]] = None) -> 'InstanceCluster':
        """
        Get an existing InstanceCluster resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cluster_type: Cluster type.
        :param pulumi.Input[str] created_at: Create time.
        :param pulumi.Input[str] domain: The base domain of the cluster.
        :param pulumi.Input[bool] enabled: Determines if cluster is active or not. Defaults to `true`. This attribute cannot be read.
        :param pulumi.Input[str] environment_scope: The associated environment to the cluster. Defaults to `*`.
        :param pulumi.Input[str] kubernetes_api_url: The URL to access the Kubernetes API.
        :param pulumi.Input[str] kubernetes_authorization_type: The cluster authorization type. Valid values are `rbac`, `abac`, `unknown_authorization`. Defaults to `rbac`.
        :param pulumi.Input[str] kubernetes_ca_cert: TLS certificate (needed if API is using a self-signed TLS certificate).
        :param pulumi.Input[str] kubernetes_namespace: The unique namespace related to the instance.
        :param pulumi.Input[str] kubernetes_token: The token to authenticate against Kubernetes. This attribute cannot be read.
        :param pulumi.Input[bool] managed: Determines if cluster is managed by gitlab or not. Defaults to `true`. This attribute cannot be read.
        :param pulumi.Input[str] management_project_id: The ID of the management project for the cluster.
        :param pulumi.Input[str] name: The name of cluster.
        :param pulumi.Input[str] platform_type: Platform type.
        :param pulumi.Input[str] provider_type: Provider type.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _InstanceClusterState.__new__(_InstanceClusterState)

        __props__.__dict__["cluster_type"] = cluster_type
        __props__.__dict__["created_at"] = created_at
        __props__.__dict__["domain"] = domain
        __props__.__dict__["enabled"] = enabled
        __props__.__dict__["environment_scope"] = environment_scope
        __props__.__dict__["kubernetes_api_url"] = kubernetes_api_url
        __props__.__dict__["kubernetes_authorization_type"] = kubernetes_authorization_type
        __props__.__dict__["kubernetes_ca_cert"] = kubernetes_ca_cert
        __props__.__dict__["kubernetes_namespace"] = kubernetes_namespace
        __props__.__dict__["kubernetes_token"] = kubernetes_token
        __props__.__dict__["managed"] = managed
        __props__.__dict__["management_project_id"] = management_project_id
        __props__.__dict__["name"] = name
        __props__.__dict__["platform_type"] = platform_type
        __props__.__dict__["provider_type"] = provider_type
        return InstanceCluster(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="clusterType")
    def cluster_type(self) -> pulumi.Output[str]:
        """
        Cluster type.
        """
        return pulumi.get(self, "cluster_type")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[str]:
        """
        Create time.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter
    def domain(self) -> pulumi.Output[Optional[str]]:
        """
        The base domain of the cluster.
        """
        return pulumi.get(self, "domain")

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Determines if cluster is active or not. Defaults to `true`. This attribute cannot be read.
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter(name="environmentScope")
    def environment_scope(self) -> pulumi.Output[Optional[str]]:
        """
        The associated environment to the cluster. Defaults to `*`.
        """
        return pulumi.get(self, "environment_scope")

    @property
    @pulumi.getter(name="kubernetesApiUrl")
    def kubernetes_api_url(self) -> pulumi.Output[str]:
        """
        The URL to access the Kubernetes API.
        """
        return pulumi.get(self, "kubernetes_api_url")

    @property
    @pulumi.getter(name="kubernetesAuthorizationType")
    def kubernetes_authorization_type(self) -> pulumi.Output[Optional[str]]:
        """
        The cluster authorization type. Valid values are `rbac`, `abac`, `unknown_authorization`. Defaults to `rbac`.
        """
        return pulumi.get(self, "kubernetes_authorization_type")

    @property
    @pulumi.getter(name="kubernetesCaCert")
    def kubernetes_ca_cert(self) -> pulumi.Output[Optional[str]]:
        """
        TLS certificate (needed if API is using a self-signed TLS certificate).
        """
        return pulumi.get(self, "kubernetes_ca_cert")

    @property
    @pulumi.getter(name="kubernetesNamespace")
    def kubernetes_namespace(self) -> pulumi.Output[Optional[str]]:
        """
        The unique namespace related to the instance.
        """
        return pulumi.get(self, "kubernetes_namespace")

    @property
    @pulumi.getter(name="kubernetesToken")
    def kubernetes_token(self) -> pulumi.Output[str]:
        """
        The token to authenticate against Kubernetes. This attribute cannot be read.
        """
        return pulumi.get(self, "kubernetes_token")

    @property
    @pulumi.getter
    def managed(self) -> pulumi.Output[Optional[bool]]:
        """
        Determines if cluster is managed by gitlab or not. Defaults to `true`. This attribute cannot be read.
        """
        return pulumi.get(self, "managed")

    @property
    @pulumi.getter(name="managementProjectId")
    def management_project_id(self) -> pulumi.Output[Optional[str]]:
        """
        The ID of the management project for the cluster.
        """
        return pulumi.get(self, "management_project_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of cluster.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="platformType")
    def platform_type(self) -> pulumi.Output[str]:
        """
        Platform type.
        """
        return pulumi.get(self, "platform_type")

    @property
    @pulumi.getter(name="providerType")
    def provider_type(self) -> pulumi.Output[str]:
        """
        Provider type.
        """
        return pulumi.get(self, "provider_type")

