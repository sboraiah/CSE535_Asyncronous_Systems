
ASSIGNMENT 2
CSE535: ASYNCRONOUS SYSTEMS
SHIVASAGAR BORAIAH #112077826
shivasagar.boraiah@stonybrook.edu

NOTE: To run the programming files, python version greater than 3.6.5 and DistAlgo version 1.1.0b12 is required


Q1.
* Use random.choice() to randomly pickup the LC(logical clock value within nrequests) and run the methods (request(), critical_section(), release()).
* File lamport_algorithm.da has a detailed algorithm explanation with comments.
* Sample command to run the file:
                                python -m da lamport_algorithm.da p r
                                where,
                                      p = number of processes
                                      r = number of requests


Q2.
* Saftey Violation:
 ===================


                                                                P0                                                P1
                                                            request(1)--->         				   .
                                                            request(2)--->					   .
                     [req(0-7) of P0 are delayed]           request(3)--->					   .
                                                            request(4)--->					   .
                                                            request(5)--->					   .
                                                            request(6)--->					   .
                                                            request(7)--->					   .
                    [P0 assumes all messages are received
                             as it receives ack at Tm, 9]                                                         
                                                 
                                 			    request(8)------------------------------------------->
														[req(8) of P0 received at P1]
                                                                                                        
												      <---request(8)
														[req(7) of P1 is delayed]

                                                                      <----------------------------------------ack(9)   [as pid(p0) < pid(p1), P1 sends ack]
                                [ack(P1) received at 9]

                                                             ================P0 enters CS with req(8)=================

                                                            release(10)------------------------------------------>
                                                                                                                  [release(10) is received at P1]
												                  [P1 assumes its request messages are received
                             									                 as it receives release (heighest Tm) at Tm, 10]

                                [as P0 has heighest Time t(9)
                                from P1, P0 enters CS with t(0)]
                                                            						           [as P1 has heighest Time t(10)
                                                            							    from P0, P1 enters CS with t(8)]

                               						
									 =======P0 enters CS with T(0)==========
                                                   			 =======P1 enters CS with T(8)==========

                                                     				   {SAFETY VIOLATED}


* Deadlock Violation:
  ==================
     According to the rule 4 of Lamport's Algorithm, every process has a freedom to remove ANY-ONE request in the queue. Because of this randomness in the rules, P0 might end up waiting for the ACK of removed request from P1, wheras, P1 might also wait for the removed ACK from P0. This will make process to starve and leads to Deadlock.


Q3.

* Correctness testing:
  Even though I have not done for corectness of algorithm. From my understanding of the algorithms, I print the following.
  As Algorithm {orig.da} and {spec.da} is in accordance with correctess, they result in a boolean of 0 for {safety, liveliness, fairness}
  Algorithm {Q1.da} generates deadlock for large inputs, gets timeout(1) and outputs boolean of 1 for {safety, liveliness, fairness}
  Assumption: Due to the random behavior and rules of Lamport, verification for deadlock can also verify for safety.


* Performance testing:
  Output of performance has been recorded in output.txt that evaluates the three algoritms {Q1.da, orig.da, spec.da}
  Performance metrices: average_elapsed_time, average_CPU_time for a given {nprocs, nreqs, nparamenters} with {nrepetations}
  Input: p r n d a
  Output: Table for random set of requests and process [(p/d) and (r/d) set] and their average CPU and elapsed time run over "a" repetations.

   Sample command to run:
                         python -m da main.da 10 20 1 5 1

  Sample output:

          Shivasagars-MacBook-Pro:CSE535-A2-112077826 shivasagar$ python -m da main.da 10 10 1 5 2
     [46] da.api<MainProcess>:INFO: <Node_:63401> initialized at 127.0.0.1:(UdpTransport=16174, TcpTransport=24949).
     [46] da.api<MainProcess>:INFO: Starting program <module 'main' from '/Users/shivasagar/Desktop/CSE535/CSE535-A2-112077826/main.py'>...
     [47] da.api<MainProcess>:INFO: Running iteration 1 ...
     [47] da.api<MainProcess>:INFO: Waiting for remaining child processes to terminate...(Press "Ctrl-C" to force kill)
     ---------------------------------------------------------------
     nrepetations: 1 nparameter: 5 Orig.da
     ---------------------------------------------------------------
     Varying Requests
     ---------------------------------------------------------------
     process: 10 requests: 2 avg_elapsed: 0.030065 avg_cpu: 0.084534

     process: 10 requests: 4 avg_elapsed: 0.052420 avg_cpu: 0.149790

     process: 10 requests: 6 avg_elapsed: 0.076091 avg_cpu: 0.217163

    process: 10 requests: 8 avg_elapsed: 0.098583 avg_cpu: 0.278240

    process: 10 requests: 10 avg_elapsed: 0.129533 avg_cpu: 0.365539






ACKNOWLEDMENT:
============
* Discussed problem three with Raveendra Soori.
* Took hints from the Q&A group.

