SET FOREIGN_KEY_CHECKS = 0;
drop table users cascade;
drop table jobs cascade;
drop table UserJobs cascade;
drop table questions cascade;
drop table tests cascade;
drop table testquestions cascade;
drop table testdata cascade;
drop table feedback cascade;


create table users (
  name TEXT NOT NULL,
  email VARCHAR(254) NOT NULL UNIQUE,
  hashed_password TEXT NOT NULL,
  id INT AUTO_INCREMENT,
  PRIMARY KEY (id)
);

create table jobs (
  title TEXT,
  description text,
  responsibilities text,
  people_management text,
  skills_needed text,
  ideal_candidate text,
  education text,
  id int AUTO_INCREMENT,
  available boolean,
  location text,
  PRIMARY KEY (id)
);

create table UserJobs (
  user_id int,
  job_id int,
  degree text,
  university text,
  degree_level text,
  a_levels text,
  languages text,
  employment text,
  skills text,
  hobbies text,
  response text,
  feedback text,
  cover_letter blob,
  score_degree float(5,1),
  score_alevels float(5,1),
  score_lang float(5,1),
  score_employment float(5,1),
  score_skills float(5,1),
  userjob_id int AUTO_INCREMENT,
  primary key(userjob_id),
  foreign key(user_id) references users(id) on delete cascade,
  foreign key(job_id) references jobs(id) on delete cascade
);

create table feedback (
  user_id int,
  job_id int,
  application_id int,
  given_feedback boolean,
  foreign key(application_id) references UserJobs(userjob_id) on delete cascade,
  foreign key(user_id) references users(id) on delete cascade,
  foreign key(job_id) references jobs(id) on delete cascade
);

create table questions (
  question text,
  question_id int AUTO_INCREMENT,
  job_id int,
  option_a text,
  option_b text,
  option_c text,
  option_d text,
  correct_answer varchar(1),
  primary key(question_id),
  foreign key(job_id) references jobs(id) on delete cascade
);

create table tests (
  user_id int,
  score int,
  iscompleted boolean,
  test_id int AUTO_INCREMENT,
  primary key(test_id),
  foreign key(user_id) references users(id) on delete cascade
);

create table testquestions (
  test_id int,
  question_id int,
  foreign key(test_id) references tests(test_id) on delete cascade,
  foreign key(question_id) references questions(question_id) on delete cascade
);

create table testdata (
  id int AUTO_INCREMENT,
  score_degree float(5,4),
  score_alevels float(5,4),
  score_lang float(5,4),
  score_employment float(5,4),
  scoreskills float(5,4),
  response int,
  primary key(id)
);
SET FOREIGN_KEY_CHECKS = 1;
