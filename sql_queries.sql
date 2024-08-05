create database mcq;
CREATE TABLE user(
user_id INT AUTO_INCREMENT PRIMARY KEY ,
user_name VARCHAR(30) NOT NULL,
user_password VARCHAR(30) NOT NULL,
user_email VARCHAR(30) NOT NULL UNIQUE,
user_role VARCHAR(9) NOT NULL
);
ALTER TABLE user AUTO_INCREMENT=300;
CREATE TABLE subject(
subject_id INT AUTO_INCREMENT PRIMARY KEY,
subject_name VARCHAR(30) NOT NULL UNIQUE
);
ALTER TABLE subject AUTO_INCREMENT=100;
CREATE TABLE module(
module_id INT AUTO_INCREMENT PRIMARY KEY,
module_name VARCHAR(30) NOT NULL,
subject_id INT,
FOREIGN KEY(subject_id)REFERENCES subject(subject_id)
);
ALTER TABLE module AUTO_INCREMENT=200;
CREATE TABLE question(
question_id INT AUTO_INCREMENT PRIMARY KEY,
question VARCHAR(100) NOT NULL,
option_1 VARCHAR(100) NOT NULL,
option_2 VARCHAR(100) NOT NULL,
option_3 VARCHAR(100) NOT NULL,
option_4 VARCHAR(100) NOT NULL,
correct_answer VARCHAR(100) NOT NULL,
subject_id INT,
module_id INT,
created_by INT,
created_date DATE NOT NULL,
FOREIGN KEY(subject_id)REFERENCES subject(subject_id),
FOREIGN KEY(module_id)REFERENCES module(module_id),
FOREIGN KEY(created_by)REFERENCES user(user_id)
);
ALTER TABLE question AUTO_INCREMENT=500;
CREATE TABLE update_question(
question_id INT NOT NULL DEFAULT 0,
updated_by INT NOT NULL DEFAULT 0,
updated_date DATE,
PRIMARY KEY(question_id,updated_by),
FOREIGN KEY(question_id)REFERENCES question(question_id), 
FOREIGN KEY(updated_by)REFERENCES user(user_id)
);
CREATE TABLE test (
test_id INT AUTO_INCREMENT PRIMARY KEY,
total_mark INT,
user_id INT,
subject_id INT,
cut_off INT,
scored_mark INT,
max_test_duration TIME,
applicant_test_duration TIME,
test_date DATE,
total_number_of_questions INT,
FOREIGN KEY (user_id) REFERENCES user(user_id),
FOREIGN KEY (subject_id) REFERENCES subject(subject_id),
);
ALTER TABLE test AUTO_INCREMENT=1;
CREATE TABLE test_question_map(
test_id INT NOT NULL,
question INT NOT NULL,
mark INT NOT NULL,
option_selected VARCHAR(100),
test_question_id INT PRIMARY KEY AUTO_INCREMENT,
FOREIGN KEY(test_id)REFERENCES test(test_id),
FOREIGN KEY(question_id)REFERENCES question(question_id)
);
ALTER TABLE test_question_map AUTO_INCREMENT=1;
CREATE TABLE user_config_map(
user_id INT,
config_file VARCHAR(100)
PRIMARY KEY(config_file,user_id),
FOREIGN KEY(user_id)REFERENCES user(user_id)
);
INSERT INTO user(user_name,user_password,user_email,user_role) VALUES("mark","mark123","mark@gmail.com","admin");
INSERT INTO user(user_name,user_password,user_email,user_role) VALUES("luke","luke123","luke@gmail.com","admin");
INSERT INTO user(user_name,user_password,user_email,user_role) VALUES("mary","mary123","mary@gmail.com","applicant");

INSERT INTO subject(subject_name) VALUES("CAO");
INSERT INTO subject(subject_name) VALUES("DSA");
INSERT INTO subject(subject_name) VALUES("TOC");

INSERT INTO module(module_name,subject_id) VALUES("IAS architecture",100);
INSERT INTO module(module_name,subject_id) VALUES("Harvard architecture",100);
INSERT INTO module(module_name,subject_id) VALUES("Sorting algorithms",101);
INSERT INTO module(module_name,subject_id) VALUES("Graph theory",101);
INSERT INTO module(module_name,subject_id) VALUES("Regular languages",102);
INSERT INTO module(module_name,subject_id) VALUES("Turing machine",102);

