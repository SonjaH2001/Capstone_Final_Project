
drop table if exists tutor;
create table tutor (
  tutor_id integer primary key autoincrement,
  name text NOT NULL ,
  courses text NOT NULL,
  monday text NULL,
  tuesday text NULL,
  wednesday text NULL,
  thursday text NULL,
  friday text NULL
);

drop table if exists admin;
create table admin (
  admin_id integer primary key autoincrement,
  user_name text NOT NULL,
  user_password text NOT NULL
);

drop table if exists student_info;
create table student_info (
  id integer primary key autoincrement,
  student_name text NOT NULL,
  star_id text NOT NULL
);
INSERT INTO tutor (name, courses, monday, tuesday, wednesday,thursday,friday)
  VALUES ("Iggy Pop", "1150","", "1-3", "", "", "10-11"),
 ("O.D.B.", "", "1150", "6-7", "","", "12-3");

-- INSERT INTO tutor (name, courses, monday, tuesday, wednesday,thursday,friday)
--   VALUES ("O.D.B.", "", "1150", "6-7", "","", "12-3");
--
-- INSERT INTO tutor (name, courses, monday, tuesday, wednesday,thursday,friday)
--   VALUES ("Joe Strummer", "guitar for nerds", "1-2", "", "", "9-4","");
--
-- INSERT INTO tutor (name, courses, monday, tuesday, wednesday,thursday,friday)
--   VALUES ("Nick Cave", "piano for nerds", "", "6-10", "","1-2", "");