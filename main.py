import random
import time

class Ticket:
    def __init__(self, ticket_id, description, complexity):
        self.ticket_id = ticket_id
        self.description = description
        self.complexity = complexity # 1 (easy) to 3 (hard)
        self.status = "Open"
        self.current_level = 0 # 0: Initial, 1: L1, 2: L2, 3: L3

    def __str__(self):
        return (f"Ticket {self.ticket_id}: '{self.description}' (Complexity: {self.complexity}) "
                f"- Status: {self.status}, Current Level: L{self.current_level}")

def handle_ticket_at_level(ticket, level):
    ticket.current_level = level
    print(f"\n--- Handling Ticket {ticket.ticket_id} at Level {level} ---")
    print(f"Ticket Description: {ticket.description}")
    print(f"Current Status: {ticket.status}")

    # Simulate resolution attempt
    time.sleep(0.5) # Simulate work

    # Determine resolution chance based on level and complexity
    # Higher level has better chance, lower complexity is easier
    resolution_chance = {
        1: 0.8 if ticket.complexity == 1 else (0.4 if ticket.complexity == 2 else 0.1), # L1 good for easy, bad for hard
        2: 0.9 if ticket.complexity <= 2 else 0.5, # L2 good for easy/medium, okay for hard
        3: 0.95 # L3 (experts) can resolve almost anything
    }

    if random.random() < resolution_chance.get(level, 0):
        ticket.status = f"Resolved by L{level}"
        print(f"SUCCESS: Ticket {ticket.ticket_id} has been RESOLVED by Level {level} support.")
        return True
    else:
        print(f"FAILURE: Level {level} could not resolve Ticket {ticket.ticket_id}.")
        # --- This is where the escalation concept is demonstrated ---
        if level < 3: # Max escalation level is 3 in this simulation
            ticket.status = f"Escalated to L{level + 1}"
            print(f"ESCALATING: Ticket {ticket.ticket_id} is being escalated to Level {level + 1}.")
            return False # Indicate not resolved, needs escalation
        else:
            ticket.status = "Unresolved - Max Level Reached"
            print(f"CRITICAL: Ticket {ticket.ticket_id} could not be resolved even at the highest level (L{level}). Further action required.")
            return False

def main():
    print("--- Escalation Management Simulation ---")

    tickets = [
        Ticket(101, "Basic password reset request", 1), # Easy
        Ticket(102, "Software installation issue on new laptop", 2), # Medium
        Ticket(103, "Database connection pool exhaustion", 3), # Hard
        Ticket(104, "Printer not connecting to network", 1), # Easy
        Ticket(105, "Intermittent API timeout for critical service", 3) # Hard
    ]

    for ticket in tickets:
        print(f"\n--- Starting process for {ticket} ---")
        resolved = False
        current_level = 1
        while not resolved and current_level <= 3:
            resolved = handle_ticket_at_level(ticket, current_level)
            if not resolved:
                current_level += 1
            time.sleep(0.2) # Small delay between levels for readability

        print(f"\n--- Final Status for Ticket {ticket.ticket_id}: {ticket.status} ---")
        print("-" * 50)

if __name__ == "__main__":
    main()
