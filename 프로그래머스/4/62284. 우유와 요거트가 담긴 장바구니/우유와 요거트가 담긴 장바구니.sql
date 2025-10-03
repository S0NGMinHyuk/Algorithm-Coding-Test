-- 코드를 입력하세요

select c.cart_id
from cart_products
left join (
    select cart_id  -- 요거트를 담은 장바구니 번호
    from cart_products
    where name = 'Yogurt') as c
on cart_products.cart_id = c.cart_id
where name = 'Milk' -- 우유를 담은 장바구니 번호
and c.cart_id is not null
order by c.cart_id