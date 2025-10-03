-- 코드를 입력하세요
select y as year, m as month, gender, count(*) as users
from (
    select distinct
        year(sales_date) as y,
        month(sales_date) as m,
        user_id
    from online_sale) as o_sale
left join user_info as u_info
on u_info.user_id = o_sale.user_id
where gender is not null
group by year, month, gender
order by year, month, gender