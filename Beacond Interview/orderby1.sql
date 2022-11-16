/*
We have to order the data by country first.
 Then, every shop within the same country should be sorted by city.
 If the shop is in the U.S.,
 we need to sort it next by the column state.
 The code that solves this little problem is:
*/

/* Ascending order*/
SELECT * from shops
ORDER BY country,
CASE
	WHEN country='USA' THEN state
	ELSE city
	end;
/* Decending order*/
select * from shops
order by country,
CASE
	WHEN country='usa' then state
	else city
	end DESC;
