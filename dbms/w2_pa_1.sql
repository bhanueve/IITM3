select managers.name 
from managers inner join teams on managers.team_id = teams.team_id
where teams.name = 'All Stars'