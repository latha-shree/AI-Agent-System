def planner_agent(task):

    plan = [

        {
            "id":1,
            "agent":"retriever",
            "task":task,
            "depends_on":[]
        },


        {
            "id":2,
            "agent":"analyzer",
            "task":"Analyze retrieved data",
            "depends_on":[1]
        },


        {
            "id":3,
            "agent":"writer",
            "task":"Write final report",
            "depends_on":[2]
        }

    ]


    return plan