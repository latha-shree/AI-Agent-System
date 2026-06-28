# Post Mortem Document


## Scaling Issue

Currently, agents execute sequentially.

When multiple users send requests at the same time, the response time can increase because every agent waits for the previous agent to complete.

Possible improvement:
Implement asynchronous execution and task queues for handling multiple requests efficiently.


## Design Change I Would Make

I would introduce a message-based communication system between agents.

Currently, agents directly pass outputs to each other.

A message queue architecture would improve scalability, debugging, and monitoring.


## Trade-offs


## Trade-off 1: Sequential Execution vs Parallel Execution

Chosen:
Sequential execution

Reason:
It provides a simple workflow and makes debugging easier.

Disadvantage:
It increases execution time for complex tasks.


## Trade-off 2: Simple Flask Frontend vs Advanced Frontend Framework

Chosen:
HTML + JavaScript frontend

Reason:
It allows faster development and clearly demonstrates the agent workflow.

Disadvantage:
It has fewer interactive features compared to frameworks like React.


## Conclusion

The current system focuses on demonstrating the complete multi-agent workflow. Future improvements can focus on scalability, reliability, and production-level deployment.