```sqlite
create table courses(
    id integer primary key,
    week integer not null,
    name nvarchar(20) not null,
    duration nvarchar(20) not null,
    section nvarchar(20) not null,
    classroom nvarchar(20) not null,
    teacher nvarchar(20) not null
);
```

```sqlite
INSERT INTO courses (id, week, name, duration, section, classroom, teacher) VALUES (1, 1, 'Web 技术', '1-9 周', '5-6', '商学院 551', '刘猛');
INSERT INTO courses (id, week, name, duration, section, classroom, teacher) VALUES (2, 2, '计算机网络', '1-18 周', '1-2', '电子楼 301', '刘猛');
INSERT INTO courses (id, week, name, duration, section, classroom, teacher) VALUES (3, 3, '主流数据库应用', '1-18 周', '1-2', '商学院 351', '衣振萍');
INSERT INTO courses (id, week, name, duration, section, classroom, teacher) VALUES (4, 3, 'Web 技术', '1-9 周', '7-8', '商学院 551', '刘猛');
INSERT INTO courses (id, week, name, duration, section, classroom, teacher) VALUES (5, 3, '美食鉴赏与食品创新设计', '1-17 周', '9-10', '商学院 453', '叶萌祺');
INSERT INTO courses (id, week, name, duration, section, classroom, teacher) VALUES (6, 4, '计算机网络', '1-18 周', '1-2', '商学院 348', '刘猛');
INSERT INTO courses (id, week, name, duration, section, classroom, teacher) VALUES (7, 4, '嵌入式系统', '1-18 周', '5-6', '商学院 451', '吕强');
INSERT INTO courses (id, week, name, duration, section, classroom, teacher) VALUES (8, 4, '植物保护创新原理与国家生物安全', '1-16 周', '9-10', '图西教学楼 208', '刘洪展');
INSERT INTO courses (id, week, name, duration, section, classroom, teacher) VALUES (9, 5, '形势与政策', '5-8 周', '3-4', '商学院 153', '王萧涵');
```