create view host_teams_new as 
select host_team_id, count(*)
from matches 
group by host_team_id;

create view guest_teams_new as
select guest_team_id, count(*)
from matches 
group by guest_team_id;

create view team_ids as
select host_team_id
from host_teams_new as ht inner join guest_teams_new as gt on ht.host_team_id = gt.guest_team_id
where ht.count + gt.count > 3;

select teams.name
from teams inner join team_ids on teams.team_id = team_ids.host_team_id;

