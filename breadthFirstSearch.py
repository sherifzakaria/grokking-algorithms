from collections import deque

graph = {}
graph["Sherif"] = ["Toqa", "Amr", "Zakaria"]
graph["Amr"] = ["Zizo", "Selim"]
graph["Toqa"] = ["Sherif", "Dodo", "Mohamed"]
graph["Zakaria"] = []
graph["Dodo"] = []
graph["Mohamed"] = []
graph["Zizo"] = []
graph["Selim"] = []


def search(name):

    search_queue = deque()
    search_queue += graph[name]
    searched = []

    while search_queue:
        person = search_queue.popleft()

        if not person in searched:
            if person_is_seller(person):
                print(person + " is a mango seller!")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False

def person_is_seller(person):
    if person.endswith("o"):
        return True
    else:
        return False


search("Sherif")

    