---
layout: note
title:  "Putzing and Barto"
date:   2023-09-03 00:00:00 -0500
modified_date: 2024-05-17 13:50:00 -0500
categories: rl
---

<video controls>
<source src="/images/mylittleracecar.mp4" type="video/mp4">
</video>

The mission to dredge up scattered scratchwork continues. This note is a dump of some meanderings through Sutton and Barto, which I haven't touched in a while (since August/September 2023 based on file modified dates, and this sentence is being written May 17th 2024).

I made it to the end of Chapter 5, though I'll need to refresh my memory on most of the topics here (hopefully via practice). I'll try to flesh out this page as I revisit bits of code and exercises.

For now, I'm trying to go for vague recollections and impressions:
* I remember feeling like this book was verbose. I think the intent of all the yapping is to set up motivation for the methods, but a lot of the time I felt that I should be presented with the math and the algorithms. It might just be because I had my nose in a lot of "definition-theorem-proof" type texts at the time and was getting use to that style. There are costs and benefits to both.
* I like the attention paid to the history of the field in the opening chapter. I am not in the think of the field, but I always get the impression that a lot of the people involved in e.g. deep RL don't have a lot of contact with the control theory or applied mathematics literature, with the exception of learning theory people that seem to be in a bit of a bubble and some optimization-heads that quietly work behind the curtains. A lot of modern machine learning research as a whole feels really ahistorical to me in a way that is hard to put my finger on.
* Perhaps a logical conclusion of 1 and 2, I recall wanting to shift to other texts and viewpoints like Bertsekas's book(s).
* There's a general tension in technical books between getting the interested reader into the action as soon as possible and cultivating a deep feeling of understanding. Despite my previous comments, I appreciate how hard writing these things are and would never claim to do any better. This book feels like the former. I think most people in the field like the former approach. I have some character defects that make me always prefer the latter, which is rough, as I am not particularly "formally gifted."
* Given how many RL papers I've seen feel the need to restate the definition of an MDP or other basic notions from the field, I question whether people who want to get into the thick of things need to start with a book like this at all. They might be better served jumping into papers ASAP and then backtracking to reference material when needed, especially if they are adept programmers.
* Implementing many exercises in Python led to some loss of speed. In some cases I probably didn't take full advantage of numpy, in other places I think there were unavoidable loops. I wound up writing a good deal of Cython, and despite my interest in Julia, I think a stupid simple move like this is fine for most learners who want to stick with the snake. If I did it over again I might just stick to something like C or C++ and only bother with another language for spitting out a graph or two. I'm not sure. It depends on if you think "writing fast Python" or "writing fast code" is a good additional goal or if you think it distracts from the RL content. Different strokes.
* I enjoyed the exercises. A good mix of conceptual questions and programming exercises. The popularity of the book and the culture of software work well together for self-study, as you are guaranteed to find many, many repos online where you can check your work against others. I think Sutton has solutions to some exercises online as well (but maybe only for the 1st edition?).

Text
* *Reinforcement Learning* Sutton and Barto