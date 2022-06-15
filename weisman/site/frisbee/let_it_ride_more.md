% Let it ride: strategy tables

# Let it ride: sample strategy tables

The tables below show equilibrium strategies for many different versions of *Let it ride.* For more details on how this works, check out my [writeup on the topic](frisbee/let_it_ride.html).

#### How to read this table

The number in each box of the table represents *how many points you should be willing to risk* in any given situation. In other words, if the box at (0, 0) reads "1", then when the score is tied at zero, you should let it ride *one time* before banking your points.

All of these tables are computed under the assumption that each team has a fixed probability of scoring on their endzone possessions (and that this probability is the same for each team). Each team is also assumed to play *rationally*. See the [full article](frisbee/let_it_ride.html) for examples of strategy tables where these assumptions are loosened.

<script src="frisbee/let_it_ride.js"></script>

<div class="table-container">
<h2>Endzone scoring percentage:
<select name="possession_prob" id="possession_prob">
	<option value="20">20%</option>
	<option value="25">25%</option>
	<option value="30">30%</option>
	<option value="35">35%</option>
	<option value="40">40%</option>
	<option value="45">45%</option>
	<option value="50" selected>50%</option>
	<option value="55">55%</option>
	<option value="60">60%</option>
	<option value="65">65%</option>
	<option value="70">70%</option>
	<option value="75">75%</option>
	<option value="80">80%</option>
	<option value="85">85%</option>
	<option value="90">90%</option>
</select></h2>

{!frisbee/table_10_0.20.html!}
{!frisbee/table_10_0.25.html!}
{!frisbee/table_10_0.30.html!}
{!frisbee/table_10_0.35.html!}
{!frisbee/table_10_0.40.html!}
{!frisbee/table_10_0.45.html!}
{!frisbee/table_10_0.50.html!}
{!frisbee/table_10_0.55.html!}
{!frisbee/table_10_0.60.html!}
{!frisbee/table_10_0.65.html!}
{!frisbee/table_10_0.70.html!}
{!frisbee/table_10_0.75.html!}
{!frisbee/table_10_0.80.html!}
{!frisbee/table_10_0.85.html!}
{!frisbee/table_10_0.90.html!}
</div>