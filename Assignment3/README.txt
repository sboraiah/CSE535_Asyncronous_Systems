Assignment 3
Due: October 5, 2018
CSE535: Asyncronous Systems
Shivasagar Boraiah
#112077826
shivasagar.boraiah@stonybrook.edu



Q1.

======================================================================================================================================================================
                                |                                       |                                           |                                                |
 SPECIFICATIONS SUMMARY         |  LamportMutex.tla                     |            TimeClocks.tla                 |       MerzLamportMutex.tla                     |
                                |                                       |                                           |                                                |
======================================================================================================================================================================
                                |                                       |                                           |                                                |
Specification Size              |                90                     |                  70                       |                89                              |
                                |                                       |                                           |                                                |
======================================================================================================================================================================
                                |                                       |                                           |                                                |
Ease of Understanding           | 1. Comments in the code made          | 1.Comments and the presenation form PODC  | 1. Use of Sites and communicator as a network  |
                                |  made the understanding easy.         | 2000 helped me to ease through the code.  | differenciate this spec and make it diffcult.  |
                                | 2.ClockConstraint acts as termination | 2.taking a MaxClock as an input and       | 2. MaxClock is taken as an input to limt the   |
                                | condition to stop the program.        | iterating through it terminates the code. | code fall into infinite running.               |
                                |                                       |                                           |                                                |
======================================================================================================================================================================
                                | Lamport's five rules are followed.    | This is implemented exactly as PODC 2000. | Rules are implemeted in weired & difficult way |
                                | API List:                             | API List confirm, 5 rules are followed:   |API List:                                       |
Algorithm close to originality  | #1 Request(p), Broadcast(s, m)        | #1 Request(p) "idle" => "waiting"         | #1 start(self) "try" => "enter", broadcast(req)|
                                | #2 ReceiveAck(p, q), network(q, p)    | #2 RceMsg(p, q), handles the reqmsq using | #2 comm(self),append(reqQ), broadcast(ack)     |
                                |                                       |lastTRequest, lastTRelease and updates reqQ| #3 exit(self), "enter" => "free"               |
                                | #3 Exit(p), Broadcast(p, q)           | #3 Release(p) "acquire" => "idle"         | #4 comm(self), remove reqQ from the queue      |
                                | #4 ReceiveRelease(p, q),tail(q, p)    | #4 RecMsg(p, q) => handle acquire.        | #5 (a) p(state) = "crit" and p.TS < all(reqQ)  |
                                | #5(a) Beats(p, q), compare            | #5 (a) p.TS < all(Proc)                   | #5 (b) p has received all acks from its queue  |
                                | #5(b) network(p, q) check for all acks| #5 (b) lastTRecd > Current.TS             |    and has timestamps greater than its req.    |
                                |                                       |                                           |                                                |
======================================================================================================================================================================
                                |                                       |                                            |                                               |
Verifying Safety property       | 1. Safeness Validated.                | 1. Safety Validated.                       | 1. Safety Validated.                          |
                                | 2. Safety Check:                      | 2. Safety Check:                           | 2. Safety Check:                              |
                                | Mutex == \A p,q \in crit : p = q      | EnsureSafety == \A p,q \in Proc:           | EnsureSafety == \A s,t \in Sites :            |
                                |                                       | (state[p] = "owner" /\ state[q] = "owner") | pc[s] = "crit" /\ pc[t] = "crit" => s = t     |
                                |                                       |                                   => p = q |                                               |
======================================================================================================================================================================
                                |                                       |                                            |                                               |
                                | 1. Liveness Violated.                 | 1. Liveness Validated.                     | 1. Liveness Validated.                        |
Verifying Liveness property     | 2. Liveness Check:                    | 2. Liveness Check:                         | 2. Liveness Check:                            |
                                |EventualyAcquires == \A p \in Proc:    |EventualyAcquires == \A p \in Proc:         | EventuallyLive == \A s \in Sites :            |
                                |(state[p] = "waiting") => <>(state[p]  |(state[p] = "waiting") => <>(state[p]       |     pc[s] = "enter" ~> pc[s] = "crit"         |
                                |                            = "owner") |                                  = "owner")|                                               |
                                |                                       |                                            |                                               |
======================================================================================================================================================================


Q2.

