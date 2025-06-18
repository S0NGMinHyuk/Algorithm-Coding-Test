-- 코드를 작성해주세요
SELECT COUNT(id) AS COUNT
FROM ecoli_data
where genotype & 2 != 2 and (genotype & 1 = 1 OR genotype & 4 = 4)