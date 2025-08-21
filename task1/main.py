from task1.rag.rag import SimpleRag
from task1.agent.workflow import Workflow as bot
def run():
    knowledge_base = input('Knowledge Base: ')
    rag = SimpleRag(knowledge_base)
    while True:
        menu_1_click = input(f'1- ingest\n2- ask question\n3- exit program\n')

        if menu_1_click == '1':
            sources = ''
            while sources.strip() != '0':
                sources = input('Address: (exp: `./storage/articles.json`\nExit: 0\n')
                rag.ingest(files_path=[sources])

        if menu_1_click == '2':
            question = input('Question:\n')
            res = bot.graph.invoke({"query": question, "knowledge": knowledge_base})
            print(res.get('response'))

        if menu_1_click == '3':
            break


if __name__ == '__main__':
   run()