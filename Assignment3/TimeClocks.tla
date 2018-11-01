------------------------- MODULE TimeClocks ----------------------
(***************************************************************************)
(* Author: Shivasagar Boraiah (shivasagar.boraiah@stonybrook.edu)          *)
(* Credits: Lamport's PODC 2000 presenatation                              *)
(* TLA+ specification of Lamport's distributed mutual-exclusion algorithm  *)
(* that follows his exact implementation as he described in                *)
(* PODC 2000 TLA+ Tutorial, 16 July 2000                                   *)
(***************************************************************************)

EXTENDS Naturals, Sequences

(** Parameter Proc is a set of posibilities of process and parameter \ll **)
(***   describes the partial ordering of requests between two process   ***)
(*** and MaxClock keeps the limit on Clock value to itertate            ***)
CONSTANT Proc, _\ll_, MaxClock

(************** definition of partial ordering of process  ****************)
ASSUME  \A p \in Proc : /\ \neg p \ll p
                        /\ \A q \in Proc \ {p} : (p \ll  q) \/ (q \ll  p)
                        /\ \A q, r \in Proc : (p \ll q) /\ (q \ll r) => (p \ll r)
                        
(*************** definition of Total ordering of process  *****************)
a \prec b == \/ a.TS < b.TS 
             \/ (a.TS = b.TS) /\ (a.proc \ll b.proc) 

VARIABLES 
   state,       \* possible states to proceed for a process
   msgQ,        \* Queue of requests from one process to another
   reqSet,      \* set of all the requests of all the process
   clock,       \* local clock of each process
   lastTSent,   \* last request\ack\release send from a process
   lastTRcvd    \* last request\ack\release receioved from a process
   
vars == <<state, msgQ, reqSet, clock, lastTSent, lastTRcvd>>

(***************************************************************************)
(* The initialization of state predicate.                                  *)
(***************************************************************************) 
Init == /\ state = [p \in Proc |-> "idle"]
        /\ msgQ = [p \in Proc |-> [q \in Proc \ {p} |-> <<>>] ]
        /\ reqSet = [p \in Proc |-> {}]
        /\ clock \in [Proc -> 1..MaxClock]
        /\ lastTSent = [p \in Proc |-> [q \in Proc \ {p} |-> 0] ]
        /\ lastTRcvd = [p \in Proc |-> [q \in Proc \ {p} |-> 0] ]

(***************************************************************************)
(* Process p requests access to critical section by changing its state.    *)
(***************************************************************************)
Request(p) ==
  /\ state[p]= "idle" 
  /\ state' = [state EXCEPT ![p] = "waiting"]
  /\ \E n \in 1..MaxClock: 
        /\ clock' = [clock EXCEPT ![p] = n]
        /\ n > clock[p] (*random value, check for geeater than previous value*)
        /\ LET msg == [TS |-> n, proc |-> p, cmd |-> "acquire"]
            IN /\ msgQ' = [msgQ EXCEPT ![p] = [q \in Proc \ {p} |-> Append(@[q], msg)]]
               /\ reqSet' = [reqSet EXCEPT ![p]= @ \union {msg}]
        /\ lastTSent' = [lastTSent EXCEPT ![p] = [q \in Proc \ {p} |-> n]]
  /\ UNCHANGED <<lastTRcvd>>
 
(***************************************************************************)
(* Process p enters into critical section by changing its state.           *)
(***************************************************************************) 
Acquire(p) ==
        LET pReq == CHOOSE req \in reqSet[p] : req.proc = p
        IN  /\ state[p] = "waiting"
            /\ \A req \in reqSet[p] \ {pReq} : pReq \prec req
            /\ \A q \in Proc \ {p} : pReq \prec [TS |-> lastTRcvd[p][q] + 1, proc |-> q]
            /\ state' = [state EXCEPT ![p] = "owner"]
            /\ reqSet' =  [reqSet EXCEPT ![p] = @ \ {pReq}]
            /\ UNCHANGED <<msgQ, clock, lastTSent, lastTRcvd>>

(***************************************************************************)
(* Process p exit from the critical section and release the resource.      *)
(***************************************************************************)             
Release(p) ==
   /\ state[p]= "owner"
   /\ state' = [state EXCEPT ![p] = "idle"]
   /\ LET msg == [TS |-> clock[p], proc |-> p, cmd |-> "release"]
       IN msgQ' = [msgQ EXCEPT ![p] = [q \in Proc \ {p} |-> Append(@[q], msg)]]
   /\ lastTSent' = [lastTSent EXCEPT ![p]=[q \in Proc \ {p} |-> clock[p]]]
   /\ UNCHANGED <<clock, lastTRcvd, reqSet>>

(***************************************************************************)
(* Process p receives a msg from q and take action according to the state  *)
(***************************************************************************)                
RcvMsg(p, q) == 
    LET msg ==  Head(msgQ[q][p])
        msgQTail == [msgQ EXCEPT ![q][p] = Tail(@)] (* local varaible, masQTail, will update later*)
        ack == [TS |-> clock'[p], proc |-> p, cmd |-> "ack"]  (* mesage of ack*)
    IN  /\ msgQ[q][p] # << >>
        /\ clock' = [clock EXCEPT ![p] = IF msg.TS > @ THEN msg.TS ELSE @ ] 
        /\ IF /\ msg.cmd = "acquire"
              /\ [TS |-> lastTSent[p][q]+1, proc |-> p] \prec msg
                 THEN /\ msgQ' = [msgQTail EXCEPT ![p][q] = Append(@, ack)]
                      /\ lastTSent' = [lastTSent EXCEPT ![p][q] = clock'[p] ]
                 ELSE /\ msgQ' = msgQTail
                      /\ UNCHANGED lastTSent
        /\ lastTRcvd' = [lastTRcvd EXCEPT ![p][q] = msg.TS]
        /\ reqSet' = [reqSet EXCEPT ![p] = 
                            CASE msg.cmd = "acquire" -> @ \union {msg}
                                [] msg.cmd = "release" -> {m \in @ : m.proc # q}
                                [] msg.cmd = "ack" -> @ ]
        /\ UNCHANGED state

(***************************************************************************)
(* Clock increment for p when there is an event enabled and implied        *)
(***************************************************************************) 
Tick(p) == /\ \E n \in 1..MaxClock: /\ n > clock[p]
                             /\ clock' = [clock EXCEPT ![p] = n]
           /\ UNCHANGED <<state, msgQ, reqSet, lastTSent, lastTRcvd>>

(***************************************************************************)
(* Defining Next-state relation.                                           *)
(***************************************************************************)
Next == \E p \in Proc : \/ Request(p) \/ Acquire(p) \/ Release(p)
                        \/ \E q \in Proc \ {p} : RcvMsg(p, q)
                        \/ Tick(p)
                        
Liveness == \A p \in Proc: /\ WF_vars (Acquire(p))
                           /\ \A q \in Proc \ {p}: WF_vars (RcvMsg(p, q))
                           
(***************************************************************************)
(* Defining spec for next-state relation.                                  *)
(***************************************************************************)                           
Spec == Init /\ [][Next]_vars 

\***************************************************************************)
\* The main safety property of mutual exclusion.                           *)
\***************************************************************************)
EnsureSafety == \A p,q \in Proc: 
            (state[p] = "owner" /\ state[q] = "owner") => p = q

\***************************************************************************)
\* The main Liveness property of mutual exclusion.                         *)
\***************************************************************************)
EventualyAcquires == \A p \in Proc: (state[p] = "waiting") => <>(state[p] = "owner") 

========================================================================================