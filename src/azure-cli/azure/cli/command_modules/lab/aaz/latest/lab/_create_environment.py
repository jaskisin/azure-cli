# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


class CreateEnvironment(AAZCommand):
    """Create virtual machines in a lab. This operation can take a while to complete.

    :example: Create a VM in the lab from a gallery image.
        az lab vm create --lab-name {LabName} -g {ResourceGroup} --name {VMName} --image "Ubuntu Server 22.04 LTS" --image-type gallery --size Standard_DS1_v2

    :example: Create a VM in the lab from a gallery image with SSH authentication.
        az lab vm create --lab-name {LabName} -g {ResourceGroup} --name {VMName} --image "Ubuntu Server 22.04 LTS" --image-type gallery --size Standard_DS1_v2 --authentication-type ssh

    :example: Create a claimable VM in the lab from a gallery image with password authentication.
        az lab vm create --lab-name {LabName} -g {ResourceGroup} --name {VMName} --image "Ubuntu Server 22.04 LTS" --image-type gallery --size Standard_DS1_v2 --allow-claim

    :example: Create a windows VM in the lab from a gallery image with password authentication.
        az lab vm create --lab-name {LabName} -g {ResourceGroup} --name {VMName} --image "Windows Server 2022 Datacenter" --image-type gallery --size Standard_DS1_v2

    :example: Create a VM in the lab from a custom image.
        az lab vm create --lab-name {LabName} -g {ResourceGroup} --name {VMName} --image "jenkins_custom" --image-type custom --size Standard_DS1_v2

    :example: Create a VM in the lab with a public IP.
        az lab vm create --lab-name {LabName} -g {ResourceGroup} --name {VMName} --image "Ubuntu Server 22.04 LTS" --image-type gallery --size Standard_DS1_v2 --ip-configuration public

    :example: Create a VM from a formula.
        az lab vm create --lab-name {LabName} -g {ResourceGroup} --name {VMName} --formula MyFormula --artifacts 'artifacts.json'
    """

    _aaz_info = {
        "version": "2018-09-15",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.devtestlab/labs/{}/createenvironment", "2018-09-15"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, None)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.lab_name = AAZStrArg(
            options=["--lab-name"],
            help="The name of the lab.",
            required=True,
            id_part="name",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.location = AAZStrArg(
            options=["--location"],
            help="The location of the new virtual machine or environment",
        )
        _args_schema.name = AAZStrArg(
            options=["-n", "--name"],
            help="The name of the virtual machine or environment",
        )
        _args_schema.allow_claim = AAZBoolArg(
            options=["--allow-claim"],
            help="Flag indicating if the VM should be created as claimable.",
            default=False,
        )
        _args_schema.artifacts_org = AAZListArg(
            options=["--artifacts-org"],
            help="The artifacts to be installed on the virtual machine.",
        )
        _args_schema.bulk_creation_parameters = AAZObjectArg(
            options=["--bulk-creation-parameters"],
            help="The number of virtual machine instances to create.",
        )
        _args_schema.created_date = AAZDateTimeArg(
            options=["--created-date"],
            help="The creation date of the virtual machine.",
        )
        _args_schema.custom_image_id = AAZStrArg(
            options=["--custom-image-id"],
            help="The custom image identifier of the virtual machine.",
        )
        _args_schema.data_disk_parameters = AAZListArg(
            options=["--data-disk-parameters"],
            help="New or existing data disks to attach to the virtual machine after creation",
        )
        _args_schema.disallow_public_ip_address = AAZBoolArg(
            options=["--disallow-public-ip-address"],
            help="Indicates whether the virtual machine is to be created without a public IP address.",
            default=False,
        )
        _args_schema.environment_id = AAZStrArg(
            options=["--environment-id"],
            help="The resource ID of the environment that contains this virtual machine, if any.",
        )
        _args_schema.expiration_date = AAZDateTimeArg(
            options=["--expiration-date"],
            help="The expiration date for VM.",
        )
        _args_schema.gallery_image_reference = AAZObjectArg(
            options=["--gallery-image-reference"],
            help="The Microsoft Azure Marketplace image reference of the virtual machine.",
        )
        _args_schema.is_authentication_with_ssh_key = AAZBoolArg(
            options=["--is-authentication-with-ssh-key"],
            help="Indicates whether this virtual machine uses an SSH key for authentication.",
        )
        _args_schema.lab_subnet_name = AAZStrArg(
            options=["--lab-subnet-name"],
            help="The lab subnet name of the virtual machine.",
        )
        _args_schema.lab_virtual_network_id = AAZStrArg(
            options=["--lab-virtual-network-id"],
            help="The lab virtual network identifier of the virtual machine.",
        )
        _args_schema.network_interface = AAZObjectArg(
            options=["--network-interface"],
            help="The network interface properties.",
        )
        _args_schema.notes = AAZStrArg(
            options=["--notes"],
            help="The notes of the virtual machine.",
        )
        _args_schema.owner_object_id = AAZStrArg(
            options=["--owner-object-id"],
            help="The object identifier of the owner of the virtual machine.",
            default="dynamicValue",
        )
        _args_schema.owner_user_principal_name = AAZStrArg(
            options=["--owner-user-principal-name"],
            help="The user principal name of the virtual machine owner.",
        )
        _args_schema.password = AAZStrArg(
            options=["--password"],
            help="The password of the virtual machine administrator.",
        )
        _args_schema.plan_id = AAZStrArg(
            options=["--plan-id"],
            help="The id of the plan associated with the virtual machine image",
        )
        _args_schema.schedule_parameters = AAZListArg(
            options=["--schedule-parameters"],
            help="Virtual Machine schedules to be created",
        )
        _args_schema.size = AAZStrArg(
            options=["--size"],
            help="The size of the VM to be created. See                                      https://azure.microsoft.com/pricing/details/virtual-machines/ for size info.",
        )
        _args_schema.ssh_key = AAZStrArg(
            options=["--ssh-key"],
            help="The SSH public key or public key file path. Use `--generate-ssh-keys` to generate SSH keys.",
        )
        _args_schema.storage_type = AAZStrArg(
            options=["--storage-type"],
            help="Storage type to use for virtual machine (i.e. Standard, Premium).",
            default="labStorageType",
        )
        _args_schema.user_name = AAZStrArg(
            options=["--user-name"],
            help="The user name of the virtual machine.",
        )
        _args_schema.tags = AAZDictArg(
            options=["--tags"],
            help="The tags of the resource.",
        )

        artifacts_org = cls._args_schema.artifacts_org
        artifacts_org.Element = AAZObjectArg()

        _element = cls._args_schema.artifacts_org.Element
        _element.artifact_id = AAZStrArg(
            options=["artifact-id"],
            help="The artifact's identifier.",
        )
        _element.artifact_title = AAZStrArg(
            options=["artifact-title"],
            help="The artifact's title.",
        )
        _element.deployment_status_message = AAZStrArg(
            options=["deployment-status-message"],
            help="The status message from the deployment.",
        )
        _element.install_time = AAZDateTimeArg(
            options=["install-time"],
            help="The time that the artifact starts to install on the virtual machine.",
        )
        _element.parameters = AAZListArg(
            options=["parameters"],
            help="The parameters of the artifact.",
        )
        _element.status = AAZStrArg(
            options=["status"],
            help="The status of the artifact.",
        )
        _element.vm_extension_status_message = AAZStrArg(
            options=["vm-extension-status-message"],
            help="The status message from the virtual machine extension.",
        )

        parameters = cls._args_schema.artifacts_org.Element.parameters
        parameters.Element = AAZObjectArg()

        _element = cls._args_schema.artifacts_org.Element.parameters.Element
        _element.name = AAZStrArg(
            options=["name"],
            help="The name of the artifact parameter.",
        )
        _element.value = AAZStrArg(
            options=["value"],
            help="The value of the artifact parameter.",
        )

        bulk_creation_parameters = cls._args_schema.bulk_creation_parameters
        bulk_creation_parameters.instance_count = AAZIntArg(
            options=["instance-count"],
            help="The number of virtual machine instances to create.",
        )

        data_disk_parameters = cls._args_schema.data_disk_parameters
        data_disk_parameters.Element = AAZObjectArg()

        _element = cls._args_schema.data_disk_parameters.Element
        _element.attach_new_data_disk_options = AAZObjectArg(
            options=["attach-new-data-disk-options"],
            help="Specifies options to attach a new disk to the virtual machine.",
        )
        _element.existing_lab_disk_id = AAZStrArg(
            options=["existing-lab-disk-id"],
            help="Specifies the existing lab disk id to attach to virtual machine.",
        )
        _element.host_caching = AAZStrArg(
            options=["host-caching"],
            help="Caching option for a data disk (i.e. None, ReadOnly, ReadWrite).",
            enum={"None": "None", "ReadOnly": "ReadOnly", "ReadWrite": "ReadWrite"},
        )

        attach_new_data_disk_options = cls._args_schema.data_disk_parameters.Element.attach_new_data_disk_options
        attach_new_data_disk_options.disk_name = AAZStrArg(
            options=["disk-name"],
            help="The name of the disk to be attached.",
        )
        attach_new_data_disk_options.disk_size_gi_b = AAZIntArg(
            options=["disk-size-gi-b"],
            help="Size of the disk to be attached in Gibibytes.",
        )
        attach_new_data_disk_options.disk_type = AAZStrArg(
            options=["disk-type"],
            help="The storage type for the disk (i.e. Standard, Premium).",
            enum={"Premium": "Premium", "Standard": "Standard", "StandardSSD": "StandardSSD"},
        )

        gallery_image_reference = cls._args_schema.gallery_image_reference
        gallery_image_reference.offer = AAZStrArg(
            options=["offer"],
            help="The offer of the gallery image.",
        )
        gallery_image_reference.os_type = AAZStrArg(
            options=["os-type"],
            help="The OS type of the gallery image.",
        )
        gallery_image_reference.publisher = AAZStrArg(
            options=["publisher"],
            help="The publisher of the gallery image.",
        )
        gallery_image_reference.sku = AAZStrArg(
            options=["sku"],
            help="The SKU of the gallery image.",
        )
        gallery_image_reference.version = AAZStrArg(
            options=["version"],
            help="The version of the gallery image.",
        )

        network_interface = cls._args_schema.network_interface
        network_interface.dns_name = AAZStrArg(
            options=["dns-name"],
            help="The DNS name.",
        )
        network_interface.private_ip_address = AAZStrArg(
            options=["private-ip-address"],
            help="The private IP address.",
        )
        network_interface.public_ip_address = AAZStrArg(
            options=["public-ip-address"],
            help="The public IP address.",
        )
        network_interface.public_ip_address_id = AAZStrArg(
            options=["public-ip-address-id"],
            help="The resource ID of the public IP address.",
        )
        network_interface.rdp_authority = AAZStrArg(
            options=["rdp-authority"],
            help="The RdpAuthority property is a server DNS host name or IP address followed by the service port number for RDP (Remote Desktop Protocol).",
        )
        network_interface.shared_public_ip_address_configuration = AAZObjectArg(
            options=["shared-public-ip-address-configuration"],
            help="The configuration for sharing a public IP address across multiple virtual machines.",
        )
        network_interface.ssh_authority = AAZStrArg(
            options=["ssh-authority"],
            help="The SshAuthority property is a server DNS host name or IP address followed by the service port number for SSH.",
        )
        network_interface.subnet_id = AAZStrArg(
            options=["subnet-id"],
            help="The resource ID of the sub net.",
        )
        network_interface.virtual_network_id = AAZStrArg(
            options=["virtual-network-id"],
            help="The resource ID of the virtual network.",
        )

        shared_public_ip_address_configuration = cls._args_schema.network_interface.shared_public_ip_address_configuration
        shared_public_ip_address_configuration.inbound_nat_rules = AAZListArg(
            options=["inbound-nat-rules"],
            help="The incoming NAT rules",
        )

        inbound_nat_rules = cls._args_schema.network_interface.shared_public_ip_address_configuration.inbound_nat_rules
        inbound_nat_rules.Element = AAZObjectArg()

        _element = cls._args_schema.network_interface.shared_public_ip_address_configuration.inbound_nat_rules.Element
        _element.backend_port = AAZIntArg(
            options=["backend-port"],
            help="The port to which the external traffic will be redirected.",
        )
        _element.frontend_port = AAZIntArg(
            options=["frontend-port"],
            help="The external endpoint port of the inbound connection. Possible values range between 1 and 65535, inclusive. If unspecified, a value will be allocated automatically.",
        )
        _element.transport_protocol = AAZStrArg(
            options=["transport-protocol"],
            help="The transport protocol for the endpoint.",
            enum={"Tcp": "Tcp", "Udp": "Udp"},
        )

        schedule_parameters = cls._args_schema.schedule_parameters
        schedule_parameters.Element = AAZObjectArg()

        _element = cls._args_schema.schedule_parameters.Element
        _element.name = AAZStrArg(
            options=["name"],
            help="The name of the virtual machine or environment",
        )
        _element.daily_recurrence = AAZObjectArg(
            options=["daily-recurrence"],
            help="If the schedule will occur once each day of the week, specify the daily recurrence.",
        )
        _element.hourly_recurrence = AAZObjectArg(
            options=["hourly-recurrence"],
            help="If the schedule will occur multiple times a day, specify the hourly recurrence.",
        )
        _element.notification_settings = AAZObjectArg(
            options=["notification-settings"],
            help="Notification settings.",
        )
        _element.status = AAZStrArg(
            options=["status"],
            help="The status of the schedule (i.e. Enabled, Disabled)",
            default="Disabled",
            enum={"Disabled": "Disabled", "Enabled": "Enabled"},
        )
        _element.target_resource_id = AAZStrArg(
            options=["target-resource-id"],
            help="The resource ID to which the schedule belongs",
        )
        _element.task_type = AAZStrArg(
            options=["task-type"],
            help="The task type of the schedule (e.g. LabVmsShutdownTask, LabVmAutoStart).",
        )
        _element.time_zone_id = AAZStrArg(
            options=["time-zone-id"],
            help="The time zone ID (e.g. China Standard Time, Greenland Standard Time, Pacific Standard time, etc.). The possible values for this property can be found in `IReadOnlyCollection<string> TimeZoneConverter.TZConvert.KnownWindowsTimeZoneIds` (https://github.com/mattjohnsonpint/TimeZoneConverter/blob/main/README.md)",
        )
        _element.weekly_recurrence = AAZObjectArg(
            options=["weekly-recurrence"],
            help="If the schedule will occur only some days of the week, specify the weekly recurrence.",
        )
        _element.tags = AAZDictArg(
            options=["tags"],
            help="The tags of the resource.",
        )

        daily_recurrence = cls._args_schema.schedule_parameters.Element.daily_recurrence
        daily_recurrence.time = AAZStrArg(
            options=["time"],
            help="The time of day the schedule will occur.",
        )

        hourly_recurrence = cls._args_schema.schedule_parameters.Element.hourly_recurrence
        hourly_recurrence.minute = AAZIntArg(
            options=["minute"],
            help="Minutes of the hour the schedule will run.",
        )

        notification_settings = cls._args_schema.schedule_parameters.Element.notification_settings
        notification_settings.email_recipient = AAZStrArg(
            options=["email-recipient"],
            help="The email recipient to send notifications to (can be a list of semi-colon separated email addresses).",
        )
        notification_settings.notification_locale = AAZStrArg(
            options=["notification-locale"],
            help="The locale to use when sending a notification (fallback for unsupported languages is EN).",
        )
        notification_settings.status = AAZStrArg(
            options=["status"],
            help="If notifications are enabled for this schedule (i.e. Enabled, Disabled).",
            default="Disabled",
            enum={"Disabled": "Disabled", "Enabled": "Enabled"},
        )
        notification_settings.time_in_minutes = AAZIntArg(
            options=["time-in-minutes"],
            help="Time in minutes before event at which notification will be sent.",
        )
        notification_settings.webhook_url = AAZStrArg(
            options=["webhook-url"],
            help="The webhook URL to which the notification will be sent.",
        )

        weekly_recurrence = cls._args_schema.schedule_parameters.Element.weekly_recurrence
        weekly_recurrence.time = AAZStrArg(
            options=["time"],
            help="The time of the day the schedule will occur.",
        )
        weekly_recurrence.weekdays = AAZListArg(
            options=["weekdays"],
            help="The days of the week for which the schedule is set (e.g. Sunday, Monday, Tuesday, etc.).",
        )

        weekdays = cls._args_schema.schedule_parameters.Element.weekly_recurrence.weekdays
        weekdays.Element = AAZStrArg()

        tags = cls._args_schema.schedule_parameters.Element.tags
        tags.Element = AAZStrArg()

        tags = cls._args_schema.tags
        tags.Element = AAZStrArg()
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        yield self.LabsCreateEnvironment(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    class LabsCreateEnvironment(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{lab-name}/createEnvironment",
                **self.url_parameters
            )

        @property
        def method(self):
            return "POST"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "lab-name", self.ctx.args.lab_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2018-09-15",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                typ=AAZObjectType,
                typ_kwargs={"flags": {"required": True, "client_flatten": True}}
            )
            _builder.set_prop("location", AAZStrType, ".location")
            _builder.set_prop("name", AAZStrType, ".name")
            _builder.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})
            _builder.set_prop("tags", AAZDictType, ".tags")

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("allowClaim", AAZBoolType, ".allow_claim")
                properties.set_prop("artifacts", AAZListType, ".artifacts_org")
                properties.set_prop("bulkCreationParameters", AAZObjectType, ".bulk_creation_parameters")
                properties.set_prop("createdDate", AAZStrType, ".created_date")
                properties.set_prop("customImageId", AAZStrType, ".custom_image_id")
                properties.set_prop("dataDiskParameters", AAZListType, ".data_disk_parameters")
                properties.set_prop("disallowPublicIpAddress", AAZBoolType, ".disallow_public_ip_address")
                properties.set_prop("environmentId", AAZStrType, ".environment_id")
                properties.set_prop("expirationDate", AAZStrType, ".expiration_date")
                properties.set_prop("galleryImageReference", AAZObjectType, ".gallery_image_reference")
                properties.set_prop("isAuthenticationWithSshKey", AAZBoolType, ".is_authentication_with_ssh_key")
                properties.set_prop("labSubnetName", AAZStrType, ".lab_subnet_name")
                properties.set_prop("labVirtualNetworkId", AAZStrType, ".lab_virtual_network_id")
                properties.set_prop("networkInterface", AAZObjectType, ".network_interface")
                properties.set_prop("notes", AAZStrType, ".notes")
                properties.set_prop("ownerObjectId", AAZStrType, ".owner_object_id")
                properties.set_prop("ownerUserPrincipalName", AAZStrType, ".owner_user_principal_name")
                properties.set_prop("password", AAZStrType, ".password", typ_kwargs={"flags": {"secret": True}})
                properties.set_prop("planId", AAZStrType, ".plan_id")
                properties.set_prop("scheduleParameters", AAZListType, ".schedule_parameters")
                properties.set_prop("size", AAZStrType, ".size")
                properties.set_prop("sshKey", AAZStrType, ".ssh_key", typ_kwargs={"flags": {"secret": True}})
                properties.set_prop("storageType", AAZStrType, ".storage_type")
                properties.set_prop("userName", AAZStrType, ".user_name")

            artifacts = _builder.get(".properties.artifacts")
            if artifacts is not None:
                artifacts.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".properties.artifacts[]")
            if _elements is not None:
                _elements.set_prop("artifactId", AAZStrType, ".artifact_id")
                _elements.set_prop("artifactTitle", AAZStrType, ".artifact_title")
                _elements.set_prop("deploymentStatusMessage", AAZStrType, ".deployment_status_message")
                _elements.set_prop("installTime", AAZStrType, ".install_time")
                _elements.set_prop("parameters", AAZListType, ".parameters")
                _elements.set_prop("status", AAZStrType, ".status")
                _elements.set_prop("vmExtensionStatusMessage", AAZStrType, ".vm_extension_status_message")

            parameters = _builder.get(".properties.artifacts[].parameters")
            if parameters is not None:
                parameters.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".properties.artifacts[].parameters[]")
            if _elements is not None:
                _elements.set_prop("name", AAZStrType, ".name")
                _elements.set_prop("value", AAZStrType, ".value")

            bulk_creation_parameters = _builder.get(".properties.bulkCreationParameters")
            if bulk_creation_parameters is not None:
                bulk_creation_parameters.set_prop("instanceCount", AAZIntType, ".instance_count")

            data_disk_parameters = _builder.get(".properties.dataDiskParameters")
            if data_disk_parameters is not None:
                data_disk_parameters.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".properties.dataDiskParameters[]")
            if _elements is not None:
                _elements.set_prop("attachNewDataDiskOptions", AAZObjectType, ".attach_new_data_disk_options")
                _elements.set_prop("existingLabDiskId", AAZStrType, ".existing_lab_disk_id")
                _elements.set_prop("hostCaching", AAZStrType, ".host_caching")

            attach_new_data_disk_options = _builder.get(".properties.dataDiskParameters[].attachNewDataDiskOptions")
            if attach_new_data_disk_options is not None:
                attach_new_data_disk_options.set_prop("diskName", AAZStrType, ".disk_name")
                attach_new_data_disk_options.set_prop("diskSizeGiB", AAZIntType, ".disk_size_gi_b")
                attach_new_data_disk_options.set_prop("diskType", AAZStrType, ".disk_type")

            gallery_image_reference = _builder.get(".properties.galleryImageReference")
            if gallery_image_reference is not None:
                gallery_image_reference.set_prop("offer", AAZStrType, ".offer")
                gallery_image_reference.set_prop("osType", AAZStrType, ".os_type")
                gallery_image_reference.set_prop("publisher", AAZStrType, ".publisher")
                gallery_image_reference.set_prop("sku", AAZStrType, ".sku")
                gallery_image_reference.set_prop("version", AAZStrType, ".version")

            network_interface = _builder.get(".properties.networkInterface")
            if network_interface is not None:
                network_interface.set_prop("dnsName", AAZStrType, ".dns_name")
                network_interface.set_prop("privateIpAddress", AAZStrType, ".private_ip_address")
                network_interface.set_prop("publicIpAddress", AAZStrType, ".public_ip_address")
                network_interface.set_prop("publicIpAddressId", AAZStrType, ".public_ip_address_id")
                network_interface.set_prop("rdpAuthority", AAZStrType, ".rdp_authority")
                network_interface.set_prop("sharedPublicIpAddressConfiguration", AAZObjectType, ".shared_public_ip_address_configuration")
                network_interface.set_prop("sshAuthority", AAZStrType, ".ssh_authority")
                network_interface.set_prop("subnetId", AAZStrType, ".subnet_id")
                network_interface.set_prop("virtualNetworkId", AAZStrType, ".virtual_network_id")

            shared_public_ip_address_configuration = _builder.get(".properties.networkInterface.sharedPublicIpAddressConfiguration")
            if shared_public_ip_address_configuration is not None:
                shared_public_ip_address_configuration.set_prop("inboundNatRules", AAZListType, ".inbound_nat_rules")

            inbound_nat_rules = _builder.get(".properties.networkInterface.sharedPublicIpAddressConfiguration.inboundNatRules")
            if inbound_nat_rules is not None:
                inbound_nat_rules.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".properties.networkInterface.sharedPublicIpAddressConfiguration.inboundNatRules[]")
            if _elements is not None:
                _elements.set_prop("backendPort", AAZIntType, ".backend_port")
                _elements.set_prop("frontendPort", AAZIntType, ".frontend_port")
                _elements.set_prop("transportProtocol", AAZStrType, ".transport_protocol")

            schedule_parameters = _builder.get(".properties.scheduleParameters")
            if schedule_parameters is not None:
                schedule_parameters.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".properties.scheduleParameters[]")
            if _elements is not None:
                _elements.set_prop("name", AAZStrType, ".name")
                _elements.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})
                _elements.set_prop("tags", AAZDictType, ".tags")

            properties = _builder.get(".properties.scheduleParameters[].properties")
            if properties is not None:
                properties.set_prop("dailyRecurrence", AAZObjectType, ".daily_recurrence")
                properties.set_prop("hourlyRecurrence", AAZObjectType, ".hourly_recurrence")
                properties.set_prop("notificationSettings", AAZObjectType, ".notification_settings")
                properties.set_prop("status", AAZStrType, ".status")
                properties.set_prop("targetResourceId", AAZStrType, ".target_resource_id")
                properties.set_prop("taskType", AAZStrType, ".task_type")
                properties.set_prop("timeZoneId", AAZStrType, ".time_zone_id")
                properties.set_prop("weeklyRecurrence", AAZObjectType, ".weekly_recurrence")

            daily_recurrence = _builder.get(".properties.scheduleParameters[].properties.dailyRecurrence")
            if daily_recurrence is not None:
                daily_recurrence.set_prop("time", AAZStrType, ".time")

            hourly_recurrence = _builder.get(".properties.scheduleParameters[].properties.hourlyRecurrence")
            if hourly_recurrence is not None:
                hourly_recurrence.set_prop("minute", AAZIntType, ".minute")

            notification_settings = _builder.get(".properties.scheduleParameters[].properties.notificationSettings")
            if notification_settings is not None:
                notification_settings.set_prop("emailRecipient", AAZStrType, ".email_recipient")
                notification_settings.set_prop("notificationLocale", AAZStrType, ".notification_locale")
                notification_settings.set_prop("status", AAZStrType, ".status")
                notification_settings.set_prop("timeInMinutes", AAZIntType, ".time_in_minutes")
                notification_settings.set_prop("webhookUrl", AAZStrType, ".webhook_url")

            weekly_recurrence = _builder.get(".properties.scheduleParameters[].properties.weeklyRecurrence")
            if weekly_recurrence is not None:
                weekly_recurrence.set_prop("time", AAZStrType, ".time")
                weekly_recurrence.set_prop("weekdays", AAZListType, ".weekdays")

            weekdays = _builder.get(".properties.scheduleParameters[].properties.weeklyRecurrence.weekdays")
            if weekdays is not None:
                weekdays.set_elements(AAZStrType, ".")

            tags = _builder.get(".properties.scheduleParameters[].tags")
            if tags is not None:
                tags.set_elements(AAZStrType, ".")

            tags = _builder.get(".tags")
            if tags is not None:
                tags.set_elements(AAZStrType, ".")

            return self.serialize_content(_content_value)

        def on_200(self, session):
            pass


class _CreateEnvironmentHelper:
    """Helper class for CreateEnvironment"""


__all__ = ["CreateEnvironment"]