-- 코드를 입력하세요
select food_product.product_id, product_name, total_amount*price as total_sales
from food_product
left join (
    select product_id, sum(amount) as total_amount
    from food_order
    where produce_date like '2022-05%'
    group by product_id) as f_order
on food_product.product_id = f_order.product_id
where total_amount is not null
order by total_sales desc, product_id