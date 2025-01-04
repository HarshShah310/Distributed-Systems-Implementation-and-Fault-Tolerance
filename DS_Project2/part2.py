import threading
import random
import time

class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.vote = None

    def prepare_vote(self, timeout=5):
        """
        Simulates the voting process during the prepare phase.
        Nodes may not respond or vote 'YES'/'NO'.
        """
        time.sleep(random.uniform(0.5, 2))  # Simulate response delay
        if random.random() < 0.2:  # Simulate non-response
            print(f"Node {self.node_id} did not respond in time.")
            self.vote = None
        else:
            self.vote = "YES" if random.random() < 0.75 else "NO"
            print(f"Node {self.node_id} votes {self.vote}")

    def commit_transaction(self):
        """Simulates the commit process for a node."""
        time.sleep(random.uniform(0.5, 1))  # Simulate commit delay
        print(f"Node {self.node_id} has committed the transaction.")

    def abort_transaction(self):
        """Simulates the abort process for a node."""
        print(f"Node {self.node_id} has aborted the transaction.")

class TransactionCoordinator:
    def __init__(self, nodes):
        self.nodes = nodes

    def initiate_prepare_phase(self):
        """
        Initiates the prepare phase where each node votes.
        Executes the voting in parallel using threads.
        """
        print("\nStarting prepare phase...")
        threads = []
        for node in self.nodes:
            thread = threading.Thread(target=node.prepare_vote)
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()  # Wait for all threads to finish
        print("Prepare phase completed.")

    def finalize_commit_phase(self):
        """
        Finalizes the transaction based on votes from the prepare phase.
        If all nodes vote 'YES', commits the transaction.
        Otherwise, aborts the transaction.
        """
        votes = [node.vote for node in self.nodes]
        print("\nVotes from all nodes:", votes)

        if None in votes:
            print("Coordinator did not receive all votes. Aborting transaction...")
            self._abort_all_nodes()
        elif "NO" in votes:
            print("At least one node voted NO. Aborting transaction...")
            self._abort_all_nodes()
        else:
            print("All nodes voted YES. Committing transaction...")
            self._commit_all_nodes()

    def _abort_all_nodes(self):
        """Helper method to abort the transaction for all nodes."""
        for node in self.nodes:
            node.abort_transaction()

    def _commit_all_nodes(self):
        """Helper method to commit the transaction for all nodes."""
        for node in self.nodes:
            node.commit_transaction()

def run_simulation():
    """
    Runs the simulation of the two-phase commit protocol.
    Creates nodes and coordinates their transaction process.
    """
    nodes = [Node("n1"), Node("n2")]
    coordinator = TransactionCoordinator(nodes)

    coordinator.initiate_prepare_phase()
    coordinator.finalize_commit_phase()

if __name__ == "__main__":
    run_simulation()
