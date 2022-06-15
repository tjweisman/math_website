% Let it ride!

<div class="center-title">Who gets it in? AUSTIN!</div>

##### Optimal strategies for *Let it Ride*

## The game

If you've practiced frisbee with Moontower before, you might be familiar with a wagering game called *Let it ride.* The rules are pretty simple:

Moontower splits into two teams (say, O line and D line). Each line takes turns trying to score on an endzone possession. If it's your turn, and you score on your possession, you get a point. Then you have two options:

1. You can "bank" your point, and add it to your score. Then it's the other team's turn.
2. You can let it ride! You get to go again, and if you score again, you'll get another point! But if you fail, you'll lose all of the points you haven't "banked," and it'll be the other team's turn to go.

You can let it ride as many times as you like, but the longer you go without banking your points, the more you stand to lose with each possession. The first team to bank a predetermined number of points (usually around 5) wins the game.

### An example

O line and D line are playing *Let it ride.* First to bank 3 points wins. O line gets to start on offense (of course), and scores their first point on an easy upline cut. They choose to bank, making the score **1 - 0**. Then it's D-line's turn. They immediately turf a swing pass, giving the disc back to O-line.

O-line scores again, and this time they decide to *let it ride,* and take another shot at the endzone to win the game. But there's a miscommunication on the iso cut and the inside throw goes to nobody, leaving the score still at **1-0**.

D-line scores on a nice hammer, and lets it ride! Then the iso defender gets caught off-guard, and they score again! Now they have two points on the line, and they decide to let it ride again for the win. A garbage throw to the back of the stack goes up, and Corey skies everyone to win the game for D-line. Final score: **3-1**, D-line wins.

-------------------------------------------------------------------------

## Strategy

For this article, let's completely set aside the question of frisbee strategy. You might want to know: 

##### Given an accurate estimate of how often both teams succesfully convert their endzone possessions, when should I bank, and when should I let it ride?

First of all - if you just want to look up what strategy you might want to use in a given situation, you can just consult [these tables](frisbee/let_it_ride_more.html). You should keep reading this article if you want to understand more of the details behind the strategies I've computed. Before we get into any careful analysis, though, let's see if we can conclude anything about *Let it ride* strategy, just based on our intuition.

### Observations

**Your choice of whether to bank or ride should depend on how confident you are in your ability to score, and your opponent's ability to score.** If you score more often, it makes sense to risk more points. For example, if you score on 99% of your endzone possessions, there's no reason for you to ever give your opponent a chance to play. You'll probably just win without ever needing to bank any points.

Conversely, if both you and your *opponent* only score on 1% of your possessions, then you should bank your points every time - getting just one point is hard enough that it makes no sense to try for two in a row.

**You should take more risks if you're behind.** Say your opponent is up 4-2 in a game to 5, and you know that both teams score on 75% of their possessions. If it's your turn, and you choose to bank your points, you'll have *at best* a 25% chance of winning the game. You have a better than 50% chance of scoring two points in a row, so letting it ride is your best option.

**Your optimal strategy might depend on your opponent's strategy.** If you happen to know that your opponents are especially risk-averse, and tend to bank points even when they *should* be letting it ride, you might be able to take advantage by playing a little more conservatively than you normally would. Conversely, if your opponents like taking irrational risks, you can possibly afford to take slightly bigger risks as well.

In technical terms, this means we shouldn't assume that there is a *dominant strategy* for the *Let it ride* game. For example, if you're up 2-1 and have 1 point at risk, whether or not you choose to bank or let it ride should depend on whether you think your opponent will make rational decisions.

-----------------------------------------------------------------

## Assumptions

To compute optimal strategies for *Let it ride*, we need to make some assumptions. As in every mathematical model, these assumptions will fail to match reality to some degree, so it's important to be explicit about them.

1. **Each team has a fixed probability of scoring on a given endzone possession.** That is, whether or not your team scores on any given endzone possession is independent of the outcome of any previous points, and doesn't change as the game drags on, new players are substituted, etc. We *won't* always assume that the two teams have *the same* fixed chance of scoring on their possessions (although we will sometimes assume this to simplify things a little).

