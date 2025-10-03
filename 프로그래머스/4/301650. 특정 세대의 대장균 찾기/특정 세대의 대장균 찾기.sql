-- 코드를 작성해주세요

select id
from ecoli_data
where parent_id in ( -- 2세대 찾기
    select id
    from ecoli_data
    where parent_id in ( -- 1세대 찾기
        select id
        from ecoli_data
        where parent_id is null))
order by id asc