-- 코드를 입력하세요
-- 최대금액을 찾긴 하지만 그 금액이 product_name과 맞는게 아니다.

select category, price as max_price, product_name
from ( -- 카테고리별로 순위 추가
    select *, rank() over (partition by category order by price desc) as rnk
    from food_product
    where category in ('과자', '국', '김치', '식용유')) as t  
where rnk = 1
order by max_price desc