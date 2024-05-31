---
layout: note
title:  "Trying AlphaZero on Some Combinatorial Games"
date:   2024-05-16 00:00:00 -0500
modified_date: 2024-05-31 13:30:00 -0500
categories: math,rl
---

One lazy thing to do when you want to try and learn a few things is to smash them all together. It is probably suboptimal but it is something of a time-saver. I had a desire to get familiar with Julia, to understand AlphaZero a little better, and to get familiar with some aspects of combinatorial games, so why not train a model to play a combinatorial game or two?

~~Current status: implemented a bad version of AlphaZero in Julia using the monkey-see-monkey-do method (monkey saw a tutorial+repo and a different Julia implementation). Working through some BatchNorm instability and figuring out if monkey did what monkey saw correctly. Will need to compare against the referenced existing implementations and troubleshoot. May wind up just using one of those two once I feel that I "get it."~~

~~Current status (5/30ish): Coming back to this after being busy w/ some work. Still figuring out what I am doing wrong w.r.t. BatchNorm. I'm thinking I did something stupid and obvious (only in retrospect of course). Going to use a canned library after some more wrestling as I am pretty eager to poke at the policies learned for some combinatorial games. I can always circle back to implementation.~~

5/31: Some lunchtime fiddling. Left this thing to run (on CPU...) last night while out. Seems to always be selecting k = 1 in the (modified) Euclid game I have set up. I might have implemented something wrong, but I have read that people have issues centered around finding the correct \\(c_{puct}\\) constant value. Going to let it rip with \\(c_{puct}\\) = 5 and see if that improves anything. Otherwise going to compare (again) what I implemented to one of those other libraries to see if that points me toward an answer (incl. re: BatchNorm instability). 

RL/Alphazero ref dump:
* [A Simple Alpha(Go) Zero Tutorial](https://suragnair.github.io/posts/alphazero.html)
* [AlphaZero.jl](https://github.com/jonathan-laurent/AlphaZero.jl)
* [Original AlphaZero paper](https://www.nature.com/articles/nature24270.epdf?author_access_token=VJXbVjaSHxFoctQQ4p2k4tRgN0jAjWel9jnR3ZoTv0PVW4gB86EEpGqTRDtpIz-2rmo8-KG06gqVobU5NSCFeHILHcVFUeMsbvwS-lxjqQGg98faovwjxeTUgZAUMnRQ)
* [Acquisition of Chess Knowledge in AlphaZero](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9704706/pdf/pnas.202206625.pdf)
* [Impartial Games: A Challenge for Reinforcement Learning](https://arxiv.org/abs/2205.12787)
* [Minimal and Clean Reinforcement Learning Examples](https://github.com/rlcode/reinforcement-learning/tree/master)
* [Reinforcement learning on the combinatorial game of Nim](https://www.csc.kth.se/utbildning/kth/kurser/DD143X/dkand11/Group6Lars/erik.jarleberg.report.pdf)

Combinatorial game ref dump:
* [Some Problems in Combinatorial Game Theory](https://www.mathcamp.org/files/math/Alfonso-CGT-handout.pdf)
* [A Game Based on the Euclidean Algorithm and A Winning Strategy for it](https://doi.org/10.2307/3612461)
* [Properties of a Game Based on Euclid's Algorithm](https://doi.org/10.2307/2689037)

Julia ref dump:
* [How to optimise Julia code: A practical guide](https://viralinstruction.com/posts/optimise/)
* [Flux.jl](https://fluxml.ai/Flux.jl/stable/)
