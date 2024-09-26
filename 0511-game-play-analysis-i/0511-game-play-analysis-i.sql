Select Min(player_id) as player_id ,Min(event_date) as first_login from Activity
Group by player_id
Order by player_id desc