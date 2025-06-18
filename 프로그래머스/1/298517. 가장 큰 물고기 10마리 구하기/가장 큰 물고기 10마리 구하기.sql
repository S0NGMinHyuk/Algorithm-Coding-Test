-- 코드를 작성해주세요
SELECT ID, LENGTH
FROM FISH_INFO
ORDER BY LENGTH DESC, ID    -- 길이 기준 내림차순 정렬 + ID 기준 오름차순 정렬
LIMIT 10                    -- 상위 10개만 가져오기