2. **Both teams are rational, and are playing to maximize the probability that they win the game.** In technical terms, this means that we will be searching for *Nash equilibrium* strategies. Since *Let it ride* is zero-sum, this means that we assume that *both teams are playing to minimize the maximum probability that their opponent wins the game* (a "minimax" strategy).
	
	Later we'll drop this assumption and see what happens when just *one* of the two teams is playing rationally.

3. **Both teams know exactly how likely they are to score, and how likely their opponents are to score.** In other words the teams have *perfect information.*

	Later we'll relax this assumption slightly too, and see how it affects the outcome of the game.

## First results

Now that we have our assumptions out of the way, let's look at some optimal strategies in various circumstances. If you want to know how these strategies are computed, see the [Technical details](frisbee/let_it_ride.html#technical_details) section below.

### An example strategy table

Let's assume that both you and your opponent have a 60% chance of scoring on each possession, and we're playing a game to 5. When should you bank, and when should you let it ride?

<div class="table-title">How many points should I risk?</div>

<div class="table-container">
{!frisbee/table_1.md!}
</div>

The table above shows *how many points you should be willing to risk* (or in other words, *how many times you should let it ride*) at each possible score. For instance, if you're down 1-2, and you score a point, you should let it ride. But if you score again, then you should bank, since the optimal strategy here is to risk just 1 point.

Notice that in this game, you should *always* let it ride if you've got at least three points. If you have two points, you should *only* ever bank if you're up 2-0. And if you're down by 3 or 4 points, you should *always* let it ride.

### Example 2: better defense

Let's adjust the scoring probabilities and see what happens to optimal play.

<div class="table-title">How many points should I risk?</div>

<div class="table-container">
{!frisbee/table_2.html!}
</div>

Optimal strategy looks pretty different! If you assume both teams score on only 45% of their possessions, you should *never let it ride* unless you're behind (except if the score is tied at 3, in which case you should go for the second point if you have the chance).

An important observation here is that *optimal strategy is fairly sensitive to actual scoring probabilities.* If all you know is that both teams score on endzone possessions "about half the time," you probably don't have enough information to determine the best strategy for your team. Later we'll see exactly how much of a difference it makes if you get it wrong.

### Example 3: asymmetric probabilities

Here we can see what optimal strategy looks like if you score on 45% of your possessions, but your opponents score on 60% of theirs. We also can see optimal strategy for the reverse situation. Notice that it's different.

<div class="table-title">How many points should I risk?</div>

<div class="table-container">

{!frisbee/table_3.html!}

{!frisbee/table_4.html!}

</div>

## How much of an advantage is it to go first?

Getting to go first is an advantage in *let it ride.* So how much does it matter?

For simplicity, let's assume that both teams are equally good at offense and defense (so the scoring probabilities are the same for each team). We can plot how likely the first player is to win the game as a function of the scoring probability (assuming both teams are playing optimally). Once again, this is for a game to 5 points.

<div class="table-title">First player advantage</div>

![first player advantage](resources/frisbee/let_it_ride/p1_advantage.png)

We can see that the first player will win no more than 55% of the time, right up until both teams score on around 70% of their possessions. Then suddenly there's a rapid increase in how important it is to go first.

So what happens at 70%? It turns out that **in a game to 5**, this is the critical probability at which it's *always better to let it ride*. That is, the best strategy for both teams is to just try to score 5 points in a row before their opponent can do the same. Essentially, *Let it ride* has been reduced to the game where players take turns flipping a (weighted) coin, and whoever gets heads first wins.

In this situation, it's not too hard to exactly compute the probability that the first player wins, since it's given by an infinite geometric series. Specifically, if each team scores on a given possession with probability \\(p\\), then the probability that the first team scores 5 points in a row before their opponent is given by
$$\begin{align}
	 &p^5 + (1 - p^5)^2 \cdot p^5 + (1 - p^5)^4 \cdot p^5 + \ldots \\\\
	 &= \sum_{i = 0}^\infty p^5 (1 - p^5)^{2i} \\\\
	 &= \dfrac{p^5}{1 - (1 - p^5)^2} = \dfrac{1}{2 - p^5}.
