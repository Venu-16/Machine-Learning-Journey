from typing import Annotated
from langchain.chat_models import init_chat_model
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
import os


os.environ["OPENAI_API_KEY"] = "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"

class State(TypedDict):
    messages: Annotated[list, add_messages]

# Initialize the chat model
llm = init_chat_model("openai:gpt-3.5-turbo")  # or use "gpt-4-turbo" if available

def chatbot(state: State):
    return {"messages": [llm.invoke(state["messages"])]}

# Build the graph
graph_builder = StateGraph(State)
graph_builder.add_node("chatbot", chatbot)
graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", END)
graph = graph_builder.compile()

# Run the chatbot
def stream_graph_updates(user_input: str):
    for event in graph.stream({"messages": [{"role": "user", "content": user_input}]}):
        for value in event.values():
            print("Assistant:", value["messages"][-1].content)

# Chat loop
print("Chatbot started! Type 'quit', 'exit', or 'q' to end the conversation.")
while True:
    try:
        user_input = input("User: ")
        if user_input.lower() in ["quit", "exit", "q"]:
            print("Goodbye!")
            break
        stream_graph_updates(user_input)
    except Exception as e:
        print(f"An error occurred: {e}")
        break