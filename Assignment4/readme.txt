Assignment 4
Due: October 22, 2018
CSE535: Asyncronous Systems
Name: Shivasagar Boraiah
Mail: shivasagar.boraiah@stonybrook.edu


Q1:
(1)
(*) While explaining eventual liveness, Algorithm never considers the action of proposers. The Algorithm only says that, eventual liveness will be acheived when acceptor eventually chooses a value and learner eventually learn a value whereas the actions of proposers have been ignored.
(*) When a proposer proposes lower value and sleeps for more that half of the time and eventually wakes up before the consensus and will have to wait for infinite time unless time out has been specified.

(2)
(*) Adding Timeout and Preemption:
(*) Page 9 of Paxos made simple: Choosing one leader amongst proposer.
(*) Inducing Proposal Timeout (as parameter: tp in our program): forces Proposer to start new round with higher value.
(*) Increasing Learner Timeout (as parameter: tl in our program): helps learner to wait for more time before terminating if message from acceptor is stuck in any delay.
(*) Introducing network delay(as parameter: d in our program): due to delay proposeer will be forced to increase the timeout value


Q2:
==
(1)
(*) Due to segregation of state information at at acceptors and leaders which will be replicated and once all the slots to replicate will be filled, the new round will be initiated which is a major drawback of MultiPaxos as it reduces the performance by restarting and loosing all the information.

(2)
(*) Solution for the state issue is that, the acceptor and leader can take a replica slot for which they propose and accept and once the half of the replicas are learnt then they can withdraw/remove the solt and free up for upcoming values.

Q3:
==
(1)

(*) Correctness Testing:
	1. Agreement == Only one value has been decided (Implemeted using Driver)
	2. Validity == Values proposed by proposer has been learned (Implemeted using Driver)
    3. Termination == Onlyu one value has been learnt (Implemented using Driver)


(*) Running times {CPU, Elapsed, StandardDeviation} have been measured and ploted for different vaiation of {Lossrate, Delay, Waittime}.

cpu time for both program is nearly equal in all cases
For Message loss : As message loss increase, basic paxos takes more elapsed time whereas preempt paxos performs better and its elapsed time is nearly equal to cpu time.

For Message delay : As message delays increases, basic paxos takes more elapsed time whereas preempt paxos elapsed time is less.
	           whereas for lower message delay values, preempt paxos elapsed time is more than basic paxos.

For Wait time : For lower wait delays, both programs have equal elapsed time. But as wait increases, preempt paxos performs better and its elapsed time is 
		nearly equal to cpu time whereas. 


(*) Implemnetation:
========

Please check the directory fopr graohs
Sample Input:
Shivasagars-MacBook-Pro:A4-5 shivasagar$ python -m da mainpaxos_new.da 3 2 2 10 .2 5 5 1 10



Sample Output:

Shivasagars-MacBook-Pro:A4-5 shivasagar$ 
Shivasagars-MacBook-Pro:A4-5 shivasagar$ 
Shivasagars-MacBook-Pro:A4-5 shivasagar$ python -m da mainpaxos_new.da 3 2 2 10 .2 5 5 1 10
mainpaxos_new.da:214:91: SyntaxError:                 proposers = new(algorithm.Proposer, (acceptors, monitor, ntp, 0 nDelayValue, nwaitValue), num= nproposers)
ImportError: Unable to compile mainpaxos_new.da, errno: 1
Shivasagars-MacBook-Pro:A4-5 shivasagar$ python -m da mainpaxos_new.da 3 2 2 10 .2 5 5 1 10
mainpaxos_new.da compiled with 0 errors and 0 warnings.
Written compiled file mainpaxos_new.py.
[430] da.api<MainProcess>:INFO: <Node_:75c01> initialized at 127.0.0.1:(UdpTransport=29521, TcpTransport=27079).
[430] da.api<MainProcess>:INFO: Starting program <module 'mainpaxos_new' from '/Users/shivasagar/Desktop/CSE535/A4-5/mainpaxos_new.py'>...
[430] da.api<MainProcess>:INFO: Running iteration 1 ...
[431] da.api<MainProcess>:INFO: Waiting for remaining child processes to terminate...(Press "Ctrl-C" to force kill)
mkdir: ./loss_results: File exists
[663] mainpaxos_new.Node_<Node_:75c01>:OUTPUT: LOSSRATE VARIATION <module 'test_bpaxos' from '/Users/shivasagar/Desktop/CSE535/A4-5/test_bpaxos.py'>


LOSSRATE VARIATION v/s MEAN CPU TIME {0.0: 0.00603, 0.05: 0.00652, 0.1: 0.00824, 0.15: 0.00816, 0.2: 0.00848}
LOSSRATE VARIATION v/s MEAN ELAPSED TIME {0.0: 0.61468, 0.05: 0.21473, 0.1: 1.91845, 0.15: 1.51811, 0.2: 1.31803}
STANDARD DEVIATION OF CPU TIME {0.0: 0.01836, 0.05: 0.01917, 0.1: 0.02171, 0.15: 0.02245, 0.2: 0.02311}
STANDARD DEVIATION OF ELAPSED TIME {0.0: 1.80682, 0.05: 1.49156, 0.1: 4.97491, 0.15: 5.08249, 0.2: 4.94392}