PERFORMANCE SUMMARY:
Hardware: Mac OS X 10.13.6 x86_64, Oracle Corporation 1.8.0_181 x86_64
State Theorom Used: Breath First Search
While performing MutexInvariant, LivenessInvariant was unchecked and viceversa. As there was a termination condition for all three codes, Deadlock was uncheced all the time.

============================================================================================================================================================
                                |                  |               |             |              |               |            |        |        |           |
 LAMPORTMUTEX.TLA               |  Ease of Setting | No. Of Process|MaxClock Time|Execution Time|Mutex Violation|No. Of Nodes|Deadlock|Heap Mem|OffHeap Mem|
                                |                  |               |             |              |               |            |        |        |           |
============================================================================================================================================================
                                |                  |               |             |              |               |            |        |        |           |
                                |  2 Parameters    |         2     |       5     |   5512ms     |      No       |    1326    |  No    |  608MB |   1365MB  |
                                |                  |         2     |       6     |   6078ms     |      No       |    2001    |  No    |  608MB |   1365MB  |
                                |                  |         2     |       7     |   7078ms     |      No       |    2812    |  No    |  608MB |   1365MB  |
                                |                  |         2     |       8     |   7051ms     |      No       |    3759    |  No    |  608MB |   1365MB  |
MUTEX PROPERTY SUMMARY          |                  |         2     |       9     |   6789ms     |      No       |    4842    |  No    |  608MB |   1365MB  |
                                |                  |         2     |       10    |   5422ms     |      No       |    6061    |  No    |  608MB |   1365MB  |
                                |                  |         3     |       2     |   4658ms     |      No       |    2203    |  No    |  608MB |   1365MB  |
                                |                  |         3     |       3     |   9800ms     |      No       |    041K    |  No    |  608MB |   1365MB  |
                                |                  |         3     |       4     |   00011s     |      No       |    226K    |  No    |  608MB |   1365MB  |
                                |                  |         3     |       5     |   00016s     |      No       |   1033K    |  No    |  608MB |   1365MB  |
                                |                  |         4     |       2     |   00007s     |      No       |    68K     |  No    |  608MB |   1365MB  |
                                |                  |               |             |              |               |            |        |        |           |
============================================================================================================================================================
                                |                  |               |             |              |               |            |        |        |           |
 LAMPORT MUTEX.TLA              |  Ease of Setting | No. Of Process|MaxClock Time|Execution Time|Live Violation |No. Of Nodes|Deadlock|Heap Mem|OffHeap Mem|
                                |                  |               |             |              |               |            |        |        |           |
============================================================================================================================================================

                                |  2 Parameters    |         2     |       5     |   0001s      |    Yes        |    1326    |  No    |  608MB |   1365MB  |
                                |                  |         2     |       6     |   0003s      |    Yes        |    2001    |  No    |  608MB |   1365MB  |
                                |                  |         2     |       7     |   0002s      |    Yes        |    2812    |  No    |  608MB |   1365MB  |
                                |                  |         2     |       8     |   0003s      |    Yes        |    3759    |  No    |  608MB |   1365MB  |
LIVENESS PROPERTYSUMMARY        |                  |         2     |       9     |   0002s      |    Yes        |    4842    |  No    |  608MB |   1365MB  |
                                |                  |         2     |       10    |   0002s      |    Yes        |    6061    |  No    |  608MB |   1365MB  |
                                |                  |         3     |       2     |   0004s      |    Yes        |    2203    |  No    |  608MB |   1365MB  |
                                |                  |         3     |       3     |   0009s      |    Yes        |    41K     |  No    |  608MB |   1365MB  |
                                |                  |         3     |       4     |   0006s      |    Yes        |    105K    |  No    |  608MB |   1365MB  |
                                |                  |         3     |       5     |   0005s      |    Yes        |    134K    |  No    |  608MB |   1365MB  |
                                |                  |         4     |       2     |   0004s      |    Yes        |    68K     |  No    |  608MB |   1365MB  |
                                |                  |               |             |              |               |            |        |        |           |
============================================================================================================================================================
                                |                  |               |             |              |               |            |        |        |           |
 TIMECLOCKS.TLA                 |  Ease of Setting | No. Of Process|MaxClock Time|Execution Time|Mutex Violation|No. Of Nodes|Deadlock|Heap Mem|OffHeap Mem|
                                |                  |               |             |              |               |            |        |        |           |
