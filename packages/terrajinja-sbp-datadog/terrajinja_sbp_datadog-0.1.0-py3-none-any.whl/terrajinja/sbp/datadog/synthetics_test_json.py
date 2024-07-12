import json

from cdktf_cdktf_provider_datadog.synthetics_test import SyntheticsTest
from constructs import Construct


def dict_to_terraform(synthetic: dict) -> dict:
    # converts the synthetic to a terraform dict
    config = synthetic.get('config')
    if config:
        del synthetic['config']

        # config.assertions is assertions
        synthetic['assertion'] = config.get('assertions')

        # convert assertion target to string if it is an int
        for assertion in synthetic['assertion']:
            if isinstance(assertion['target'], (int, float)):
                # ensure status code has no decimal
                if assertion['type'] == 'statusCode':
                    assertion['target'] = "%.0f" % (assertion['target'])
                else:
                    # ensure target is a string
                    assertion['target'] = str(assertion['target'])

        # config.request is request_headers + request_definitions
        request = config.get('request')
        if request:
            synthetic['request_headers'] = request.get('headers')
            del request['headers']
            synthetic['request_definition'] = request

    name = synthetic.get('name')

    # these fields are not in the terraform resource
    synthetic.pop('created_at', None)
    synthetic.pop('modified_at', None)
    synthetic.pop('creator', None)
    synthetic.pop('monitor_id', None)
    synthetic.pop('public_id', None)

    options = synthetic.get('options')
    if options:
        del synthetic['options']

        # ensure monitor name is same as check name for consistency
        options['monitor_name'] = name

        # bindings is not an option in the terraform resource
        options.pop('bindings', None)

        monitor_options = options.get('monitor_options')
        if monitor_options:
            # this is not an option in the terraform resource
            monitor_options.pop('notification_preset_name', None)
            options['monitor_options'] = monitor_options

        # options should be options_list
        synthetic['options_list'] = options

    return synthetic


class SbpDatadogSyntheticsTestJson(SyntheticsTest):
    """SBP version of vault.kv_secret_v2"""

    def __init__(self, scope: Construct, ns: str, synthetic_test: str, **kwargs):
        """Replaces the original datadog.synthetics_test

        Args:
            scope (Construct): Cdktf App
            id (str): uniq name of the resource
            synthetic_test (str): a json string specifying the synthetic test

        Original:
            https://registry.terraform.io/providers/hashicorp/datadog/latest/docs/resources/synthetic_test
        """

        synthetic_dict = dict_to_terraform(json.loads(synthetic_test))

        super().__init__(
            scope=scope,
            id_=ns,
            **synthetic_dict,
        )
