---
layout: note
title:  "Hysteresis and the Markov Property"
date:   2023-12-01 16:13:00 -0500
modified_date: 2024-05-16 16:35:00 -0500
categories: math
---

![migrating](/images/husteros.png)

Hysteresis is informally defined as "dependence of the state of a system on its history." 

The Markov property is informally defined as "the future state of a system depends only on its present state."

So we have a proprty that we might say is memoryful, and another property that we might say is memoryless.

Does the Markov property preclude hysteresis? One would think so. I don't know if that's quite true though, because you can kind of abuse the concept of the Markov property by expanding your state. We can probably come up with some definition of "hysteresis-like" behavior that can be wedged in here. Maybe doing this, and seeing how and when things break down, will help us understand both concepts better, or maybe we'll enjoy a pleasant waste of time.

Suppose you have a set \\(S\\) of states, and you care about \\(n\\) timesteps in the past. Then clearly you can just create a new set of states \\(S' = S^n\\) and you've recovered the Markov property. It might be trivial, but I find it interesting that you can pay a (pretty steep) memory cost to work with a certain kind of model.

A common toy model of hysteresis is a thermostat in a room that controls a heater. The thermostat turns on when the temperature goes below the setpoint, and the thermostat turns off when the temperature goes above the setpoint. This is a recipe for rapid cycling, so generally there will be some sort of "deadband" such that the thermostat effectively has two setpoints -- a \\(T_{high}\\) and \\(T_{low}\\). Thus when the temperature is below the low setpoint, the heater turns on, until the temperature rises above the high setpoint, at which point the heater turns off.  So \\(S = \set{0, 1\}\\) here. Suppose we are at a temperature we'll call medium s.t. \\(T_{low}\\) < \\(T_{t}\\) < \\(T_{high}\\). Is the thermostat on or off? It's actually the case that

$$
\forall T_t \; s.t. T_{low} < T_t < T_{high},
$$
$$
s(T_t) = \begin{cases}
0 & \text{if } s(T_{t-1}) = 0 \\
1 & \text{if } s(T_{t-1}) = 1
\end{cases}
$$

If we do not know the previous state of the thermostat, we cannot determine the next state.

Hysteresis ref dump:
* [What is Hysteresis?](https://www.math.uwaterloo.ca/~kmorris/Preprints/Morris_hysteresis_final.pdf)
* *Microelectronic Circuits* Sedra & Smith (13.4.2-13.4.6ish, Schmitt triggers?)
* also *The Art of Electronics* Horowitz (4.3.2 B ?)
* *Differential Models of Hysteresis* Vistin, Augusto
* *Applications in Ecological Engineering* Jorgensen (applications to lake restoration)
