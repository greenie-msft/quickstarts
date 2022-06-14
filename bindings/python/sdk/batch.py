#
# Copyright 2021 The Dapr Authors
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#     http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#


import json
from dapr.ext.grpc import App, BindingRequest
from dapr.clients import DaprClient

app = App()
cron_bindingName = "batch"
sql_binding = "SqlDB"

@app.binding(cron_bindingName)
def cron_binding(request: BindingRequest):

    json_file = open("../../orders.json","r")
    json_array = json.load(json_file)

    for order_line in json_array['orders']:
       sql_output(order_line)

    json_file.close()
    return 'Cron event processed'

def sql_output(order_line):

    with DaprClient() as d:
        sqlCmd = 'insert into orders (orderid, customer, price) values ({}, \'{}\', {});'.format(order_line['orderid'], order_line['customer'], order_line['price'])
        payload = {  'sql' : sqlCmd }
        print(json.dumps(payload), flush=True)
        try:
            d.invoke_binding(binding_name=sql_binding, operation='exec', binding_metadata=payload, data='')        
        except Exception as e:
            print(e, flush=True)

app.run(50051)