INSERT INTO question(question,option_1,option_2,option_3,option_4,correct_answer,module_id,created_by,created_date) VALUES("What does IAS stand for in computer architecture?","Integrated Arithmetic System","Instruction Arithmetic Set","Instruction Address System","Instruction Set Architecture","Instruction Set Architecture",200,300,"2024-06-20");
INSERT INTO question(question,option_1,option_2,option_3,option_4,correct_answer,module_id,created_by,created_date) VALUES("In IAS architecture, what is the primary function of the Control Unit (CU)?","Perform arithmetic and logic operations","Store data temporarily","Direct the operation of the processor","Manage input and output operation","Direct the operation of the processor",200,301,"2024-06-20");

INSERT INTO question(question,option_1,option_2,option_3,option_4,correct_answer,module_id,created_by,created_date) VALUES("The Harvard architecture _____","created the Von Neumann bottleneck problem","is the unique solution for the Von Neumann bottleneck problem","is a solution for the Von Neumann bottleneck problem","allows for only one transaction at a time","is a solution for the Von Neumann bottleneck problem",201,301,"2024-06-20");


INSERT INTO question(question,option_1,option_2,option_3,option_4,correct_answer,module_id,created_by,created_date) VALUES("Which architecture involves both the volatile and the non volatile memory?","Harvard architecture","Von Neumann architecture","None of the mentioned","All of the mentioned","Harvard architecture",201,300,"2024-06-20");

INSERT INTO question(question,option_1,option_2,option_3,option_4,correct_answer,module_id,created_by,created_date) VALUES("What type of computer architecture utilizes both volatile and non-volatile memory?","Harvard architecture","Von Neumann architecture","None of the mentioned","All of the mentioned","Harvard architecture",201,300,"2024-06-20");


INSERT INTO question(question,option_1,option_2,option_3,option_4,correct_answer,module_id,created_by,created_date) VALUES("What is an example of a system design that includes both volatile and non-volatile memory?","Harvard architecture","Von Neumann architecture","None of the mentioned","All of the mentioned","Harvard architecture",201,301,"2024-06-20");

INSERT INTO question(question,option_1,option_2,option_3,option_4,correct_answer,module_id,created_by,created_date) VALUES("What is the meaning of IAS in the context of computer architecture?","Instruction Arithmetic Set","Instruction Address System","Instruction Set Architecture","Integrated Arithmetic System","Instruction Set Architecture",200,301,"2024-06-20");

INSERT INTO question(question,option_1,option_2,option_3,option_4,correct_answer,module_id,created_by,created_date) VALUES("What does the acronym IAS represent in computer architecture?","Instruction Arithmetic Set","Instruction Address System","Instruction Set Architecture","Integrated Arithmetic System","Instruction Set Architecture",200,301,"2024-06-20");

INSERT INTO question(question,option_1,option_2,option_3,option_4,correct_answer,module_id,created_by,created_date) VALUES("In computer architecture, what does IAS stand for?","Instruction Arithmetic Set","Instruction Address System","Instruction Set Architecture","Integrated Arithmetic System","Instruction Set Architecture",200,300,"2024-06-20");

INSERT INTO question(question,option_1,option_2,option_3,option_4,correct_answer,module_id,created_by,created_date) VALUES("Which architecture provides separate buses for program and data memory?","Harvard architecture","Von Neumann architecture","None of the mentioned","All of the mentioned","Harvard architecture",201,300,"2024-06-20");

INSERT INTO question(question,option_1,option_2,option_3,option_4,correct_answer,module_id,created_by,created_date) VALUES("Which architecture features distinct buses for program memory and data memory?","Harvard architecture","Von Neumann architecture","None of the mentioned","All of the mentioned","Harvard architecture",201,301,"2024-06-20");

INSERT INTO question(question,option_1,option_2,option_3,option_4,correct_answer,module_id,created_by,created_date) VALUES("What type of architecture uses separate buses for accessing program memory and data memory?","Harvard architecture","Von Neumann architecture","None of the mentioned","All of the mentioned","Harvard architecture",201,301,"2024-06-20");

INSERT INTO user_config_map VALUES(302,"cao_config1.yml");
INSERT INTO user_config_map VALUES(302,"cao_config2.yml");
INSERT INTO user_config_map VALUES(302,"cao_config3.yml");


