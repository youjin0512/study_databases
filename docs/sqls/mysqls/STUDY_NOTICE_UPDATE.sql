-- 기본구문
-- UPDATE table_name
-- SET column1 = value1, column2 = value2, ...
-- WHERE condition;

UPDATE NOTICE
SET CONTENTS = '결제 시스템 업그레이드 안내', WRITER = '운영팀'
WHERE NOTICE_ID = 'NOTICE_01';

-- NOTICE_05의 모든 VISITOR_NAME을 '백지영'으로 변경 
UPDATE VISITOR
SET VISITOR_NAME = '백지영'
WHERE NOTICE_ID = 'NOTICE_05';