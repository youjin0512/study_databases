-- CREATE TABLE `NOTICE` (
-- 	`NOTICE_ID`	VARCHAR(255)	NOT NULL,
-- 	`VISITOR_ID`	VARCHAR(255)	NOT NULL,
-- 	`CONTENTS`	VARCHAR(255)	NULL,
-- 	`WRITER`	VARCHAR(255)	NULL
-- );

-- INSERT INTO NOTICE
-- (NOTICE_ID, CONTENTS, WRITER)
-- VALUES
-- ('NOTICE_01', '서비스 점검 안내', '관리자');

-- INSERT INTO NOTICE
-- (NOTICE_ID, CONTENTS, WRITER)
-- VALUES
-- ('NOTICE_05', '서비스 이용약관 변경 안내', '운영팀');

-- CREATE TABLE `VISITOR` (
-- 	`VISITOR_ID`	VARCHAR(255)	NOT NULL,
-- 	`NOTICE_ID`	VARCHAR(255)	NOT NULL,
-- 	`VISITOR_NAME`	VARCHAR(255)	NULL
-- );

INSERT INTO VISITOR
(VISITOR_ID, NOTICE_ID, VISITOR_NAME)
VALUES
('VISITE_01', 'NOTICE_01', '홍길동');

INSERT INTO VISITOR
(VISITOR_ID, NOTICE_ID, VISITOR_NAME)
VALUES
('VISITE_09', 'NOTICE_04', '임현서');
-- Error Code: 1452.
-- Cannot add or update a child row: a foreign key constraint fails (STUDY_NOTICES.VISITOR, CONSTRAINT FK_NOTICE_TO_VISITOR_1 FOREIGN KEY (NOTICE_ID) REFERENCES NOTICE (NOTICE_ID))

INSERT INTO VISITOR
(VISITOR_ID, NOTICE_ID, VISITOR_NAME)
VALUES
('VISITE_10', 'NOTICE_05', '강수민');

INSERT INTO VISITOR
(VISITOR_ID, NOTICE_ID, VISITOR_NAME)
VALUES
('VISITE_11', 'NOTICE_05', '백지영');

INSERT INTO VISITOR
(VISITOR_ID, NOTICE_ID, VISITOR_NAME)
VALUES
('VISITE_12', 'NOTICE_05', '박정희');