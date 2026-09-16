**I recommend 70 core problems, organized into 14 chapters, followed by 12 targeted extensions.** The order below builds from basic queries to joins, analytical calculations, window functions, and advanced combinations.

This builds on LeetCode’s [SQL 50](https://leetcode.com/studyplan/top-sql-50/), with additional exercises to strengthen the progression. The **70 core problems are available without Premium**; the **12 optional extensions currently require Premium**.

**SQL curriculum — 70 core problems + 12 advanced extensions**

**How to use this curriculum**

- Follow the chapters and the problems within each chapter in order.
- Use **MySQL** consistently for your first pass. Learn another dialect after the underlying ideas are solid.
- Treat each listed technique as the learning objective. Some problems have several valid approaches.
- A solution completed with hints or an explanation still needs an independent reattempt.
- Move forward when you can explain why your query returns the correct rows, including duplicates, ties, and missing data.

Before starting, learn what tables, primary keys, foreign keys, and `NULL` represent.

The most useful habit throughout this curriculum is to state:

**“One row in my answer represents ______.”**

That might be one customer, one department, one customer per day, or one transaction. This is the result’s **grain**, and it guides your joins and grouping.

**1. Selecting, filtering, and ordering — 6 problems**

Learn to select columns, apply conditions, remove duplicate results, and control output order.

| Technique | Problem |
|---|---|
| Select rows satisfying multiple conditions | [1757. Recyclable and Low Fat Products](https://leetcode.com/problems/recyclable-and-low-fat-products/) |
| Combine alternative conditions with `OR` | [595. Big Countries](https://leetcode.com/problems/big-countries/) |
| Compare columns and return distinct results | [1148. Article Views I](https://leetcode.com/problems/article-views-i/) |
| Filter using a string-length expression | [1683. Invalid Tweets](https://leetcode.com/problems/invalid-tweets/) |
| Combine arithmetic conditions, exclusions, and sorting | [620. Not Boring Movies](https://leetcode.com/problems/not-boring-movies/) |
| Handle missing values explicitly | [584. Find Customer Referee](https://leetcode.com/problems/find-customer-referee/) |

**Checkpoint:** Explain why `referee_id <> 2` does not include rows where `referee_id` is `NULL`. Ordinary comparisons with `NULL` do not evaluate to true. [MySQL’s explanation](https://dev.mysql.com/doc/refman/8.4/en/working-with-null.html).

**2. Grouping and aggregation — 6 problems**

Learn to turn multiple input rows into a summary for each group.

| Technique | Problem |
|---|---|
| Identify repeated values using `GROUP BY` and `HAVING` | [182. Duplicate Emails](https://leetcode.com/problems/duplicate-emails/) |
| Count distinct values within each group | [2356. Number of Unique Subjects Taught by Each Teacher](https://leetcode.com/problems/number-of-unique-subjects-taught-by-each-teacher/) |
| Sum calculated values using a compound grouping key | [1741. Find Total Time Spent by Each Employee](https://leetcode.com/problems/find-total-time-spent-by-each-employee/) |
| Filter groups by their size | [596. Classes With at Least 5 Students](https://leetcode.com/problems/classes-with-at-least-5-students/) |
| Count relationships and order the grouped output | [1729. Find Followers Count](https://leetcode.com/problems/find-followers-count/) |
| Find the group with the largest count | [586. Customer Placing the Largest Number of Orders](https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/) |

**Checkpoint:** Explain the differences between `WHERE` and `HAVING`, and between `COUNT(*)`, `COUNT(column)`, and `COUNT(DISTINCT column)`.

**3. Joins and missing matches — 8 problems**

Learn how tables connect, which rows survive a join, and when one input row produces multiple joined rows.

| Technique | Problem |
|---|---|
| Preserve every row from the main table using `LEFT JOIN` | [175. Combine Two Tables](https://leetcode.com/problems/combine-two-tables/) |
| Look up an optional identifier | [1378. Replace Employee ID With The Unique Identifier](https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/) |
| Enrich records using an `INNER JOIN` | [1068. Product Sales Analysis I](https://leetcode.com/problems/product-sales-analysis-i/) |
| Find entities with no matching records | [183. Customers Who Never Order](https://leetcode.com/problems/customers-who-never-order/) |
| Count unmatched events for each entity | [1581. Customer Who Visited but Did Not Make Any Transactions](https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/) |
| Filter a joined result while retaining missing matches | [577. Employee Bonus](https://leetcode.com/problems/employee-bonus/) |
| Exclude entities having any prohibited relationship | [607. Sales Person](https://leetcode.com/problems/sales-person/) |
| Aggregate optional matches and substitute zero when needed | [1407. Top Travellers](https://leetcode.com/problems/top-travellers/) |

For **183** and **607**, practice both an appropriate join approach and `NOT EXISTS`. Discuss what can go wrong with `NOT IN` when its subquery contains `NULL`.

**Checkpoint:** Predict the joined rows by hand before writing the query. Explain how placing a condition in `WHERE` can remove unmatched rows from a left join.

**4. Self-joins and relationships within a table — 6 problems**

Learn to give the same table different roles and match the correct records.

| Technique | Problem |
|---|---|
| Compare an employee with their manager | [181. Employees Earning More Than Their Managers](https://leetcode.com/problems/employees-earning-more-than-their-managers/) |
| Match records exactly one calendar day apart | [197. Rising Temperature](https://leetcode.com/problems/rising-temperature/) |
| Pair start and end events using the complete key | [1661. Average Time of Process per Machine](https://leetcode.com/problems/average-time-of-process-per-machine/) |
| Aggregate direct reports for each manager | [1731. The Number of Employees Which Report to Each Employee](https://leetcode.com/problems/the-number-of-employees-which-report-to-each-employee/) |
| Filter managers by their number of direct reports | [570. Managers with at Least 5 Direct Reports](https://leetcode.com/problems/managers-with-at-least-5-direct-reports/) |
| Detect references to records that no longer exist | [1978. Employees Whose Manager Left the Company](https://leetcode.com/problems/employees-whose-manager-left-the-company/) |

**Checkpoint:** Explain each table alias’s role. For **1661**, explain why matching only on the machine is insufficient.

**5. Conditional logic and analytical metrics — 6 problems**

Learn `CASE`, conditional aggregation, percentages, and denominator selection.

| Technique | Problem |
|---|---|
| Calculate a value conditionally | [1873. Calculate Special Bonus](https://leetcode.com/problems/calculate-special-bonus/) |
| Classify rows using several constraints | [610. Triangle Judgement](https://leetcode.com/problems/triangle-judgement/) |
| Combine averages with a conditional percentage | [1211. Queries Quality and Percentage](https://leetcode.com/problems/queries-quality-and-percentage/) |
| Calculate several conditional metrics per month and country | [1193. Monthly Transactions I](https://leetcode.com/problems/monthly-transactions-i/) |
| Calculate a rate while preserving users with no activity | [1934. Confirmation Rate](https://leetcode.com/problems/confirmation-rate/) |
| Compare a group count with the overall population | [1633. Percentage of Users Attended a Contest](https://leetcode.com/problems/percentage-of-users-attended-a-contest/) |

Use `CASE` explicitly before relying on shortcuts such as summing Boolean expressions.

**Checkpoint:** State the numerator, denominator, and treatment of missing activity in plain English. Explain when rounding should happen.

**6. Combining joins and aggregates — 5 problems**

Learn to calculate summaries across related tables without accidentally multiplying contributions.

| Technique | Problem |
|---|---|
| Average an attribute across members of a group | [1075. Project Employees I](https://leetcode.com/problems/project-employees-i/) |
| Join on date intervals and calculate a weighted average | [1251. Average Selling Price](https://leetcode.com/problems/average-selling-price/) |
| Generate all expected combinations and retain zero counts | [1280. Students and Examinations](https://leetcode.com/problems/students-and-examinations/) |
| Combine date filtering, joins, and aggregate thresholds | [1327. List the Products Ordered in a Period](https://leetcode.com/problems/list-the-products-ordered-in-a-period/) |
| Find entities associated with every required item | [1045. Customers Who Bought All Products](https://leetcode.com/problems/customers-who-bought-all-products/) |

For **1280**, learn why a `CROSS JOIN` is useful. For **1045**, distinguish the number of purchases from the number of distinct products purchased.

**Checkpoint:** Explain whether each join preserves, removes, or multiplies rows. Identify when aggregating a table before joining would help.

**7. Subqueries, CTEs, and selecting records within groups — 7 problems**

Learn to build a query in stages: calculate an intermediate result, then use it.

| Technique | Problem |
|---|---|
| Filter groups, then aggregate again; handle no qualifying value | [619. Biggest Single Number](https://leetcode.com/problems/biggest-single-number/) |
| Establish the earliest date for each entity | [511. Game Play Analysis I](https://leetcode.com/problems/game-play-analysis-i/) |
| Filter a time period before selecting its latest timestamp | [1890. The Latest Login in 2020](https://leetcode.com/problems/the-latest-login-in-2020/) |
| Find a group maximum and return every matching employee | [184. Department Highest Salary](https://leetcode.com/problems/department-highest-salary/) |
| Return records belonging to each product’s first sales year | [1070. Product Sales Analysis III](https://leetcode.com/problems/product-sales-analysis-iii/) |
| Combine an explicit primary designation with a single-membership fallback | [1789. Primary Department for Each Employee](https://leetcode.com/problems/primary-department-for-each-employee/) |
| Reconstruct the latest applicable value as of a cutoff date | [1164. Product Price at a Given Date](https://leetcode.com/problems/product-price-at-a-given-date/) |

Use these problems to practice derived tables and named CTEs with `WITH`. Compare a correlated subquery with a grouped intermediate result where appropriate.

**Checkpoint:** Explain what every intermediate table contains. Distinguish finding the maximum value from retrieving the full records associated with it.

**8. Date-based analytics and first-event reasoning — 3 problems**

Learn to measure activity over time and define the correct population.

| Technique | Problem |
|---|---|
| Count distinct daily users within an inclusive date interval | [1141. User Activity for the Past 30 Days I](https://leetcode.com/problems/user-activity-for-the-past-30-days-i/) |
| Select each customer’s first event before calculating a percentage | [1174. Immediate Food Delivery II](https://leetcode.com/problems/immediate-food-delivery-ii/) |
| Measure next-day return relative to each player’s first login | [550. Game Play Analysis IV](https://leetcode.com/problems/game-play-analysis-iv/) |

**Checkpoint:** Explain why “returned the day after their first login” differs from “has any two consecutive login days.”

Also practice timestamp boundaries such as `>= start` and `< next_period_start`.

**9. Text processing and validation — 3 problems**

Learn to transform strings and match precisely defined patterns.

| Technique | Problem |
|---|---|
| Combine substring extraction and case conversion | [1667. Fix Names in a Table](https://leetcode.com/problems/fix-names-in-a-table/) |
| Match a condition prefix at the correct token boundary | [1527. Patients With a Condition](https://leetcode.com/problems/patients-with-a-condition/) |
| Validate a complete string with explicit character and domain rules | [1517. Find Users With Valid E-Mails](https://leetcode.com/problems/find-users-with-valid-e-mails/) |

**Checkpoint:** Test patterns against near misses, including the right text in the wrong position. For **1517**, follow the problem’s specified email rules and domain case requirement.

**10. Combining result sets and reshaping data — 7 problems**

Learn to combine queries, convert columns into rows, and build reporting categories.

| Technique | Problem |
|---|---|
| Find identifiers present in only one of two tables | [1965. Employees With Missing Information](https://leetcode.com/problems/employees-with-missing-information/) |
| Unpivot columns into rows using `UNION ALL` | [1795. Rearrange Products Table](https://leetcode.com/problems/rearrange-products-table/) |
| Pivot rows into columns using conditional aggregation | [1179. Reformat Department Table](https://leetcode.com/problems/reformat-department-table/) |
| Return every required category, including categories with zero members | [1907. Count Salary Categories](https://leetcode.com/problems/count-salary-categories/) |
| Create a sorted, distinct string summary per group | [1484. Group Sold Products By The Date](https://leetcode.com/problems/group-sold-products-by-the-date/) |
| Combine both endpoints of a relationship before counting | [602. Friend Requests II: Who Has the Most Friends](https://leetcode.com/problems/friend-requests-ii-who-has-the-most-friends/) |
| Combine separately calculated answers with explicit tie-breaking | [1341. Movie Rating](https://leetcode.com/problems/movie-rating/) |

**Checkpoint:** Explain when `UNION` would incorrectly remove useful duplicates and when `UNION ALL` would preserve unwanted ones.

**11. Ranking and top results within groups — 4 problems**

Learn `OVER`, `PARTITION BY`, and the differences between `ROW_NUMBER`, `RANK`, and `DENSE_RANK`.

| Technique | Problem |
|---|---|
| Rank values while preserving ties without gaps | [178. Rank Scores](https://leetcode.com/problems/rank-scores/) |
| Select the second distinct value and handle its absence | [176. Second Highest Salary](https://leetcode.com/problems/second-highest-salary/) |
| Generalize distinct-value selection to an arbitrary rank | [177. Nth Highest Salary](https://leetcode.com/problems/nth-highest-salary/) |
| Return the top three distinct salary levels within each department | [185. Department Top Three Salaries](https://leetcode.com/problems/department-top-three-salaries/) |

Window functions calculate across related rows while retaining individual query rows; this differs from collapsing rows with grouping. [MySQL window-function concepts](https://dev.mysql.com/doc/refman/8.4/en/window-functions-usage.html).

**Checkpoint:** Given salaries `100, 100, 90, 80`, predict all three ranking functions. Explain why “three employees” and “three salary levels” can produce different answers.

Revisit **184** with a window-function solution without counting it as a new problem.

**12. Ordered windows, running totals, and neighboring rows — 4 problems**

Learn how row order and the window frame determine a calculation.

| Technique | Problem |
|---|---|
| Access neighboring rows; compare `LAG`/`LEAD` with a conditional solution | [626. Exchange Seats](https://leetcode.com/problems/exchange-seats/) |
| Calculate a running total and find the last permitted row | [1204. Last Person to Fit in the Bus](https://leetcode.com/problems/last-person-to-fit-in-the-bus/) |
| Aggregate daily values before calculating a moving total and average | [1321. Restaurant Growth](https://leetcode.com/problems/restaurant-growth/) |
| Detect repeated values across consecutive positions | [180. Consecutive Numbers](https://leetcode.com/problems/consecutive-numbers/) |

Practice explicit window frames, especially `ROWS BETWEEN ...`.

**Checkpoint:** Explain the partition, ordering, and frame independently. For **1321**, explain why seven rows represent seven days after daily aggregation under the problem’s assumptions—and what would change if dates were missing.

**13. Combined-pattern capstones — 3 problems**

Attempt these after the earlier chapters. Write a plan for the intermediate results before writing SQL.

| Technique | Problem |
|---|---|
| Combine duplicate detection with uniqueness of a column pair | [585. Investments in 2016](https://leetcode.com/problems/investments-in-2016/) |
| Apply eligibility rules to two user roles before calculating daily rates | [262. Trips and Users](https://leetcode.com/problems/trips-and-users/) |
| Identify qualifying consecutive runs using a gaps-and-islands approach | [601. Human Traffic of Stadium](https://leetcode.com/problems/human-traffic-of-stadium/) |

For **601**, the required continuity is in **IDs**, which is distinct from consecutive calendar dates.

**Checkpoint:** Explain why each intermediate step is necessary and construct a small example that would break a tempting incorrect solution.

**14. Updating and deleting data — 2 problems**

Learn how SQL changes stored rows.

| Technique | Problem |
|---|---|
| Transform existing values using a conditional `UPDATE` | [627. Swap Sex of Employees](https://leetcode.com/problems/swap-sex-of-employees/) |
| Delete duplicates while retaining the row with the smallest identifier | [196. Delete Duplicate Emails](https://leetcode.com/problems/delete-duplicate-emails/) |

Problem **627** appears under the older title *Swap Salary* in some lists.

**Checkpoint:** Describe exactly which rows change and which survive. For **196**, explain how the rule chooses one survivor from a group of three or more duplicates.

**Targeted extensions — 12 additional problems**

These currently require **LeetCode Premium**. Add them after their prerequisites are comfortable; they are optional for completing the core curriculum.

| Area | Problem | Learning objective |
|---|---|---|
| Group benchmarks | [1126. Active Businesses](https://leetcode.com/problems/active-businesses/) | Compare each business’s activity with event-specific averages |
| Multiple aggregation levels | [615. Average Salary: Departments VS Company](https://leetcode.com/problems/average-salary-departments-vs-company/) | Compare department and company metrics for the same month |
| Cohort retention | [1097. Game Play Analysis V](https://leetcode.com/problems/game-play-analysis-v/) | Measure next-day retention separately for each installation-date cohort |
| Complete reporting grids | [1127. User Purchase Platform](https://leetcode.com/problems/user-purchase-platform/) | Classify users across platforms and include empty reporting categories |
| Exclusion across all events | [1412. Find the Quiet Students in All Exams](https://leetcode.com/problems/find-the-quiet-students-in-all-exams/) | Require participation while excluding anyone who ever meets a disqualifying condition |
| Median rows | [569. Median Employee Salary](https://leetcode.com/problems/median-employee-salary/) | Select middle employee rows within each company |
| Frequency-weighted median | [571. Find Median Given Frequency of Numbers](https://leetcode.com/problems/find-median-given-frequency-of-numbers/) | Locate the median using cumulative frequencies |
| Calendar-based windows | [579. Find Cumulative Salary of an Employee](https://leetcode.com/problems/find-cumulative-salary-of-an-employee/) | Handle rolling month intervals, missing months, and excluded latest records |
| Calendar streaks | [1454. Active Users](https://leetcode.com/problems/active-users/) | Detect consecutive login dates after handling repeated daily activity |
| Contiguous intervals | [1225. Report Contiguous Dates](https://leetcode.com/problems/report-contiguous-dates/) | Turn consecutive dates of the same status into intervals |
| Recursive CTEs | [1613. Find the Missing IDs](https://leetcode.com/problems/find-the-missing-ids/) | Generate an expected sequence and identify absent values |
| Overlapping intervals | [2494. Merge Overlapping Events in the Same Hall](https://leetcode.com/problems/merge-overlapping-events-in-the-same-hall/) | Merge intervals while correctly handling nested overlaps |

That gives you **70 core + 12 extensions = 82 unique problems**, with no duplicates.

**How to turn this into lasting skill**

For each problem, follow this routine:

1. **Define the output grain.** State what one answer row represents.
2. **Identify the relationships.** Write down the keys and whether a join can multiply rows.
3. **Describe the transformations.** For example: filter → aggregate → join → rank → select.
4. **Write the query independently.**
5. **Test the assumptions.** Consider duplicates, ties, `NULL`, absent matches, empty results, and date boundaries.
6. **Explain the result.** Account for every join condition, grouping column, and denominator.

Track progress using four states:

| State | Meaning |
|---|---|
| Attempted | You worked on it but do not yet have a correct explanation and solution |
| Solved with help | A hint, editorial, or walkthrough contributed to the solution |
| Independent | You solved and explained it without assistance |
| Retained | You independently solved it again after a delay |

Reattempt assisted problems after **2–3 days**, then again roughly **a week later**. After each chapter, mix in older problems without looking at their technique labels.

A reasonable starting pace is **7–10 new problems per week plus review**, adjusted to your experience. Give joins, grouped calculations, and window functions extra time when needed.

This curriculum develops query-writing and analytical SQL skills. For broader database competence, add separate hands-on practice with schema design, constraints, indexes, `EXPLAIN`, and transactions.

**Start with Chapter 1, problem 1757.** Before writing SQL, identify the requested output column and the two conditions a row must satisfy.