from task2.agent.workflow import Workflow as bot


class Controller:

    @staticmethod
    def invoke(session_id: int, message: str):
        config = {"configurable": {"thread_id": (f"user_{str(session_id)}")}}
        input_data = {
            "query": message,
        }
        result = bot.graph.invoke(input=input_data, config=config)
        return result.get("messages")[-1].content

    @staticmethod
    def stream(knowledge: str, query: str):
        pass