\end{align}$$

If we plot this probability as a function of \\(p\\), we can see that it does in fact match up with optimal play after around \\(p = 0.7\\).

<div class="table-title">First player advantage: optimal play vs. always ride</div>

![optimal vs. always ride](resources/frisbee/let_it_ride/compare_always_ride.png)

------------------------------------------------------

## When should you always ride?

If your scoring probability is high enough, the best available strategy is to just always let it ride. What does "high enough" mean, exactly? That depends on the length of the game. The plot below shows the *minimum* scoring percentage both teams need to have in order for them to *always* let it ride.

<div class="table-title">How good does offense need to be for banking to always be suboptimal?</div>

![let it ride confidence](resources/frisbee/let_it_ride/risk_cutoff.png)

For instance, we can see that in a game to 5, the cutoff is at about 70%, just like we saw before.

I strongly suspect (but do not know for sure) that as the length of the game tends to infinity, the level of confidence you need to always let it ride tends to 1. It's also not hard to see that if the scoring probability is high enough, letting it ride is the *dominant* strategy and not just the minimax strategy.

### What about always banking?

If your scoring probability is *low* enough, you should hold onto your points at all costs. How hard does it need to be to score in order for it to never make sense to take any risks? It turns out that this is *independent* of the length of the game.

![let it ride risk/bank confidence](resources/frisbee/let_it_ride/both_cutoff.png)

In other words, if both teams have the same scoring probability, and that probability is below 30%, banking is *always* the better option. Why is this happening? I don't have a rigorous justification, but empirically, it seems the *best* time to risk points is towards the end of the game, when both teams are close to winning, but one team is one point ahead.

That is, it's *most* crucial to take risks when you're down **0-1**, game to 2. If both teams score with probability \\(p\\), then if you let it ride every time, you'll win with probability
$$
\frac{p}{1 + p - p^2}.
$$

If you bank every time, you'll win with probability
$$
\frac{1 - p}{(2 - p)^2}.
$$

The intersection occurs at about \\(p = 0.29289\\). So **if both teams score with probability < 0.29289, then banking is optimal (assuming both teams are playing rationally).** In fact, this rule generalizes to the situation where the two teams have asymmetric scoring probabilities. If your team scores with probability \\(p\\), and your opponents score with probability \\(q\\), then if you let it ride when you're down 0-1, you'll win a game to 2 with probability
$$
\frac{p^2}{1 - (1 - p^2)(1 - q)}.
$$
If you bank, you'll win with probability
$$
\left(\frac{p}{1 - (1 - p)(1 - q)}\right)^2 \cdot (1 - q).
$$
Justifying all of these formulas is a straightforward probability exercise.

The blue region of the chart below shows where banking is the better strategy in a game to 2. The point (0.29289, 0.29289) lies on the boundary.

![p,q plot](resources/frisbee/let_it_ride/contour.png)

Again, I suspect that banking is in fact the *dominant* strategy when the scoring probability is low enough, but I haven't verified this empirically or otherwise.

--------------------------------------------------------------------

## So how much of an advantage can you get?

What if you employ an optimal strategy against an opponent who is *not* playing rationally? How much of an extra edge do you get by playing minimax? It depends on exactly what your opponent is doing, but it turns out that you can do pretty well.

<div class="table-title">Minimax strategy against suboptimal strategies</div>
![irrational opponents](resources/frisbee/let_it_ride/irrational_opponents.png)

Here we can see how likely the first player is to win a game to **8 points** if they're employing a minimax strategy against an opponent who is making a suboptimal choice (either always letting it ride, always banking, or letting it ride only if they're losing). The exact benefit of playing optimally varies with scoring probability and opponent's strategy, but for conversion percentages in the 30% - 70% range, you get a pretty solid edge if you go first and play optimally against an irrational opponent.

### What if you know your opponent's strategy?

