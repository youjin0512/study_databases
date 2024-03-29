INSERT INTO NOTICE
(NOTICE_ID, CONTENTS, WRITER)
VALUES
('NOTICE_02', '이벤트 안내', '마케팅팀');

INSERT INTO VISITOR
(VISITOR_ID, NOTICE_ID, VISITOR_NAME)
VALUES
('VISITE_03', 'NOTICE_02', '백지영');

INSERT INTO VISITOR
(VISITOR_ID, NOTICE_ID, VISITOR_NAME)
VALUES
('VISITE_04', 'NOTICE_02', '최민호');

INSERT INTO VISITOR
(VISITOR_ID, NOTICE_ID, VISITOR_NAME)
VALUES
('VISITE_05', 'NOTICE_02', '송지현');


-- PARENT KEY 알고 있을 때(NOTICE_02에 해당하는 모든 데이터 삭제)
DELETE FROM VISITOR
WHERE NOTICE_ID = 'NOTICE_02'; 

DELETE FROM NOTICE
WHERE NOTICE_ID = 'NOTICE_02';

-- ** DELETE
-- Error Code: 1451. Cannot delete or update a parent row: a foreign key constraint fails (`STUDY_NOTICES`.`VISITOR`, CONSTRAINT `FK_NOTICE_TO_VISITOR_1` FOREIGN KEY (`NOTICE_ID`) REFERENCES `NOTICE` (`NOTICE_ID`))
