# Dapr Bindings (Dapr SDK)

In this quickstart, you'll create a microservice to demonstrate Dapr's bindings API to work with external systems as inputs and outputs. The service listens to input binding events from a system CRON and then outputs the contents of local data to a PostreSql output binding. 

Visit [this](https://docs.dapr.io/developing-applications/building-blocks/bindings/) link for more information about Dapr and Bindings.

> **Note:** This example leverages the Dapr SDK.  If you are looking for the example using HTTP REST only [click here](../http).

This quickstart includes one service:
 
- Javascript/Node.js service `bindings`

### Run and initialize PostgreSQL container

1. Open a new terminal, change directories to `../../db`, and run the container with [Docker Compose](https://docs.docker.com/compose/): 

<!-- STEP
name: Run and initialize PostgreSQL container
-->

```bash
cd ../../db
docker compose up
```

<!-- END_STEP -->

### Run Javascript service with Dapr

2. Open a new terminal window in the quickstart directory and run: 

<!-- STEP
name: Install Javascript dependencies
-->

```bash
npm install
```

<!-- END_STEP -->
3. Run the Javascript service app with Dapr: 

<!-- STEP
name: Run javascript-quickstart-binding-sdk service
expected_stdout_lines:
  - '== APP == {"operation": "exec", "metadata": {"sql" : "insert into orders (orderid, customer, price) values(1, \'John Smith\', 100.32)"} }'
  - '== APP == {"operation": "exec", "metadata": {"sql" : "insert into orders (orderid, customer, price) values(2, \'Jane Bond\', 15.4)"} }'
  - '== APP == {"operation": "exec", "metadata": {"sql" : "insert into orders (orderid, customer, price) values(3, \'Tony James\', 35.56)"} }'
  - '== APP == Finished processing batch'
expected_stderr_lines:
output_match_mode: substring
background: true
sleep: 15
-->
    
```bash
dapr run --app-id javascript-quickstart-binding-sdk --app-port 5001 --dapr-http-port 3500 --components-path ../../components -- node index.js
```

<!-- END_STEP -->

4. Clean up: 

<!-- STEP
name: Clean up
-->


```bash
dapr stop --app-id javascript-quickstart-binding-sdk
```

```bash
docker compose down 
```

<!-- END_STEP -->