============================================================================================================================================================
                                |                  |               |             |              |               |            |  No    |        |           |
                                |  3 Parametes     |      {1, 2}   |       5     |          6s  |      No       |    16K     |  No    | 608MB  |    1365MB |
                                |                  |      {1, 2}   |       6     |          8s  |      No       |    59K     |  No    | 608MB  |    1365MB |
                                |                  |      {1, 2}   |       7     |         14s  |      No       |   126K     |  No    | 608MB  |    1365MB |
                                |                  |      {1, 2}   |       8     |         14s  |      No       |   513K     |  No    | 608MB  |    1365MB |
MUTEX PROPERTY SUMMARY          |                  |      {1, 2}   |       9     |         19s  |      No       |  1285K     |  No    | 608MB  |    1365MB |
                                |                  |      {1, 2}   |      10     |         26s  |      No       |  2978K     |  No    | 608MB  |    1365MB |
                                |                  |      {2, 3}   |       2     |          6s  |      No       |     39     |  No    | 608MB  |    1365MB |
                                |                  |      {2, 3}   |       5     |          9s  |      No       |    16K     |  No    | 608MB  |    1365MB |
                                |                  |      {2, 3}   |       8     |         15s  |      No       |   513K     |  No    | 608MB  |    1365MB |
                                |                  |    {1, 2, 3}  |       2     |          7s  |      No       |   1056     |  No    | 608MB  |    1356K  |
                                |                  |    {1, 2, 3}  |       3     |          8s  |      No       |    75K     |  No    | 608MB  |    1356K  |
                                |                  |               |             |              |               |            |        |        |           |
============================================================================================================================================================
                                |                  |               |             |              |               |            |        |        |           |
 TIMECLOCKS.TLA                 |  Ease of Setting | No. Of Process|MaxClock Time|Execution Time| Live Violation|No. Of Nodes|Deadlock|Heap Mem|OffHeap Mem|
                                |                  |               |             |              |               |            |        |        |           |
============================================================================================================================================================
                                |                  |               |             |              |               |            |  No    |        |           |
                                |                  |               |             |              |               |            |  No    |        |           |
                                |  3 Parametes     |      {1, 2}   |       5     |          6s  |      No       |    16K     |  No    | 608MB  |    1365MB |
                                |                  |      {1, 2}   |       6     |          8s  |      No       |    59K     |  No    | 608MB  |    1365MB |
                                |                  |      {1, 2}   |       7     |         10s  |      No       |   186K     |  No    | 608MB  |    1365MB |
                                |                  |      {1, 2}   |       8     |         11s  |      No       |   513K     |  No    | 608MB  |    1365MB |
LIVENESS PROPERTY SUMMARY       |                  |      {1, 2}   |       9     |         13s  |      No       |  1285K     |  No    | 608MB  |    1365MB |
                                |                  |      {1, 2}   |      10     |         19s  |      No       |  2978K     |  No    | 608MB  |    1365MB |
                                |                  |      {2, 3}   |       2     |          5s  |      No       |     39     |  No    | 608MB  |    1365MB |
                                |                  |      {2, 3}   |       5     |          9s  |      No       |    16K     |  No    | 608MB  |    1365MB |
                                |                  |      {2, 3}   |       8     |         15s  |      No       |   513K     |  No    | 608MB  |    1365MB |
                                |                  |    {1, 2, 3}  |       2     |          7s  |      No       |   1056     |  No    | 608MB  |    1356K  |
                                |                  |    {1, 2, 3}  |       3     |          8s  |      No       |    75K     |  No    | 608MB  |    1356K  |
                                |                  |               |             |              |               |            |        |        |           |
============================================================================================================================================================
                                |                  |               |             |              |               |            |        |        |           |
 MERZLAMPORTMUTEX.TLA           |  Ease of Setting | No. Of Process|MaxClock Time|Execution Time|Mutex Violation|No. Of Nodes|Deadlock|Heap Mem|OffHeap Mem|
                                |                  |               |             |              |               |            |        |        |           |
