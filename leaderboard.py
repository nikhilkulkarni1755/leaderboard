class Node:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.next, self.express = None, None

class Leaderboard:
    def __init__(self):
        self.head = Node("dummy", -1)
        self.top = head

    def add_score(self, name, score):
        
    def top(self):

    def remove_score(self, name):
    
    def get_score(self, name):
    



if __name__ == "__main__":
    leaderboard = Leaderboard()
