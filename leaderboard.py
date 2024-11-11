import random

class Node:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.next, self.express = None, None

# decreasing order, the max is the head. getting all the scores becomes linear then.
class Leaderboard:
    def __init__(self):
        self.head = Node("dummy", -1)
        # self.top = head

    def add_score(self, name, score):
        new_node = Node(name, score)

        # Initialize pointers for the main and express lanes
        prev = None
        curr = self.head

        # Find the insertion point in decreasing order
        while curr.next and curr.next.score > score:
            prev = curr
            curr = curr.next

        # Insert the new node in the list
        new_node.next = curr.next
        curr.next = new_node

        # Randomly assign express pointers for skip list functionality
        # This is a simple method where each node has a 50% chance of being an express node
        express_chance = random.choice([True, False])
        if express_chance and prev:
            prev.express = new_node
            
    def top(self):
        if self.head.next:
            return (self.head.next.name, self.head.next.score)
        else:
            return None

    def remove_score(self, name):
        prev = self.head
        curr = self.head.next

        # Find the node to remove
        while curr and curr.name != name:
            prev = curr
            curr = curr.next

        # Remove node by adjusting pointers
        if curr:
            prev.next = curr.next

            # Update express pointers as needed
            express_prev = self.head
            while express_prev and express_prev.express != curr:
                express_prev = express_prev.express
            if express_prev:
                express_prev.express = curr.next

    
    def get_score(self, name):
        curr = self.head

        if curr.name == name:
            return curr.score

        # ahhhh
        if curr.next and curr.next.name == name:
            return curr.next.score

        # Use express pointers when possible for faster traversal
        while curr.express and curr.express.name != name and curr.express.score > -1:
            curr = curr.express
        
        # Continue on the main next pointers if needed
        while curr.next and curr.next.name != name:
            curr = curr.next
        
        # Return the score if found
        if curr.next and curr.next.name == name:
            return curr.next.score
        else:
            return None

    def get_all_scores(self):
        # Print all scores from the leaderboard
        scores = []
        curr = self.head.next
        while curr:
            scores.append((curr.name, curr.score))
            curr = curr.next
        return scores



if __name__ == "__main__":
    leaderboard = Leaderboard()
    leaderboard.add_score("Doublelift", 90)
    leaderboard.add_score("Faker", 95)
    leaderboard.add_score("Dhokla", 85)
    leaderboard.add_score("Lourlo", 92)
    leaderboard.add_score("Bjergsen", 88)
    leaderboard.add_score("Rekkles", 87)

    print("Top score:", leaderboard.top())  # Should print Faker with 95
    print("All scores:", leaderboard.get_all_scores())  # Should print scores in descending order

    print("Faker's score:", leaderboard.get_score("Faker"))  # Should print 95
    print("Rekkles' score:", leaderboard.get_score("Rekkles"))  # Should print 87
    leaderboard.remove_score("Lourlo")
    print("All scores after removing Lourlo:", leaderboard.get_all_scores())  # Lourlo should be removed
