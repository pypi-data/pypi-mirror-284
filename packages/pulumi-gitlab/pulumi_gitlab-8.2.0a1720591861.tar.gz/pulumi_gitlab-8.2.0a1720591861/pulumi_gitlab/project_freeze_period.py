# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['ProjectFreezePeriodArgs', 'ProjectFreezePeriod']

@pulumi.input_type
class ProjectFreezePeriodArgs:
    def __init__(__self__, *,
                 freeze_end: pulumi.Input[str],
                 freeze_start: pulumi.Input[str],
                 project: pulumi.Input[str],
                 cron_timezone: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ProjectFreezePeriod resource.
        :param pulumi.Input[str] freeze_end: End of the Freeze Period in cron format (e.g. `0 2 * * *`).
        :param pulumi.Input[str] freeze_start: Start of the Freeze Period in cron format (e.g. `0 1 * * *`).
        :param pulumi.Input[str] project: The ID or URL-encoded path of the project to add the schedule to.
        :param pulumi.Input[str] cron_timezone: The timezone.
        """
        pulumi.set(__self__, "freeze_end", freeze_end)
        pulumi.set(__self__, "freeze_start", freeze_start)
        pulumi.set(__self__, "project", project)
        if cron_timezone is not None:
            pulumi.set(__self__, "cron_timezone", cron_timezone)

    @property
    @pulumi.getter(name="freezeEnd")
    def freeze_end(self) -> pulumi.Input[str]:
        """
        End of the Freeze Period in cron format (e.g. `0 2 * * *`).
        """
        return pulumi.get(self, "freeze_end")

    @freeze_end.setter
    def freeze_end(self, value: pulumi.Input[str]):
        pulumi.set(self, "freeze_end", value)

    @property
    @pulumi.getter(name="freezeStart")
    def freeze_start(self) -> pulumi.Input[str]:
        """
        Start of the Freeze Period in cron format (e.g. `0 1 * * *`).
        """
        return pulumi.get(self, "freeze_start")

    @freeze_start.setter
    def freeze_start(self, value: pulumi.Input[str]):
        pulumi.set(self, "freeze_start", value)

    @property
    @pulumi.getter
    def project(self) -> pulumi.Input[str]:
        """
        The ID or URL-encoded path of the project to add the schedule to.
        """
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: pulumi.Input[str]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter(name="cronTimezone")
    def cron_timezone(self) -> Optional[pulumi.Input[str]]:
        """
        The timezone.
        """
        return pulumi.get(self, "cron_timezone")

    @cron_timezone.setter
    def cron_timezone(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cron_timezone", value)


@pulumi.input_type
class _ProjectFreezePeriodState:
    def __init__(__self__, *,
                 cron_timezone: Optional[pulumi.Input[str]] = None,
                 freeze_end: Optional[pulumi.Input[str]] = None,
                 freeze_start: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ProjectFreezePeriod resources.
        :param pulumi.Input[str] cron_timezone: The timezone.
        :param pulumi.Input[str] freeze_end: End of the Freeze Period in cron format (e.g. `0 2 * * *`).
        :param pulumi.Input[str] freeze_start: Start of the Freeze Period in cron format (e.g. `0 1 * * *`).
        :param pulumi.Input[str] project: The ID or URL-encoded path of the project to add the schedule to.
        """
        if cron_timezone is not None:
            pulumi.set(__self__, "cron_timezone", cron_timezone)
        if freeze_end is not None:
            pulumi.set(__self__, "freeze_end", freeze_end)
        if freeze_start is not None:
            pulumi.set(__self__, "freeze_start", freeze_start)
        if project is not None:
            pulumi.set(__self__, "project", project)

    @property
    @pulumi.getter(name="cronTimezone")
    def cron_timezone(self) -> Optional[pulumi.Input[str]]:
        """
        The timezone.
        """
        return pulumi.get(self, "cron_timezone")

    @cron_timezone.setter
    def cron_timezone(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cron_timezone", value)

    @property
    @pulumi.getter(name="freezeEnd")
    def freeze_end(self) -> Optional[pulumi.Input[str]]:
        """
        End of the Freeze Period in cron format (e.g. `0 2 * * *`).
        """
        return pulumi.get(self, "freeze_end")

    @freeze_end.setter
    def freeze_end(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "freeze_end", value)

    @property
    @pulumi.getter(name="freezeStart")
    def freeze_start(self) -> Optional[pulumi.Input[str]]:
        """
        Start of the Freeze Period in cron format (e.g. `0 1 * * *`).
        """
        return pulumi.get(self, "freeze_start")

    @freeze_start.setter
    def freeze_start(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "freeze_start", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        """
        The ID or URL-encoded path of the project to add the schedule to.
        """
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)


class ProjectFreezePeriod(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cron_timezone: Optional[pulumi.Input[str]] = None,
                 freeze_end: Optional[pulumi.Input[str]] = None,
                 freeze_start: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The `ProjectFreezePeriod` resource allows to manage the lifecycle of a freeze period for a project.

        **Upstream API**: [GitLab REST API docs](https://docs.gitlab.com/ee/api/freeze_periods.html)

        ## Example Usage

        ```python
        import pulumi
        import pulumi_gitlab as gitlab

        schedule = gitlab.ProjectFreezePeriod("schedule",
            project=foo["id"],
            freeze_start="0 23 * * 5",
            freeze_end="0 7 * * 1",
            cron_timezone="UTC")
        ```

        ## Import

        GitLab project freeze periods can be imported using an id made up of `project_id:freeze_period_id`, e.g.

        ```sh
        $ pulumi import gitlab:index/projectFreezePeriod:ProjectFreezePeriod schedule "12345:1337"
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cron_timezone: The timezone.
        :param pulumi.Input[str] freeze_end: End of the Freeze Period in cron format (e.g. `0 2 * * *`).
        :param pulumi.Input[str] freeze_start: Start of the Freeze Period in cron format (e.g. `0 1 * * *`).
        :param pulumi.Input[str] project: The ID or URL-encoded path of the project to add the schedule to.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ProjectFreezePeriodArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The `ProjectFreezePeriod` resource allows to manage the lifecycle of a freeze period for a project.

        **Upstream API**: [GitLab REST API docs](https://docs.gitlab.com/ee/api/freeze_periods.html)

        ## Example Usage

        ```python
        import pulumi
        import pulumi_gitlab as gitlab

        schedule = gitlab.ProjectFreezePeriod("schedule",
            project=foo["id"],
            freeze_start="0 23 * * 5",
            freeze_end="0 7 * * 1",
            cron_timezone="UTC")
        ```

        ## Import

        GitLab project freeze periods can be imported using an id made up of `project_id:freeze_period_id`, e.g.

        ```sh
        $ pulumi import gitlab:index/projectFreezePeriod:ProjectFreezePeriod schedule "12345:1337"
        ```

        :param str resource_name: The name of the resource.
        :param ProjectFreezePeriodArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ProjectFreezePeriodArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cron_timezone: Optional[pulumi.Input[str]] = None,
                 freeze_end: Optional[pulumi.Input[str]] = None,
                 freeze_start: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ProjectFreezePeriodArgs.__new__(ProjectFreezePeriodArgs)

            __props__.__dict__["cron_timezone"] = cron_timezone
            if freeze_end is None and not opts.urn:
                raise TypeError("Missing required property 'freeze_end'")
            __props__.__dict__["freeze_end"] = freeze_end
            if freeze_start is None and not opts.urn:
                raise TypeError("Missing required property 'freeze_start'")
            __props__.__dict__["freeze_start"] = freeze_start
            if project is None and not opts.urn:
                raise TypeError("Missing required property 'project'")
            __props__.__dict__["project"] = project
        super(ProjectFreezePeriod, __self__).__init__(
            'gitlab:index/projectFreezePeriod:ProjectFreezePeriod',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            cron_timezone: Optional[pulumi.Input[str]] = None,
            freeze_end: Optional[pulumi.Input[str]] = None,
            freeze_start: Optional[pulumi.Input[str]] = None,
            project: Optional[pulumi.Input[str]] = None) -> 'ProjectFreezePeriod':
        """
        Get an existing ProjectFreezePeriod resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cron_timezone: The timezone.
        :param pulumi.Input[str] freeze_end: End of the Freeze Period in cron format (e.g. `0 2 * * *`).
        :param pulumi.Input[str] freeze_start: Start of the Freeze Period in cron format (e.g. `0 1 * * *`).
        :param pulumi.Input[str] project: The ID or URL-encoded path of the project to add the schedule to.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ProjectFreezePeriodState.__new__(_ProjectFreezePeriodState)

        __props__.__dict__["cron_timezone"] = cron_timezone
        __props__.__dict__["freeze_end"] = freeze_end
        __props__.__dict__["freeze_start"] = freeze_start
        __props__.__dict__["project"] = project
        return ProjectFreezePeriod(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="cronTimezone")
    def cron_timezone(self) -> pulumi.Output[Optional[str]]:
        """
        The timezone.
        """
        return pulumi.get(self, "cron_timezone")

    @property
    @pulumi.getter(name="freezeEnd")
    def freeze_end(self) -> pulumi.Output[str]:
        """
        End of the Freeze Period in cron format (e.g. `0 2 * * *`).
        """
        return pulumi.get(self, "freeze_end")

    @property
    @pulumi.getter(name="freezeStart")
    def freeze_start(self) -> pulumi.Output[str]:
        """
        Start of the Freeze Period in cron format (e.g. `0 1 * * *`).
        """
        return pulumi.get(self, "freeze_start")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        """
        The ID or URL-encoded path of the project to add the schedule to.
        """
        return pulumi.get(self, "project")

