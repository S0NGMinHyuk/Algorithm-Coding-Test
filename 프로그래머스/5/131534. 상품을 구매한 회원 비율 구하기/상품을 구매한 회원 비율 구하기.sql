-- 코드를 입력하세요

# select count(user_id) as cnt
# from user_info
# where joined like "2021%"
with cte as (
    select count(user_id) as cnt
    from user_info
    where joined like "2021%"
)
select 
    year(sales_date) as year, 
    month(sales_date) as month, 
    count(distinct user_id) as purchased_users,
    round(count(distinct user_id)/cnt, 1) as puchased_ratio
from user_info
join cte
join online_sale
using (user_id)
where joined like "2021%"
and online_sale_id is not null
group by year, month
order by year, month