#!/usr/bin/env python
from constructs import Construct
from cdktf import App, TerraformStack, TerraformOutput
from imports.aws.provider import AwsProvider
from imports.aws.instance import Instance


class MyStack(TerraformStack):
    def __init__(self, scope: Construct, ns: str):
        super().__init__(scope, ns)

        AwsProvider(self, "AWS", region="us-east-1")

        instance = Instance(self, "compute",
                            ami="ami-04a81a99f5ec58529",
                            instance_type="t2.micro",
                            subnet_id="subnet-0e565f757c72b9769"
                            )

        TerraformOutput(self, "public_ip",
                        value=instance.public_ip,
                        )


app = App()
stack = MyStack(app, "cdktf-example")

app.synth()
