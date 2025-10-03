-- 코드를 작성해주세요

with front as (
    select sum(code) as bit
    from skillcodes
    where category = 'Front End'
)

select id, email, first_name, last_name
from developers, front  -- developers 테이블에 bit 열이 추가된 테이블
where skill_code & bit > 0
order by id asc