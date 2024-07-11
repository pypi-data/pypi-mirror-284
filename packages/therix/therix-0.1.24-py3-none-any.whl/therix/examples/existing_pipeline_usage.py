from therix.core.agent import Agent
import sys

#Executing an existing agent with session id 



if len(sys.argv) > 1:
    agent = Agent.from_id(sys.argv[1])
    question = sys.argv[2]
    session_id = None

    if len(sys.argv) < 4:
        pass
    else:
        session_id = sys.argv[3]  

    ans = agent.invoke(question, session_id)
    print(ans)
else:
    agent_id = '9a3c35f3-99e0-4b3a-b73a-93d1f8d74ad4'
    question = "Please don't mention my name and answer What is ablation study"
    session_id = 'add1d536-0f36-4fc3-a6a9-aebe66a755a1'
   
    agent = Agent.from_id(agent_id)

    ans = agent.invoke(question, session_id)
    print(ans)

