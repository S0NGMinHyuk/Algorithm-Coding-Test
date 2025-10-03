-- 코드를 입력하세요

with recursive timetable as (
    select 0 as h
    union
    select h+1 from timetable
    where h < 23
)

select h as hour, count(animal_outs.animal_id) as count
from timetable
left outer join animal_outs
on timetable.h = hour(animal_outs.datetime)
group by hour
order by hour asc