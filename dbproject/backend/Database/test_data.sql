insert into users values('test', 'user_one', 'test_user_one@gmail.com', 'hashed_password_one', NULL);

INSERT INTO jobs values('Java', 'You will will work as part of a cross-functional agile delivery team, including analysts,
developers and testers. You will bring an innovative approach to software
development, using the latest technologies and practices, as part of a focus on
business value. You will be someone who sees engineering as team activity, with a
predisposition to open code, open discussion and creating a supportive, collaborative
environment. You will be ready to take a leading role in all stages of software delivery,
from intial analysis right through to production support. You will have an opportunity to work in an environment that provides continuous
growth and learning, with an emphasis excellence and mutual respect.',
 'Work as part of a delivery team, collaborating with others to understand
requirements, analyse and refine stories, design solutions, implement them, test
them and support them in production, Use BDD techniques, collaborating closely with users, analysts, developers and
other testers. Make sure we are building the right thing, Write code and write it well. Be proud to call yourself a programmer. Use test
driven development, write clean code and refactor constantly. Make sure we are
building the thing right, Be ready to work on a range of technologies and components, including user
interfaces, services and databases. Act as a generalizing specialist, Define and evolve the architecture of the components you are working on.
Contribute to architectural decisions at a department and bank-wide level, Ensure that the software you build is reliable and easy to support in production.
Be prepared to take your turn on call providing 3 rd line support when it’s needed, Help your team can build, test and release software with the short lead times
and a minimum of waste. Work to develop and maintain a highly automated
Continuous Delivery pipeline, Help create a culture of learning and continuous improvement within your team
and beyond', 'As a Assistant Vice President, you will be expected to lead others. For example in
sharing knowledge, facilitating meetings and workshops, defining new designs and
disovering new techniques. In some cases, it may also include elements of team
leadership or line management., As a Vice President, your role will include management and leadership responsibilities,
such as: Leading teams, Line management, Mentoring and teaching, Discovering new techniques and helping others to adopt them, Leading by example',
'You will need: Deep knowledge of at least one modern programming language, along with
understanding of both object oriented and functional programming. Ideally
knowledge of Java and Scala, Practical experience of test driven development and constant refactoring in
continuous integration environment, An understanding of web technologies, frameworks and tools, for example:
HTML, CSS, Javascript, Angular, Bootstrap, React, D3, Node.js, Knowledge of SQL and relational databases, Experience working in an agile team, practicing Scrum, Kanban or XP
The ideal candidate will also have: Behaviour Driven Development, particularly experience of how it can be used to
define requirements in a collaborative manner, ensure that the team builds the
right thing and create a system of living documentation, Experience with a range of technologies that store, transport and manipulate
data, for example: relational databases, nosql, document databases, graph
databases, Hadoop/HDFS, streaming and messaging, Knowledge gained in Financial Services environments, for example products,
instruments, trade lifecycles, regulation, risk, financial reporting or accounting, Architecture and design approaches that support rapid, incremental and
interative delivery, such as Domain Driven Design, CQRS, Event Sourcing and
microservices',
'The ideal candidate has a strong programming knowledge and experience of working in this field',
'We are happy to consider candidates with a wide variety of educational backgrounds
and qualifications. Qualifications in computer science, STEM subjects, other numerate
disciplines, business and economics are beneficial for the role.
We also look favourably upon candidates with equivalent practical experience. This
could have be gained in the workplace or in other contexts, such as contributing to
open source software or working on personal projects.', NULL, TRUE, 'Cornwall', '2019-01-11', '2019-04-11');

INSERT INTO UserJobs values('test_user_one', 1, 1, 'Computer Science', 'University of East Anglia', '2:1', '[{"Subject": "Mathematics", "Grade": "A*"}, {"Subject": "Computer Science", "Grade": "A"}, {"Subject": "Chemistry", "Grade": "B"}]',
  '[{"Language": "Python", "Expertise": 8}, {"Language": "Java", "Expertise": 7}, {"Language": "PHP", "Expertise": 6}, {"Language": "C#", "Expertise": 5}, {"Language": "Pascal", "Expertise": 5}]',
'[{"Company": "Google", "Position": "Web developer", "Length of Employment": "1 year 5 months"}, {"Company": "Burleigh and Stronginthearm", "Position": "Senior Web developer", "Length of Employment": "8 months"}]',
'[{"Skill": "Scrum", "Expertise": 8}, {"Skill": "Web development", "Expertise": 6}]', '[{"Name": "Singing", "Interest": 6}, {"Name": "Netball", "Interest": 3}]', 'Further tests', 'Not accepted',
'cv', 6, 6, 8, 4, 4, NULL);

INSERT INTO UserJobs values('test_user_one', 1, 1, 'Data Science', 'University of Warwick', '1st', '[{"Subject": "Mathematics", "Grade": "A*"}, {"Subject": "Further Mathematics", "Grade": "A"}, {"Subject": "Biology", "Grade": "A"}]',
  '[{"Language": "Java", "Expertise": 8}, {"Language": "SQL", "Expertise": 10}, {"Language": "C", "Expertise": 8}, {"Language": "C#", "Expertise": 4}, {"Language": "Visual Basic .NET", "Expertise": 4}, {"Language": "Hack", "Expertise": 4}, {"Language": "Pascal", "Expertise": 6}]',
'[{"Company": "Bluth Company", "Position": "Consultant", "Length of Employment": "1 year"}]', '[{"Skill": "Teamwork", "Expertise": 6}, {"Skill": "Scrum", "Expertise": 3}]', '[{"Name": "Cooking", "Interest": 6}, {"Name": "Netball", "Interest": 8}]', 'Further tests', 'Further tests',
'cv', 9, 8, 7, 4, 4, NULL);

INSERT INTO UserJobs values('test_user_one', 1, 1, 'Biological Sciences', 'University of Exeter', '3rd', '[{"Subject": "Mathematics", "Grade": "A"}, {"Subject": "Biology", "Grade": "A"}, {"Subject": "Chemistry", "Grade": "B"}]',
  '[{"Language": "Python", "Expertise": 4}, {"Language": "SQL", "Expertise": 2}, {"Language": "R", "Expertise": 7}, {"Language": "C#", "Expertise": 0}]',
'[{"Company": "Gringots", "Position": "Secretary", "Length of Employment": "5 months"}]', '[{"Skill": "Teamwork", "Expertise": 2}]', '[{"Name": "Singing", "Interest": 6}, {"Name": "Netball", "Interest": 3}]', 'Not accepted', 'Not accepted',
'cv', 1, 2, 1, 1, 1, NULL);

INSERT INTO admin_users values('admin_test_one@gmail.com', 'admin_password_one', NULL);

INSERT INTO tokens values(NULL, 'randomtesttoken_test_user_one', 1, false);
INSERT INTO tokens values(NULL, 'randomtesttoken_admin_test_one@gmail.com', 1, true);

INSERT INTO key_admin values(NULL, 1234)