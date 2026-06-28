# executor.py

import time
from agents import retriever_agent, analyzer_agent, writer_agent


# =========================
# AGENT REGISTRY
# =========================

AGENTS = {

    "retriever": retriever_agent,
    "analyzer": analyzer_agent,
    "writer": writer_agent

}


# =========================
# EXECUTOR ENGINE
# =========================

class Executor:


    def __init__(self):

        self.queue = []

        self.results = {}

        self.logs = []



    # =========================
    # LOAD DAG TASKS
    # =========================

    def load(self, tasks):

        self.queue = tasks



    # =========================
    # CHECK DEPENDENCIES
    # =========================

    def can_run(self, task):

        for dependency in task["depends_on"]:

            if dependency not in self.results:

                return False


        return True



    # =========================
    # MANUAL BATCHING
    # =========================

    def create_batches(self, tasks, size=2):

        batches = []


        for i in range(0, len(tasks), size):

            batches.append(
                tasks[i:i+size]
            )


        return batches



    # =========================
    # RETRY SYSTEM
    # =========================

    def execute_with_retry(self, agent, task, retries=2):


        for attempt in range(retries + 1):

            try:

                output = agent(task)

                return output


            except Exception as e:


                print(
                    f"⚠️ {agent.__name__} failed attempt {attempt+1}"
                )


                if attempt == retries:

                    return {

                        "error":
                        f"{agent.__name__} failed after retries"

                    }


                time.sleep(1)




    # =========================
    # MAIN EXECUTION PIPELINE
    # =========================

    def run(self):


        print("\n==== EXECUTION STARTED ====\n")


        # manual batching

        batches = self.create_batches(
            self.queue,
            size=2
        )



        batch_number = 1



        for batch in batches:


            print(
                f"\n📦 Processing Batch {batch_number}"
            )


            batch_number += 1



            for task in batch:



                # wait until dependency complete

                if not self.can_run(task):

                    self.queue.append(task)

                    continue



                agent_name = task["agent"]


                agent = AGENTS[agent_name]



                print(
                    f"\n🚀 Running {agent_name}"
                )



                self.logs.append({

                    "task_id": task["id"],

                    "status":"started"

                })



                # choose input

                if agent_name == "retriever":


                    input_data = task["task"]



                elif agent_name == "analyzer":


                    input_data = self.results.get(1)



                elif agent_name == "writer":


                    input_data = self.results.get(2)




                # execute

                output = self.execute_with_retry(

                    agent,

                    input_data

                )




                # failure handling

                if isinstance(output,dict) and "error" in output:


                    print(
                        "❌ Failure detected → fallback used"
                    )


                    output = {

                        "fallback":

                        f"{agent_name} completed with fallback"

                    }




                self.results[task["id"]] = output



                self.logs.append({

                    "task_id":task["id"],

                    "status":"success"

                })




                # STREAM OUTPUT

                yield {

                    "agent":agent_name,

                    "output":output

                }



                time.sleep(0.5)





        # FINAL RESPONSE

        yield {


            "final":True,

            "results":self.results,

            "logs":self.logs


        }