============================================================================================================================================================
                                |  2 Parameters    |      2        |      5      |      5s      |      No       |     23K    |  No    | 608MB  |    1365MB |
                                |                  |      2        |      6      |      6s      |      No       |     43K    |  No    | 608MB  |    1365MB |
                                |                  |      2        |      7      |      6s      |      No       |     67K    |  No    | 608MB  |    1365MB |
                                |                  |      2        |      8      |      8s      |      No       |     95K    |  No    | 608MB  |    1365MB |
MUTEX PROPERTY SUMMARY          |                  |      2        |      9      |      8s      |      No       |    128K    |  No    | 608MB  |    1365MB |
                                |                  |      2        |      10     |      7s      |      No       |    164K    |  No    | 608MB  |    1365MB |
                                |                  |      3        |      2      |      6s      |      No       |     21K    |  No    | 608MB  |    1365MB |
                                |                  |      3        |      3      |     13s      |      No       |    578K    |  No    | 608MB  |    1365MB |
                                |                  |      3        |      4      |     89s      |      No       |   7763K    |  No    | 608MB  |    1365MB |
                                |                  |               |             |              |               |            |        |        |           |
============================================================================================================================================================
                                |                  |               |             |              |               |            |        |        |           |
 MERZLAMPORTMUTEX.TLA           |  Ease of Setting | No. Of Process|MaxClock Time|Execution Time|Live Violation |No. Of Nodes|Deadlock|Heap Mem|OffHeap Mem|
                                |                  |               |             |              |               |            |        |        |           |
============================================================================================================================================================
                                |  2 Parameters    |      2        |      5      |     10s      |      No       |     23K    |  No    | 608MB  |    1365MB |
                                |                  |      2        |      6      |     11s      |      No       |     43K    |  No    | 608MB  |    1365MB |
                                |                  |      2        |      7      |      6s      |      No       |     67K    |  No    | 608MB  |    1365MB |
                                |                  |      2        |      8      |     15s      |      No       |     95K    |  No    | 608MB  |    1365MB |
LIVENESS PROPERTY SUMMARY       |                  |      2        |      9      |     17s      |      No       |    128K    |  No    | 608MB  |    1365MB |
                                |                  |      2        |      10     |     23s      |      No       |    164K    |  No    | 608MB  |    1365MB |
                                |                  |      3        |      2      |     11s      |      No       |     21K    |  No    | 608MB  |    1365MB |
                                |                  |      3        |      3      |    114s      |      No       |    578K    |  No    | 608MB  |    1365MB |
                                |                  |      3        |      4      |     89s      |      No       |   7763K    |  No    | 608MB  |    1365MB |
                                |                  |               |             |              |               |            |        |        |           |
------------------------------------------------------------------------------------------------------------------------------------------------------------



**BONOUS ATTEMPT:
================

* Analysis of Lamport's variations of TLA code with Ricart Agrwala Algorithm.
* State formation in RA is less compared to Lamport's algorithm as there is a elimination of sending ACK every request.

(1) RICART AGRAWALA ALGORITHMM:
*Specification Size*: 166 lines (Omitting space and comments)
*Ease of Understanding*: As the code comes with a lot of comments it was easy to understand the code.
*Algorithm closeness to originality*: As the Algorithm is different from Lamport's,It follows exactly RA algorthm.
*Mutex Property*: Code is Safe. Safety Check: Invariant ==   \A i \in SITES: \A j \in SITES : i \in cs /\ i # j => j \notin cs
*Liveness Property*: Code violates Liveness. Check: Liveness == \A s \in SITES: SF_var(Choose_a_sequence_number(s))
*Comments*: Code has followed the RA Algorithm and used lot of unncessary variables, will try to update the modified version into my github.

(2) RICART AGRAWALA TOKEN BASED ALGORITHMM:
*Specification Size*: 166 lines (Omitting space and comments)
*Ease of Understanding*: Understanding was difficulty as I need revist my kmnown facts about the algorithm and code followes site-communication format.
*Algorithm closeness to originality*: As the Algorithm is different from Lamport's,It follows exactly RAT algorthm.
*Mutex Property*: Code violates Safe. Safety Check: Mutex == \A s,t \in Sites : pc[s] = "crit" /\ pc[t] = "crit" => s = t
*Liveness Property*: Code violates Liveness. Check: EventuallyLive == \A p \in Sites : <>(pc[p] = "crit")
*Comments*: Code lagged liveness property check. added, updated and verified.