You can do *even better* if you know ahead of time exactly when your opponent will let it ride, and exactly when they'll bank it (assuming they make consistent choices throughout the game). Here, instead of employing a minimax strategy, you can simply maximize your odds of winning *given your opponent's choices*. If those choices happen to be suboptimal, you can get a slight extra edge.

Here's a side-by-side comparison of optimal strategies in a game to 6 with a scoring probability of 60%. On the left is the strategy you should employ if you assume your opponent is playing rationally. On the right is your best strategy if you think your opponent will *always* bank their points.

<div class="table-title">Optimal strategies vs. known opponent strategy</div>

<div class="table-container">

{!frisbee/table_5.html!}

{!frisbee/table_7.html!}

</div>

Notice that in this situation, you get an advantage by playing more conservatively if you know your opponent is highly risk-averse. Here's another table showing your optimal strategy if you know that your opponent *always* takes risks:

<div class="table-title">Optimal strategies vs. known opponent strategy</div>

<div class="table-container">
{!frisbee/table_5.html!}

{!frisbee/table_6.html!}
</div>

Here things aren't so clear-cut. Sometimes you want to take *fewer* risks even if you know your opponent is taking too many.

So how succesful can you be by knowing your opponent's strategy? Here's how your odds change as the scoring probability varies in a game to 8:

<div class="table-title">Optimal strategies and minimax strategies vs. suboptimal strategies</div>

![max opp strategies vs minimax strategies](resources/frisbee/let_it_ride/compare_opp_strats.png)

Notice that your odds don't change much if you account for the fact that your opponent takes too many risks, but you can get a sizeable edge by accounting for the fact that your opponent is highly risk-averse (reflected in the difference between the green and brown curves).

### What if you're wrong about the conversion percentage?

So far, we've assumed that both teams have perfect information, and know exactly how likely each team is to score on a given possession. But what if one of the teams is wrong? Unsurprisingly, their odds will go down.

<div class="table-title">Incorrect conversion percentage assumptions</div>

![incorrect conversion assumption](resources/frisbee/let_it_ride/incorrect_probabilities.png)

Here's your odds of winning a game to 8 if you're playing against an opponent who's employing an optimal (minimax) strategy, when you employ what you *think* is an optimal strategy *but your estimate of the conversion percentage is off by 0.1*. In other words, the orange curve shows how often you expect to win if you believe both teams score with probability \\(p + 0.1\\), when both teams actually score with probability \\(p\\). The green curve shows your expected win percentage if instead you *underestimate* by 0.1. 

If your opponent knows the true percentage exactly, you lose most of the time, even if you get to go first! So knowing your own team's conversion percentage to a high degree of accuracy is crucial to building an optimal strategy for *let it ride.*


------------------------------------------------------------------------------

<span id="technical_details"></span>
## Technical details: how does all of this work, anyway?

If you've gotten this far and you're *still* not scared away by the phrase "technical details," congratulations! Keep reading if you want to get an idea of how all of these strategies and probabilities are actually computed.

### Formal description of the game

We're modeling *Let it ride* as a *competitive Markov decision process* (or *competitive MDP*), a special case of a *stochastic game* and a generalization of a typical *Markov process*. We can think of the game as taking place on the vertices of a directed graph, each of which represents a *game state*. The *state* of the game depends only on the scores of each player, whose turn it is, and how many points that player currently has at risk.

Each state is *controlled* by one of the two players. If a player controls a state, then whenever the game is in that state, the player can choose to either *bank* or *ride*. Then the game will transition to some other state. Which state it transitions to depends only on the player's choice and the outcome of a random variable (whether or not that player scores a point, if they choose to let it ride).

A number of states represent *win conditions* for each player. The goal of each player is to assign a choice to each game state in their control which maximizes the probability that the game ends in one of their win conditions.

### Naive solution for competitive MDP: backwards induction

