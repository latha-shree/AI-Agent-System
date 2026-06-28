# System Design Document

## Project Overview

Multi-Agent AI Research Assistant is an AI system that converts user queries into structured reports using multiple specialized agents.

## Architecture


User Input
    |
    v
Planner Agent
    |
    v
Retriever Agent
    |
    v
Analyzer Agent
    |
    v
Writer Agent
    |
    v
Final Response


## Agent Responsibilities

### Planner Agent

Responsible for understanding the user task and creating execution steps.

### Retriever Agent

Collects relevant information based on the planned task.

### Analyzer Agent

Processes retrieved information and generates summaries and key insights.

### Writer Agent

Creates the final structured report in a readable format.


## Data Flow

1. User enters a query through the web interface.
2. Flask receives the request.
3. Planner Agent creates a workflow.
4. Executor runs each agent sequentially.
5. Output from each agent is passed to the next agent.
6. Final response is displayed in the frontend.


## Technology Stack

Backend:
- Python
- Flask

Frontend:
- HTML
- JavaScript

AI:
- Large Language Model based agents


## Future Improvements

- Parallel agent execution
- Better error handling
- Database storage
- User authentication