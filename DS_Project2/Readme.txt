Team Members:
Harsh Shah- 1002057387
Vashishth Gajjar- 1002160256

The project consists of four parts, each demonstrating different aspects of a voting or transactional system involving participants (voters) and a coordinator. Here's a brief summary of each part:

Part 1: Coordinator Failure Before Prepare Phase

Demonstrates a coordinator failure before it sends the prepare message.
Highlights the ability of the system to recover after the coordinator comes back online.

Part 2: Node Non-Response Simulation

Introduces potential non-responses from nodes during the prepare phase.
Simulates scenarios where nodes may fail to respond within a timeout or vote "NO", prompting the coordinator to abort the transaction.

Part 3: Coordinator Recovery with Log Persistence

Focuses on coordinator failure after sending some commit messages.
Introduces persistent logging to ensure that, upon recovery, the coordinator can commit or abort transactions based on the state saved in the log.

Part 4: Node Recovery After Failure

Simulates node failures and their ability to recover transaction state upon rejoining.
Shows how nodes restore their transaction information if they voted "YES" but had not yet committed.

Project Structure

part1.py: Simulates coordinator failure before the prepare phase and recovery.
part2.py: Introduces node non-responses and how the coordinator handles timeouts and votes.
part3.py: Implements coordinator recovery with persistent logs to ensure the state is restored after a failure.
part4.py: Demonstrates node recovery, showing how nodes retrieve their transaction state after a failure.


Instructions to Run the Code:

Unzip the folder.
Run the files for each part (part1.py, part2.py, part3.py, part4.py). i.e. python part1.py
For parts 1 and 4, select options provided to run test cases.
For parts 2 and 3, the output will be generated automatically.
Select 'exit' options in parts 1 and 4 to exit the programs.
