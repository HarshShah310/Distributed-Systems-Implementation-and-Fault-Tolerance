import threading
import random
import time


class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.vote = None
        self.transaction_info = None
        self.committed = False

    def prepare_vote(self, transaction_id):
        """Simulates the voting process during the prepare phase."""
        print(f"Node {self.node_id} is preparing to vote...")
        self.transaction_info = f"Transaction Info for {transaction_id}"
        self.vote = "YES" if random.random() < 0.75 else "NO"
        print(f"Node {self.node_id} votes {self.vote}")

    def commit_transaction(self):
        """Simulates the commit process."""
        if not self.committed:
            print(f"Node {self.node_id} is committing...")
            time.sleep(random.uniform(0.5, 1))
            self.committed = True
            print(f"Node {self.node_id} has committed.")

    def abort_transaction(self):
        """Simulates the abort process."""
        print(f"Node {self.node_id} has aborted.")

    def recover(self, transaction_id):
        """Simulates the recovery process after a failure."""
        if self.vote == "YES" and not self.committed:
            print(f"Node {self.node_id} is recovering and restoring transaction info...")
            if self.transaction_info:
                print(f"Node {self.node_id} has restored transaction info.")
        else:
            print(f"Node {self.node_id} had no recovery needs or did not vote YES.")


class TransactionCoordinator:
    def __init__(self):
        self.threads = []

    def initiate_prepare_phase(self, transaction_id, nodes):
        """Starts the prepare phase by initiating voting for all nodes."""
        print("\nStarting prepare phase...")
        for node in nodes:
            thread = threading.Thread(target=node.prepare_vote, args=(transaction_id,))
            thread.start()
            self.threads.append(thread)

        for thread in self.threads:
            thread.join()
        print("Prepare phase completed.")

    def finalize_commit_phase(self, nodes):
        """Finalizes the commit or abort process based on node votes."""
        print("\nFinalizing commit phase...")
        votes = [node.vote for node in nodes]
        print("Votes from all nodes:", votes)
        if "NO" not in votes:
            print("All nodes voted YES. Committing transaction...")
            for node in nodes:
                node.commit_transaction()
        else:
            print("At least one node voted NO. Aborting transaction...")
            for node in nodes:
                node.abort_transaction()


def run_simulation():
    """Simulates transaction management with recovery handling."""
    while True:
        print("\nOptions:")
        print("1. Simulate node recovery after failure.")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            # Initialize nodes and coordinator
            nodes = [Node(f"n{i}") for i in range(1, 3)]
            coordinator = TransactionCoordinator()
            transaction_id = "T1"

            # Simulate prepare phase
            coordinator.initiate_prepare_phase(transaction_id, nodes)

            # Simulate node failure and recovery
            print("Simulating node failure...")
            time.sleep(3)
            print("Recovering nodes...")
            for node in nodes:
                node.recover(transaction_id)

            # Finalize commit phase
            coordinator.finalize_commit_phase(nodes)

        elif choice == "2":
            print("Exiting simulation.")
            break
        else:
            print("Invalid choice. Please select again.")


if __name__ == "__main__":
    run_simulation()
