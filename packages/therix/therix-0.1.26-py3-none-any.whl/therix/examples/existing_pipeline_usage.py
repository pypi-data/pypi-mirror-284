from therix.core.agent import Agent
import sys

#Executing an existing agent with session id 
# variables = {
#         "calendar": "List of booked events",
#         "current_time": "tHIS IS MY time zoneeeee",
#         "todays_date": "2024-07-10",
#         "working_hours_acc_to_user_timezone_start": "10:00 am",
#         "working_hours_acc_to_user_timezone_end": "9:00 pm"
#     }
variables = {
    "name": "Nilesh Sanap",
}

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
    agent_id = "f0a4242e-2ac3-4fd9-a4eb-3f739328de51"
    question = "hIIII HOW ARE YOU"
    session_id = '257e261f-6885-4617-b019-40c6a013a41f'
   
    agent = Agent.from_id(agent_id)

    ans = agent.invoke(question,dynamic_system_prompt_variables=variables,session_id=session_id)
    print(ans)