[64604] mainpaxos_new.Node_<Node_:75c01>:OUTPUT: LOSSRATE VARIATION <module 'preempt_paxos' from '/Users/shivasagar/Desktop/CSE535/A4-5/preempt_paxos.py'>


LOSSRATE VARIATION v/s MEAN CPU TIME {0.0: 0.00856, 0.05: 0.00914, 0.1: 0.01037, 0.15: 0.01037, 0.2: 0.01069}
LOSSRATE VARIATION v/s MEAN ELAPSED TIME {0.0: 0.31535, 0.05: 0.51661, 0.1: 1.51935, 0.15: 1.31982, 0.2: 1.41854}
STANDARD DEVIATION OF CPU TIME {0.0: 0.02631, 0.05: 0.02632, 0.1: 0.02763, 0.15: 0.02823, 0.2: 0.02889}
STANDARD DEVIATION OF ELAPSED TIME {0.0: 0.88826, 0.05: 1.4085, 0.1: 3.98554, 0.15: 4.16821, 0.2: 4.20514}


mkdir: ./delay_results: File exists
[123668] mainpaxos_new.Node_<Node_:75c01>:OUTPUT: DELAY VARIATION <module 'test_bpaxos' from '/Users/shivasagar/Desktop/CSE535/A4-5/test_bpaxos.py'>


DELAY VARIATION v/s MEAN CPU TIME {0.0: 0.00919, 1.25: 0.01069, 2.5: 0.01071, 3.75: 0.01157, 5.0: 0.01237}
DELAY VARIATION v/s MEAN ELAPSED TIME {0.0: 0.01353, 1.25: 0.21457, 2.5: 0.41519, 3.75: 1.31667, 5.0: 1.1168}
STANDARD DEVIATION OF CPU TIME {0.0: 0.02811, 1.25: 0.03017, 2.5: 0.03064, 3.75: 0.03157, 5.0: 0.03279}
STANDARD DEVIATION OF ELAPSED TIME {0.0: 0.04178, 1.25: 0.70617, 2.5: 1.17237, 3.75: 3.86791, 5.0: 3.83909}


[162587] mainpaxos_new.Node_<Node_:75c01>:OUTPUT: DELAY VARIATION <module 'preempt_paxos' from '/Users/shivasagar/Desktop/CSE535/A4-5/preempt_paxos.py'>


DELAY VARIATION v/s MEAN CPU TIME {0.0: 0.01102, 1.25: 0.01204, 2.5: 0.01447, 3.75: 0.01269, 5.0: 0.01383}
DELAY VARIATION v/s MEAN ELAPSED TIME {0.0: 0.01519, 1.25: 0.11598, 2.5: 0.42513, 3.75: 0.516, 5.0: 1.11777}
STANDARD DEVIATION OF CPU TIME {0.0: 0.0329, 1.25: 0.03321, 2.5: 0.03614, 3.75: 0.0363, 5.0: 0.03719}
STANDARD DEVIATION OF ELAPSED TIME {0.0: 0.04528, 1.25: 0.33209, 2.5: 0.77883, 3.75: 1.53702, 5.0: 2.77277}


mkdir: ./waittime_results: File exists
[192893] mainpaxos_new.Node_<Node_:75c01>:OUTPUT: WAITIME VARIATION <module 'test_bpaxos' from '/Users/shivasagar/Desktop/CSE535/A4-5/test_bpaxos.py'>


WAITTIME VARIATION v/s MEAN CPU TIME {0.0: 0.0166, 1.25: 0.01337, 2.5: 0.01342, 3.75: 0.01376, 5.0: 0.01404}
WAITTIME VARIATION v/s ELAPSED CPU TIME {0.0: 0.02789, 1.25: 0.01649, 2.5: 0.01627, 3.75: 0.01648, 5.0: 0.01636}
STANDARD DEVIATION OF CPU TIME {0.0: 0.0502, 1.25: 0.04542, 2.5: 0.04309, 3.75: 0.04224, 5.0: 0.04201}
STANDARD DEVIATION OF ELAPSED TIME {0.0: 0.08424, 1.25: 0.07761, 2.5: 0.07041, 3.75: 0.06589, 5.0: 0.06313}


[202039] mainpaxos_new.Node_<Node_:75c01>:OUTPUT: WAITIME VARIATION <module 'preempt_paxos' from '/Users/shivasagar/Desktop/CSE535/A4-5/preempt_paxos.py'>


WAITTIME VARIATION v/s MEAN CPU TIME {0.0: 0.02299, 1.25: 0.01539, 2.5: 0.01631, 3.75: 0.01578, 5.0: 0.01636}
WAITTIME VARIATION v/s ELAPSED CPU TIME {0.0: 0.07574, 1.25: 0.02012, 2.5: 0.02084, 3.75: 0.01806, 5.0: 0.01962}
STANDARD DEVIATION OF CPU TIME {0.0: 0.06973, 1.25: 0.06102, 2.5: 0.05719, 3.75: 0.05452, 5.0: 0.05306}
STANDARD DEVIATION OF ELAPSED TIME {0.0: 0.24556, 1.25: 0.23671, 2.5: 0.20768, 3.75: 0.18781, 5.0: 0.17245}


[212073] da.api<MainProcess>:INFO: Main process terminated.
Shivasagars-MacBook-Pro:A4-5 shivasagar$ Shivasagars-MacBook



