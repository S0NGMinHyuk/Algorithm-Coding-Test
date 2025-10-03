-- 코드를 입력하세요

select first_half.flavor
from first_half
left outer join (
    select flavor, sum(total_order) as orders
    from july
    group by flavor) as j
on first_half.flavor = j.flavor
order by total_order + orders desc
limit 3