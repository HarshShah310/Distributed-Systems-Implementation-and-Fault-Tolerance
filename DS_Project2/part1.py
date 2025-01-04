import threading
import random
import time

class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.vote = None

    def prepare_vote(self, coordinator_failure):
        """Simulates the voting process during the prepare phase."""
        if coordinator_failure:
            print(f"Node {self.node_id} timed out due to coordinator failure.")
            self.vote = "NO"
        else:
            self.vote = "YES" if random.random() < 0.75 else "NO"
        print(f"Node {self.node_id} votes {self.vote}")

    def commit_transaction(self):
        """Simulates the commit process."""
        time.sleep(random.uniform(0.5, 1))
        print(f"Node {self.node_id} has committed.")

    def abort_transaction(self):
        """Simulates the abort process."""
        print(f"Node {self.node_id} has aborted.")

class TransactionCoordinator:
    def __init__(self, nodes):
        self.nodes = nodes
        self.failure_simulated = False

    def simulate_coordinator_failure(self):
        """Simulates coordinator failure before sending the prepare message."""
        print("\nCoordinator failed before sending prepare message.")
        self.failure_simulated = True
        time.sleep(5)  # Simulating downtime
        print("Coordinator has recovered.")

    def initiate_prepare_phase(self, coordinator_failure):
        """Initiates the prepare phase for all nodes."""
        if coordinator_failure and not self.failure_simulated:
            self.simulate_coordinator_failure()

        print("\nStarting prepare phase...")
        threads = [
            threading.Thread(target=node.prepare_vote, args=(coordinator_failure,))
            for node in self.nodes
        ]

        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()

        print("Prepare phase completed.")

    def finalize_commit_phase(self):
        """Finalizes the transaction by committing or aborting based on votes."""
        votes = [node.vote for node in self.nodes]
        print("\nVotes from all nodes:", votes)
        if "NO" not in votes:
            print("All nodes voted YES. Committing transaction...")
            for node in self.nodes:
                node.commit_transaction()
        else:
            print("At least one node voted NO. Aborting transaction...")
            for node in self.nodes:
                node.abort_transaction()

def run_simulation():
    """Runs the Two-Phase Commit protocol simulation."""
    while True:
        print("\nOptions:")
        print("1. Coordinator does not fail before sending prepare message.")
        print("2. Coordinator fails before sending prepare message.")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            nodes = [Node("n1"), Node("n2")]
            coordinator = TransactionCoordinator(nodes)
            coordinator.initiate_prepare_phase(coordinator_failure=False)
            coordinator.finalize_commit_phase()

        elif choice == "2":
            nodes = [Node("n1"), Node("n2")]
            coordinator = TransactionCoordinator(nodes)
            coordinator.initiate_prepare_phase(coordinator_failure=True)
            coordinator.finalize_commit_phase()

        elif choice == "3":
            print("Exiting simulation.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    run_simulation()
