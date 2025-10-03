-- 코드를 입력하세요
-- group by 신경쓰기

select a.author_id, a.author_name, category, sum(price*amount) as total_sales
from book
left join (
    select book_id, sum(sales) as amount
    from book_sales
    where sales_date like '2022-01%'
    group by book_id) as b_sales
on book.book_id = b_sales.book_id
left join (
    select author_id, author_name
    from author) as a
on book.author_id = a.author_id
group by category, author_id
order by a.author_id, category desc