PERORMANCE ANALYSIS OF 5 ALGORITHMS:
-----------------------------------
================================================================================================================================
              |             |                          MUTEX PERFORMANCE COMPARISON TABLE                                      |
No. Of Process|MaxClock Time|===================================================================================================
              |             |   LAMPORTMUTEX    |     TIME CLOCK   |        MERZ       |   RICARTAGRAWALA  |RICARTAGRAWALATOKEN|
              |             |   Time   | Nodes  |  Time   | Nodes  |   Time   | Nodes  |   Time   | Nodes  |   Time   | Nodes  |
================================================================================================================================
        2     |       5     |   5512ms | 1326   |   6s    |   16K  |    5s    |   23K  |    5s    |  560   |   2s    |   23K   |
        2     |       6     |   6078ms | 2001   |   8s    |   59K  |    6s    |   43K  |    6s    |  648   |   2s    |   23K   |
        2     |       7     |   7078ms | 2812   |  14s    |  186K  |    6s    |   67K  |    6s    |  736   |   2s    |   22.8K |
        2     |       8     |   7051ms | 3759   |  14s    |  513K  |    8s    |   95K  |    5s    |  824   |   2s    |   22.9K |
        2     |       9     |   6789ms | 4842   |  19s    | 1285K  |    8s    |  128K  |    5s    |  912   |   2s    |   22.9K |
        2     |       10    |   5422ms | 6061   |  26s    | 2978K  |    7s    |  164K  |    7s    | 1000   |   3s    |   23.1K |
        3     |       2     |   4658ms | 2203   |   6s    |    39  |    6s    |   21K  |    4s    |  296   |   4s    |   125K  |
        3     |       3     |   9800ms | 041K   |   9s    |   16K  |   13s    |  578K  |    5s    |  384   |  30s    |   919K  |
        3     |       4     |   00011s | 226K   |  15s    |  513K  |   89s    | 7763K  |    6s    |  472   |  31s    |   921K  |
              |             |          |        |         |        |          |        |          |        |         |         |
================================================================================================================================


================================================================================================================================
              |             |                          LIVENESS PERFORMANCE COMPARISON TABLE                                   |
No. Of Process|MaxClock Time|===================================================================================================
              |             |   LAMPORTMUTEX    |     TIME CLOCK   |        MERZ       |   RICARTAGRAWALA  |RICARTAGRAWALATOKEN|
              |             |   Time   | Nodes  |  Time   | Nodes  |   Time   | Nodes  |   Time   | Nodes  |   Time   | Nodes  |
================================================================================================================================
        2     |       5     |  1s      | 1326   |   6s    |   16K  |   10s    |   23K  |    2s    |  560   |   5s    |   27K   |
        2     |       6     |  3s      | 2001   |   8s    |   59K  |   11s    |   43K  |    2s    |  648   |   5s    |   27K   |
        2     |       7     |  2s      | 2812   |  10s    |  186K  |    6s    |   67K  |    1s    |  736   |   4s    |   27.6K |
        2     |       8     |  3s      | 3759   |  11s    |  513K  |   15s    |   95K  |    1s    |  824   |   4s    |   27.9K |
        2     |       9     |  2s      | 4842   |  13s    | 1285K  |   17s    |  128K  |    1s    |  912   |   4s    |   27.9K |
        2     |       10    |  2s      | 6061   |  19s    | 2978K  |   23s    |  164K  |    1s    | 1000   |   3s    |   27.3K |
        3     |       2     |  4s      | 2203   |   5s    |    39  |   11s    |   21K  |    1s    |  296   |   7s    |   77K   |
        3     |       3     |  9s      | 41K    |   9s    |   16K  |  114s    |  578K  |    1s    |  384   |   6s    |   71K   |
        3     |       4     |  6s      | 105K   |  15s    |  513K  |   89s    | 7763K  |    1s    |  472   |   4s    |   67K   |
================================================================================================================================



ACKNOLEDGMENT:
==============
1. Discused the MerzImplementation with Akanksha Mahajan.
2. Thanks to Weituo for RA Algorithm summary in his Github code: https://github.com/weituo12321/Asynchronous_Systems/blob/master/Week3%20Distributed%20mutex%20specifications/rats.tla

