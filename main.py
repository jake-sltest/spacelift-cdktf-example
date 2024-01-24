#!/usr/bin/env python
from constructs import Construct
from cdktf import App, TerraformStack, TerraformOutput
from imports.aws.provider import AwsProvider
from imports.aws.instance import Instance


class MyStack(TerraformStack):
    def __init__(self, scope: Construct, ns: str):
        super().__init__(scope, ns)

        AwsProvider(self, "AWS", region="eu-west-1")

        instance = Instance(self, "compute",
                            ami="ami-02a66cf05465c373f",
                            instance_type="t2.micro",
                            )

        TerraformOutput(self, "public_ip",
                        value=instance.public_ip,
                        )


app = App()
stack = MyStack(app, "cdktf-example")

app.synth()
