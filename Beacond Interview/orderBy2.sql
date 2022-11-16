/*
write a SQL query to find the details of 1970 Nobel Prize winners.
 Order the results by subject,
 ascending except for 'Chemistry' and ‘Economics’
 which will come at the end of the result set.
 */
 SELECT * from novel_win
 WHERE YEAR = 1970
 order by 
 CASE
	when subject in ('Economics’,Chemistry') THEN 1
	ELSE 0
end ASC,
subject,winner;