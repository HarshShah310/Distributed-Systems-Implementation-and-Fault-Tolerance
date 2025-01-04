import threading
import time
import os

class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.state = "INIT"

    def commit_transaction(self):
        """Simulate the commit process."""
        self.state = "COMMITTED"
        print(f"Node {self.node_id} has committed.")

class TransactionCoordinator:
    def __init__(self, nodes):
        self.nodes = nodes
        self.log_file = "tc_log.txt"
        self.recovered_commit_nodes = []

    def log_transaction(self, message):
        """Log the transaction state to a file."""
        with open(self.log_file, "a") as log:
            log.write(message + "\n")

    def recover(self):
        """Recover the transaction state from the log file."""
        if os.path.exists(self.log_file):
            with open(self.log_file, "r") as log:
                for line in log:
                    if "commit" in line:
                        node_id = line.strip().split()[-1]
                        self.recovered_commit_nodes.append(node_id)
            print(f"Recovered committed nodes: {self.recovered_commit_nodes}")

    def finalize_commit_phase(self):
        """Send the commit message to all nodes."""
        for node in self.nodes:
            if node.node_id not in self.recovered_commit_nodes:
                self.log_transaction(f"commit {node.node_id}")
                node.commit_transaction()

def run_simulation():
    """Simulate the coordinator's commit process with failure and recovery."""
    # Create nodes
    nodes = [Node("n1"), Node("n2")]
    coordinator = TransactionCoordinator(nodes)

    # Begin the first commit phase
    print("\nCoordinator begins commit phase.")
    coordinator.log_transaction(f"commit {nodes[0].node_id}")
    nodes[0].commit_transaction()

    # Simulate coordinator failure
    print("\nCoordinator fails after sending one commit message.")
    time.sleep(5)

    # Recovery phase
    print("Coordinator recovers.")
    coordinator.recover()
    time.sleep(2)

    # Finalize the commit phase
    print("\nCoordinator finalizes commit phase.")
    coordinator.finalize_commit_phase()

if __name__ == "__main__":
    run_simulation()
