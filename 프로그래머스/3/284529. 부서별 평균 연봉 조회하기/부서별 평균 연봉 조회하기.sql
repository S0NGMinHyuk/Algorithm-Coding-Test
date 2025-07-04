-- 코드를 작성해주세요
SELECT A.DEPT_ID, A.DEPT_NAME_EN, B.AVG_SAL
FROM HR_DEPARTMENT AS A
INNER JOIN (
    SELECT DEPT_ID, ROUND(AVG(SAL)) AS AVG_SAL  -- 부서ID별 평균 연봉 테이블
    FROM HR_EMPLOYEES
    GROUP BY DEPT_ID) AS B
ON A.DEPT_ID = B.DEPT_ID
ORDER BY B.AVG_SAL DESC