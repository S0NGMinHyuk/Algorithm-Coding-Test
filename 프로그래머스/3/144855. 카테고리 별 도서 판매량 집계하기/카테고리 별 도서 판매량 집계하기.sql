-- 코드를 입력하세요
SELECT
    CATEGORY,
    SUM(B.SALES) AS TOTAL_SALES
FROM BOOK AS A
INNER JOIN (
    SELECT BOOK_ID, SALES
    FROM BOOK_SALES
    WHERE SALES_DATE LIKE '2022-01%'
) AS B
ON 
    A.BOOK_ID = B.BOOK_ID
GROUP BY 
    A.CATEGORY
ORDER BY 
    A.CATEGORY