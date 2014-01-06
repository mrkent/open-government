open-government
===============

Open source algorithmic government with voluntary participation



Background
----------

What some anarchists understand as a "government" in it's current state is an organization with a monopoly on force or violence. Regardless whether a government's actions are beneficial for society or to what degree violence is required for an orderly society, all power governments currently wield derives from this monopoly. If most people can agree that monopolies are generally bad for consumers (citizens in this case), then it’s at least rational to explore the possibility of competing governments with voluntary participation by citizens. 

Such a system has historically been difficult. Throughout history, governments are replaced by new ones when it becomes incapable managing its affairs, resulting in either domestic uprisings or foreign takeovers. These transitions are extremely expensive and rarely peaceful. The new regimes rarely give up the newfound, highly lucrative monopoly after fronting the cost of the revolution/war with their human or monetary capital. 

The American Revolution attempted to create a non-monopolistic government by limiting the government’s power with the Constitution (separating power between three branches of the government and granting high level of autonomy to states) and the Bill of Rights (granting individuals with inalienable* rights). The ever westward expansion further limited the government’s control of those seeking new opportunities or evading the government’s grasp. Coincidentally, the federal government’s power has grown increasingly after the last major westward migrations in the mid 1800’s. 

Given the size and opacity of governments today, it’s fair to say that no citizen knows everything his government does, much less agree with it. If there are any major disagreements, an average citizen has the following choices (in order of increasing cost):

1. Tolerate it - protesting would fall into this category too as it’s a low cost and low return proposition
2. Influence legislators to change or become one - legislators have limited time, not enough to give to ever average citizen; difficult to achieve and once achieved, one’s views may have changed
3. Exit - Relocate to a geographic location, possibly a different nation, which is expensive both in monetary and social capital
4. Forcefully implement change - as the cost is almost certain death if failed, this only becomes an achievable option when the other options are worse for a large portion of the population

We can perhaps model the history of governments with an overly simple Markov chain in which each state is a level of citizen satisfaction rate. State 0 is completely satisfied which we assume to be the case at the start of any new regime. States 1-4 correspond to above list. A state can only move up or down 1 step at a time, with exception to state 4 (on the edge of a rebellion), which can go to state 0 when the rebellion succeeds. Each arrow in the Markov chain indicate the probability of moving between states in each iteration. These transition probabilities were arbitrarily assigned while being reasonable and simple. We assign high values to all self-transitions except state 0 because governments generally stay the same. A fully satisfied population is rarely the case so we assigned state 0’s self-transition to be a low value (0.2). The transition from 1->0 and 4->3 are assigned 0 because there is no incentive and it’s beyond saving respectively. It’s clear that for the majority of the time (both in history and our model), we’d reside in either state 1 or 2. If this model is a reasonable approximation, then we can say that the role of governments are to stay in the lower states for as long as possible. We assume a government at state 2 is equally likely to change for better or for worse, while in state 3, the system has become more biased towards unsavory politicians. 

![alt text](http://i.imgur.com/9qjlo93.png "Government life cycle MC")

This Markov chain can be analyzed to make further conclusions about the society we’d live in. For example, an equilibrium distribution which represents the amount of time people spend in certain levels of satisfaction with their government can be calculated with the following python code. 

```python
>>> import numpy as np
>>> a = np.matrix('0.2 0.8 0 0 0; 0 0.9 0.1 0 0; 0 0.1 0.8 0.1 0; 0 0 0.1 0.6 0.3; 0.5 0 0 0 0.5')
>>> print a
[[ 0.2  0.8  0.   0.   0. ]
 [ 0.   0.9  0.1  0.   0. ]
 [ 0.   0.1  0.8  0.1  0. ]
 [ 0.   0.   0.1  0.7  0.2]
 [ 0.5  0.   0.   0.   0.5]]
>>> np.linalg.matrix_power(a,100)[0]
```

As previously claimed, most time will be spent in states 1 and 2. This model also predicts a total of over 15% of the time we can expect to live in states 3 and 4, representing very unfavorable conditions. And as most of us have lived in periods mostly considered state 1 and 2 that value may be surprising. Generating random walks using `randwalk.py` starting from state 1 and ending when reaching 0 or 20 iterations result in the following scenarios. In most cases, someone with experience of 20 time steps won’t experience state 3 or 4. 

```python
randwalk.py
```

Globalization and the internet have lower the cost of relocation and enabled easy global communication. The emergence cryptocurrencies now allows greater numbers of unsatisfied citizens to exit his nation state economically, although not necessarily physically. Together, these advancements may produce a significantly different Markov chain in the not-immediate-but-perhaps-foreseeable future, one without state 4 and the resulting period of despair. 

To take it one step further, suppose governments are completely transparent, taxes (or membership dues) are voluntary, and anyone can propose changes to his government for review (state 2). If the changes are quickly accepted, then citizens would only be briefly in state 2 before going back to state 1. Now suppose governments can be created at a trivial cost. A rejection of proposed change (or even a delayed decision) then either results in immediate exits, either to an existing competing government or new clone of the original with added updates. We effectively remove state 3 and dramatically alter governments willingness to change (in order to preserve citizenship and their voluntary tax contributions). 


To do
--------


