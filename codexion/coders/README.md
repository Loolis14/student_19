*This project has been created as part of the 42 curriculum by mmeurer*

# Description
# Instructions
# Blocking cases handled
# Threadsynchronization mechanisms
# Resources

https://youtu.be/VSkvwzqo-Pk

Thread : https://koor.fr/C/cthreads/Index.wp
https://man7.org/linux/man-pages/man3/pthread_create.3.html


Ce projet est tres relie a des concepts informatiques.

Vocabulaire:

Deadlock:
Un interblocage (deadlock) en informatique est une situation de blocage mutuel où deux ou plusieurs processus (ou transactions) attendent indéfiniment des ressources détenues les uns par les autres. Cela paralyse le système, car aucun processus ne peut progresser, nécessitant généralement une intervention externe comme l'arrêt d'une des tâches.

Starvation:
In computer science, resource starvation is a problem encountered in concurrent computing where a process is perpetually denied necessary resources to process its work. Starvation may be caused by errors in a scheduling or mutual exclusion algorithm, but can also be caused by resource leaks, and can be intentionally caused via a denial-of-service attack such as a fork bomb. 

Lifelock:
Livelock in computer science (CS) is a concurrency problem where two or more processes continuously change their states in response to each other without making any functional progress. Unlike deadlock, where processes are stuck waiting, in a livelock, the processes are actively running but trapped in an infinite, unproductive loop

Preemption:
In computer science,
preemptive refers to a type of scheduling or multitasking in an operating system (OS) where the system can forcibly interrupt a currently running task (process or thread) and switch the CPU to another task, without requiring the first task's cooperation.

Mutual Exclusion:
Mutual exclusion is a concurrency control property in computer science that ensures only one thread or process accesses a shared resource (such as memory, files, or devices) at a time. 

Coffman conditions : Conditions pour qu'un deadlock puisse se produire. Pour éviter le deadlock, il suffit d'empêcher l'une des conditions de se réaliser

EDF:
In Computer Science (CS),
EDF stands for Earliest Deadline First, a dynamic scheduling algorithm used in real-time operating systems. It prioritizes tasks with the closest deadline, ensuring optimal CPU utilization for periodic, independent tasks.

Sémaphores:
A semaphore is a synchronization primitive in computer science, specifically an atomic integer variable used to manage concurrent access to shared resources by multiple threads or processes. 

spurious wakeup:
A spurious wakeup occurs in multithreaded programming when a thread waiting on a condition variable wakes up without being signaled, interrupted, or timing out. While rare in user code, it is allowed by POSIX and C++ standards for performance reasons on multiprocessor systems.

Mesa semantics and hoare:
Hoare semantics (signal-and-wait) and Mesa semantics (signal-and-continue) differ primarily in how monitors handle signaling threads. Hoare immediately transfers the lock to the awakened thread, guaranteeing the condition is true. Mesa allows the signaler to keep the lock, meaning waiters must recheck conditions (often via while loops).

condition variable
Semaphores and condition variables build on top of the mutual exclusion provide by locks and are used for providing synchronized access to shared resources.

The Dining Philosopher Problem is a classic synchronization problem introduced by Edsger Dijkstra in 1965. It illustrates the challenges of resource sharing in concurrent programming, such as deadlock, starvation, and mutual exclusion.

Problem Statement

    K philosophers sit around a circular table.
    Each philosopher alternates between thinking and eating.
    There is one chopstick between each philosopher (total K chopsticks).
    A philosopher must pick up two chopsticks (left and right) to eat.
    Only one philosopher can use a chopstick at a time.

The challenge: Design a synchronization mechanism so that philosophers can eat without causing deadlock (all waiting forever) or starvation (some never get a chance to eat).

Issues in the Problem

    Deadlock: If every philosopher picks up their left chopstick first, no one can pick up the right one circular wait.
    Starvation: Some philosophers may never get a chance to eat if others keep eating.
    Concurrency Control: Must ensure no two adjacent philosophers eat simultaneously.

Semaphore Solution to Dining Philosopher

We use semaphores to manage chopsticks and avoid deadlock.
Algorithm

    Each chopstick is represented as a binary semaphore (mutex).
    Philosopher must acquire both left and right semaphores before eating.
    After eating, the philosopher releases both semaphores.

https://www.geeksforgeeks.org/operating-systems/dining-philosopher-problem-using-semaphores/

💥 Le danger sans mutex

👉 Ces deux actions peuvent arriver en même temps

Exemple :

Thread coder      → écrit last_compile
Thread monitor    → lit last_compile en même temps

💀 Résultat possible :

valeur corrompue
valeur partiellement écrite
lecture incohérente

👉 Ça s’appelle une data race

🎯 Règle ultra importante

👉 Dès que tu as :

une variable partagée
modifiée + lue
par plusieurs threads

➡️ 🔒 MUTEX OBLIGATOIRE