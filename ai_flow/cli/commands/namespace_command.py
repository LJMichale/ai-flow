# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# 'License'); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# 'AS IS' BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

"""Namespace command"""
import json

from ai_flow import ops
from ai_flow.cli.simple_table import AIFlowConsole


def add_namespace(args):
    """Uploads the namespace by name."""
    properties = json.loads(args.properties) if args.properties is not None else {}
    namespace = ops.add_namespace(name=args.namespace_name, properties=properties)
    print("Namespace: {}, created.".format(namespace.name))


def delete_namespace(args):
    """Deletes the namespace by name."""
    ops.delete_namespace(args.namespace_name)
    print("Namespace: {}, deleted.".format(args.namespace_name))


def list_namespaces(args):
    """Lists all namespaces."""
    namespaces = ops.list_namespace()
    AIFlowConsole().print_as(
        data=sorted(namespaces, key=lambda w: w.name),
        output=args.output,
        mapper=lambda x: {
            'name': x.name,
            'properties': x.properties
        },
    )
