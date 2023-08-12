/*선행 테이블 먼저 생성*/
/* cctv_info가 메인테이블*/
CREATE TABLE DB_TEST.cctv_info(
    cctv_id INT NOT NULL,
    event_name VARCHAR(50) NOT NULL ,
    address VARCHAR(50) NOT NULL ,
    gps_xy VARCHAR(50),
    cctv_status VARCHAR(50),
    /*식별 가능한 항목인cctv_id를 pk로 지정(not null,unique)*/
    PRIMARY KEY (cctv_id) 
    )
;
    
CREATE TABLE DB_TEST.cctv_events(
    cctv_id INT NOT NULL,
    event_time DATETIME NOT NULL ,
    event_type VARCHAR(10) NOT NULL ,
    event_descript VARCHAR(50),
    PRIMARY KEY (cctv_id, event_time, event_type),
    /*cctv_info 테이블에서 cctv_id를 외래키로 참조*/
    FOREIGN KEY (cctv_id) REFERENCES DB_TEST.cctv_info(cctv_id) 
    )cctv_events
;
    
/*테이블 조회*/
select*from DB_TEST.cctv_events;
select*from DB_TEST.cctv_info;