When the directed graph for a competitive MDP is acyclic (in particular, if it's a tree), then it's fairly straightforward to solve for optimal strategies using *backwards induction*. Each leaf node of the tree is a win state for one of the players. So we simply compute win probabilities going backwards up the tree, starting from the leaves and ending at the root: at each vertex, we can just compute the probability that we win the game going down each child branch, and then select the branch that gives us the highest probability of winning. This approach lends itself well to dynamic programming and isn't too hard to implement.

However, the directed graph representing the *Let it ride* competitive MDP *contains loops.* That is, it's possible for the game state to *return* to an earlier state. In this particular game, this happens whenever both teams consecutively fail to score a point, because then no overall progress is made. So if we attempt backwards induction, we'll end up in an infinite loop.

### Approximate solution

We're saved by the fact that no matter what strategies the players choose, the resulting Markov process is *never recurrent.* That is, no matter what choices the players make, the game will *almost surely terminate* in finite time.

That means we can approximate *Let it ride* as a competitive MDP *whose graph is acyclic* by adding an extra variable to each state, which counts the total number of turns that have elapsed since the start of the game. After some (large) fixed number of turns have elapsed, the game automatically ends and we flip a coin to see who wins the game.

We can use backward induction to find optimal strategies for this approximation, and then let the maximum number of turns tend to infinity. The optimal strategies *should* converge, since for fixed scoring probabilties, the probability that the game lasts \\(n\\) turns rapidly tends to zero as n tends to infinity.

### Exact solution

Approximating solutions is useful, in part because it's in some ways a more accurate model of how *Let it ride* actually works in real life: when we play the game at practice, we don't assume that it will go on for arbitrarily long times. The main disadvantage of approximating optimal strategies is that the backwards induction algorithm is fairly slow when the length of the game is long. That's because we have to artificially introduce more and more branches to get rid of the cycles in our original graph.

To get an *exact* solution, we can modify our model a little bit. We still think of the game as being played on the vertices of a directed graph. Each vertex corresponds to a particular game state, but we *only* keep track of the game states where there are no points currently at risk.

The players' strategies are represented by a choice, at each of these states, of *how many times they will let it ride*. This is exactly what's recorded in the strategy tables above. The key observation is the following: 

##### If both players always employ the same strategies at a particular state, we can exactly compute the probability that the game eventually transitions to another state, given those strategies.

For example, say that the first player scores with probability \\(p\\), and the second player scores with probability \\(q\\). Let's say the score of the game is **2-1**. If we know that at this stage of the game, the first player will *always* let it ride *once*, and the second player will *always* bank, then the probability that the game transitions to state **4-1** is
$$
p_{4-1} = p^2 \cdot \frac{1}{1 - (1 - p^2)(1 - q)}.
$$
This is just the probability that the first player scores twice in a row before the second player manages to score at all. Since the game will almost surely *eventually* leave the state **2-1**, the probability that the game transitions to state **2-2** is just \\(1 - p_{4-1}\\).

This turns *Let it ride* into a *stochastic game* played on an *acyclic* finite directed graph, since the total score always *increases* whenever we transition to a new state. At each vertex we have a two-player zero-sum game, where the choices correspond to possible maximum allowable risks (at that particular state), and the payoffs for a pair of choices correspond to the likelihood of winning the game, should the players employ that pair of strategies. Once the payoffs have been computed, we can just use a minimax algorithm to find optimal play for each player, and thus the win probability for each player at that state (given optimal play). The payoffs themselves are computed recursively, by traversing the graph from leaves to root. The leaf nodes are win states for a single player.

This approach generalizes if we want to compute win probabilities when the players *aren't* using minimax to select their strategies, which is how we can compare optimal vs. suboptimal play.

### Simulation

What about simulation? While this is not too hard to implement, I didn't use simulation to compute optimal strategies because it's not as easy to do efficiently in this case. Brute-forcing an optimal strategy with simulation requires playing through *many* games with *every* possible combination of strategies, and figuring out rates of convergence is hard. Simulation is nice as a check to make sure the probabilities you're getting are reasonable, since once you've found what you believe to be the optimal strategy, you can verify that it does win about as often as you'd expect it to. But, it's not at the center of any of these computations.

------------------------------------------------------------------