SET FOREIGN_KEY_CHECKS = 0;
drop table users cascade;
drop table jobs cascade;
drop table UserJobs cascade;
drop table questions cascade;
drop table tests cascade;
drop table testquestions cascade;
drop table feedback cascade;
drop table admin_users cascade;
drop table key_admin cascade;
drop table tokens cascade;

create table users (
  firstname TEXT NOT NULL,
  lastname TEXT NOT NULL,
  email VARCHAR(255)  NOT NULL,
  hashed_password TEXT NOT NULL,
  id INT AUTO_INCREMENT,
  UNIQUE(email),
  PRIMARY KEY (id)
);

create table admin_users (
  email VARCHAR(255)  NOT NULL,
  hashed_password TEXT NOT NULL,
  id INT AUTO_INCREMENT,
  UNIQUE(email),
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
  date_posted date,
  date_expiry date,
  PRIMARY KEY (id)
);

create table UserJobs (
  name text,
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
  net_feedback text,
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
  feedback_id int AUTO_INCREMENT,
  user_id int,
  job_id int,
  application_id int,
  given_feedback boolean, 
  foreign key(application_id) references UserJobs(userjob_id) on delete cascade,
  foreign key(user_id) references users(id) on delete cascade,
  foreign key(job_id) references jobs(id) on delete cascade, 
  primary key(feedback_id)
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
  testquestion_id int AUTO_INCREMENT,
  test_id int,
  question_id int,
  foreign key(test_id) references tests(test_id) on delete cascade,
  foreign key(question_id) references questions(question_id) on delete cascade,
  primary key(testquestion_id)
);

create table key_admin (
  key_admin_id int AUTO_INCREMENT,
  key_num int,
  primary key(key_admin_id)
);

create table tokens (
  token_id int AUTO_INCREMENT,
  token text,
  user_id int,
  is_admin boolean,
  primary key(token_id)
);

SET FOREIGN_KEY_CHECKS = 1;
