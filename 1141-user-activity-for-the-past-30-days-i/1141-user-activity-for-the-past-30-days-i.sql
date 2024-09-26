Select activity_date as day,count(Distinct user_id) as active_users from Activity
Where  activity_date >= '2019-07-27'::date - INTERVAL'30 days' 
    AND activity_date <= '2019-07-27'::date
group by activity_date
order by activity_date