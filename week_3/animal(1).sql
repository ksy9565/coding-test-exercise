-- 코드를 입력하세요
-- 결과: 동물 id, 보호 시작일
-- 조건: INS에만 있고 OUTS에 없는 행
--      DATETIME 오름차순 -> ORDER BY
--      3마리 -> LIMIT
SELECT i.name, i.datetime
FROM animal_ins i
LEFT JOIN animal_outs o ON i.animal_id = o.animal_id
WHERE o.animal_id IS NULL
ORDER BY i.datetime
LIMIT 3;

SELECT name, datetime
FROM animal_ins
WHERE animal_id NOT IN (SELECT animal_id FROM animal_outs)
ORDER BY datetime
LIMIT 3;