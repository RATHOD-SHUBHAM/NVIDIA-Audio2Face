import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# Agents
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper

from langchain_community.utilities import SerpAPIWrapper

from langchain.agents import Tool
from langchain.agents import initialize_agent
from langchain.agents import load_tools
from langchain.chains.conversation.memory import ConversationBufferWindowMemory


# Load the envs
load_dotenv()
os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')
os.environ["OPENWEATHERMAP_API_KEY"] = os.getenv('OPENWEATHERMAP_API_KEY')
os.environ['SERPAPI_API_KEY'] = os.getenv('SERPAPI_API_KEY')

os.environ['LANGSMITH_API_KEY'] = os.getenv('LANGSMITH_API_KEY')
os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGSMITH_API_KEY')
os.environ['LANGSMITH_TRACING'] = "true"
os.environ["LANGCHAIN_PROJECT"] = "MultiAgent"


class Agent:
    def __init__(self):
        # LLM
        self.llm = ChatOpenAI(
            temperature=0
        )

    def agents_tool(self, user_input):
        # Wikipedia Agent
        wiki_api_wrapper = WikipediaAPIWrapper(
            top_k_results=1,
            doc_content_chars_max=100
        )
        wiki_tool = WikipediaQueryRun(api_wrapper=wiki_api_wrapper)

        # defining a single tool
        wikipedia_tool = Tool(
            name="wiki_tool",
            func=wiki_tool.run,
            description="useful when you need to answer questions that references to work in history. You should ask targeted questions"
        )

        # Serp Agent
        search_engine = SerpAPIWrapper()

        search_engine_tool = Tool(
            name="search_engine",
            func=search_engine.run,
            description="useful for when you need to answer general user question and need to browse internet. You should ask targeted questions"
        )

        # Toolkit
        my_toolkit = [wikipedia_tool, search_engine_tool]
        tools = load_tools([], llm=self.llm)
        tools = tools + my_toolkit

        # conversational agent memory
        memory = ConversationBufferWindowMemory(
            memory_key='chat_history',
            k=2,
            return_messages=True
        )

        # create our agent
        conversational_agent = initialize_agent(
            agent='chat-conversational-react-description',
            tools=tools,
            llm=self.llm,
            verbose=True,
            max_iterations=3,
            early_stopping_method='generate',
            memory=memory
        )

        result = conversational_agent(user_input)

        return result['output']

